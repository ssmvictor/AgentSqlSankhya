"""
Command-line utilities for managing the project's cache directory and tests.

This module consolidates the behaviour from the previous cache scripts
(`clear_cache.py`, `remove_cache.py`, `limpar_e_testar.py`) into a single,
discoverable interface.

Usage examples:
    python -m scripts.manage_cache clear
    python -m scripts.manage_cache info
    python -m scripts.manage_cache test
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from config.settings import CACHE_DIR
from src.constants import CACHE_HASH_FILE as CACHE_HASH_NAME
from src.constants import CACHE_INDEX_FILE as CACHE_INDEX_NAME

CACHE_DIR = Path(CACHE_DIR)
CACHE_INDEX_FILE = CACHE_DIR / CACHE_INDEX_NAME
CACHE_HASH_FILE = CACHE_DIR / CACHE_HASH_NAME


def clear_cache(args: argparse.Namespace) -> int:
    """Remove the cache directory and report the outcome."""
    cache_path = CACHE_DIR

    if not cache_path.exists():
        print("ℹ️ Não há cache para limpar. Ele será criado na próxima execução.")
        return 0

    if args.verbose:
        print(f"Removendo cache em: {cache_path.resolve()}")

    try:
        shutil.rmtree(cache_path)
    except PermissionError as exc:
        print(f"❌ Não foi possível apagar o cache: {exc}")
        print("   Verifique se algum processo está utilizando arquivos do cache.")
        return 1
    except OSError as exc:
        print(f"❌ Erro inesperado ao limpar o cache: {exc}")
        return 1

    print("✅ Cache limpo com sucesso. Um novo cache será criado conforme necessário.")
    return 0


def _format_size_kb(size_bytes: int) -> str:
    return f"{size_bytes / 1024:.1f} KB"


def show_cache_info(args: argparse.Namespace) -> int:
    """Display details about the cache contents."""
    cache_path = CACHE_DIR

    if not cache_path.exists():
        print("ℹ️ Cache ainda não foi gerado. Ele será criado na primeira execução que exigir.")
        return 0

    entries = list(cache_path.rglob("*"))
    if not entries:
        print(f"ℹ️ Cache vazio em {cache_path.resolve()}.")
        return 0

    print(f"📁 Cache localizado em: {cache_path.resolve()}")

    total_size = 0
    file_count = 0

    for entry in sorted(entries):
        if entry.is_file():
            stats = entry.stat()
            total_size += stats.st_size
            file_count += 1
            rel_path = entry.relative_to(cache_path)
            mtime = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            print(f"- {rel_path} • {_format_size_kb(stats.st_size)} • atualizado em {mtime}")
        elif args.verbose:
            rel_path = entry.relative_to(cache_path)
            print(f"- {rel_path}/ (diretório)")

    print(f"\nTotal: {file_count} arquivo(s), {_format_size_kb(total_size)}")

    known_files = [CACHE_INDEX_FILE, CACHE_HASH_FILE]
    available_known = [path for path in known_files if path.exists()]
    if available_known:
        print("\nArquivos conhecidos detectados:")
        for file_path in available_known:
            try:
                rel = file_path.relative_to(cache_path)
            except ValueError:
                rel = file_path
            print(f"- {rel}")

    return 0


def run_tests(args: argparse.Namespace) -> int:
    """Execute the indexer tests."""
    command = [sys.executable, "-m", "tests.test_indexer"]
    if args.verbose:
        print(f"Executando testes com comando: {' '.join(command)}")

    try:
        result = subprocess.run(command, check=False)
    except FileNotFoundError:
        print("❌ Python não encontrado. Verifique a instalação do interpretador.")
        return 1
    except OSError as exc:
        print(f"❌ Falha ao iniciar os testes: {exc}")
        return 1

    if result.returncode == 0:
        print("✅ Testes concluídos com sucesso.")
    else:
        print("❌ Testes falharam. Consulte os logs acima para mais detalhes.")

    return result.returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Utilitário para limpar e inspecionar o cache, além de executar testes."
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Exibe informações adicionais durante a execução.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    clear_parser = subparsers.add_parser(
        "clear",
        help="Remove o diretório de cache do projeto.",
    )
    clear_parser.set_defaults(handler=clear_cache)

    info_parser = subparsers.add_parser(
        "info",
        help="Mostra informações detalhadas sobre os arquivos do cache.",
    )
    info_parser.set_defaults(handler=show_cache_info)

    test_parser = subparsers.add_parser(
        "test",
        help="Executa a suíte de testes relacionada ao cache e indexação.",
    )
    test_parser.set_defaults(handler=run_tests)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handler = getattr(args, "handler")
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
