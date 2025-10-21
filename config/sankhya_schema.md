# Dicionário de Dados Sankhya

## Tabela: TGFACF
### Descrição: GF  Acerto de Ordem de Carga Financeiros e Notas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Empresa | I |  |
| `ORDEMCARGA` | Ordem de Carga | I |  |
| `RETORNADO` | Retornado | S |  |
| `CODHIST` | Histórico | I |  |
| `NUFIN` | Número Único do Financeiro | I |  |
| `NUNOTA` | Número Único da Nota | I |  |
| `OBSERVACAO` | Observação | S |  |

## Tabela: TGFACT
### Descrição: Acompanhamento de Notas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DHOCOR` | Data | D |  |
| `HRACT` | Hr. acompanhamento | T |  |
| `OCORRENCIAS` | Ocorrências | S |  |
| `REFERENCIA` | Referência | S | Veja opções na seção OPÇÕES |
| `NOTAQUALIDADE` | Nota para qualidade | I |  |
| `NOTAPONTUAL` | Nota para pontualidade | I |  |
| `CODUSU` | Cód. Usuário | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `NUMNOTA` | Número Nota | I |  |
| `DIGITADO` | Digitado | S |  |
| `NUNOTA` | Número único Nota | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo REFERENCIA (Tabela: TGFACT)
| Valor | Descrição |
|-------|-----------|
| C | Contato |
| E | Empresa |
| F | Frete |
| I | Veículo |
| N | Nota |
| P | Parceiro |
| R | Produto |
| T | Transportadora |
| V | Vendedor |


## Tabela: TGFAEV
### Descrição: Acompanhamento de Eventos de NFe

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | NUNOTA | I |  |
| `OCORRENCIA` | Ocorrenvia | C |  |
| `CODEVENTO` | CODEVENTO | I |  |
| `SEQEVENTO` | SEQEVENTO | I |  |
| `DHOCOR` | DHOCOR | H |  |

## Tabela: TGFAID
### Descrição: Alíquota Interna Destino do Produto

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPROD` | Produto | I |  |
| `CODUF` | UF | I |  |
| `ALIQINTDEST` | Alíq. Interna Destino | F |  |
| `PERCICMSFCP` | Perc. ICMS Fundo Comb. Pobreza | F |  |
| `PERCREDBASEDEST` | Perc. Red. Base Destino | F |  |

## Tabela: TGFASN
### Descrição: Anexos do Simples Nacional

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUANEXO` | Nro. do Anexo | I |  |
| `DTINICIO` | Dt. Inicio | D |  |
| `DESCR` | Descrição do Anexo | S |  |
| `TIPOANEXO` | Tipo do Anexo | I | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOANEXO (Tabela: TGFASN)
| Valor | Descrição |
|-------|-----------|
| 1 | Anexo I |
| 2 | Anexo II |
| 3 | Anexo III |
| 4 | Anexo IV |
| 7 | Anexo V |


## Tabela: TGFAVE
### Descrição: Averbações do Seguro MDF-e

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUVIAG` | Nro. Viagem | I |  |
| `SEQMDFE` | Sequência do manifesto | I |  |
| `NUMAPOLICE` | Nro. Apólice | S |  |
| `NUMAVERB` | Nro. Averbação | S |  |

## Tabela: TGFBAR
### Descrição: Códigos de Barras

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODBARRA` | Cód. Barras | S |  |
| `CODPROD` | Cód. Produto | I |  |
| `DHALTER` | Dt. Alteração | H |  |
| `CODUSU` | Usuário | I |  |
| `CODVOL` | Unidade de Volume | S |  |

## Tabela: TGFCAB
### Descrição: Entrada e Saída de Produto

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DESCTERMACORD` | Desc. ref. termo de acordo CT-e | F |  |
| `TIMCODPROD` | Serviço | I |  |
| `TIMDESCPROD` | Descrição (Serviço da Nota) | S |  |
| `CODINTERM` | Intermediador da Transação | I |  |
| `INTERMED` | Indicador de Intermediador/Marketplace | S | Veja opções na seção OPÇÕES |
| `CODCHECKOUT` | Cód. Checkout | I |  |
| `CLIENTEIDPARCERIA` | Id do cliente no parceiro | F |  |
| `IDDESCPARCERIA` | Id de desconto da parceria | F |  |
| `IDPONTUACAOPARCERIA` | Id de pontuação no parceiro | F |  |
| `VLRDESCPARCERIA` | Valor cupom desconto parceria | F |  |
| `DISDESAUTIMPEMB` | Distribui desconto autom. com impostos embutidos? | S | Veja opções na seção OPÇÕES |
| `CODPARCRETIRADA` | Cód. Parceiro Retirada | I |  |
| `CODPARC` | Parceiro | I |  |
| `INDNEGMODAL` | Indicador negociável Multimodal | S | Veja opções na seção OPÇÕES |
| `TIPSERVCTE` | Tipo de serviço CT-e | I | Veja opções na seção OPÇÕES |
| `TIPOCTE` | Tipo do CT-e | S | Veja opções na seção OPÇÕES |
| `VLRFRETETOTAL` | Vlr. Frete Total | F |  |
| `CODPARCTRANSPFINAL` | Transportadora Final | I |  |
| `LIBPENDENTE` | Liberação Pendente | S |  |
| `NUNOTA` | Nro. Único | I |  |
| `PEDIDOIMPRESSO` | Pedido foi impresso? | S |  |
| `SITUACAOWMS` | Situação WMS | I | Veja opções na seção OPÇÕES |
| `STATUSCONFERENCIA` | Status conferência | S | Veja opções na seção OPÇÕES |
| `STATUSWMS` | Status WMS | S | Veja opções na seção OPÇÕES |
| `TIPLIBERACAO` | Liberação | S | Veja opções na seção OPÇÕES |
| `VLRCOMPENSACAO` | Valor do crédito | F |  |
| `RETORNADOAC` | Entregue | S | Veja opções na seção OPÇÕES |
| `OBSERVACAOAC` | Observação | S |  |
| `DESCRHISTAC` | Descrição histórico | S |  |
| `NUMNOTA` | Nro. Nota | I |  |
| `DTNEG` | Dt. Neg. | D |  |
| `DTESCRCONT` | Dt. Escrituração Contábil. | D |  |
| `VLRNOTA` | Vlr. Nota | F |  |
| `SERIENOTA` | Série da nota | S |  |
| `SERIENFSE` | Série NFS-e | S |  |
| `CODEMP` | Empresa | I |  |
| `CODTIPOPER` | Tipo Operação | I |  |
| `CODTIPVENDA` | Tipo Negociação | I |  |
| `CONTABILIZADO` | Contabilizado? | S | Veja opções na seção OPÇÕES |
| `CONFIRMADA` | Confirmada | S |  |
| `CODVEND` | Vendedor | I |  |
| `STATUSNOTA` | Status da Nota | S | Veja opções na seção OPÇÕES |
| `CODNAT` | Natureza | I |  |
| `CODCENCUS` | Centro Resultado | I |  |
| `TIPMOV` | Tipo de Movimento | S | Veja opções na seção OPÇÕES |
| `CODLOCALORIG` | Local | I |  |
| `M3AENTREGAR` | M3 a Entregar | F |  |
| `PESOAENTREGAR` | Peso a Entregar | F |  |
| `PESOBRUTOITENS` | Peso bruto dos Itens | F |  |
| `PESOLIQITENS` | Peso liq. dos Itens | F |  |
| `CODMOEDA` | Moeda | I |  |
| `CODHISTAC` | Histórico | I |  |
| `BASESUBSTIT` | Base da Substituição | F |  |
| `HRMOV` | Hr. do Movimento | T |  |
| `BASEICMSFRETE` | Base do ICMS do Frete | F |  |
| `BASEICMSSTFRETE` | Base do ICMS/ST do Frete | F |  |
| `NUMCONTRATO` | Contrato | I |  |
| `BASEINSS` | Base de INSS | F |  |
| `OBSERVACAO` | Observação | S |  |
| `DTALTER` | Dt. de Alteração | H |  |
| `VLRICMS` | Vlr. do ICMS | F |  |
| `VLRDESCTOT` | Desconto no total | F |  |
| `VENCIPI` | Vencimento do IPI | H |  |
| `VLRVENDOR` | Vlr. do Vendor | F |  |
| `TOTALCUSTOSERV` | Custo Total do Serviço | F |  |
| `VENCFRETE` | Vencimento do frete | D |  |
| `VLRDESCTOTITEM` | Desconto total por item | F |  |
| `NUMCOTACAO` | Nro. da Cotação | I |  |
| `PERCDESC` | Percentual de Desconto | F |  |
| `ICMSFRETE` | ICMS sobre o frete | F |  |
| `ICMSSTFRETE` | Vlr. ICMS/ST sobre o frete | F |  |
| `PESO` | Peso | F |  |
| `VLRSUBST` | Vlr. da Substituição | F |  |
| `DTFATUR` | Dt. do Faturamento | H |  |
| `LOCALENTREGA` | Local de Entrega | S |  |
| `VLRREPREDTOT` | Desconto Redução de Base | F |  |
| `BASEISS` | Base do ISS | F |  |
| `CODUSU` | Cód. Usuário | I |  |
| `IPIEMB` | IPI da embalagem | F |  |
| `CODPARCDEST` | Parceiro Destinatário | I |  |
| `LOCALCOLETA` | Local de coleta | S |  |
| `VLRFRETECPL` | Vlr. Frete Complementar | F |  |
| `VLRISS` | Valor do ISS | F |  |
| `VLRIRF` | Vlr. do IRF | F |  |
| `VLRFRETE` | Vlr. do Frete | F |  |
| `VLRMERCADORIA` | Vlr. da Mercadoria | F |  |
| `VLREMB` | Vlr. da Embalagem | F |  |
| `COMGER` | Comissão Gerente | F |  |
| `VOLUME` | Volume | S |  |
| `BASEICMS` | Base do ICMS | F |  |
| `CODPROJ` | Projeto | I |  |
| `IRFRETIDO` | o INSS é retido? | S | Veja opções na seção OPÇÕES |
| `NOTASCF` | Notas do conhecimento de frete | S |  |
| `TIPFRETE` | Tipo do frete | S | Veja opções na seção OPÇÕES |
| `VLRJURO` | Valor do Juro | F |  |
| `VLRDESTAQUE` | Vlr. Destaque | F |  |
| `BASEIPI` | Base do IPI | F |  |
| `VLRIPI` | Vlr. do IPI | F |  |
| `BASESUBSTSEMRED` | Base Substituição Sem Redução | F |  |
| `NUMCF` | Nro. Conhec. de Frete | I |  |
| `DTENTSAI` | Dt. Entrada/Saída | D |  |
| `DTCONTAB` | Dt. da Contabilização | H |  |
| `CODPARCREDESPACHO` | Redespacho (Recebedor) | I |  |
| `VLRDESCSERV` | Total desc. serviços | F |  |
| `TOTALCUSTOPROD` | Custo Total do Produto | F |  |
| `PREMIACAOESTADUAL` | Premiação Estadual | S |  |
| `CODOBSPADRAO` | Observação padrão | I |  |
| `ORDEMCARGA` | Ordem de carga | I |  |
| `CODPARCTRANSP` | Parceiro Transportadora | I |  |
| `VLRINSS` | Vlr. de INSS | F |  |
| `NUMOS` | Nro. da OS | I |  |
| `KMVEICULO` | KM | I |  |
| `CODPARCREMETENTE` | Parceiro Remetente | I |  |
| `COMISSAO` | Comissão | F |  |
| `VLRSEG` | Vlr. do Seguro | F |  |
| `VLRICMSEMB` | Valor do ICMS da embalagem | F |  |
| `VLROUTROS` | Vlr. Outros | F |  |
| `CODCONTATO` | Contato | I |  |
| `IRINNAVIO` | IRIN do navio | S |  |
| `CODDOCARRECAD` | Cód. Mod. Documento de arrecadação | I | Veja opções na seção OPÇÕES |
| `CODVEICULO` | Veículo | I |  |
| `CODCIDINICTE` | Cód. Cid. Inicio CT-e | I |  |
| `CODPARCDESCARGAMDFE` | Parceiro Descarregamento (MDF-e) | I |  |
| `TIMORIGEM` | Origem | S | Veja opções na seção OPÇÕES |
| `TIMNUNOTAMOD` | Nota Modelo | I |  |
| `TIMCONTRATOVENDA` | Contrato de Venda de Imóvel | I |  |
| `TIMCONTRATOLTV` | Contrato de Venda de Lote | I |  |
| `NFEDEVRECUSA` | NF-e de Devolução via Recusa | S | Veja opções na seção OPÇÕES |
| `VLRFRETECALC` | Vlr. frete calc. | F |  |
| `NUCFR` | Cód. cálculo de frete | I |  |
| `FRETEVLRPAGO` | Vlr. frete pago | F |  |
| `VLRPRESTAFRMM` | Vlr. prest. AFRMM | F |  |
| `VLRAFRMM` | Valor AFRMM | F |  |
| `NUMDOCARRECAD` | Número Documento de arrecadação | S |  |
| `IDNAVIO` | Identificação do navio | S |  |
| `IDBALSA03` | ID da Balsa 3 | S |  |
| `MODRECEBPDVWEB` | Modo de recebimento PDV | S | Veja opções na seção OPÇÕES |
| `AGRUPFINNOTA` | Agrupar financeiro | S | Veja opções na seção OPÇÕES |
| `CONFIRMNOTAFAT` | Confirmar ao faturar | S | Veja opções na seção OPÇÕES |
| `DIRECAOVIAG` | Direção da viagem | S | Veja opções na seção OPÇÕES |
| `IDBALSA01` | ID da Balsa 1 | S |  |
| `IDBALSA02` | ID da BAlsa 2 | S |  |
| `CODCIDFIMCTE` | Cód. Cid. Fim CT-e | I |  |
| `CODCIDPREST` | Cidade de Prestação do Serviço | I |  |
| `TPAMBNFSE` | Ambiente NFS-e | S | Veja opções na seção OPÇÕES |
| `NULOTENFCOM` | Lote NFCom | I |  |
| `CODRASTREAMENTOECT` | Cód. Rastreamento ECT | S |  |
| `PERCDESCFOB` | Perc. desc. FOB | F |  |
| `TERMACORDNOTA` | Termo de Acordo  p/ CT-e na Nota | S |  |
| `SEQCARGA` | Sequência da carga | I |  |
| `SERIENFDES` | DES-BH Série NF | S |  |
| `NATUREZAOPERDES` | DES-BH Tipo de Negócio | S |  |
| `MODELONFDES` | DES-BH Modelo NF | S |  |
| `STATUSNFE` | Status NF-e | S | Veja opções na seção OPÇÕES |
| `ANTT` | RNTRC | S |  |
| `VLRICMSFCP` | Valor do ICMS Fundo de Pobreza | F |  |
| `FUSOEMISSEPEC` | Fuso Horário Emissão EPEC | S |  |
| `CLASCONS` | Cód. Classe de Cons. | S |  |
| `CHAVENFEREF` | Chave NF-e referenciada | S |  |
| `CIOT` | CIOT | I |  |
| `TIMNUFINORIG` | Financeiro Repasse | I |  |
| `REGESPTRIBUT` | DES-BH Regime Especial de Tributação | S |  |
| `EXIGEISSQN` | DES-BH Exigibilidade do ISSQN | S |  |
| `SITESPECIALRESP` | DES-BH Situação Especial de Responsabilidade | S |  |
| `MOTNAORETERISSQN` | DES-BH Motivo de não Retenção ISSQN | S |  |
| `CODCIDORIGEM` | Cód. Cidade de Origem | I |  |
| `CODCIDDESTINO` | Cód. Cidade de Destino | I |  |
| `CLASSIFICMS` | Cód. Classificação ICMS | S |  |
| `NUODP` | Ordem de Despacho | I |  |
| `NUFOP` | Finalidade da Operação | I |  |
| `CODUFENTREGA` | Cód. UF de Entrega | I |  |
| `CODUFORIGEM` | Cód. UF de Origem | I |  |
| `CODCONTATOENTREGA` | Contato de Entrega | I |  |
| `CODUFDESTINO` | Cód. UF de Destino | I |  |
| `CODCIDENTREGA` | Cód. Cidade de Entrega | I |  |
| `ISSRETIDO` | ISS Retido na fonte | S | Veja opções na seção OPÇÕES |
| `DHTIPOPER` | Dt./Hr. Operação | H |  |
| `PENDENTE` | Pendente | S | Veja opções na seção OPÇÕES |
| `TIPIPIEMB` | Tipo do Valor Embalagem | S | Veja opções na seção OPÇÕES |
| `CODFUNC` | Funcionário | I |  |
| `CODPARCCONSIGNATARIO` | Consignatário (Expedidor) | I |  |
| `DTMOV` | Dt. do Movimento | D |  |
| `DTPREVENT` | Previsão de entrega | H |  |
| `DHREGDPEC` | Dt. Reg. EPEC | H |  |
| `INDPRESNFCE` | Indicador de Presença para NF-e/NFC-e | S | Veja opções na seção OPÇÕES |
| `CPFCNPJADQUIRENTE` | CPF/CNPJ Adquirente | S |  |
| `MODENTREGA` | Mod. Entrega | S | Veja opções na seção OPÇÕES |
| `PRODPRED` | Produto Predominante | S |  |
| `CHAVENFSE` | Chave NFS-e | S |  |
| `CODOBRA` | Cód. da Obra | S |  |
| `UFADQUIRENTE` | UF do Adquirente | S | Veja opções na seção OPÇÕES |
| `VIATRANSP` | Tipo de Transporte | S | Veja opções na seção OPÇÕES |
| `CNPJADQUIRENTE` | CNPJ/CPF do Adquirente | S |  |
| `TIPPROCIMP` | Tipo Processo de Importação | S | Veja opções na seção OPÇÕES |
| `PRODUETLOC` | Produção por Etapa e Local? | S | Veja opções na seção OPÇÕES |
| `NUNOTASUB` | Nro. Unico. Nota Substituída | I |  |
| `VLRICMSDIFALDEST` | Valor DIFAL UF Destino | F |  |
| `VLRICMSDIFALREM` | Valor DIFAL UF Remet. | F |  |
| `NOTAEMPENHO` | Nota de empenho | S |  |
| `REBOQUE3` | Reboque 3 | I |  |
| `SITUACAOCTE` | Situação CT-e | S | Veja opções na seção OPÇÕES |
| `LOTACAO` | Lotação CT-e | S | Veja opções na seção OPÇÕES |
| `TPEMISCTE` | Tipo de emissão do CT-e | I | Veja opções na seção OPÇÕES |
| `TPAMBCTE` | Ambiente CT-e | S | Veja opções na seção OPÇÕES |
| `NUMALEATORIOCTE` | Nro. Aleat. CT-e | I |  |
| `STATUSCTE` | Status CT-e | S | Veja opções na seção OPÇÕES |
| `DTDECLARA` | Dt. Declaração CT-e de Anulação | H |  |
| `REBOQUE1` | Reboque 1 | I |  |
| `REBOQUE2` | Reboque 2 | I |  |
| `NULOTECTE` | Lote CT-e | I |  |
| `NUMPROTOCCTE` | Nro. Protocolo CT-e | S |  |
| `NUMPROTOCINCTE` | Nro. Protocolo Insucesso CT-e | S |  |
| `NUMPROTOCINNFE` | Nro. Protocolo Insucesso NF-e | S |  |
| `DHPROTOCCTE` | Dh. Protocolo CT-e | H |  |
| `DHEMISSEPEC` | Dt. Emissão Epec | H |  |
| `CODART` | Cód. Art | S |  |
| `DTREMRET` | Data de Remessa/Retorno | H |  |
| `PESOLIQUIMANUAL` | Peso liquido Manual | S | Veja opções na seção OPÇÕES |
| `VLRDESCTOTITEMMOE` | Desc.Total dos itens em Moeda | F |  |
| `VLRTOTLIQITEMMOE` | Total Líq. Itens em Moeda | F |  |
| `CTELOTACAO` | Lotação | S | Veja opções na seção OPÇÕES |
| `VLRICMSDIFERIDO` | Vlr. ICMS Diferido | F |  |
| `NFSEID` | NFSe ID | S |  |
| `PESOBRUTOMANUAL` | Peso bruto manual | S | Veja opções na seção OPÇÕES |
| `IDIPROC` | Nro. Ordem Produção | I |  |
| `CHAVECTE` | Chave CTe | S |  |
| `CODVTP` | Cód. Meio de Transporte | I |  |
| `NUPCA` | Núm. Planejamento de Compras | I |  |
| `NOMEADQUIRENTE` | Nome Adquirente | S |  |
| `LOCEMBARQ` | Local do Embarque | S |  |
| `UFEMBARQ` | UF Local Embarque | S | Veja opções na seção OPÇÕES |
| `DTENTSAIINFO` | Data Extemporânea | D |  |
| `M3` | Metro Cúbico | F |  |
| `DTVAL` | Dt. da Validade | H |  |
| `APROVADO` | Aprovado | S | Veja opções na seção OPÇÕES |
| `VLRICMSSEG` | Vlr. do ICMS do seguro | F |  |
| `CODMAQ` | Identifica impressora CF | I |  |
| `CODEMPNEGOC` | Empresa da negociação | I |  |
| `CHAVENFE` | Chave NF-e | S |  |
| `CODCID` | Cidade | I |  |
| `CODMODDOCNOTA` | Modelo do Documento Fiscal | I | Veja opções na seção OPÇÕES |
| `CODMOTORISTA` | Motorista | I |  |
| `VLRLIQITEMNFE` | VLRLIQITEMNFE | S |  |
| `CODTPD` | Cód. Tipo de Pedido | I |  |
| `CODVENDTEC` | Vendedor Técnico | I |  |
| `DHTIPVENDA` | Dt./Hr. Tipo de negociação | H |  |
| `LIBCONF` | Liberado conferência | S |  |
| `NUCONFATUAL` | Nro Conferência atual | I |  |
| `NUMPEDIDO2` | Número Pedido | S |  |
| `AD_NROPEDCLIENTE` | Nro. Ped. Cliente | I |  |
| `PESOBRUTO` | Peso bruto | F |  |
| `QTDVOL` | Qtd. volumes | I |  |
| `TPAMBNFE` | Ambiente NF-e | S |  |
| `VLRJURODIST` | Valor de juro distribuído | F |  |
| `VLRSTEXTRANOTATOT` | Valor Total ST Extra Nota | F |  |
| `RATEADO` | Rateado | S | Veja opções na seção OPÇÕES |
| `CIF_FOB` | CIF / FOB | S | Veja opções na seção OPÇÕES |
| `HRENTSAI` | Hr. Ent./Saída | H |  |
| `TPFRETAMENTO` | Tipo Fretamento | I | Veja opções na seção OPÇÕES |
| `DHVIAGEM` | Data e hora da viagem | H |  |
| `NUMERACAOVOLUMES` | Numeração de Volumes | S |  |
| `TPEMISNFE` | Emissão NF-e | I | Veja opções na seção OPÇÕES |
| `HRADIAM` | Hr. Adiamento | T |  |
| `TIPOPTAGJNFE` | Tipo Operação Veículos Novos | I | Veja opções na seção OPÇÕES |
| `MARCA` | Marca | S |  |
| `VLRINDENIZDIST` | Vlr. Indenização Distribuído | F |  |
| `NUREM` | Remessa | I |  |
| `CODGRUPOTENSAO` | Cód.Grupo de Tensão | S |  |
| `TPLIGACAO` | Cód.Tipo de Ligação | I |  |
| `TPASSINANTE` | Cód.Tipo de Assinante | I | Veja opções na seção OPÇÕES |
| `TROCO` | Troco | F |  |
| `NROREDZ` | Nro. Redução Z | I |  |
| `VLRMOEDA` | Vlr. Moeda | F |  |
| `DANFE` | Nro. DANFE | I |  |
| `DHPROTOC` | Dt. Protocolo NF-e | H |  |
| `DTENVIOPMB` | Dt. de Envio à PMB | H |  |
| `DTENVSUF` | Dt. de Envio Suframa | H |  |
| `NULOTENFSE` | Lote NFS-e | I |  |
| `NUMNFSE` | Nro. NFS-e | S |  |
| `OCCN48` | Ordem de Carga CN48 | I |  |
| `STATUSNFSE` | Status NFS-e | S | Veja opções na seção OPÇÕES |
| `TPEMISNFSE` | Emissão NFS-e | I | Veja opções na seção OPÇÕES |
| `VLRINDENIZ` | Vlr. Indenização | F |  |
| `ALIQIRF` | Alíquota IRF | F |  |
| `BASECOFINS` | Base do COFINS | F |  |
| `BASECOFINSST` | Base do COFINSST | F |  |
| `BASEIRF` | Base do IRF | F |  |
| `BASEPIS` | Base de PIS | F |  |
| `BASEPISST` | Base do PISST | F |  |
| `CODDOCA` | Doca | I |  |
| `CODEMPFUNC` | Empresa do funcionário | I |  |
| `CODUSUINC` | Cód. Usuário Inclusão | I |  |
| `DIGITAL` | Digital | S |  |
| `DTADIAM` | Adiamento | H |  |
| `NROCAIXA` | Nro. Caixa | I |  |
| `NULOTENFE` | Lote NF-e | I |  |
| `NUMALEATORIO` | Nro. Aleat. NF-e | I |  |
| `NUMPROTOC` | Nro. Protocolo NF-e | S |  |
| `NUMREGDPEC` | Nro. Reg. DPEC | S |  |
| `NUNOTAPEDFRET` | Nro. Único Ped. Frete | I |  |
| `NURD8` | Nro. Único do RD8 | I |  |
| `NUTRANSF` | Nro. Transferência | I |  |
| `TIPNOTAPMB` | Tipo de Nota PMB | S |  |
| `TOTDISPDESC` | Total Disponível p/ Desc. | F |  |
| `VLRCOFINS` | Vlr. COFINS | F |  |
| `VLRCOFINSST` | Vlr. COFINSST | F |  |
| `VLRPIS` | Vlr. PIS | F |  |
| `VLRPISST` | Vlr. PISST | F |  |
| `VLRROYALT` | Vlr. ROYALT | F |  |
| `CODSITE` | Site | I |  |
| `CODUSUCOMPRADOR` | Cód. Usuário Comprador | I |  |
| `PLACA` | Placa | S |  |
| `UFVEICULO` | UF do veículo | I |  |
| `LACRES` | Lacres | S |  |
| `CODCC` | CODCC | I |  |
| `NUPEDFRETE` | Nro. Pedido Frete | I |  |
| `AD_COMISSAOEX` | Comissão Vend | F |  |
| `FORMPGTCTE` | Forma de Pagamento do CT-e | S | Veja opções na seção OPÇÕES |
| `VLRICMSFCPINT` | Valor do ICMS FCP Interno | F |  |
| `AD_VLRCOMISSAO` | Vlr. Comissão | F |  |
| `VLRSTFCPINT` | Vlr. ST FCP Interno | F |  |
| `AD_PERCFRETE` | % Frete | F |  |
| `AD_IMPRESSO` | Impresso? | S |  |
| `VLRSTFCPINTANT` | Vlr. ST FCP Interno Anterior | F |  |
| `CTEGLOBAL` | CT-e Globalizado | S | Veja opções na seção OPÇÕES |
| `AD_VLRPROD` | Vlr. Produtos | F |  |
| `VLRCARGAAVERB` | Valor da Carga Para Averbação | F |  |
| `AD_QTDPROD` | Qtd. Total | F |  |
| `AD_ORDEMREP` | Ordem de carga da Reposição | I |  |
| `FISTEL` | FISTEL (Nota Fiscal de Comunicação/Telecomunicação) | S |  |
| `AD_RELATORIO` | Gera Relatório? | S | Veja opções na seção OPÇÕES |
| `NUMCSTC` | Nro. Característica Sv Tele/Comunicação | I |  |
| `QTDUSU` | Quantidade de usuário / login | I |  |
| `AD_CHKAVISO` | Avisou sobre reposição check list? | S | Veja opções na seção OPÇÕES |
| `NUMTERMTEL` | Nro. Identificação do Terminal Telefônico | S |  |
| `TIPCLIENTESERVCOM` | Tipo Cliente de Serviços de Comunicação | I | Veja opções na seção OPÇÕES |
| `AD_TIPOPEDIDO` | Selecione o tipo  | S | Veja opções na seção OPÇÕES |
| `MD5MODCOMTEL` | MD5MODCOMTEL | S |  |
| `PERMALTERCENTRAL` | Permite Alteração na Central | S | Veja opções na seção OPÇÕES |
| `AD_CIDADE` | Nome Cidade | S |  |
| `DTREF` | Data de Referência | D |  |
| `DTREF2` | Data de Referência 2 | D |  |
| `DTREF3` | Data de Referência 3 | D |  |
| `VLRREPREDTOTSEMDESC` | Vlr. redução total sem desconto | F |  |
| `CODGUF` | Código GNRE Unidade Federativa | I |  |
| `AD_VLRPRODFRETE` | Porc. Frete | F |  |
| `LONGITUDE` | Longitude | S |  |
| `AD_ORDEMCARGANF` | Ordem de carga (NF) | I |  |
| `LATITUDE` | Latitude | S |  |
| `BASEICMSAT` | Base de ICMS AT | F |  |
| `AD_FRETEOUTROS` | Frete Outros | F |  |
| `AD_UFENTREGA` | UF da Entrega | S |  |
| `VLRICMSAT` | Valor de ICMS AT | F |  |
| `AD_RASTREIO` | Rastreio | S | Veja opções na seção OPÇÕES |
| `VLRFETHAB` | Vlr. FETHAB | F |  |
| `VALORDESONPISCOFINS` | Valor PIS/COFINS Desonerados | F |  |
| `VLRREPREDST` | Vlr. redução ST | F |  |
| `QTDPRODDISTINTOS` | Qtd. Prod. Distintos | I |  |
| `AD_NEGOCIACAO` | Negociação | S |  |
| `AD_TEMANEXO` | Anexos | S |  |
| `AD_DTPEDIDO` | Data do Pedido | D |  |
| `AD_PESOCARGA` | Peso Carga | F |  |
| `AD_VLRNT` | Vlr Nota | F |  |
| `NOTAPORPEDIDOPDV` | Nota gerada por pedido | S | Veja opções na seção OPÇÕES |
| `AD_VLRFRETE` | VlrFrete | F |  |
| `AD_VENDSEC` | Vend Interno | I |  |
| `AD_OBSERVACOES` | Obs. | S |  |
| `SUMVLRIIOUTNOTA` | Tratar II em NF-e Nacionalização | I |  |
| `NURECEBIMENTO` | Nro. Recebimento | I |  |
| `RETGERWMS` | Retorno Gerencial de Estoque | S |  |
| `CODAUTHVM` | Cód. de Autorização Venda Mais | S |  |
| `CARACSER` | Característica adicional do serviço | S |  |
| `SOMICMSNFENAC` | Tratar ICMS em NF-e Nacionalização | I |  |
| `NUNOTAREC` | Numero da Nota Gerada para o Retorno | I |  |
| `CARACAD` | Característica adicional do transporte | S |  |
| `SOMPISCOFNFENAC` | Tratar PIS/COFINS em NF-e Nacionalização | I |  |
| `CHVNFEINEREF` | Chave NFe Referenciada Inexistente | S |  |
| `SOMDESPADUNFENAC` | Somar despesas aduaneiras à NF-e de Nacionalização | I |  |
| `STATUSCFE` | Status CF-e | S | Veja opções na seção OPÇÕES |
| `RETORNOEQUIPFISCAL` | Retorno Equipamento Fiscal | S |  |
| `AD_CIDENTREGA` | Cidade Entrega | S |  |
| `NUSESSAO` | Número da Sessão do Aparelho Fiscal | I |  |
| `AD_ORDPED` | OC Pedido | I |  |
| `CHAVECTEREF` | Chave CT-e referenciada | S |  |
| `STATUSVM` | Status Venda Mais | S | Veja opções na seção OPÇÕES |
| `AD_DTENTR` | Dt. Entrega | D |  |
| `HISTCONFIG` | Gravar o histórico de configuração do parâmetro CONSIMPRETNOTA | S |  |
| `AD_OBSCARGA` | Observacao Carga | S |  |
| `DTVALAUTVENDAMAIS` | Dt. Validade Crédito | D |  |
| `AD_MIX` | %Mix | F |  |
| `AD_CONFIRMAR` | Comfirma | I |  |
| `STATUSAUTORIZACAOVM` | Status Autorização Venda Mais | S | Veja opções na seção OPÇÕES |
| `AD_MOTOOC` | Motorista OC | S |  |
| `VLRREPTERC` | Vlr. Repasse a Terceiros (NFS-e) | F |  |
| `CHAVESINIEF1324` | Chaves de acesso AJUSTE SINIEF 13/24 | S |  |
| `AD_VLRPAGO` | Vlr. Pago Imposto | F |  |
| `AD_PERCST` | %ST | F |  |
| `NUMRECEITAGRO` | Número da receita ou receituário do agrotóxico / defensivo agrícola. | S |  |
| `CPFRESPTEC` | CPF do Responsável Técnico, emitente do receituário | S |  |
| `TIPOGUIA` | Tipo da Guia | S | Veja opções na seção OPÇÕES |
| `UFEMISS` | UF de emissão | I |  |
| `UFEMISSAO` | UF de emissão | S |  |
| `SERIEGUIA` | Série da Guia | S |  |
| `NUMGUIA` | Número da Guia | I |  |
| `NUMPROTOCNFCOM` | Nro. Protocolo NFCom | S |  |
| `TPRETISS` | Tipo de Retenção do ISS | S | Veja opções na seção OPÇÕES |
| `SITUACAONFCOM` | Situação NFCom | S | Veja opções na seção OPÇÕES |
| `NFCOM` | NFCom | S | Veja opções na seção OPÇÕES |
| `CHAVENFCOM` | Chave NFCom | S |  |
| `STATUSNFCOM` | Status NFCom | S | Veja opções na seção OPÇÕES |
| `TPEMISNFCOM` | Emissão NFCom | I | Veja opções na seção OPÇÕES |
| `TPAMBNFCOM` | Ambiente NFCom | S | Veja opções na seção OPÇÕES |
| `AD_ERAORCA` | Era Orçamento | I | Veja opções na seção OPÇÕES |
| `VLRSERVICO` | Valor do Serviço | F |  |
| `BCICMSRET` | Base de Cálculo da Retenção do ICMS | F |  |
| `ALIQICMSRET` | Alíquota da Retenção | F |  |
| `VLRICMSRET` | Valor do ICMS Retido | F |  |
| `CODCFO` | CFOP | I |  |
| `CMUNFATGER` | Código do Município do Fato Gerador | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo INTERMED (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Operação sem intermediador (em site ou plataforma própria) |
| 1 | 1-Operação em site ou plataforma de terceiros (intermediadores/marketplace) |

### Opções para campo DISDESAUTIMPEMB (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDNEGMODAL (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | Não negociável |
| 1 | Negociável |

### Opções para campo TIPSERVCTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | Normal |
| 1 | Subcontratação |
| 2 | Redespacho |
| 3 | Redespacho Intermediário |
| 4 | Serviço Vinculado a Multimodal |

### Opções para campo TIPOCTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Anulação |
| C | Complementar |
| N | Normal |
| S | Substituição |

### Opções para campo SITUACAOWMS (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | Aguardando separação |
| -1 | Não Enviado |
| 1 | Enviado para separação |
| 10 | Aguardando conferência(Separação) |
| 100 | Cancelada |
| 12 | Conferência com divergência |
| 13 | Parcialmente conferido |
| 14 | Aguardando armazenagem |
| 15 | Enviado para armazenagem |
| 16 | Concluído |
| 17 | Aguardando conferência volumes |
| 18 | Armazenado parcial |
| 19 | Armazenado |
| 2 | Em processo separação |
| 3 | Aguardando conferência |
| 4 | Em processo conferência |
| 5 | Prob/Erro. confirmação nota |
| 6 | Aguardando recontagem |
| 7 | Pedido totalmente cortado |
| 8 | Pedido parcialmente cortado |
| 9 | Conferência validada |
| 98 | Aguardando formação de  volumes |

### Opções para campo STATUSCONFERENCIA (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Em andamento |
| AC | Aguardando conferência |
| AL | Aguardando liberação p/ conferência |
| C | Aguardando liberação de corte |
| D | Finalizada divergente |
| F | Finalizada OK |
| R | Aguardando recontagem |
| RA | Recontagem em andamento |
| RD | Recontagem finalizada divergente |
| RF | Recontagem finalizada OK |
| Z | Aguardando finalização |

### Opções para campo STATUSWMS (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | Pedido parcialmente cortado |
| 1 | Enviado totalmente |
| 2 | Enviado parcialmente |
| 3 | Não enviado |
| 4 | Não Controlado pelo WMS |
| 5 | Pedido totalmente cortado |

### Opções para campo TIPLIBERACAO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Aprovado |
| P | Pendente |
| R | Reprovado |
| S | Sem pendência |

### Opções para campo RETORNADOAC (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| D | Devolvido |
| E | Entregue |
| N | Não Entregue |
| R | Reentregar |

### Opções para campo CONTABILIZADO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSNOTA (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Atendimento |
| L | Liberada |
| P | Pendente |

### Opções para campo TIPMOV (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| B | B-Movimento bancário |
| C | C-Compra |
| D | D-Devolução de venda |
| E | E-Devolução de compra |
| F | F-Produção |
| G | G-Pagamento |
| I | I-Financeiro |
| J | J-Pedido de Requisição |
| K | K-Pedido de Transferência |
| L | L-Devolução de Requisição |
| M | M-Devolução de Transf. |
| N | N-Entradas |
| O | O-Pedido de compra |
| P | P-Pedido de venda |
| Q | Q-Requisição |
| R | R-Recebimento |
| T | T-Transferência |
| V | V-Venda |
| 1 | 1-NF Depósito |
| 2 | 2-PD Devol. / Procuração / Warrant |
| 3 | 3-Saídas |
| 4 | 4-Faturamento |
| 8 | 8-RD8 |

### Opções para campo IRFRETIDO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPFRETE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Extra nota |
| S | Incluso |

### Opções para campo CODDOCARRECAD (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | Documento Estadual de Arrecadação |
| 1 | GNRE |

### Opções para campo TIMORIGEM (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| CP | Comissão Cancelada |
| MF | MFD |
| PC | Comissão Venda Lote |

### Opções para campo NFEDEVRECUSA (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MODRECEBPDVWEB (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| G | Tipo de negociação |
| T | Tipo de título |

### Opções para campo AGRUPFINNOTA (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONFIRMNOTAFAT (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIRECAOVIAG (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| L | Leste |
| N | Norte |
| O | Oeste |
| S | Sul |

### Opções para campo TPAMBNFSE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Produção |
| 2 | Homologação |

### Opções para campo STATUSNFE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Aprovada |
| D | DENEGADA |
| E | Aguardando Autorização |
| I | Enviada |
| M | Não é NF-e |
| null | Não enviada |
| P | Pendente de Retorno |
| R | Aguardando Correção |
| S | Enviada EPEC |
| T | NF-e Terceiro |
| V | Com erro de Validação |

### Opções para campo ISSRETIDO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PENDENTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPIPIEMB (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| I | Incluso |
| N | Extra nota |

### Opções para campo INDPRESNFCE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Não se aplica |
| 1 | 1-Operação presencial |
| 2 | 2-Não presencial, internet |
| 3 | 3-Não presencial, teleatendimento |
| 4 | 4-NFC-e com entrega em domicílio |
| 5 | 5-Presencial, fora do estabelecimento |
| 9 | 9-Não presencial, outros |

### Opções para campo MODENTREGA (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Auto Distribuição |
| F | Multientrega Faturar Para |
| M | Multientrega |
| N | Entrega Direta |
| P | Porta-a-Porta |
| S | Sem Entrega |

### Opções para campo UFADQUIRENTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| AC | Acre |
| AL | Alagoas |
| AM | Amazonas |
| AP | Amapá |
| BA | Bahia |
| CE | Ceará |
| DF | Distrito Federal |
| ES | Espírito Santo |
| GO | Goiás |
| MA | Maranhão |
| MG | Minas Gerais |
| MS | Mato Grosso do Sul |
| MT | Mato Grosso |
| PA | Pará |
| PB | Paraíba |
| PE | Pernambuco |
| PI | Piauí |
| PR | Paraná |
| RJ | Rio de Janeiro |
| RN | Rio G. do Norte |
| RO | Rondônia |
| RR | Roraima |
| RS | Rio G. do Sul |
| SC | Santa Catarina |
| SE | Sergipe |
| SP | São Paulo |
| TO | Tocantins |

### Opções para campo VIATRANSP (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 01 | Marítima |
| 02 | Fluvial |
| 03 | Lacustre |
| 04 | Aérea |
| 05 | Postal |
| 06 | Ferroviária |
| 07 | Rodoviária |
| 08 | Conduto / Rede Transmissão |
| 09 | Meios Próprios |
| 10 | Entrada / Saída ficta |
| 11 | Courier |
| 12 | Handcarry |
| 13 | Por reboque |

### Opções para campo TIPPROCIMP (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| C | Compra e Venda |
| E | Encomenda |
| O | Conta e Ordem |

### Opções para campo PRODUETLOC (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SITUACAOCTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Anulado |
| B | Em Substituição |
| L | Em Anulação |
| N | Normal |
| S | Substituído |

### Opções para campo LOTACAO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TPEMISCTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Normal |
| 3 | Emissão pelo regime especial da NFF |
| 4 | EPEC pela SVC |
| 5 | Contingência FSDA |
| 7 | Autorização pela SVC-RS |
| 8 | Autorização pela SVC-SP |

### Opções para campo TPAMBCTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Produção |
| 2 | Homologação |

### Opções para campo STATUSCTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Aprovada |
| D | DENEGADA |
| E | Aguardando Autoriz. |
| I | Enviada |
| M | Não é CT-e |
| null | Não enviada |
| R | Aguardando Correção |
| S | Enviada EPEC |
| T | CT-e Terceiros |
| V | Com erro de Validação |

### Opções para campo PESOLIQUIMANUAL (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CTELOTACAO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PESOBRUTOMANUAL (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UFEMBARQ (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| AC | Acre |
| AL | Alagoas |
| AM | Amazonas |
| AP | Amapá |
| BA | Bahia |
| CE | Ceará |
| DF | Distrito Federal |
| ES | Espírito Santo |
| GO | Goiás |
| MA | Maranhão |
| MG | Minas Gerais |
| MS | Mato Grosso do Sul |
| MT | Mato Grosso |
| PA | Pará |
| PB | Paraíba |
| PE | Pernambuco |
| PI | Piauí |
| PR | Paraná |
| RJ | Rio de Janeiro |
| RN | Rio Grande do Norte |
| RO | Rondônia |
| RR | Roraima |
| RS | Rio Grande do Sul |
| SC | Santa Catarina |
| SE | Sergipe |
| SP | São Paulo |
| TO | Tocantins |

### Opções para campo APROVADO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODMODDOCNOTA (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Sem Modelo |
| 1 | 01-Nota Fiscal |
| 10 | 10-Conhecimento Aéreo |
| 11 | 11-Conhecimento de Transporte Ferroviário de Cargas |
| 13 | 13-Bilhete de Passagem Rodoviário |
| 14 | 14-Bilhete e Passagem Aquaviário |
| 15 | 15-Bilhete de Passagem e Nota de Bagagem |
| 16 | 16-Bilhete de Passagem Ferroviário |
| 17 | 17-Despacho de Transporte |
| 18 | 18-Resumo Movimento Diário |
| 2 | 02-Nota Fiscal de Venda a Consumidor |
| 20 | 20-Ordem de Coleta de Carga |
| 21 | 21-Nota Fiscal de Serviço de Comunicação |
| 22 | 22-Nota Fiscal de Serviço de Telecomunicações |
| 23 | 23-GNRE |
| 24 | 24-Autorização de Carregamento de Transporte |
| 25 | 25-Manifesto de Carga |
| 26 | 26-Conhecimento de Transporte Multimodal de Cargas |
| 27 | 27-Nota Fiscal De Transporte Ferroviário De Carga |
| 28 | 28-Nota Fiscal/Conta de Fornecimento de Gás Canalizado |
| 29 | 29-Nota Fiscal/Conta De Fornecimento D''água Canalizada |
| 3 | 03-Nota Fiscal de Entrada |
| 4 | 04-Nota Fiscal de Produtor |
| 55 | 55-Nota Fiscal Eletrônica |
| 57 | 57-Conhecimento Transporte Rodoviário Eletrônico |
| 59 | 59-Cupom Fiscal Eletrônico |
| 6 | 06-Nota Fiscal Conta de Energia Elétrica |
| 62 | 62-Nota Fiscal Eletrônica de Serviços de Comunicação |
| 63 | 63-Bilhete de Passagem Eletrônico |
| 65 | 65-Nota Fiscal Eletrônica de Venda a Consumidor |
| 66 | 66-Nota Fiscal de Energia Elétrica Eletrônica |
| 67 | 67-Conhecimento Transporte Rodoviário Eletrônico OS |
| 7 | 07-Nota Fiscal de Serviço de Transporte |
| 8 | 08-Conhecimento de Transporte Rodoviário de Cargas |
| 9 | 09-Conhecimento de Transporte Aquaviário de Cargas |
| 901 | 1B-Nota Fiscal Avulsa |
| 902 | 8B-Conhecimento de Transporte de Cargas Avulso |

### Opções para campo RATEADO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CIF_FOB (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| C | CIF - Contratação do Frete por conta do Remetente |
| D | Transp. Próprio Destinatário |
| F | FOB - Contratação do Frete por conta do Destinatário |
| R | Transp. Próprio Remetente |
| S | Sem Frete |
| T | Terceiros |

### Opções para campo TPFRETAMENTO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Eventual |
| 2 | 2 - Contínuo |

### Opções para campo TPEMISNFE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Sec. da Faz. |
| 2 | Danfe de Segurança |
| 3 | S.C.Amb.Nac. |
| 4 | EPEC |
| 6 | S.V.C.Amb.Nacional |
| 7 | S.V.C.Rio Grande do Sul |
| 9 | Conting.Off-Line NFC-e |

### Opções para campo TIPOPTAGJNFE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | Outros |
| 1 | Venda concessionária |
| 2 | Faturamento direto |
| 3 | Venda direta |

### Opções para campo TPASSINANTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Comercial/Industrial |
| 2 | Poder Público |
| 3 | Residencial/Pessoa física |
| 4 | Público |
| 5 | Semi-Público |
| 6 | Outros |

### Opções para campo STATUSNFSE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Aprovada |
| D | Denegada |
| E | Aguardando Autorização |
| I | Enviada |
| L | Lote Rejeitado |
| N | Não enviada |
| null | Não é NFS-e |
| P | Pendente de Retorno |
| R | Aguardando Correção |
| V | Com erro de Validação |

### Opções para campo TPEMISNFSE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Secretaria municipal da fazenda |
| 2 | Recibo Provisório de Serviços |

### Opções para campo FORMPGTCTE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | Pago |
| 1 | A pagar |
| 2 | Outros |

### Opções para campo CTEGLOBAL (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AD_RELATORIO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Não |

### Opções para campo AD_CHKAVISO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCLIENTESERVCOM (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | 01 - Comercial |
| 2 | 02 - Industrial |
| 3 | 03 - Residencial/Pessoa Física |
| 4 | 04 - Produtor Rural |
| 5 | 05 - Órgão da administração..., nos termos do Convênio ICMS 107/95 |
| 6 | 06 - Prestador de serviço de telecomunicação..., nos termos do Convênio ICMS 17/13 |
| 7 | 07 - Missões Diplomáticas, Repartições Consulares..., nos termos do Convênio ICMS 158/94 |
| 8 | 08 - Igrejas e Templos de qualquer natureza |
| 99 | 99 - Outros não especificados anteriormente |

### Opções para campo AD_TIPOPEDIDO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| Orcamento | Orçamento |

### Opções para campo PERMALTERCENTRAL (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não permite |
| null | Não se aplica |
| S | Permite |

### Opções para campo AD_RASTREIO (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| ENTREGUE | Entregue |

### Opções para campo NOTAPORPEDIDOPDV (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSCFE (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Aprovada |
| C | Não é CF-e |
| E | Erro de Validação |
| I | Enviada |
| N | Não enviada |

### Opções para campo STATUSVM (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Crédito aprovado |
| D | Devolução aprovada |
| E | Erro |
| F | Falha no envio da devolução |
| N | Não Enviada |
| P | Devolução pendente de envio |

### Opções para campo STATUSAUTORIZACAOVM (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Autorizado |
| C | Cancelado |
| E | Expirado |
| U | Utilizado |

### Opções para campo TIPOGUIA (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - GTA - Guia de Trânsito Animal |
| 2 | 2 - TTA - Termo de Trânsito Animal |
| 3 | 3 - DTA - Documento de Transferência Animal |
| 4 | 4 - ATV - Autorização de Trânsito Vegetal |
| 5 | 5 - PTV - Permissão de Trânsito Vegetal |
| 6 | 6 - GTV - Guia de Trânsito Vegetal |
| 7 | 7 - Guia Florestal (DOF, SisFlora - PA e MT ou SIAM - MG) |

### Opções para campo TPRETISS (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Não Retido |
| 2 | Retido pelo Tomador |
| 3 | Retido pelo Intermediário |

### Opções para campo SITUACAONFCOM (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| B | Em Substituição |
| N | Normal |
| S | Substituído |

### Opções para campo NFCOM (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Ajuste |
| C | Complementar |
| D | Devolução |
| M | Convencional (Não Usa NFCom) |
| N | Normal |
| S | Substituição |
| T | Terceiros |

### Opções para campo STATUSNFCOM (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| A | Aprovada |
| E | Aguardando Autorização |
| I | Enviada |
| M | Não é NFCom |
| null | Não enviada |
| P | Pendente de Retorno |
| R | Aguardando Correção |
| T | NFCom Terceiro |
| V | Com erro de Validação |

### Opções para campo TPEMISNFCOM (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Sec. da Faz. |
| 2 | Contingência Offline |

### Opções para campo TPAMBNFCOM (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 1 | Produção |
| 2 | Homologação |

### Opções para campo AD_ERAORCA (Tabela: TGFCAB)
| Valor | Descrição |
|-------|-----------|
| 0 | Não |
| 1 | Sim |


## Tabela: TGFCAB_EXC
### Descrição: Cabeçalho da Nota Excluídas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Número Único da Nota | I |  |
| `CODPARCTRANSPFINAL` | Transportadora Final | I |  |
| `NUMNOTA` | Número da Nota | I |  |
| `DTNEG` | Data de Negociação | H |  |
| `VLRNOTA` | Valor da Nota | F |  |
| `TIPMOV` | Tipo do Movimento | S |  |
| `NT_USERNAME` | Nt_username | S |  |
| `HOSTNAME` | HostName | S |  |
| `DHEXCLUSAO` | Data e Hora da Exclusão | H |  |
| `CODPARC` | Cód. Parceiro Nota | I |  |
| `CODVEND` | Vendedor | I |  |
| `CODEMP` | CODEMP | I |  |
| `CODCENCUS` | Cód.Centro Resultado | I |  |
| `SERIENOTA` | SERIENOTA | S |  |
| `DTFATUR` | DTFATUR | H |  |
| `DTENTSAI` | DTENTSAI | H |  |
| `DTVAL` | DTVAL | H |  |
| `DTMOV` | DTMOV | H |  |
| `DTCONTAB` | DTCONTAB | H |  |
| `HRMOV` | HRMOV | I |  |
| `CODEMPNEGOC` | CODEMPNEGOC | I |  |
| `CODCONTATO` | CODCONTATO | I |  |
| `RATEADO` | RATEADO | S |  |
| `CODVEICULO` | CODVEICULO | I |  |
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `DHTIPOPER` | DHTIPOPER | H |  |
| `CODTIPVENDA` | CODTIPVENDA | I |  |
| `DHTIPVENDA` | DHTIPVENDA | H |  |
| `NUMCOTACAO` | NUMCOTACAO | I |  |
| `COMISSAO` | COMISSAO | F |  |
| `CODMOEDA` | CODMOEDA | I |  |
| `CODOBSPADRAO` | CODOBSPADRAO | I |  |
| `OBSERVACAO` | OBSERVACAO | S |  |
| `VLRSEG` | VLRSEG | F |  |
| `VLRICMSSEG` | VLRICMSSEG | F |  |
| `VLRDESTAQUE` | VLRDESTAQUE | F |  |
| `VLRJURO` | VLRJURO | F |  |
| `VLRVENDOR` | VLRVENDOR | F |  |
| `VLROUTROS` | VLROUTROS | F |  |
| `VLREMB` | VLREMB | F |  |
| `VLRICMSEMB` | VLRICMSEMB | F |  |
| `VLRDESCSERV` | VLRDESCSERV | F |  |
| `IPIEMB` | IPIEMB | F |  |
| `TIPIPIEMB` | TIPIPIEMB | S |  |
| `VLRDESCTOT` | VLRDESCTOT | F |  |
| `VLRDESCTOTITEM` | VLRDESCTOTITEM | F |  |
| `VLRFRETE` | VLRFRETE | F |  |
| `ICMSFRETE` | ICMSFRETE | F |  |
| `VLRFRETETOTAL` | Vlr. Frete Total | F |  |
| `BASEICMSFRETE` | BASEICMSFRETE | F |  |
| `TIPFRETE` | TIPFRETE | S |  |
| `CIF_FOB` | CIF_FOB | S |  |
| `VENCFRETE` | VENCFRETE | H |  |
| `VENCIPI` | VENCIPI | H |  |
| `ORDEMCARGA` | ORDEMCARGA | I |  |
| `SEQCARGA` | SEQCARGA | I |  |
| `KMVEICULO` | KM | I |  |
| `CODPARCTRANSP` | Cód.Parceiro Transportadora | I |  |
| `QTDVOL` | QTDVOL | I |  |
| `PENDENTE` | PENDENTE | S |  |
| `BASEICMS` | BASEICMS | F |  |
| `VLRICMS` | VLRICMS | F |  |
| `BASEIPI` | BASEIPI | F |  |
| `VLRIPI` | VLRIPI | F |  |
| `ISSRETIDO` | ISSRETIDO | S |  |
| `BASEISS` | BASEISS | F |  |
| `VLRISS` | VLRISS | F |  |
| `APROVADO` | APROVADO | S |  |
| `STATUSNOTA` | STATUSNOTA | S |  |
| `IRFRETIDO` | IRFRETIDO | S |  |
| `COMGER` | COMGER | F |  |
| `VLRIRF` | VLRIRF | F |  |
| `DTALTER` | DTALTER | H |  |
| `VOLUME` | VOLUME | S |  |
| `CODPARCDEST` | Cód. Parceiro Dest | I |  |
| `VLRSUBST` | VLRSUBST | F |  |
| `BASESUBSTIT` | BASESUBSTIT | F |  |
| `CODPROJ` | CODPROJ | I |  |
| `NUMCONTRATO` | NUMCONTRATO | I |  |
| `BASEINSS` | BASEINSS | F |  |
| `VLRINSS` | VLRINSS | F |  |
| `VLRREPREDTOT` | VLRREPREDTOT | F |  |
| `PERCDESC` | PERCDESC | F |  |
| `CODPARCREMETENTE` | Cód. Parceiro Remetente | I |  |
| `CODPARCCONSIGNATARIO` | Cód. Parceiro Consignatário | I |  |
| `CODPARCREDESPACHO` | Cód. Parceiro Credespacho | I |  |
| `LOCALCOLETA` | LOCALCOLETA | S |  |
| `LOCALENTREGA` | LOCALENTREGA | S |  |
| `VLRMERCADORIA` | VLRMERCADORIA | F |  |
| `PESO` | PESO | F |  |
| `NOTASCF` | NOTASCF | S |  |
| `CODNAT` | Cód. Natureza | I |  |
| `CODUSU` | Cód. Usuário | I |  |
| `NROREDZ` | Número Redução Z | I |  |
| `CODMAQ` | Máquina | I |  |
| `VLRICMSDIFALREM` | Valor DIFAL UF Remet. | F |  |
| `VLRICMSDIFALDEST` | Valor DIFAL UF Destino | F |  |
| `VLRICMSFCP` | Vlr. ICMS Fundo Comb. Pobreza | F |  |
| `NUMNFSE` | NUMNFSE | S |  |
| `VLRSTFCPINTANT` | Vlr. ST FCP Interno Anterior | F |  |
| `VLRICMSFCPINT` | Vlr. ICMS FCP Interno | F |  |
| `VLRSTFCPINT` | Vlr. ST FCP Interno | F |  |
| `FISTEL` | FISTEL | S |  |
| `NUMCSTC` | Número da Característica de Serviço de Tele/Comunicação | I |  |
| `QTDUSU` | Quantidade de usuário / login | I |  |
| `NUMTERMTEL` | Número de Identificação do Terminal Telefônico | S |  |
| `TIPCLIENTESERVCOM` | Tipo Cliente de Serviços de Comunicação | I | Veja opções na seção OPÇÕES |
| `MD5MODCOMTEL` | MD5MODCOMTEL | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPCLIENTESERVCOM (Tabela: TGFCAB_EXC)
| Valor | Descrição |
|-------|-----------|
| 1 | 01 - Comercial |
| 2 | 02 - Industrial |
| 3 | 03 - Residencial/Pessoa Física |
| 4 | 04 - Produtor Rural |
| 5 | 05 - Órgão da administração..., nos termos do Convênio ICMS 107/95 |
| 6 | 06 - Prestador de serviço de telecomunicação..., nos termos do Convênio ICMS 17/13 |
| 7 | 07 - Missões Diplomáticas, Repartições Consulares..., nos termos do Convênio ICMS 158/94 |
| 8 | 08 - Igrejas e Templos de qualquer natureza |
| 99 | 99 - Outros não especificados anteriormente |


## Tabela: TGFCAN
### Descrição: Nota Cancelada

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDPONTUACAOPARCERIA` | Id de pontuação no parceiro | F |  |
| `NUMNOTA` | Número da Nota | I |  |
| `CODEMP` | Empresa | I |  |
| `SERIENOTA` | Série | S |  |
| `DTNEG` | Dt. de Neg. | D |  |
| `DTFATUR` | Dt. de Fatur. | D |  |
| `DTMOV` | Dt. de Mov. | D |  |
| `MOTCANCEL` | Motivo | S |  |
| `ATUALLIVFIS` | Atualiza Livros Fiscais | S | Veja opções na seção OPÇÕES |
| `ATUALLIVISS` | Atualiza Livro de ISS | S |  |
| `DTCANC` | Dt. de Canc. | D |  |
| `NUNOTA` | Número Único da Nota | I |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `CODMODDOC` | Modelo do Documento | I | Veja opções na seção OPÇÕES |
| `CHAVENFE` | Chave NF-e | S |  |
| `NUMPROTOCNFE` | Nro. Protocolo NF-e | S |  |
| `DHPROTOCNFE` | Dt. Protocolo NF-e | H |  |
| `NUMPROTOCCAN` | Nro. Protocolo Cancelamento | S |  |
| `DHPROTOCCAN` | Dt. Protocolo Cancelamento | H |  |
| `TPEMISNFE` | Emissão NF-e | I |  |
| `VLRNOTA` | Valor da Nota | F |  |
| `CODMAQ` | Idendifica impressora CF | I |  |
| `NROREDZ` | Nro. Redução Z | I |  |
| `NUMREGDPEC` | Nro. Reg. DPEC | S |  |
| `DHREGDPEC` | Dt. Reg. DPEC | H |  |
| `NUMCF` | Nro. Conhec. de Frete | I |  |
| `NATUREZAOPERDES` | Natureza de Operação | S | Veja opções na seção OPÇÕES |
| `SERIENFDES` | Série NF DES-BH | S | Veja opções na seção OPÇÕES |
| `MODELONFDES` | Modelo da Nota Fiscal | S | Veja opções na seção OPÇÕES |
| `NUMNFSE` | Nro. NFS-e | S |  |
| `NUREM` | Remessa | I |  |
| `NUMPROTOCESPONT` | Nro. Protoc. Canc. Esp. | S |  |
| `DHPROTOCESPONT` | Dh. Protoc. Canc. Esp. | H |  |
| `TPAMBNFE` | TPAMBNFE | S |  |
| `CHAVECTE` | Chave CT-e | S |  |
| `NUMPROTOCCTE` | Nro. Protocolo de Autorização | S |  |
| `DHPROTOCCTE` | Dh. Protocolo de Autorização | H |  |
| `NUMPROTOCCANCTE` | Nro. Protocolo de Autorização de Cancelamento | S |  |
| `DHPROTOCCANCTE` | Dh. Protocolo de Autorização de Cancelamento | H |  |
| `TPAMBCTE` | Tipo de Ambiente de CT-e | S | Veja opções na seção OPÇÕES |
| `TPEMISCTE` | Tipo de Emissão de CT-e | I | Veja opções na seção OPÇÕES |
| `NUNOTASUB` | Nro. Unico. Nota Substituída | I |  |
| `TPAMBNFSE` | Ambiente NFS-e | S |  |
| `PROTCANCNFSE` | Protocolo de cancelamento (NFS-e) | S |  |
| `DHCANCPREFNFSE` | Data cancelamento prefeitura (NFS-e) | H |  |
| `TIPCANCNFSE` | Tipo cancelamento NFS-e | S | Veja opções na seção OPÇÕES |
| `NFSECABCEXT` | NFS-e Cancelada Extemporaneamente | S |  |
| `STATUSVM` | Status Venda Mais | S | Veja opções na seção OPÇÕES |
| `NUMPROTOCNFCOM` | Nro. Protocolo NFCom | S |  |
| `NUMPROTOCCANFCOM` | Nro. Cancelamento Protocolo NFCom | S |  |
| `CHAVENFCOM` | Chave NFCom | S |  |
| `TPEMISNFCOM` | Emissão NFCom | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATUALLIVFIS (Tabela: TGFCAN)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| E | Livro de entrada |
| N | Não atualiza |
| S | Livro de saída |

### Opções para campo CODMODDOC (Tabela: TGFCAN)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Sem Modelo |
| 1 | 01-Nota Fiscal |
| 10 | 10-Conhecimento Aéreo |
| 11 | 11-Conhecimento de Transporte Ferroviário de Cargas |
| 13 | 13-Bilhete de Passagem Rodoviário |
| 14 | 14-Bilhete e Passagem Aquaviário |
| 15 | 15-Bilhete de Passagem e Nota de Bagagem |
| 16 | 16-Bilhete de Passagem Ferroviário |
| 17 | 17-Despacho de Transporte |
| 18 | 18-Resumo Movimento Diário |
| 2 | 02-Nota Fiscal de Venda a Consumidor |
| 20 | 20-Ordem de Coleta de Carga |
| 21 | 21-Nota Fiscal de Serviço de Comunicação |
| 22 | 22-Nota Fiscal de Serviço de Telecomunicações |
| 23 | 23-GNRE |
| 24 | 24-Autorização de Carregamento de Transporte |
| 25 | 25-Manifesto de Carga |
| 26 | 26-Conhecimento de Transporte Multimodal de Cargas |
| 27 | 27-Nota Fiscal De Transporte Ferroviário De Carga |
| 28 | 28-Nota Fiscal/Conta de Fornecimento de Gás Canalizado |
| 29 | 29-Nota Fiscal/Conta De Fornecimento D''água Canalizada |
| 3 | 03-Nota Fiscal de Entrada |
| 4 | 04-Nota Fiscal de Produtor |
| 55 | 55-Nota Fiscal Eletrônica |
| 57 | 57-Conhecimento Transporte Rodoviário Eletrônico |
| 59 | 59-Cupom Fiscal Eletrônico |
| 6 | 06-Nota Fiscal Conta de Energia Elétrica |
| 62 | 62-Nota Fiscal Eletrônica de Serviços de Comunicação |
| 63 | 63-Bilhete de Passagem Eletrônico |
| 65 | 65-Nota Fiscal Eletrônica de Venda a Consumidor |
| 66 | 66 - Nota Fiscal de Energia Elétrica Eletrônica |
| 67 | 67-Conhecimento Transporte Eletrônico Outros Serviços |
| 7 | 07-Nota Fiscal de Serviço de Transporte |
| 8 | 08-Conhecimento de Transporte Rodoviário de Cargas |
| 9 | 09-Conhecimento de Transporte Aquaviário de Cargas |
| 901 | 1B-Nota Fiscal Avulsa |
| 902 | 8B-Conhecimento de Transporte de Cargas Avulso |

### Opções para campo NATUREZAOPERDES (Tabela: TGFCAN)
| Valor | Descrição |
|-------|-----------|
| A | Sem Dedução |
| B | Com Dedução |
| C | Isenta de ISSQN |
| D | Devolução/Simples Remessa |
| E | Não Incidência |
| F | Imune |
| G | Construção Civil |
| H | Regime Estimativa |
| I | Sociedade Profissional |
| J | Microempresa |
| K | Depósito em Juízo |
| L | Incentivo a Cultura |
| M | Inscrito na PBH |
| N | Turismo/Fundos |
| O | Intermed./Public. - Isento |
| P | Intermediação / Publicidade |
| Q | Não Tributável |

### Opções para campo SERIENFDES (Tabela: TGFCAN)
| Valor | Descrição |
|-------|-----------|
| AV | NF Avulsa |
| B | Borderô |
| C | C.C.T. |
| CF | Cupom Fiscal |
| G | Contribuintes Dispensados de Utilizar NF |
| IA | Ingresso Autorizado |
| OM | NF de Outro Município |
| OT | Outros Documentos (Pessoa Jurídica) |
| R | RPA ou Recibo (Pessoa Física) |
| RE | Regime Especial |
| S | NF Serviço |
| SF | NF Serviços-Fatura |
| ST | NF Serviços-Conhecimento de Transportes |
| TF | NF Venda e Serviços Transporte-Fatura |
| TP | NF Venda e Serviços Transporte |
| VF | NF Venda e Serviços Modelo 1-Fatura |
| V1 | NF Venda e Serviços Modelo 1 |
| 1A | NF Venda e Serviços Modelo 1A |
| 1F | NF Venda e Serviços Modelo 1A-Fatura |

### Opções para campo MODELONFDES (Tabela: TGFCAN)
| Valor | Descrição |
|-------|-----------|
| _ | Modelo Único para Documento/Série V1, VF, 1A, 1F, TP, TF, CF, AV, G, R, OM, B, C e RE |
| B | Nota de Balcão para Documento/Série OT |
| C | Contrato para Documento/Série OT |
| D | Duplicata para Documento/Série OT |
| E | Série E para Documento/Série S e IA |
| F | Fatura para Documento/Série OT |
| O | Orçamento para Documento/Série OT |
| P | Pedido para Documento/Série OT |
| Q | Tiquete para Documento/Série OT |
| R | Recibo para Documento/Série OT |
| S | Ordem de Serviço para Documento/Série OT |
| T | Outros para Documento/Série OT |
| U | Série Única para Documento/Série S, SF, ST e IA |
| Z | Boleto Bancário - para Documento/Série OT |
| 1 | Série 1 para Documento/Série SF, V1, VF, 1A, 1F, TP e TF |
| 2 | Série 2 para Documento/Série SF, V1, VF, 1A, 1F, TP e TF |
| 3 | Série 3 para Documento/Série SF, V1, VF, 1A, 1F, TP e TF |
| 4 | Série 4 para Documento/Série SF, V1, VF, 1A, 1F, TP e TF |
| 5 | Série 5 para Documento/Série SF, V1, VF, 1A, 1F, TP e TF |
| 6 | Série 6 para Documento/Série SF, V1, VF, 1A, 1F, TP e TF |
| 7 | Série 7 para Documento/Série SF, V1, VF, 1A, 1F, TP e TF |
| 8 | Série 8 para Documento/Série SF, V1, VF, 1A, 1F, TP e TF |
| 9 | Série 9 para Documento/Série SF, V1, VF, 1A, 1F, TP e TF |

### Opções para campo TPAMBCTE (Tabela: TGFCAN)
| Valor | Descrição |
|-------|-----------|
| 1 | Produção |
| 2 | Homologação |

### Opções para campo TPEMISCTE (Tabela: TGFCAN)
| Valor | Descrição |
|-------|-----------|
| 1 | Normal |
| 4 | EPEC pela SVC |
| 5 | Contingência FSDA |
| 7 | Autorização pela SVC-RS |
| 8 | Autorização pela SVC-SP |

### Opções para campo TIPCANCNFSE (Tabela: TGFCAN)
| Valor | Descrição |
|-------|-----------|
| 1 | Via web service |
| 2 | Via web service com valor limite de cancelamento |
| 3 | Via prefeitura com número de protocolo |
| 4 | Via prefeitura sem número de protocolo |

### Opções para campo STATUSVM (Tabela: TGFCAN)
| Valor | Descrição |
|-------|-----------|
| C | Operação cancelada |
| E | Operação não cancelada |
| P | Cancelamento pendente de envio |


## Tabela: TGFCCE
### Descrição: Carta de Correção CT-e

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Único da Nota | I |  |
| `SEQCCE` | Sequência da CC-e | I |  |
| `XMLCCE` | XML da CC-e | C |  |
| `PATHALT` | Path do XML da CC-e | S |  |

## Tabela: TGFCCM
### Descrição: Comissão Multipla

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Número Único Nota | I |  |
| `CODVEND` | Vendedor | I |  |
| `PERCCOM` | Percentual de Comissão | F |  |
| `OBS` | Observação | S |  |
| `AD_TIPO` | TIPO | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo AD_TIPO (Tabela: TGFCCM)
| Valor | Descrição |
|-------|-----------|
| E | Executor |
| I | Indicador |


## Tabela: TGFCER
### Descrição: Certificação da Regra

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TIPO` | Tipo | S |  |
| `DTALTER` | Data de Alteração | H |  |
| `CODUSU` | Cód. Usuário | I |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `CODREGRA` | Regra | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `FILTRAR` | Não Visualizar | S | Veja opções na seção OPÇÕES |
| `RECONTAR` | Permite executar recontagem | S | Veja opções na seção OPÇÕES |
| `CHAVE` | Chave | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFCER)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FILTRAR (Tabela: TGFCER)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECONTAR (Tabela: TGFCER)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFCFO
### Descrição: Código Fiscal de Operações

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCFO` | Código | I |  |
| `DESCRCFO` | Descrição da CFOP | S |  |
| `TRIBUTADASCIAP` | Utilizar nas Tributadas do CIAP | S | Veja opções na seção OPÇÕES |
| `TIPICMS` | ICMS p/ o Livro Fiscal | S | Veja opções na seção OPÇÕES |
| `CODCTACTB` | Conta Contábil | I |  |
| `GRUPOCFO` | Grupo da CFOP | I | Veja opções na seção OPÇÕES |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `CONVPRODUZ` | Convênio Produzir | S | Veja opções na seção OPÇÕES |
| `CALCDIFICMS` | Calcular Diferença de ICMS | S | Veja opções na seção OPÇÕES |
| `DESCONSIDERARCFOREG47` | Desconsiderar CFOP na geração do registro 47 da DIME-SC? | S | Veja opções na seção OPÇÕES |
| `RECBRUTAEFDBLOCOP` | Receita bruta p/EFD Contribuições | S | Veja opções na seção OPÇÕES |
| `TIPOPERPRODEPE` | Tipo de Operação PRODEPE | S | Veja opções na seção OPÇÕES |
| `MOVIMFISICA` | Movimentação Física do Item/Produto (IND_MOV C170 EFD) | S | Veja opções na seção OPÇÕES |
| `EMPCODSIT08EFD` | Empresas para considerar a situação do documento '08' nos EFDs | S |  |
| `RECBRUTACIAP` | Receita Bruta p/ CIAP | S | Veja opções na seção OPÇÕES |
| `INDAQUISICAO` | Indicador de Aquisição | S | Veja opções na seção OPÇÕES |
| `OPERESSACOMP` | Operação com Ressarcimento/Complemento de ST | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TRIBUTADASCIAP (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| B | Base de ICMS |
| C | Considerar config. por CST |
| N | Não Utilizar |
| V | Valor Contábil |

### Opções para campo TIPICMS (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| 1 | Usar da TOP/Empresa |
| 2 | Sem créd/déb - Isentas |
| 3 | Sem créd/deb - Outras |

### Opções para campo GRUPOCFO (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| 0 | 0.00 - Definição Automática |
| 100 | 1.00 - Entrada do estado |
| 200 | 2.00 - Entrada de outro estado |
| 300 | 3.00 - Entrada do exterior |
| 500 | 5.00 - Saída para o estado |
| 600 | 6.00 - Saída para outro estado |
| 700 | 7.00 - Saída para o exterior |

### Opções para campo TIPO (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| C | Compras |
| D | Devoluções e anulações de valores |
| E | Energia Elétrica |
| M | Comunicação |
| O | Outras |
| R | Transportes |
| T | Transferências |
| V | Vendas |

### Opções para campo CONVPRODUZ (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCDIFICMS (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCONSIDERARCFOREG47 (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECBRUTAEFDBLOCOP (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| N | Não afeta |
| S | Soma |
| T | Subtrai |

### Opções para campo TIPOPERPRODEPE (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| N | Operação Não Incentivada |
| null | Operação Incentivada |

### Opções para campo MOVIMFISICA (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| null | Não se aplica |
| S | Sim |

### Opções para campo RECBRUTACIAP (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| B | Buscar da TOP |
| N | Não afeta |
| S | Soma |
| T | Subtrai |

### Opções para campo INDAQUISICAO (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| 1 | 1-Aquisição da produção de produtor rural pessoa física ou segurado especial em geral |
| 2 | 2-Aquisição da produção de produtor rural PF ou segurado especial em geral por Entidade do PAA |
| 3 | 3-Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA |
| 4 | 4-Aquisição de produção de produtor rural pessoa física ou segurado especial em geral |
| 5 | 5-Aquisição de produção de produtor rural pessoa física ou segurado especial por entidade do PAA |
| 6 | 6-Aquisição de produção de produtor rural pessoa jurídica por entidade do PAA - Produção isenta |
| 7 | 7-Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação |

### Opções para campo OPERESSACOMP (Tabela: TGFCFO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFCGM
### Descrição: TABELA TGFCGM

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód. Empresa | I |  |
| `ANO` | Ano | I |  |
| `MES` | Mês | I |  |
| `DTREF` | Dt. Referência | H |  |
| `PERCCFFAB` | % C. F. Fab. Próp. | F |  |
| `PERCCFOUTROS` | % C.F. Outros | F |  |
| `PERCCFSERVICO` | % C. F. Serviço | F |  |
| `PERCCOFINS` | % COFINS | F |  |
| `PERCCSL` | % CSLL | F |  |
| `PERCCUSVAR` | % C. Variável | F |  |
| `PERCCVARSEMST` | % C. Variável sem ST | F |  |
| `PERCMARGEM` | % Outros | F |  |
| `PERCPIS` | % PIS | F |  |
| `PERCCFFABCALC` | % C. F. Fab. Próp. Calc. | F |  |
| `PERCCFOUTROSCALC` | % C.F. Outros Calc. | F |  |
| `PERCCFSERVICOCALC` | % C. F. Serviço Calc. | F |  |
| `TEMPERCPARTSIMP` | Utiliza % Partilha Simples | S | Veja opções na seção OPÇÕES |
| `PERCIRPJ` | % IRPJ | F |  |
| `PERCCPP` | % CPP | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo TEMPERCPARTSIMP (Tabela: TGFCGM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFCINFCOM
### Descrição: Código de Itens da NFCom

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Codigo | S |  |
| `DESCRICAO` | Descrição | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFCINFCOM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFCNF
### Descrição: Contingências

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUCONTING` | Nro. Contingência | I |  |
| `CODEMP` | Empresa | I |  |
| `TIPODOC` | Tipo de documento | S | Veja opções na seção OPÇÕES |
| `TPEMISNFE` | Emissão NF-e | I | Veja opções na seção OPÇÕES |
| `TPEMISNFCOM` | Emissão NFCom | I | Veja opções na seção OPÇÕES |
| `TPEMISCTE` | Emissão CT-e | I | Veja opções na seção OPÇÕES |
| `TIPOCONTING` | Tipo Contingência | S | Veja opções na seção OPÇÕES |
| `DHABERTURA` | Dh. Abertura | H |  |
| `DHFECHAMENTO` | Dh. Fechamento | H |  |
| `JUSTIFICATIVA` | Justificativa | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DHALTER` | Dh. Alter | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPODOC (Tabela: TGFCNF)
| Valor | Descrição |
|-------|-----------|
| C | CT-e |
| N | NF-e |

### Opções para campo TPEMISNFE (Tabela: TGFCNF)
| Valor | Descrição |
|-------|-----------|
| 2 | Danfe de Segurança |
| 3 | S.C.Amb.Nac. |
| 4 | DPEC |
| 6 | S.V.Ambiente Nacional |
| 7 | S.V. do Rio Grande do Sul |
| 9 | Conting.Off-Line NFC-e |

### Opções para campo TPEMISNFCOM (Tabela: TGFCNF)
| Valor | Descrição |
|-------|-----------|
| 2 | Contingência Offline |

### Opções para campo TPEMISCTE (Tabela: TGFCNF)
| Valor | Descrição |
|-------|-----------|
| 4 | EPEC - CT-e |
| 5 | FSDA - CT-e |

### Opções para campo TIPOCONTING (Tabela: TGFCNF)
| Valor | Descrição |
|-------|-----------|
| A | Automática |
| M | Manual |


## Tabela: TGFCOM
### Descrição: Valores de Comissões de Vendedores

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODVEND` | Cód. Vendedor | I |  |
| `NUFINORIG` | Financeiro de origem | I |  |
| `NUNOTAORIG` | Nota de origem | I |  |
| `NUFIN` | Número Financeiro | I |  |
| `VLRCOM` | Valor da comissão | F |  |
| `REFERENCIA` | Referência | H |  |
| `CODEMP` | Empresa | I |  |
| `CODFUNC` | Funcionário | I |  |
| `CODEVENTO` | Evento | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `NUMOSORIG` | Número OS Origem | I |  |
| `NUMITEMORIG` | Número Item Origem | I |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `VLRHORA` | Valor Hora | F |  |
| `QTDHORA` | Quantidade de Horas | I |  |
| `VLRHORAEXTRA` | Valor hora extra | F |  |
| `QTDHORAEXTRA` | Quantidade de Horas extras | I |  |
| `INDICEPRODUTIVIDADE` | Índice de Produtividade | F |  |
| `CODFORM` | Cód. Fórmula | I |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DHALTER` | Data do fechamento | H |  |
| `NUFECHAMENTO` | Nro do fechamento da comissão | I |  |
| `VLRRESIDUOCOM` | Resíduo de Comissão | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TGFCOM)
| Valor | Descrição |
|-------|-----------|
| M | Múltipla |
| O | Outros |
| S | Serviço |


## Tabela: TGFCONTR
### Descrição: Contratante MDF-e

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUVIAG` | Nro. Viagem | I |  |
| `SEQMDFE` | Sequência do manifesto | I |  |
| `CODPARCCONTR` | Cód. Parceiro Contratante | I |  |

## Tabela: TGFCPL
### Descrição: Dados Complementares de Parceiros

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `SEQENTREGA` | Sequência de entrega | I |  |
| `CEPENTREGA` | CEP p/ entrega | S |  |
| `CODINDNIF` | Indicativo do NIF | I | Veja opções na seção OPÇÕES |
| `NUMINDNIF` | Nro. do NIF – Número de Identificação Fiscal | S |  |
| `CODENDENTREGA` | Endereço p/ entrega | I |  |
| `TPFONTEPAG` | Tipo Relação fonte pagadora | I | Veja opções na seção OPÇÕES |
| `NUMENTREGA` | Número entrega | S |  |
| `COMPLENTREGA` | Complemento entrega | S |  |
| `TPIRRFEXT` | Tributação IRRF - Exterior REINF | I | Veja opções na seção OPÇÕES |
| `INFOISENIMUNI` | Informações sobre isenção e imunidade | I | Veja opções na seção OPÇÕES |
| `CODBAIENTREGA` | Bairro p/ entrega | I |  |
| `CODCIDENTREGA` | Cód. Cidade Entrega | I |  |
| `CEPRECEB` | CEP p/ recebimento | S |  |
| `CODENDRECEB` | Endereço p/ recebimento | I |  |
| `NUMRECEB` | Número recebimento | S |  |
| `COMPLRECEB` | Complemento recebimento | S |  |
| `CODBAIRECEB` | Bairro p/ recebimento | I |  |
| `CODCIDRECEB` | Cód. Cidade Recebimento | I |  |
| `LOCALTRAB` | Local de trabalho | S |  |
| `CEPTRAB` | CEP do trabalho | S |  |
| `CODENDTRAB` | Endereço do trabalho | I |  |
| `NUMTRAB` | Número trabalho | S |  |
| `COMPLTRAB` | Complemento trabalho | S |  |
| `CODBAITRAB` | Bairro do trabalho | I |  |
| `CODCIDTRAB` | Cód. Cidade Trabalho | I |  |
| `TELTRAB` | Telefone do trabalho | S |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `TEMPORESID` | Data ocupação residência | D |  |
| `CODMOEDARENDA` | Moeda p/ renda | I |  |
| `CODPARCTRANSP` | Cód. Parceiro Transportadora preferencial | I |  |
| `NATURALIDADE` | Naturalidade | I |  |
| `NACIONALIDADE` | Nacionalidade do parceiro | I |  |
| `EXIGEPEDIDO` | Exige pedido na OS | S | Veja opções na seção OPÇÕES |
| `ISENTOTAXAMINBOLETA` | Isento taxa boleto | S | Veja opções na seção OPÇÕES |
| `CODMOEDALIM` | Moeda para limite | I |  |
| `IMAGEM` | Imagem | B |  |
| `CONJUGE` | Cônjuge | S |  |
| `RAMAL` | Ramal | I |  |
| `DIAPAG` | Dia para pagamento | I |  |
| `DIASEMANAPAG` | Dia da semana para pagamento | I | Veja opções na seção OPÇÕES |
| `PLACAVEICULO` | Placa do veículo | S |  |
| `NROCNH` | Número da CNH | S |  |
| `VENCIMENTOCNH` | Vencimento da CNH | H |  |
| `CATEGORIACNH` | Categoria da CNH | S |  |
| `SEQVISITA` | Sequência de visita | I |  |
| `CODSUFRAMA` | Código SUFRAMA | S |  |
| `VIATRANSP` | Via de transporte | S |  |
| `CODTABCOT` | Tabela p/ usar módulo cotação | I |  |
| `DTADM` | Data de admissão | H |  |
| `GRUPODESCPARC` | Grupo Desconto Parceiro | S |  |
| `IDENTIFICACAO` | Identificação do Parceiro | S |  |
| `MAE` | Mãe | S |  |
| `PAI` | Pai | S |  |
| `TIPMORADIA` | Tipo imóvel/moradia | S | Veja opções na seção OPÇÕES |
| `SUGTIPNEGENTR` | Sugestão Entrada/Cotação | I |  |
| `RENDAMENSAL` | Renda mensal | F |  |
| `SUGTIPNEGSAID` | Sugestão Saída | I |  |
| `CODUSU` | Cód. Usuário | I |  |
| `CODCRED` | Fórm.p/Cálculo Lim.Crédito | I |  |
| `USASAIDAFATPER` | Usa no Fat. por Período? | S | Veja opções na seção OPÇÕES |
| `DTALTER` | Data de Alteração | H |  |
| `LIMCREDAUTOM` | Efetiva Lim.Créd.Calc.automaticamente? | S | Veja opções na seção OPÇÕES |
| `FATMIN` | Faturamento Mínimo | F |  |
| `GERARFRETE` | Gerar Conhec.Transp. | S | Veja opções na seção OPÇÕES |
| `MULTHORAEXTRA` | Mult. por Hora Extra | F |  |
| `CREA` | Número CREA | S |  |
| `DTCREA` | Data de Registro CREA | H |  |
| `UFCREA` | UF CREA expedidor | S |  |
| `LOGISTICA` | Logística | S |  |
| `CODVOLFAT` | CODVOLFAT | S |  |
| `LATITUDEENTREGA` | Latitude p/ entrega | S |  |
| `LONGITUDEENTREGA` | Longitude p/ entrega | S |  |
| `SITCADSUFRAMA` | Situação Cadastral SUFRAMA | S | Veja opções na seção OPÇÕES |
| `DHCADSUFRAMA` | Data/Hora da Última Consulta SUFRAMA | H |  |
| `SEMREPREDAGRO` | Desconsidera desoneração p/uso agropecuário (NF-e terceiros) | S | Veja opções na seção OPÇÕES |
| `DIAPAG2` | Dia 2 | I |  |
| `DIAPAG3` | Dia 3 | I |  |
| `DIAPAG4` | Dia 4 | I |  |
| `DIAPAG5` | Dia 5 | I |  |
| `DIAPAG6` | Dia 6 | I |  |
| `TEMSUFRAMAPISCOF` | Possui Suframa para PIS/COFINS | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo CODINDNIF (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Beneficiário com NIF |
| 2 | 2 - Beneficiário dispensado do NIF |
| 3 | 3 - País não exige NIF |

### Opções para campo TPFONTEPAG (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| 500 | 500 - Matriz da beneficiária no exterior |
| 510 | 510 - Filial, sucursal ou agência de beneficiária no exterior |
| 520 | 520 - Controlada ou Coligada da beneficiária no exterior, Lei no 6.404, de 15 de dezembro de 1976 |
| 530 | 530 - Controladora ou Coligada da beneficiária no exterior, Lei no 6.404, de 1976 |
| 540 | 540 - Sob controle societário/admin. comum ou ao menos 10% capital de cada, pertencer a mesma PF/PJ |
| 550 | 550 - Particip. soc. capital de 3ªPJ, soma como controladoras ou coligadas da Lei no 6.404, de 1976 |
| 560 | 560 - Contrato exclusividade agente, distrib ou concessionário nas op. bens, serviços e direitos |
| 570 | 570 - Acordo de atuação conjunta |
| 900 | 900 - Não há relação entre a fonte pagadora e a beneficiária no exterior |

### Opções para campo TPIRRFEXT (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| 40 | 40 - Não retenção do IRRF - isenção estabelecida em convênio |
| 41 | 41 - Não retenção do IRRF - isenção prevista em lei interna |
| 42 | 42 - Não retenção do IRRF - alíquota zero prevista em lei interna |
| 43 | 43 - Não retenção do IRRF - pagamento antecipado do imposto |
| 44 | 44 - Não retenção do IRRF - medida Judicial |
| 50 | 50 - Não retenção do IRRF - outras hipóteses |

### Opções para campo INFOISENIMUNI (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Entidade não isenta/não imune - Tributação normal |
| 2 | 2 - Instituição de educação e assistência social sem fins lucrativos art 12 Lei 9532 de 10 dez 1997 |
| 3 | 3 - Instituição filantrópica, recreativa, cultural, científico e assoc. civis, art 15 Lei 9.532/1997 |

### Opções para campo EXIGEPEDIDO (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ISENTOTAXAMINBOLETA (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIASEMANAPAG (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| 1 | Indefinido |
| 2 | Segunda-feira |
| 3 | Terça-feira |
| 4 | Quarta-feira |
| 5 | Quinta-feira |
| 6 | Sexta-feira |

### Opções para campo TIPMORADIA (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| A | Alugado |
| F | Financiado |
| O | Outros com despesa |
| P | Próprio |
| S | Outros sem despesa |

### Opções para campo USASAIDAFATPER (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo LIMCREDAUTOM (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERARFRETE (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SITCADSUFRAMA (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Validado |
| 1 | Bloqueada |
| 2 | Habilitada |
| 3 | Não encontrada |

### Opções para campo SEMREPREDAGRO (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMSUFRAMAPISCOF (Tabela: TGFCPL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFCTE
### Descrição: GF Contagem de Estoque

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPROD` | Produto | I |  |
| `CODVOL` | Unidade | S |  |
| `QTDEST` | Estoque | F |  |
| `DTCONTAGEM` | Data contagem | D |  |
| `CONTROLE` | Controle | S |  |
| `CODLOCAL` | Local | I |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `CODPARC` | Cód. Parceiro | I |  |
| `CODEMP` | Empresa | I |  |
| `DTVAL` | Dt. Validade | D |  |
| `NOMEARQBOMI` | NOMEARQBOMI | S |  |
| `DHCONFBOMI` | DHCONFBOMI | H |  |
| `ERROCONFBOMI` | ERROCONFBOMI | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `QTDESTUNCAD` | Qtd. Unidade Padrão | F |  |
| `NUIVT` | Inventário WMS | I |  |
| `DTFABRICACAO` | Dt. Fabricação | D |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TGFCTE)
| Valor | Descrição |
|-------|-----------|
| P | Próprio |
| T | Terceiros |


## Tabela: TGFCTENT
### Descrição: Nota Técnica CTe

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Empresa | I |  |
| `ATIVONT` | Ativo | S | Veja opções na seção OPÇÕES |
| `VERSAONT` | Versão Nota Técnica | S | Veja opções na seção OPÇÕES |
| `DTENTPROD` | Data de Produção | H |  |
| `DTENTHOMOLOG` | Data de Homologação | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVONT (Tabela: TGFCTENT)
| Valor | Descrição |
|-------|-----------|
| N | Nao |
| S | Sim |

### Opções para campo VERSAONT (Tabela: TGFCTENT)
| Valor | Descrição |
|-------|-----------|
| 0 | Anterior |
| 1 | Nota Técnica 2024.001 - v1.00 |
| 2 | Nota Técnica 2024.004 - v1.04 |


## Tabela: TGFCTT
### Descrição: Contatos dos Parceiros

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCONTATO` | Contato | I |  |
| `TIPPESSOA` | Tipo de pessoa | S | Veja opções na seção OPÇÕES |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `NOMECONTATO` | Nome Contato | S |  |
| `TELEFONE` | Telefone | S |  |
| `TELRESID` | Telefone Residencial | S |  |
| `NIVELCOB` | Nível p/cobrança | I |  |
| `CARGO` | Cargo | S |  |
| `EMAIL` | Email | S |  |
| `APELIDO` | Apelido | S |  |
| `DTNASC` | Data Nascimento | D |  |
| `CPF` | CPF | S |  |
| `CNPJ` | CNPJ | S |  |
| `INSCESTAD` | Inscrição Estadual | S |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `CEP` | CEP | S |  |
| `CODCID` | Cód. Cidade | I |  |
| `CODBAI` | Bairro | I |  |
| `CODEND` | Endereço | I |  |
| `NUMEND` | Número | S |  |
| `COMPLEMENTO` | Complemento | S |  |
| `FAX` | Fax | S |  |
| `RAMAL` | Ramal | I |  |
| `CELULAR` | Celular | S |  |
| `DTCAD` | Data Cadastro | H |  |
| `PRIORIDADE` | Prioridade | I |  |
| `POSSUIACESSOBT` | Possui Acesso Banco Talentos | S | Veja opções na seção OPÇÕES |
| `SENHAACESSO` | Senha de acesso | S |  |
| `CODUSU` | Cód. Usuário B2B | I |  |
| `RECEBENOTAEMAIL` | Recebe Nota por email | S | Veja opções na seção OPÇÕES |
| `RECEBEBOLETOEMAIL` | Recebe boleto/Pix p/ email | S | Veja opções na seção OPÇÕES |
| `SOCIO` | Sócio | S | Veja opções na seção OPÇÕES |
| `LATITUDE` | Latitude | S |  |
| `LONGITUDE` | Longitude | S |  |
| `CODREG` | Cód. Região | I |  |
| `RESPCOBRANCA` | Responsável pela cobrança | S | Veja opções na seção OPÇÕES |
| `TIMRG` | RG | S |  |
| `ENVIANOTIFCOTA` | Enviar notificações de cotação? | S | Veja opções na seção OPÇÕES |
| `TIMPROFISSAO` | Profissão | I |  |
| `HABPLANENTCESTAS` | Participa plan. entrega cesta | S | Veja opções na seção OPÇÕES |
| `TIMNACIONALIDAD` | Nacionalidade | I |  |
| `TIMAGENCIA` | Agência | S |  |
| `QTDENTREGACESTAS` | Quantidade Cestas | I |  |
| `RECEMAILIMPPED` | Recebe e-mails de importação de pedidos | S | Veja opções na seção OPÇÕES |
| `TIMBANCO` | Banco | I |  |
| `TIMTIPO` | Tipo de Conta | I | Veja opções na seção OPÇÕES |
| `TIMCONTA` | Conta | S |  |
| `TIMBENEFICIARIO` | Benef. Repasse | S | Veja opções na seção OPÇÕES |
| `TIMPROCURADOR` | Procurador | I |  |
| `TIMREPRESENTANTE` | Representante | S | Veja opções na seção OPÇÕES |
| `AD_OBSERVACAO` | OBSERVACAO | C |  |
| `DHALTER` | Dt. Alteração | H |  |
| `CODUSUALT` | Cód. Usuário Alteração | I |  |
| `AD_NOTA` | Único | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPPESSOA (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| F | Física |
| J | Jurídica |

### Opções para campo ATIVO (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo POSSUIACESSOBT (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECEBENOTAEMAIL (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECEBEBOLETOEMAIL (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SOCIO (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RESPCOBRANCA (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVIANOTIFCOTA (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo HABPLANENTCESTAS (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECEMAILIMPPED (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMTIPO (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| 0 | Corrente |
| 1 | Poupança |
| 2 | Aplicação |

### Opções para campo TIMBENEFICIARIO (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | NÃO |
| S | SIM |

### Opções para campo TIMREPRESENTANTE (Tabela: TGFCTT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFCUS
### Descrição: Custos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPROD` | Produto | I |  |
| `DTATUAL` | Data Atualização | D |  |
| `CUSMEDICM` | Custo Médio com ICMS | F |  |
| `CUSSEMICM` | Custo Médio sem ICMS | F |  |
| `CUSREP` | Custo de Reposição | F |  |
| `CUSVARIAVEL` | Custo Variável | F |  |
| `CUSGER` | Custo Gerencial | F |  |
| `CUSMED` | Custo Médio Gerencial | F |  |
| `VLRVENDAFIXO` | Valor de Venda Fixo | F |  |
| `ENTRADACOMICMS` | Entrada com ICMS | F |  |
| `ENTRADASEMICMS` | Entrada sem ICMS | F |  |
| `CODLOCAL` | Local | I |  |
| `CONTROLE` | Controle | S |  |
| `CODEMP` | Empresa | I |  |
| `QTDNEG` | Quantidade Negociada | F |  |
| `AUTOMATICO` | Automático | S | Veja opções na seção OPÇÕES |
| `ALTPRECO` | Altera Preço? | S | Veja opções na seção OPÇÕES |
| `NUNOTA` | Nro. Nota | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `TOTALCOMICMS` | Total com ICMS | F |  |
| `TOTALSEMICMS` | Total sem ICMS | F |  |
| `TOTALCOMICMSANT` | Total com ICMS Antigo | F |  |
| `TOTALSEMICMSANT` | Total sem ICMS Antigo | F |  |
| `CUSMEDCALC` | Custo Médio Calculado | S | Veja opções na seção OPÇÕES |
| `PROCESSO` | Processo | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo AUTOMATICO (Tabela: TGFCUS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALTPRECO (Tabela: TGFCUS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CUSMEDCALC (Tabela: TGFCUS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFCUSITE
### Descrição: Custo Item

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Nota | I |  |
| `SEQUENCIA` | Sequencia | I |  |
| `CODPROD` | Produto | I |  |
| `CODEMP` | Empresa | I |  |
| `CODLOCAL` | Local | I |  |
| `CONTROLE` | Controle | S |  |
| `DTATUAL` | DTATUAL | H |  |
| `CUSGER` | CUSGER | F |  |
| `CUSVARIAVEL` | Custo variável | F |  |
| `CUSREP` | CUSREP | F |  |
| `ENTRADACOMICMS` | ENTRADACOMICMS | F |  |
| `ENTRADASEMICMS` | ENTRADASEMICMS | F |  |
| `QTDNEG` | Qtd. Negociada | F |  |
| `FAMILIA` | FAMILIA | S |  |
| `ALTPRECO` | Alt. Preço Igual | S |  |
| `TIPONOTA` | TIPONOTA | S |  |
| `SINAL` | SINAL | I |  |
| `COMPLCUST` | Complemento de Custo | I |  |

## Tabela: TGFDES
### Descrição: Descontos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TIPGRUPOPROD` | Tipo Desconto Produto | S | Veja opções na seção OPÇÕES |
| `DTINICIAL` | Data Inicial | D |  |
| `DTFINAL` | Data Final | D |  |
| `CODEMP` | Empresa | I |  |
| `TIPGRUPO` | Tipo Grupo | S | Veja opções na seção OPÇÕES |
| `GRUPODESCPARC` | Grupo Desconto Parceiro | S |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `GRUPODESCPROD` | Grupo Desconto Produto/Serviço | S |  |
| `CODPROD` | Produto | I |  |
| `CODLOCAL` | Local | I |  |
| `PERCENTUAL` | Percentual | F |  |
| `CODVOL` | Unidade | S |  |
| `NUVERSAO` | NUVERSAO | I |  |
| `VLRDESC` | Valor do desconto | F |  |
| `VLRVENDA` | Valor de venda | F |  |
| `PERCDESCBONIF` | % Desc. Bonificação | F |  |
| `TIPPROMOCAO` | Tipo Promoção | S |  |
| `AVISARVCT` | Avisar Vencimento | S | Veja opções na seção OPÇÕES |
| `DESCRPROMOCAO` | Descrição | S |  |
| `ATUNUVERSAO` | ATUNUVERSAO | S |  |
| `GRUPODESCVEND` | Grupo Desconto Vendedor | S |  |
| `NUPROMOCAO` | Nro. único | I |  |
| `CODVEND` | Vendedor | I |  |
| `USADESCQTD` | Usa desconto por quantidade | S | Veja opções na seção OPÇÕES |
| `USADESCESP` | Usa desconto especial | S | Veja opções na seção OPÇÕES |
| `CODTAB` | Atua sobre a tabela de preço | I |  |
| `LIQUIDACAO` | Liquidação | S | Veja opções na seção OPÇÕES |
| `APLICDESCPORLOCAL` | Aplicar desconto por local | S | Veja opções na seção OPÇÕES |
| `AD_COMISSAO` | Comissão | F |  |
| `USADESCCTRL` | Usa desconto por controle | S | Veja opções na seção OPÇÕES |
| `CONTROLE` | Controle | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPGRUPOPROD (Tabela: TGFDES)
| Valor | Descrição |
|-------|-----------|
| G | Grupo de Produto |
| P | Produto |
| T | Todos |

### Opções para campo TIPGRUPO (Tabela: TGFDES)
| Valor | Descrição |
|-------|-----------|
| D | Grupo Parceiro |
| G | Grupo Vendedor |
| P | Parceiro |
| T | Todos |
| V | Vendedor |

### Opções para campo AVISARVCT (Tabela: TGFDES)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USADESCQTD (Tabela: TGFDES)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USADESCESP (Tabela: TGFDES)
| Valor | Descrição |
|-------|-----------|
| 0 | Não |
| 1 | Sim |

### Opções para campo LIQUIDACAO (Tabela: TGFDES)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APLICDESCPORLOCAL (Tabela: TGFDES)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USADESCCTRL (Tabela: TGFDES)
| Valor | Descrição |
|-------|-----------|
| 0 | Não |
| 1 | Sim |


## Tabela: TGFDFPI
### Descrição: Documentos Referenciados pelo Portal de Importação

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUARQUIVO` | Código | I |  |
| `CHAVEREF` | Chave do Documento | S |  |

## Tabela: TGFDIN
### Descrição: Impostos Item de nota

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Único Nota | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `CODIMP` | Imposto | I | Veja opções na seção OPÇÕES |
| `CODINC` | Incidência | I | Veja opções na seção OPÇÕES |
| `BASE` | Base de Cálculo | F |  |
| `BASERED` | Base Cálc.Reduzida | F |  |
| `VLRREPRED` | Vlr.Repasse de Redução | F |  |
| `PAUTA` | Pauta | F |  |
| `ALIQUOTA` | Alíquota | F |  |
| `IDALIQ` | Código Alíquota | I |  |
| `VALOR` | Valor | F |  |
| `ALIQDESPACESS` | Alíquota Despesas Acessórias | F |  |
| `TIPO` | Tipo Retenção | I | Veja opções na seção OPÇÕES |
| `TPIRRFEXT` | Tributação IRRF - Exterior REINF | I | Veja opções na seção OPÇÕES |
| `VLRCRED` | Vlr.Crédito | F |  |
| `CST` | Cst/Csosn | I |  |
| `CODNATREND` | Código Natureza de Rendimento | I |  |
| `RETEMFIN` | Retém Financeiro | S | Veja opções na seção OPÇÕES |
| `PERCVLR` | Percentual / Valor | S | Veja opções na seção OPÇÕES |
| `COMIVA` | Tem IVA | S | Veja opções na seção OPÇÕES |
| `IVA` | IVA | F |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DHALTER` | Dt.Alteração | H |  |
| `DIGITADO` | Digitado | S | Veja opções na seção OPÇÕES |
| `TIPODEDISS` | Tipo Ded. ISS | S |  |
| `CODTRIBMUNISS` | Cod. Trib. Município | S |  |
| `CODLST` | Tipo de Serviço | I |  |
| `PERCREDBASE` | Perc.Red.base | F |  |
| `ALIQUOTANORMAL` | Alíquota Normal | F |  |
| `ALIQINTDEST` | Alíq. Interna Destino | F |  |
| `PERCPARTDIFAL` | Percentual de Partilha DIFAL | F |  |
| `VLRDIFALDEST` | Valor DIFAL UF Destino | F |  |
| `VLRDIFALREM` | Valor DIFAL UF Remet. | F |  |
| `PERCFCP` | Perc. para Fundo Comb. Pobreza | F |  |
| `VLRFCP` | Vlr. para Fundo Comb. Pobreza | F |  |
| `BASEDIFAL` | Base Difal | F |  |
| `TIPCALCDIFAL` | Tipo de Cálculo do DIFAL | I | Veja opções na seção OPÇÕES |
| `BASEFCP` | Base para Fundo Comb. Pobreza | F |  |
| `BASEFCPINT` | Base FCP Interno | F |  |
| `PERCFCPINT` | % FCP Interno | F |  |
| `VLRFCPINT` | Vlr. FCP Interno | F |  |
| `ALIQPARADIFAL` | Alíquota para cálculo do DIFAL | F |  |
| `VLRICMSPARADIFAL` | Vlr. Icms Para Difal | F |  |
| `TIPOINSSESPECIAL` | Tipo de INSS Especial | S | Veja opções na seção OPÇÕES |
| `VLRREPDIFALFCP` | Vlr. Repasse Difal e Fcp | F |  |
| `PERCINSSESPECIAL` | % INSS Especial | F |  |
| `VLRINSSESPECIAL` | Vlr. INSS Especial | F |  |
| `ALIQDIFERENCIAL` | Alíquota de Diferencial | F |  |
| `VALORDIFERENCIAL` | Valor de Diferencial | F |  |
| `PERCREDBASEEFET` | Perc. Red. base Efetivo | F |  |
| `BASEREDEFET` | Base Cálc.Reduzida Efetivo | F |  |
| `ALIQUOTAEFET` | Alíquota Efetivo | F |  |
| `VALOREFET` | Valor Efetivo | F |  |
| `PERCREDVLRIPI` | % Redução de Vlr. IPI | F |  |
| `VLRREPREDSEMDESC` | Vlr. redução sem desconto | F |  |
| `BASENORMDIFICMS` | Base Normal Diferimento ICMS | F |  |
| `ALIQUOTADESON` | Alíquota PIS/COFINS Desonerados | F |  |
| `VALORDESON` | Valor PIS/COFINS Desonerados | F |  |
| `TIPCALCFCPESPEC` | Tipo de Cálculo de FCP Específico | I | Veja opções na seção OPÇÕES |
| `PERCALIQADREMICMS` | % Redução Alíquota ad rem ICMS | F |  |
| `MOTREDADREM` | Motivo Redução do ad rem | I |  |
| `VLRICMSMONODEV` | Valor do ICMS Monofásico Devido | F |  |
| `VLRICMSMONODIF` | Valor ICMS Monofásico Diferido | F |  |
| `PERCREDPR` | Percentual do Crédito Presumido | F |  |
| `CODBEN` | Código de Benefício Fiscal de Crédito Presumido na UF aplicado ao item | S |  |
| `VLRCREDPR` | Valor do Crédito Presumido | F |  |
| `SOMARPISCOFINSST` | Indica se o valor do PIS/COFINS ST compõe o valor total da NF-e | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo CODIMP (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| 1 | ICMS |
| 10 | IRPJ |
| 11 | CPP |
| 2 | ST |
| 3 | IPI |
| 4 | ISS |
| 5 | INSS |
| 6 | PIS |
| 7 | COFINS |
| 8 | IRF |
| 9 | CSSL |

### Opções para campo CODINC (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| 0 | Geral |
| 1 | Produto |
| 2 | Serviço |
| 3 | Frete |
| 4 | Seguro |
| 5 | Destaque |
| 6 | Embalagem |
| 7 | Juro |
| 8 | Desconto |

### Opções para campo TIPO (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Aplicado |
| -1 | Retido |
| 1 | Não Retido |

### Opções para campo TPIRRFEXT (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| 10 | 10 - Retenção do IRRF - Alíquota padrão |
| 11 | 11 - Retenção do IRRF - Alíquota da tabela progressiva |
| 12 | 12 - Retenção do IRRF - Alíquota diferenciada (países com tributação favorecida) |
| 13 | 13 - Retenção do IRRF - Alíquota limitada conforme cláusula em convênio |
| 30 | 30 - Retenção do IRRF - Outras hipóteses |

### Opções para campo RETEMFIN (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERCVLR (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| P | Percentual |
| V | Valor |

### Opções para campo COMIVA (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIGITADO (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCALCDIFAL (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Sem considerar Redução da Base |
| 1 | 1 - Com redução da base aplicada na base |
| 10 | 10 - Cálculo da base, valor do DIFAL e do FCP por fórmula |
| 2 | 2 - Com redução da base aplicada na alíquota |
| 3 | 3 - ICMS Interestadual calculado sob a BC do DIFAL |
| 4 | 4 - Cálculo do DIFAL com ICMS Destino por dentro |
| 5 | 5 - Cálculo do DIFAL Convênio 142/2018 |
| 6 | 6 - Cálculo do DIFAL com a redução do ICMS Próprio |
| 7 | 7 - ICMS Difal base dupla UF Sergipe |
| 8 | 8 - Base de cálculo do DIFAL por fórmula |
| 9 | 9 - Cálculo do DIFAL com ICMS Destino por dentro - Base Dupla |

### Opções para campo TIPOINSSESPECIAL (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| 1 | INSS 15 anos |
| 2 | INSS 20 anos |
| 3 | INSS 25 anos |

### Opções para campo TIPCALCFCPESPEC (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| null | 0 - Não específico (Regra Geral) |
| 1 | 1 - FECOP ST Majorado (CE) |

### Opções para campo SOMARPISCOFINSST (Tabela: TGFDIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFDPQ
### Descrição: Desconto por quantidade

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUPROMOCAO` | Nro. único | I |  |
| `QTDE` | Quantidade até | F |  |
| `PERCDESC` | %Desc./Vlr. Unit. | F |  |
| `CODUSU` | Cód. Usuário Alteração | I |  |
| `DTALTER` | Data alteração | H |  |
| `TIPDESC` | Tipo Desconto | S | Veja opções na seção OPÇÕES |
| `NUVERSAO` | NUVERSAO | I |  |
| `ATUNUVERSAO` | ATUNUVERSAO | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPDESC (Tabela: TGFDPQ)
| Valor | Descrição |
|-------|-----------|
| P | Percentual |
| V | Valor |


## Tabela: TGFEBOL
### Descrição: Email de boletos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODFILA` | Código na Fila | I |  |
| `NUFIN` | Nro Único | I |  |

## Tabela: TGFECT
### Descrição: Serviço Correios

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODSERVICO` | Cód. Serviço | S |  |
| `DESCRSERVICO` | Serviço | S |  |

## Tabela: TGFECTE
### Descrição: Eventos do CT-e

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Único da Nota | I |  |
| `CODEVE` | Cód. Evento | I |  |
| `SEQEVE` | Sequência do Evento | I |  |
| `DESCEVE` | Descrição do Evento | S |  |
| `DHRECIBO` | Dh. Recibo | H |  |
| `NRORECIBO` | Nro. Recibo | S |  |
| `CODSTATUS` | Cód. Status | I |  |
| `DESCRSTATUS` | Descrição do Status | S |  |
| `JUSTEVE` | Justificativa do evento | S |  |
| `XML` | XML | C |  |
| `CODUSU` | Usuário Solicitante | I |  |
| `ARQUIVO` | Arquivo | B |  |

## Tabela: TGFEFB
### Descrição: Blocos Escrituracao Fiscal Digital

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | CODEMP | I |  |
| `BLOCO` | Bloco | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `DESCRICAO` | Descrição | S |  |
| `GERARBLOCO` | Gerar Bloco | S | Veja opções na seção OPÇÕES |
| `TIPO` | Tipo | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo GERARBLOCO (Tabela: TGFEFB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFEFR
### Descrição: Registros Escrituracao Fiscal Digital

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | CODEMP | I |  |
| `BLOCO` | Bloco | S |  |
| `REGISTRO` | Registro | S |  |
| `DESCRICAO` | Descrição | S |  |
| `GERARREGISTRO` | Gerar Registro | S | Veja opções na seção OPÇÕES |
| `GERARENTRADA` | Gerar Entrada | S | Veja opções na seção OPÇÕES |
| `GERARSAIDA` | Gerar Saída | S | Veja opções na seção OPÇÕES |
| `TIPO` | Tipo | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo GERARREGISTRO (Tabela: TGFEFR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERARENTRADA (Tabela: TGFEFR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERARSAIDA (Tabela: TGFEFR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFEMDF
### Descrição: Evento MDF-e

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUVIAG` | Nro. Viagem | I |  |
| `SEQMDFE` | Sequência do manifesto | I |  |
| `SEQEVE` | Sequência Evento | I |  |
| `CODEVE` | Cód. Evento | S |  |
| `DESCREVE` | Descrição do Evento | S |  |
| `DHRECIBO` | Dt. e Hora do Evento | H |  |
| `NRORECIBO` | Nro. Recibo | S |  |
| `CODSTATUS` | Cód. Status | S |  |
| `DESCRSTATUS` | Descrição do Status | S |  |
| `JUSTEVE` | Justificativa do Evento | S |  |
| `UFEVE` | UF de encerramento | I |  |
| `CODCIDEVE` | Cidade de encerramento | I |  |
| `XML` | XML | C |  |
| `CODUSU` | Usuário | I |  |
| `XMLPROT` | XML Autorização | C |  |
| `CODMOTORISTA` | Motorista | I |  |

## Tabela: TGFEMP
### Descrição: Empresa Financeiro

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `ALIQPISBONIF` | Alíquota de Pis | F |  |
| `CODMODEMAILNFE` | Modelo de e-mail para NF-e | I |  |
| `MODEMAILLIBLIM` | Modelo de E-mail p/ Liberação de Limites | I |  |
| `ALIQFUNTTEL` | Alíquota FUNTTEL | F |  |
| `ALIQFUST` | Alíquota FUST | F |  |
| `EFDCODBCO` | Banco | I |  |
| `EFDCODCENCUS` | Centro Resultado | I |  |
| `EFDCODCTABCOINT` | Conta Bancária | I |  |
| `TIPOIMPKITFOX` | Tipo Kit | S |  |
| `CODEMP` | Código | I |  |
| `TIPICMSFENVALBEM` | Tipo do ICMS do Frete Extra Nota no valor de aquisição/depreciação do bem | I | Veja opções na seção OPÇÕES |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `ESTRNCREDICMSST` | Considerar TOP’s de Estorno para Crédito de ICMS/ST | S | Veja opções na seção OPÇÕES |
| `CONTBAIBEMSUBIMPREC` | Contabilização da baixa do bem subtraindo os impostos recuperáveis? | S | Veja opções na seção OPÇÕES |
| `USAVLRMEDTRANSFEMP` | Usa valor médio de venda nas transferências entre empresas do mesmos grupo | S | Veja opções na seção OPÇÕES |
| `GERCIAPCOMPEFD` | Gerar CIAP de componentes para SPED | S | Veja opções na seção OPÇÕES |
| `CODCTACTBBONIF` | Conta Contábil | I |  |
| `ALIQCFBONIF` | Alíquota de COFINS | F |  |
| `CALCICMS` | Calcula ICMS? | S | Veja opções na seção OPÇÕES |
| `EFDCODTIPTIT` | Tipo de Título | I |  |
| `CODSTPISCFBONIF` | Cód. Sit. Tribut. PIS/COFINS Bonificação | S | Veja opções na seção OPÇÕES |
| `TRABCOMIPI` | Trabalha com IPI ? | S | Veja opções na seção OPÇÕES |
| `EFDCODTIPOPER` | Tipo Operação | I |  |
| `DESTIPIDEVCOM` | Destacar o IPI na tag <vIPIDevol> em devoluções | S | Veja opções na seção OPÇÕES |
| `IPIINCICMS` | IPI incide no ICMS ? | S | Veja opções na seção OPÇÕES |
| `EFDCODNATDESPRECICMS` | Natureza Despesa Receitas ICMS | I |  |
| `TRIBPISCFBONIF` | Tributa PIS/COFINS sobre Aquisições em Bonificações? | S | Veja opções na seção OPÇÕES |
| `CALCIRRF` | Calcula IRRF ? | S | Veja opções na seção OPÇÕES |
| `DESCRICAO` | DescricaoConta | S |  |
| `CALCFUNRURAL` | Calcula FUNRURAL/INSS? | S | Veja opções na seção OPÇÕES |
| `DESCRNAT` | DescricaoNatureza | S |  |
| `ICMSSCTTD` | Habilita Alíq. incidência ICMS SC nas TTDs 409, 410 e 411 | S | Veja opções na seção OPÇÕES |
| `CODLANCBCOREC` | Lançamento bancário receitas | I |  |
| `EFDDIAVENC` | Dia de vencimento | I | Veja opções na seção OPÇÕES |
| `CODLANCBCOPAG` | Lançamento bancário despesas | I |  |
| `CALCISS` | ISS | S | Veja opções na seção OPÇÕES |
| `TOPSANGSUPRI` | TOP para sangria / suprimento | I |  |
| `TOPDESPESA` | TOP para despesa | I |  |
| `CSTIPIENT` | Código Sit.Trib.IPI Entrada | I | Veja opções na seção OPÇÕES |
| `CSTIPISAI` | Código Sit.Trib.IPI Saída | I | Veja opções na seção OPÇÕES |
| `CODENQIPIENT` | Código Enq. Legal IPI Entrada | I |  |
| `CODENQIPISAI` | Código Enq. Legal IPI Saída | I |  |
| `TEMPIS` | Calcula PIS? | S | Veja opções na seção OPÇÕES |
| `PREFIXSERIENACIONAL` | Prefixo Série NFS-e Padrão Nacional | S |  |
| `TEMCOFINS` | Calcula COFINS? | S | Veja opções na seção OPÇÕES |
| `EMITNFSENACIONAL` | Emitir NFS-e Padrão Nacional | S | Veja opções na seção OPÇÕES |
| `TEMCSSL` | Calcula CSLL? | S | Veja opções na seção OPÇÕES |
| `SERIEACOMPCF` | Série p/ Nota de Acomp. de CF | S |  |
| `CODTIPOPERACOMP` | Cód.Tipo Operação Nota de Acomp. de CF | I |  |
| `SALDOLIVQUINZ` | Frequência saldo livro ICMS | S | Veja opções na seção OPÇÕES |
| `SALDOLIVQUINZIPI` | Frequência saldo livro IPI | S | Veja opções na seção OPÇÕES |
| `ULTPAGLIVISS` | Última página do livro ISS | I |  |
| `ULTPAGLIVSAIDA` | Última página do registro de saídas | I |  |
| `ULTPAGLIVENTRAD` | Última página do registro de entradas | I |  |
| `ULTPAGCIAPMODC` | Última Página do CIAP Modelo C | I |  |
| `GERARLIVROS` | Gerar livros? | S | Veja opções na seção OPÇÕES |
| `GEROBSIPIREGENT` | Gerar Observação de IPI no registro de entrada? | S | Veja opções na seção OPÇÕES |
| `RECMINTARE` | Tem convênio TARE na geração do livro fiscal? | S | Veja opções na seção OPÇÕES |
| `LIVRO1PARA1TGFITE` | Gerar linhas da Nota separadamente no Livro Fiscal? | S | Veja opções na seção OPÇÕES |
| `GERAGNRE` | Gerar GNRE? | S | Veja opções na seção OPÇÕES |
| `CALCVLRAQUISBEM` | Calcular o valor de aquisição do bem | I | Veja opções na seção OPÇÕES |
| `REG54SEQ997ST` | Reg.54.Seq.997 p/ ST? | S | Veja opções na seção OPÇÕES |
| `CODCTACTB_1` | Conta contábil 1 | I |  |
| `CODCTACTB_2` | Conta contábil 2 | I |  |
| `CODCTACTB_3` | Conta contábil 3 | I |  |
| `CODCENCUS` | Cód.Centro Resultado | I |  |
| `CODCENCUSDESP` | Centro Resultado desp. | I |  |
| `ULTDUPL` | Última duplicata | I |  |
| `MODDUPL` | Modelo duplicata | I |  |
| `IMPEXPED` | Impressora | S |  |
| `MODEXPED` | Modelo | I |  |
| `TIPOIMPRESSORA` | Tipo de Imp. | S | Veja opções na seção OPÇÕES |
| `EMPSOMA` | Empresa para agrupar estoque | I |  |
| `CODTABCALC` | Tabela de preço padrão | I |  |
| `CODFORMPREC` | Fórmula de Custo/Preço | I |  |
| `CODTAB` | Tabela de preço para venda | I |  |
| `CODPARCCTB` | Cód. Parceiro | I |  |
| `NOMECONTADOR` | Nome do Contador | S |  |
| `CPFCONTADOR` | CPF | S |  |
| `UFCRCCONTADOR` | UF CRC | S |  |
| `CRCCONTADOR` | CRC | S |  |
| `TELCONTADOR` | Telefone | S |  |
| `EMAILCONTADOR` | Email | S |  |
| `ALTCONTADOR` | Alterou? | S | Veja opções na seção OPÇÕES |
| `EMITEEXPED` | Emite expedição | S | Veja opções na seção OPÇÕES |
| `PARTICMETA` | Participação na meta | F |  |
| `ULTPAGLIVICMS` | Última Página Livro ICMS | I |  |
| `CALPERCPIS` | Calcula percentual do PIS | I |  |
| `PERPROJ` | Periodicidade projeção | S | Veja opções na seção OPÇÕES |
| `PROJONLINE` | Projeção Online | S | Veja opções na seção OPÇÕES |
| `CODCTABCOIPAD` | Conta bancária padrão | I |  |
| `ULTPAGLIVIPI` | Última Página Livro IPI | I |  |
| `ULTAUTORPAG` | Última autorização de pagamento | I |  |
| `PERCCUSVAR` | % Custo Variável | F |  |
| `PERCMARGEM` | % Outros | F |  |
| `PERCPIS` | % PIS | F |  |
| `PERCCSL` | % CSLL (Contrib. Social s/Lucro) | F |  |
| `PERCCOFINS` | % COFINS | F |  |
| `PERCCFSERVICO` | % Custo Fixo Serviço | F |  |
| `PERCCFFAB` | % Custo Fixo Fabricação | F |  |
| `PERCCFOUTROS` | % Custo Fixo Outros | F |  |
| `CODTRIB20RED` | 20 - Com redução de base de cálculo (Redução da base vai p/) | S | Veja opções na seção OPÇÕES |
| `CODTRIB30` | 30 - Isenta e não tribut.e c/cobrança por S.T. (Valor Contábil vai p/) | S | Veja opções na seção OPÇÕES |
| `CODTRIB40ISENT` | 40 - Isentas (Valor Contábil vai p/) | S | Veja opções na seção OPÇÕES |
| `CODTRIB41NAOTRIB` | 41 - Não tributadas (Valor Contábil vai p/) | S | Veja opções na seção OPÇÕES |
| `CODTRIB50SUSP` | 50 - Suspensão (Valor Contábil vai p/) | S | Veja opções na seção OPÇÕES |
| `CODTRIB51DIF` | 51 - Diferimento (Valor Contábil vai p/) | S | Veja opções na seção OPÇÕES |
| `CODTRIB60STANT` | 60 - ICMS cobrado anteriormente por S.T. (Valor Contábil vai p/) | S | Veja opções na seção OPÇÕES |
| `CODTRIB70REDST` | 70 - C/ redução de base de cálculo e cobrança do ICMS por S.T.(Redução vai p/) | S | Veja opções na seção OPÇÕES |
| `CODTRIB90OUT` | 90 - Outras (Valor Contábil vai p/) | S | Veja opções na seção OPÇÕES |
| `NFE` | Ambiente NF-e/NFC-e | S | Veja opções na seção OPÇÕES |
| `TIPODANFE` | Impressão do DANFE | S | Veja opções na seção OPÇÕES |
| `LAYOUTDANFE` | Layout do DANFE | S | Veja opções na seção OPÇÕES |
| `COPIASDANFE` | Número de cópias DANFE | I |  |
| `VERSAONFE` | Versão NF-e/NFC-e | I | Veja opções na seção OPÇÕES |
| `VERSAONT` | Versão da nota técnica | I | Veja opções na seção OPÇÕES |
| `CODMODDANFE` | Modelo do DANFE | I |  |
| `CODMODDANFECONTINGENCIA` | Modelo do DANFE em contingência | I |  |
| `LOGODANFE` | Arquivo logomarca | S |  |
| `IPINAOINCID` | Valor do IPI quando não incidir na base de ICMS | S | Veja opções na seção OPÇÕES |
| `STINCLUSA` | Valor da Substituição Tributária ou Valor Contábil p/Cód.Trib.10 e 15 em Entradas | S | Veja opções na seção OPÇÕES |
| `CREDPIS` | Tem Créd.PIS? | S | Veja opções na seção OPÇÕES |
| `STINCLUSA70` | Valor da Substituição Tributaria ou Valor Contábil p/Cód.Trib.70 em Entradas | S | Veja opções na seção OPÇÕES |
| `CREDCOFINS` | Tem Créd.COFINS? | S | Veja opções na seção OPÇÕES |
| `NURFE` | Relatório formatado do DANFE | I |  |
| `PRIORCODNAT` | Prioridade de Cod. Natureza (M410/M810) | I | Veja opções na seção OPÇÕES |
| `PERFILEFD` | Perfil de Apresentação do Arquivo | S | Veja opções na seção OPÇÕES |
| `INCENTCULT` | Tem incentivador cultural? | S | Veja opções na seção OPÇÕES |
| `TIPOATIVIDADE` | Tipo de Atividade | I | Veja opções na seção OPÇÕES |
| `CODLOJAECONECT` | Loja na Integração EConect | I |  |
| `NFSE` | Ambiente NFS-e | S | Veja opções na seção OPÇÕES |
| `REGIMEESPTRIBISS` | Regime esp. tributação ISS (NFS-e) | S | Veja opções na seção OPÇÕES |
| `COMPIPI` | Compensa o IPI? | S | Veja opções na seção OPÇÕES |
| `ALIQCFDESC` | Alíquota de COFINS | F |  |
| `ALIQCFJUROS` | Alíquota de COFINS | F |  |
| `ALIQCFMULT` | Alíquota de COFINS | F |  |
| `ALIQPISDESC` | Alíquota de Pis | F |  |
| `ALIQPISJUROS` | Alíquota de Pis | F |  |
| `ALIQPISMULT` | Alíquota de Pis | F |  |
| `BAIXAFINPREEMISSNFCE` | Baixar financeiros na pré-transmissão da NFC-e? | S | Veja opções na seção OPÇÕES |
| `CODCLASSIFESTAB` | Cód. de Classificação do Estabelecimento | I | Veja opções na seção OPÇÕES |
| `CODSTPISCFMULT` | Cód. Sit. Tribut. PIS/COFINS Multas | S | Veja opções na seção OPÇÕES |
| `CODEMPIMPOSTO` | Empresa modelo para regra fiscal | I |  |
| `CODTABCKC` | Tabela de preço exclusiva | I |  |
| `CONTINGENCIANFCE` | Envio em contingência | S | Veja opções na seção OPÇÕES |
| `EMAILNOTFECREINF` | E-mail p/ notificação de fechamento do Reinf | S |  |
| `GERARTAXFINEMBNFE` | Desconsiderar valores de taxas financeiras na geração do XML? | S | Veja opções na seção OPÇÕES |
| `IDENTECTRASTREIO` | Usuário rastreamento | S |  |
| `IMPNFEEMISSPROP` | Importa NF-e de emissão própria? | S | Veja opções na seção OPÇÕES |
| `JOBMDENDDIGITAL` | Nome Job NDDigital | S |  |
| `NFESTANTCONSFINAL` | Valor da ST anterior no CST 60 do XML de NF-e p/ consumidor final | S | Veja opções na seção OPÇÕES |
| `NUMDOCR2020` | Nro. Documento do Evento R2020 | S | Veja opções na seção OPÇÕES |
| `NUNOTADEMFX` | NF demonstração | I |  |
| `NUNOTAMODFX` | NF modelo | I |  |
| `NUNOTATRCFX` | NF de troca | I |  |
| `CODMODDANFESIMPLIFNFE` | Modelo do DANFE simplificado | I |  |
| `NURFEPRODUCAO` | Modelo de etiqueta | I |  |
| `QRCODENFCEVERSAO2` | Usar o QR Code versão 2.0? | S | Veja opções na seção OPÇÕES |
| `QRCODENFCEVERSAO` | Versão QR Code | S | Veja opções na seção OPÇÕES |
| `SENHAECTRASTREIO` | Senha rastreamento | S |  |
| `TIPCTACTBEFD` | Tipo da Conta Contábil para EFD | S | Veja opções na seção OPÇÕES |
| `TIPCTACTBEFDF` | Tipo de conta contábil para EFD ICMS/IPI | S | Veja opções na seção OPÇÕES |
| `TIPOENVIONFCE` | Tipo de envio da NFC-e | S | Veja opções na seção OPÇÕES |
| `TOPCORBANECONECT` | TOP para CorBan | I |  |
| `TRIBPISCFMULT` | Tributa PIS/COFINS sobre Receitas Obtidos de Multas? | S | Veja opções na seção OPÇÕES |
| `USASTEXTNOTARESTST` | Usar ST Extra Nota na Restituição de ST | S | Veja opções na seção OPÇÕES |
| `USATROCOCHECKOUT` | Utilizar troco no PDV WEB? | S | Veja opções na seção OPÇÕES |
| `BLQNFACOMPNFCPEND` | Bloquear NF-e de acompanhamento em NFC-e pendente? | S | Veja opções na seção OPÇÕES |
| `SUPRIMIREMAILDEST` | Suprimir email do destinatário para NF-e? | S | Veja opções na seção OPÇÕES |
| `LOCALPADECONECT` | Local Padrão EConect | I |  |
| `CODSTPISCFDESC` | Cód. Sit. Tribut. PIS/COFINS Descontos | S | Veja opções na seção OPÇÕES |
| `CODSTPISCFJUROS` | Cód. Sit. Tribut. PIS/COFINS Juros | S | Veja opções na seção OPÇÕES |
| `TRIBPISCFDESC` | Tributa PIS/COFINS sobre Descontos Obtidos de Despesas? | S | Veja opções na seção OPÇÕES |
| `TRIBPISCFJUROS` | Tributa PIS/COFINS sobre Juros Recebidos de Receitas? | S | Veja opções na seção OPÇÕES |
| `MAXNOTASLOTENFE` | Max. notas lote NF-e/NFC-e | I |  |
| `NURFECARTACORR` | Relatório de carta de correção | I |  |
| `COPIASDANFECONTING` | Número de cópias do DANFE em contingência | I |  |
| `METCALCDIFICMS` | Método para Calcular Diferencial de Alíquota | S | Veja opções na seção OPÇÕES |
| `CODFORDIFALIQ` | Fórmula para cálculo diferencial de alíquota | I |  |
| `IDENTECT` | Identificação Correios | S |  |
| `APLCALCDIFALIQFRT` | Aplicar Método para Calcular Diferencial de Alíquota sobre Frete Extra Nota? | S | Veja opções na seção OPÇÕES |
| `DIFALIQDESPACESS` | Utilizar Fórmula do Diferencial de Alíquotas p/ Despesas Acessórias? | S | Veja opções na seção OPÇÕES |
| `DIFALIQFCPINT` | Considerar alíquota FCP/FECP no cálculo de Diferencial de Alíquota? | S | Veja opções na seção OPÇÕES |
| `TPOEMPRESA` | Tipo de Empresa | I | Veja opções na seção OPÇÕES |
| `FILTROALIQICMSSQL` | Filtro p/ obtenção da alíquota de ICMS | S |  |
| `CODRELMINUTAODP` | Minuta de Despacho | I |  |
| `EFDH010` | Conta p/ inventário (H010) do EFD | S |  |
| `EFDH010_TER` | Conta p/ inventário Terceiro (H010) do EFD | S |  |
| `EFDH010_PRTER` | Conta p/ inventário Prop. c/ Terc (H010) do EFD | S |  |
| `SENHAECT` | Senha Correios | S |  |
| `COMPIPISEPICM` | Compensa o IPI Separando o ICMS? | S | Veja opções na seção OPÇÕES |
| `TOPRECARGACELECONECT` | TOP recarga celular EConect | I |  |
| `TOPNFCEECONECT` | TOP para NFC-e | I |  |
| `TOPSATECONECT` | TOP para SAT | I |  |
| `MODETQVOL` | Modelo padrão de Etiqueta de Volume | I |  |
| `IGPERMCOMPPRODS` | Ignorar permissão para compra de produtos | S | Veja opções na seção OPÇÕES |
| `TIPICMSTOPENTSIMNAC` | Considerar Tipo de ICMS da TOP p/ entrada em empresa Simp.Nac.? | S | Veja opções na seção OPÇÕES |
| `UTILIZAMDE` | Utiliza distribuição de DF-e? | S | Veja opções na seção OPÇÕES |
| `CODLOCALTERC` | Local específico para estoque de terceiros | I |  |
| `INDESCRIT` | Indicador da apuração das contribuições e créditos | I | Veja opções na seção OPÇÕES |
| `HORAINICIAL` | Hora inicial | I |  |
| `DTINICIOKARDEX` | Data Início Kardex | H |  |
| `CODEMPGRUPFRETE` | Empresa Agrupamento para Cálculo Frete | I |  |
| `TIPTRANSMNFSE` | Tipo de Transmissão NFS-e | S | Veja opções na seção OPÇÕES |
| `CODTABALT` | Tabela de preço alternativa | I |  |
| `CODSMTP` | Conta SMTP | I |  |
| `INCENTFISCALISSQN` | Tem incentivo fiscal ISSQN? | S | Veja opções na seção OPÇÕES |
| `JOBKEYNDD` | JobKey NDDigital | S |  |
| `CONECTORNFSE` | Conector NFS-e | S | Veja opções na seção OPÇÕES |
| `IMPCTEEMISPROP` | Importar CT-e de emissão própria? | S | Veja opções na seção OPÇÕES |
| `TERACPCTE` | Termo de Acordo p/ CT-e | S | Veja opções na seção OPÇÕES |
| `ENVIOSINCRONOCTE` | Usar modo síncrono para envio do XML? | S | Veja opções na seção OPÇÕES |
| `CODMODDACTE` | Modelo DACTE | I |  |
| `UTILIZADFETRANSP` | Utilizar distribuição de DF-e? | S | Veja opções na seção OPÇÕES |
| `TPAMBCTE` | Ambiente CT-e | S | Veja opções na seção OPÇÕES |
| `TPAMBNFCOM` | Ambiente NFCom | S | Veja opções na seção OPÇÕES |
| `CONTINGENCIACTE` | Envio de contingência | S | Veja opções na seção OPÇÕES |
| `HORAFINAL` | Hora final | I |  |
| `TIPOENVIOCTE` | Tipo de envio CT-e | S | Veja opções na seção OPÇÕES |
| `NOTAMODELODAGENDA` | Modelo de nota e pedidos | I |  |
| `CODTIPPARC` | Cód. perfil | I |  |
| `VERSAONTCTE` | Versão da nota técnica do CT-E | I | Veja opções na seção OPÇÕES |
| `VERSAOCTE` | Versão CT-e | I | Veja opções na seção OPÇÕES |
| `INTERVALO` | Minutos p/ módulo | I | Veja opções na seção OPÇÕES |
| `QTDLIMITEMES` | Limite de dias p/ histórico | I |  |
| `COPIASDACTE` | Número de cópias do DACTE | I |  |
| `VALIDACPFCNPJ` | CPF obrigatório | S | Veja opções na seção OPÇÕES |
| `NURFECARTACORRCTE` | Relatório carta de correção | I |  |
| `CORAGENDADO` | Agendado | I |  |
| `TIPODACTE` | Impressão do DACTE | S | Veja opções na seção OPÇÕES |
| `CORFIXADO` | Fixado | I |  |
| `CORBLOQUEADO` | Bloqueado | I |  |
| `CORENCAIXADO` | Encaixado | I |  |
| `CORATENDIDO` | Atendido | I |  |
| `CORFATURADO` | Faturado | I |  |
| `CODMETA` | Meta Padrão para PCP | I |  |
| `TPAMBMDFE` | Ambiente MDF-e | S | Veja opções na seção OPÇÕES |
| `MARGSEGPCP` | Margem de segurança para PCP | F |  |
| `CODEMPMATRIZEFD` | Empresa Matriz (EFD) | I |  |
| `CODEMPMATRIZNFSE` | Empresa certificado (NFS-e) | I |  |
| `CODMODNFCECOMPL` | Modelo do DANFE da NFC-e completo/contingência | I |  |
| `CODMODNFCESIMPL` | Modelo do DANFE da NFC-e simplificado/normal | I |  |
| `CODPARCNFCE` | Parceiro padrão da NFC-e | I |  |
| `NATPESSOAJURIDICA` | Natureza da Pessoa Jurídica | S | Veja opções na seção OPÇÕES |
| `RASTRESTOQUE` | Rastreamento de Estoques | S | Veja opções na seção OPÇÕES |
| `SEQTOKENNFCE` | Sequencia do token da NFC-e | I |  |
| `CONESTORIGPROD` | Controla estoque por origem de produto | I | Veja opções na seção OPÇÕES |
| `TOKENNFCE` | Token NFC-e | S |  |
| `BANCOPIXCHECKOUT` | Código do banco Pix Checkout | I | Veja opções na seção OPÇÕES |
| `VLRLIQITEMNFCE` | Considerar o valor líquido do item na NFC-e? | S | Veja opções na seção OPÇÕES |
| `APIKEYPIXCHECKOUT` | Chave da API Pix Checkout | S |  |
| `CLIENTSECRETPIXCHECKOUT` | Senha do Cliente Pix Checkout | S |  |
| `TIPOATIVIDADEPISCOFINS` | Tipo de Atividade | I | Veja opções na seção OPÇÕES |
| `CLIENTIDPIXCHECKOUT` | ID do Cliente Pix Checkout | S |  |
| `COPIASDANFCE` | Número de cópias DANFE (NFC-e) | I |  |
| `TIRASERVLRCONTAB` | Tirar Serviço do Valor Contábil | S | Veja opções na seção OPÇÕES |
| `GRAVAROBSNOTA` | Gravar Observação da Nota? | S | Veja opções na seção OPÇÕES |
| `CODEMPOC` | Empresa p/ Ordem de Carga | I |  |
| `LOCALPAD` | Local Padrão | I |  |
| `ARQMODBOLETO` | Modelo de boleto (e-mail) | S |  |
| `TIPOENVIONFCOM` | Tipo de envio NFCom | S | Veja opções na seção OPÇÕES |
| `TIPOENVIONFE` | Tipo de envio NF-e | S | Veja opções na seção OPÇÕES |
| `GERADEDUCAOPF` | Gera deduções para Pessoa Física? | S | Veja opções na seção OPÇÕES |
| `AGRUPASERVFAT` | Agrupar serviços faturamento? | S | Veja opções na seção OPÇÕES |
| `TEMPREMIACAOESTADUAL` | Tem programa de premiação estadual? | S | Veja opções na seção OPÇÕES |
| `COMPLRESTITUICAOICMSST` | Complemento/Restituição ICMS/ST - MG | S | Veja opções na seção OPÇÕES |
| `MARCANOTRPS` | Marcar nota como RPS por padrão? | S | Veja opções na seção OPÇÕES |
| `CONSVLRLIQNFSE` | Considera valor líquido para NFS-e? | S | Veja opções na seção OPÇÕES |
| `NOTAENTAJUSTEST` | Modelo Ajuste de Entrada de Estoque | I |  |
| `NOTASAIAJUSTEST` | Modelo Ajuste de Saída de Estoque | I |  |
| `NOTAENTAJUSTESTCONS` | Modelo Ajuste de Entrada de Estoque Consignado | I |  |
| `NOTASAIAJUSTESTCONS` | Modelo Ajuste de Saída de Estoque Consignado | I |  |
| `NOTAENTAJUSTESTDTER` | Modelo Ajuste de Entrada de Estoque de Terceiros | I |  |
| `NOTASAIAJUSTESTDTER` | Modelo Ajuste de Saída de Estoque de Terceiros | I |  |
| `TPLIGACAO` | Cód.Tipo de Ligação | I | Veja opções na seção OPÇÕES |
| `CODGRUPOTENSAO` | Cód.Grupo de Tensão | S | Veja opções na seção OPÇÕES |
| `NOTAENTAJUSTESTCTER` | Modelo Ajuste de Entrada de Estoque com Terceiros | I |  |
| `CLASCONS_ENERG` | Cód. Classe de Cons. Energia | S | Veja opções na seção OPÇÕES |
| `NOTASAIAJUSTESTCTER` | Modelo Ajuste de Saída de Estoque com Terceiros | I |  |
| `TPLIGACAOINF` | Permite informar Ligação na Central? | S | Veja opções na seção OPÇÕES |
| `CLASCONS_GAS` | Cód. Classe de Cons. Gás | S | Veja opções na seção OPÇÕES |
| `CLASCONS_AGUA` | Cód. Clase de Cons. Agua | S | Veja opções na seção OPÇÕES |
| `TPASSINANTE` | Cód.Tipo de Assinante | I | Veja opções na seção OPÇÕES |
| `TPASSINANTEINF` | Permite infomar Assinante na Central? | S | Veja opções na seção OPÇÕES |
| `COMPLITEMNOTA` | Compl. Itens Nota | S |  |
| `CONTINGENCIANFCOM` | Envio em contingência | S | Veja opções na seção OPÇÕES |
| `CONTINGENCIANFE` | Envio em contingência | S | Veja opções na seção OPÇÕES |
| `DTCERTIFNFEFIM` | Data de fim da vigência do certificado digital | H |  |
| `DTCERTIFNFEINI` | Data de início da vigência do certificado digital | H |  |
| `FLEX` | Usar Créd. Flex? | S | Veja opções na seção OPÇÕES |
| `GRAVAROBSPADRAO` | Gravar Observação Padrão da Nota? | S | Veja opções na seção OPÇÕES |
| `VLRLIQITEMNFE` | Considerar o valor líquido do item para NF-e (geração do XML e imp. do DANFE)? | S | Veja opções na seção OPÇÕES |
| `MAXCREDINDENIZ` | % Máx.Crédito de Indenização | F |  |
| `MAXDEBINDENIZ` | % Máx.Débito de Indenização | F |  |
| `PRODEPE` | Beneficiário de Incentivo PRODEPE/FUNCRESCE? | S | Veja opções na seção OPÇÕES |
| `TEMREAICMS` | Tem Convênio REA/ICMS? | S | Veja opções na seção OPÇÕES |
| `GERNOTAENT` | Gerar Notas de Entrada Form. Próprio na Obs. do Livro de Saída? | S | Veja opções na seção OPÇÕES |
| `GRAVARSERIENOTA` | Gravar Série Igual a da Nota? | S | Veja opções na seção OPÇÕES |
| `TRATARTRIBUT` | Tratar Código Tributação Isentas como Isentas? | S | Veja opções na seção OPÇÕES |
| `TRATARDIFPARC` | Tratar Diferenciamento Parcial? | S | Veja opções na seção OPÇÕES |
| `USATRIBUTITENS` | Usar Código de Tributação dos Itens? | S | Veja opções na seção OPÇÕES |
| `FRETESEPCONSTRANSP` | Gravar Frete Separado p/ Conhecimento de Transporte (Modelo 8)? | S | Veja opções na seção OPÇÕES |
| `FRETESEPSEMPRE` | Gravar Frete Separado Sempre? | S | Veja opções na seção OPÇÕES |
| `CONSOUTROSIMP` | Considerar Outros Impostos? | S | Veja opções na seção OPÇÕES |
| `CODTRIB53` | 53 - Tributação monofásica sobre combustíveis com recolhimento diferido | S | Veja opções na seção OPÇÕES |
| `CODTRIB61` | 61 - Tributação monofásica sobre combustíveis cobrada anteriormente | S | Veja opções na seção OPÇÕES |
| `GERARPRODLIVENT` | Gerar Produção no Livro de Entrada? | S | Veja opções na seção OPÇÕES |
| `GERARPRODORIGKIT` | Gerar Produto Origem de Kit? | S | Veja opções na seção OPÇÕES |
| `TRATARTRIBUTDEFEMP` | Usar Tratamento de Código Tributação Definido no Cadastro de Empresas? | S | Veja opções na seção OPÇÕES |
| `USUARIONFSE` | Usuário NFS-e | S |  |
| `SENHANFSE` | Senha NFS-e | S |  |
| `FRASENFSE` | Frase de segurança da NFS-e | S |  |
| `CONSDEVTEREVTR2050` | Considerar devolução de NF-e de Terceiros no R-2050? | S | Veja opções na seção OPÇÕES |
| `GEROBSFING4000` | Gerar observação do financeiro p/ eventos Grupo 4000? | S | Veja opções na seção OPÇÕES |
| `GEROBSNOTAG4000` | Gerar observação da nota p/ eventos Grupo 4000? | S | Veja opções na seção OPÇÕES |
| `DESCREDDIFCIAP` | Desconsiderar Crédito Dif. Alíquota No CIAP? | S | Veja opções na seção OPÇÕES |
| `CGCPROCURADOR` | CNPJ/CPF Procurador | S |  |
| `CODUSUNFSE` | Código do usuário da NFS-e | S |  |
| `CODCONTRINFSE` | Código do contribuinte da NFS-e | S |  |
| `USADTFABLOTNFE` | Usar data de fabricação do lote? | S | Veja opções na seção OPÇÕES |
| `PRZREGCANNOTA` | Prazo regulamentar p/ cancelamento de nota (horas) | I |  |
| `PRAZORCANCCTE` | Prazo regulamentar p/ cancelamento de CT-e (horas) | I |  |
| `USADTVALLOTNFE` | Usar data de validade do lote? | S | Veja opções na seção OPÇÕES |
| `PRAZOTCANCCTE` | Prazo com tolerância p/ cancelamento de CT-e (horas) | I |  |
| `PRZTOLCANNOTA` | Prazo com tolerância p/ cancelamento de nota (horas) | I |  |
| `USANOMECOMPLITEM` | Usar nome do campo no complemento para itens da nota? | S | Veja opções na seção OPÇÕES |
| `TEMDENUESPONT` | Tem denúncia espontânea? | S | Veja opções na seção OPÇÕES |
| `DENUNCESPCTE` | Tem denúncia espontânea? | S | Veja opções na seção OPÇÕES |
| `ENVRESPCONTNFE` | Enviar responsável contábil na NFE? | S | Veja opções na seção OPÇÕES |
| `ISALIQINTSEXC` | Usar a alíquota interna sem exceção para o cálculo do Diferencial de Alíquota | S | Veja opções na seção OPÇÕES |
| `SERNAOTRIBBASEISS` | Serviços não Trib./Isentos para compor base do ISS? | S | Veja opções na seção OPÇÕES |
| `ENVRESPCONTCTE` | Enviar responsável contábil no CT-e? | S | Veja opções na seção OPÇÕES |
| `CCM` | Cadastro de contribuinte mobiliário | S |  |
| `CHAVEACESSONFSE` | Chave de Acesso da NFS-e | S |  |
| `CHAVEDIGITALAGILIBLUE` | Chave Digital NFSe | S |  |
| `CERTIFICADOPIX` | Certificado Pix | S |  |
| `VERSAOMDFE` | Versão MDF-e | I | Veja opções na seção OPÇÕES |
| `ENVMDFSINC` | Usar modo síncrono para envio do XML | S | Veja opções na seção OPÇÕES |
| `TRANSPCARGA` | Transportadora de cargas | S | Veja opções na seção OPÇÕES |
| `REDICMSBCPISCONFINS` | Deduzir valor do ICMS na BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `REDISSBCPISCONF` | Deduzir valor do ISS na BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `REDDIFALBCPISCOF` | Deduzir DIFAL junto com o ICMS na BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `CONSREPICMSBASEPISCOF` | Considera Repasse ICMS na BC PIS/COFINS? | S | Veja opções na seção OPÇÕES |
| `ULTNSU` | Último NSU | S |  |
| `AMBIENTEREINF` | Ambiente EFD-Reinf | I | Veja opções na seção OPÇÕES |
| `PARTCANALVERDE` | Participa do canal verde? | S | Veja opções na seção OPÇÕES |
| `RESPENTREINF` | Responsável pela Entrega | I |  |
| `TRIBREINF` | Classificação Tributária - EFD-Reinf | I | Veja opções na seção OPÇÕES |
| `ENTREGAECD` | Entrega a ECD ? | S | Veja opções na seção OPÇÕES |
| `SITEMPREINF` | Situação da Empresa | I | Veja opções na seção OPÇÕES |
| `EMPADMPUBDIR` | Empresa de Adm. Pública Direta? | S | Veja opções na seção OPÇÕES |
| `DESONERAFOLHACPRB` | Desoneração da Folha - CPRB ? | S | Veja opções na seção OPÇÕES |
| `DTVALINIREINF` | Data Validade Inicial Reinf | D |  |
| `DTVALFINREINF` | Data Validade Final Reinf | D |  |
| `VINCULOEFR` | EFR ou Vinculada a EFR? | S | Veja opções na seção OPÇÕES |
| `CNPJEFRVINC` | CNPJ da EFR Vinculada | S |  |
| `AEDFE` | Número de Autorização para Emissão de Documentos Fiscais Eletrônicos (AEDF-e) | S |  |
| `CAMCONVPREF` | Campos a serem convertidos conforme manual da prefeitura | S | Veja opções na seção OPÇÕES |
| `DTREFPRODREINF` | Referência Atual Reinf - Produção | D |  |
| `DTREFPREPRODREAISREINF` | Referência Atual Reinf - Pré-produção - dados reais | D |  |
| `DTREFPREPRODFICTREINF` | Referência Atual Reinf - Pré-produção - dados fictícios | D |  |
| `ULTNSUCTE` | Último NSU CT-e | S |  |
| `CONSDEVEVTR2050` | Considerar devoluções para geração do evento R-2050? | S | Veja opções na seção OPÇÕES |
| `GERNOTAENTCANC` | Gerar Notas de Entrada Canceladas Form. Próprio na Obs. do Livro de Saída? | S | Veja opções na seção OPÇÕES |
| `CONSIDBENEF` | Considerar benefícios ao alterar item da nota? | S | Veja opções na seção OPÇÕES |
| `REDSTCOMPBCPISCOFINS` | Deduzir valor de ST da compra da BC do PIS e COFINS da Venda? | S | Veja opções na seção OPÇÕES |
| `FISTEL` | FISTEL | S |  |
| `DEDICMSBCPISCOFINS` | Deduzir valor de ICMS próprio da compra da BC do PIS e COFINS da Venda? | S | Veja opções na seção OPÇÕES |
| `CSTNREDICMSBCPISCOF` | CSTs que não Reduzem o ICMS da BC do PIS e COFINS. | S |  |
| `CODTRIB90CREDDEB` | 90 - Outras Com Crédito/Débito (Valor Contábil vai p/) | S | Veja opções na seção OPÇÕES |
| `PROXEXECSMTPXML` | Próxima consulta | H |  |
| `INTCONSSMTPXML` | Intervalo de Consulta em minutos | I |  |
| `USUARIOSMTPXML` | Usuário do e-mail | S |  |
| `SENHASMTPXML` | Senha do e-mail | S |  |
| `SERVIDORSMTPXML` | Servidor de e-mail | S |  |
| `PORTASMTPXML` | Porta | I |  |
| `INSXMLPORIMPSMTPXML` | Inserir XML no Portal de Importação | S |  |
| `TIPCONEXSMTPXML` | Tipo de Conexão | S | Veja opções na seção OPÇÕES |
| `IGCERTIFSMTPXML` | Ignorar validação do certificado no servidor? | S |  |
| `CODCTACTBDESC` | Conta Contábil | I |  |
| `CODCTACTBJUROS` | Conta Contábil | I |  |
| `CODCTACTBMULT` | Conta Contábil | I |  |
| `GERARRETENCAO` | Gerar retenção (valor da retenção considerado no total da nota) | I | Veja opções na seção OPÇÕES |
| `NOTASAIAJUSTBEM` | Modelo Ajuste de Baixa de Bem | I |  |
| `TIPGERINFGVEICGREB` | Gerar as informações do Grupos Veículo Transporte e Grupo Reboque | S | Veja opções na seção OPÇÕES |
| `CONICMSMAJFCPINT` | Considerar ICMS e ST majorados com o FCP Interno | S | Veja opções na seção OPÇÕES |
| `GERLIVICMSEMPSN` | Escriturar valor de ICMS de entrada para Empresa Simples? | S | Veja opções na seção OPÇÕES |
| `CALCICMSSTNAOCONT` | Permitir o cálculo do ICMS ST para consumidor final não contribuinte | S | Veja opções na seção OPÇÕES |
| `ENVEMAILCONF` | Enviar XML por email na confirmação? | S | Veja opções na seção OPÇÕES |
| `PROGAQUISALIM` | Participa do Programa Aquisição de Alimentos (PAA) | S | Veja opções na seção OPÇÕES |
| `VERSAONTMDFE` | Versão da nota técnica do MDF-e | I | Veja opções na seção OPÇÕES |
| `OBTSTANTMEDENT` | Obtém ST Anterior pela média das entradas? | S | Veja opções na seção OPÇÕES |
| `IPITRIBUTDEFEMP` | Usar Tratamento de Código Tributação de IPI Definido no Cadastro de Empresas? | S | Veja opções na seção OPÇÕES |
| `DEFCSTIPI00` | 00 - Entrada com Recuperação de Crédito | S | Veja opções na seção OPÇÕES |
| `DEFCSTIPI01` | 01 - Entrada Tributada com Alíquota Zero | S | Veja opções na seção OPÇÕES |
| `DEFCSTIPI02` | 02 - Entrada Isenta | S | Veja opções na seção OPÇÕES |
| `DEFCSTIPI03` | 03 - Entrada Não Tributada | S | Veja opções na seção OPÇÕES |
| `DEFCSTIPI04` | 04 - Entrada Imune | S | Veja opções na seção OPÇÕES |
| `CALCPISCFSFIN` | Calcula PIS e Cofins na confirmação do financeiro. | S | Veja opções na seção OPÇÕES |
| `USACUSTOMEDIOMPS` | Usar custo médio das MPs para calcular custo do PA | S | Veja opções na seção OPÇÕES |
| `DEFCSTIPI05` | 05 - Entrada Com Suspensão | S | Veja opções na seção OPÇÕES |
| `USACUSMEDICMPRO` | Utiliza custo médio das matérias primas no cálculo do custo com ICMS e sem ICMS do PA? | S | Veja opções na seção OPÇÕES |
| `GERCHAVEREFSIG` | Gerar chave referenciada sigilosa? | S | Veja opções na seção OPÇÕES |
| `ORIGPRODCOMIPI` | Origens de produto p/compensar IPI no Livro Fiscal | S |  |
| `INDTIPLAYOUTK010` | Indicador de tipo de Layout (Registro K010) | I | Veja opções na seção OPÇÕES |
| `ENVINFISSSOMDEVIDO` | Enviar o Valor do ISS e alíquota no XML, apenas quando o ISS for devido a outro município? | S | Veja opções na seção OPÇÕES |
| `CREDICMSCOMBUS` | Creditar ICMS e ICMS/ST de NFe Compra Combustível (CST 060) | S |  |
| `DEFCSTIPI49` | 49 - Outras Entradas | S | Veja opções na seção OPÇÕES |
| `SOMARFCPBCCIAP` | Somar FCP na Base de Crédito do CIAP? | S | Veja opções na seção OPÇÕES |
| `TIPOPIX` | Tipo de PIX | S | Veja opções na seção OPÇÕES |
| `CODCTAPIXTEF` | Conta para Recebimento PIX TEF | I |  |
| `TIPDATAEVTSERV` | Tipo de data p/ busca das notas de serviço dos eventos 2010 e 2020 (exceto financeiros) | S | Veja opções na seção OPÇÕES |
| `DEFCSTIPI50` | 50 - Saída Tributada | S | Veja opções na seção OPÇÕES |
| `TOPCANPIXFIN` | TOP Cancelamento Pix - Financeiro | I |  |
| `DEFCSTIPI51` | 51 - Saída Tribrutável com Alíquota Zero | S | Veja opções na seção OPÇÕES |
| `TOPCANPIXREC` | TOP Cancelamento Pix - Recebimento | I |  |
| `DEFCSTIPI52` | 52 - Saída Isenta | S | Veja opções na seção OPÇÕES |
| `TOPCANPIXPAG` | TOP Cancelamento Pix - Pagamento | I |  |
| `DEFCSTIPI53` | 53 - Saída Não tributada | S | Veja opções na seção OPÇÕES |
| `NATCANPIX` | Natureza Cancelamento Pix | I |  |
| `DEFCSTIPI54` | 54 - Saída Imune | S | Veja opções na seção OPÇÕES |
| `DEFCSTIPI55` | 55 - Saída Com Suspensão | S | Veja opções na seção OPÇÕES |
| `DEFCSTIPI99` | 99 - Outras Saídas | S | Veja opções na seção OPÇÕES |
| `ENVIOSINCRONONFE` | Usar modo síncrono para envio do XML? | S | Veja opções na seção OPÇÕES |
| `ENVIOSINCRONONFCE` | Usar modo síncrono para envio do XML? | S | Veja opções na seção OPÇÕES |
| `ATUALCBENEFFAT` | Atualização do cód. do benefício no faturamento pelo produto | S | Veja opções na seção OPÇÕES |
| `ICMSNORMALDIFICMSSN` | Calcular diferencial de ICMS pela alíquota normal para Simples Nacional ? | S | Veja opções na seção OPÇÕES |
| `MDFEDOCSEMISPROPRIA` | Gerar MDF-e apenas com documentos de emissão própria? | S | Veja opções na seção OPÇÕES |
| `ESCRITCOMPRAEMISSPROP` | Escriturar compras de emissão própria (Tributação 10 e 70)? | S | Veja opções na seção OPÇÕES |
| `NFSEOBSITERPS` | Conteúdo a ser enviado na descrição de NFS-e | I | Veja opções na seção OPÇÕES |
| `QTDCARNFSEOBSITERPS` | Qtd. de caracteres a serem enviados na descrição de NFS-e | I |  |
| `REDPISBCPISCOFINS` | Deduzir valor do PIS/COFINS na BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `CONSIDQTCARCDESC` | Considerar o campo “Qtd. de caracteres", consid. inf. da Lei da Transparência? | S | Veja opções na seção OPÇÕES |
| `ENVLEITRANSPDESC` | Enviar as inf. da Lei da Transparência na desc. de cada item? | S | Veja opções na seção OPÇÕES |
| `CAFIR` | Cód. CAFIR - Cadastro de Imóveis Rurais | S |  |
| `ENVLEITRANSPTOTOBS` | Enviar inf. da Lei da Transparência com o total de impostos, na obs. da nota? | S | Veja opções na seção OPÇÕES |
| `GERALCDPR` | Gera informações para o Livro Caixa Digital Produtor Rural | S | Veja opções na seção OPÇÕES |
| `TIPOEXPLORACAO` | Tipo de Exploração | S | Veja opções na seção OPÇÕES |
| `CODEMPORIGMOVFIN` | Empresa de origem da movimentação financeira | I |  |
| `AMBIENTEGNRE` | Ambiente p/ GNRE | S | Veja opções na seção OPÇÕES |
| `VERSAOGNRE` | Versão GNRE | S | Veja opções na seção OPÇÕES |
| `CAEPF` | Cód. CAEPF - Cadastro de Atividade Econômica Pessoa Física | S |  |
| `DIRFPGEXT` | Declarante de rendimentos pagos a residentes ou domiciliados no exterior | S | Veja opções na seção OPÇÕES |
| `CODEMPMATRIZGNRE` | Empresa certificado (GNRE) | I |  |
| `CHAVEPIXCHECKOUT` | Chave PIX | S |  |
| `DIRFSITESP` | Situação Especial | S | Veja opções na seção OPÇÕES |
| `CALCVENCGNREAPU` | Calcula vencimento GNRE por Apuração? | S | Veja opções na seção OPÇÕES |
| `URLPIXCHECKOUT` | URL PIX | S |  |
| `DIRFDHEVENTO` | Data do Evento | D |  |
| `DIRFCPFRESP` | Cpf | S |  |
| `DIRFSOCOST` | Sócio ostensivo de sociedade em conta de participação | S | Veja opções na seção OPÇÕES |
| `DIRFDEPDECJUD` | Declarante depositário de crédito decorrente de decisão judicial | S | Veja opções na seção OPÇÕES |
| `DIRFDEPFUNINV` | Declarante de instituição administradora ou intermediadora de fundo ou clube de investimento | S | Veja opções na seção OPÇÕES |
| `DIRFPLPRIASS` | Plano privado de assistência à saúde – coletivo empresarial | S | Veja opções na seção OPÇÕES |
| `DIRFENTIMUNE` | Entidade em que a União detém maioria do capital social sujeito a voto | S | Veja opções na seção OPÇÕES |
| `DIRFPGFUNDPUB` | Fundação pública de direito privado | S | Veja opções na seção OPÇÕES |
| `DIRFNATDECL` | Natureza Declarante | S | Veja opções na seção OPÇÕES |
| `EMPCENTRALMOVFIN` | Empresa centralizadora da movimentação financeira | S | Veja opções na seção OPÇÕES |
| `DEDUZFCPBCPISCOFINS` | Deduzir valor de FCP e FCP ST na BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `USAINDPRESTOPFAT` | Buscar da TOP o indicador de presença ao faturar pedido/nota | S | Veja opções na seção OPÇÕES |
| `DTOPMULTA` | Data da Operação Multa (Campo 05) | S | Veja opções na seção OPÇÕES |
| `DTOPJUROS` | Data da Operação Juros (Campo 05) | S | Veja opções na seção OPÇÕES |
| `ENVINUTNOTAEXC` | Enviar inutilização de numeração na exclusão da nota (NF-e/NFC-e/CT-e) | S | Veja opções na seção OPÇÕES |
| `JUSINUTNOTAEXC` | Justificativa da inutilização de numeração na exclusão da nota (NF-e/NFC-e/CT-e) | S |  |
| `CALCFETHAB` | Calcular FETHAB | S | Veja opções na seção OPÇÕES |
| `CALCICMSAT` | Calcular ICMS Antecipado Entrada Interestaduais | S | Veja opções na seção OPÇÕES |
| `MSGINFADICFETHAB` | Mensagem FETHAB para Inform.Adicional NF-e | S |  |
| `CONSDEVNFEREINF` | Considerar devoluções de NF-e no R-2055 do EFD-REINF? | S | Veja opções na seção OPÇÕES |
| `NFECANEXTCANMES` | Considerar NF-e Cancelada Extemporânea como Cancelada no mês no EFD | S | Veja opções na seção OPÇÕES |
| `TOKENNFSE` | Token NFS-e | S |  |
| `INTFINOBRICMSSTREC` | Integrar o ICMS Normal Op. Própria a Recolher ao Financeiro | S | Veja opções na seção OPÇÕES |
| `GERCTECREDPISCOF` | Gerar CT-e somente com crédito de PIS/COFINS | S | Veja opções na seção OPÇÕES |
| `DESRESTRFCPCST` | Desabilita restrição de FCP por CST | S | Veja opções na seção OPÇÕES |
| `DESRESTRFCPSTCST` | Desabilita restrição de FCP/ST por CST | S | Veja opções na seção OPÇÕES |
| `EFDTIPREENCHNOTA` | Tipo Preenchimento Número Doc./Nota | S | Veja opções na seção OPÇÕES |
| `REDSTBCPISCOFINS` | Deduzir valor do ICMS/ST na BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `ORIGDESCONTOS` | Origem dos Descontos | I | Veja opções na seção OPÇÕES |
| `NOTAENTAJUSTERECLAS` | Modelo Ajuste de Entrada Reclassificação (Registro K220) | I |  |
| `NOTASAIAJUSTERECLAS` | Modelo Ajuste de Saída Reclassificação (Registro K220) | I |  |
| `INTEGRARIPIFIN` | Integrar IPI a Recolher ao Financeiro | S | Veja opções na seção OPÇÕES |
| `CODNATIPI` | Natureza Despesa Receitas IPI | I |  |
| `CODTIPOPERIPI` | Tipo Operação | I |  |
| `CODTIPTITIPI` | Tipo de Título | I |  |
| `DIAVENCIPI` | Dia de vencimento | I |  |
| `CODBCOIPI` | Banco | I |  |
| `CODCENCUSIPI` | Centro Resultado | I |  |
| `CODCTABCOIPI` | Conta Bancária | I |  |
| `CODPARCIPI` | Código do Parceiro | I |  |
| `CODRECEITAIPI` | Código de Receita | S |  |
| `TIPDATAEVTPAG` | Tipo Data p/ Dados Eventos Grupo 4000 - IR | S | Veja opções na seção OPÇÕES |
| `TIPDATAEVTPAGXIR` | Tipo Data p/ Dados Eventos Grupo 4000 - Exceto IR | S | Veja opções na seção OPÇÕES |
| `GER0220UNDFORN` | Gerar registro 0220 utilizando UND enviada pelo Fornecedor | S | Veja opções na seção OPÇÕES |
| `CODRECEITAREINF` | Código de Receita para atribuir Agregado/CSRF/PCC | S |  |
| `DTREFPREPRODREAISREINFG4000` | Referência Atual Reinf Grupo 4000 - Pré-produção - dados reais | D |  |
| `DTREFPRODREINFG4000` | Referência Atual Reinf Grupo 4000 - Produção | D |  |
| `CREDICMSREMG` | Creditar ICMS e ICMS/ST da NFe Entrada ref. Remessa Garantida (CST 010) | S |  |
| `DESAPCPRODEPE` | Desabilita a aplicação do PRODEPE do Dec. 38.296/2012 sobre as despesas acessórias | S | Veja opções na seção OPÇÕES |
| `CONSDIFPARCOUTICMS` | Considerar o valor diferimento parcial de ICMS (CST 51) para "Outras ICMS" no Livro Fiscal? | S | Veja opções na seção OPÇÕES |
| `GERMULTPLACRES` | Gerar múltiplas tags <Lacres> no XML? | S | Veja opções na seção OPÇÕES |
| `INDUNIAO` | Entidade Vinculada a União | I | Veja opções na seção OPÇÕES |
| `TPOBSFING4000` | Tipo de observação do financeiro p/ evento Grupo 4000 | I | Veja opções na seção OPÇÕES |
| `TPOBSNOTAG4000` | Tipo de observação da nota p/ evento Grupo 4000 | I | Veja opções na seção OPÇÕES |
| `DTTRANSFFINSLUCR` | Data transformação da entidade em fins lucrativos | D |  |
| `DTOBITO` | Data Óbito do Contribuinte | D |  |
| `STATUS` | Status | I | Veja opções na seção OPÇÕES |
| `USAMEDDIAIMP` | Usar o valor unitário do item nos valores médios de imposto | S | Veja opções na seção OPÇÕES |
| `CONSIDERARRESCOMPLST` | Considerar Operações com Ressarcimento/Complemento de ST | S | Veja opções na seção OPÇÕES |
| `REGAPURTRIBSN` | Regime de Apuração dos Tributos do Simples Nacional | S | Veja opções na seção OPÇÕES |
| `GERLDPERTRI` | Gerar Lucros e Dividendos com periodicidade trimestral | S | Veja opções na seção OPÇÕES |
| `WMSRASTSERMED` | Habilita controle de rastreabilidade série de medicamentos no WMS | S | Veja opções na seção OPÇÕES |
| `RUPTURAEST` | Calcular Ruptura de Estoque? | S | Veja opções na seção OPÇÕES |
| `UTILIZAWMS` | Controlado pelo WMS? | S | Veja opções na seção OPÇÕES |
| `EMPDESTINOWMS` | Empresa para estoque no WMS | I |  |
| `VLRUNITICMSOP` | Vlr. unitário do ICMS da operação de saída | S |  |
| `VLRICMSOPANT` | Vlr. do ICMS da operação anterior | S |  |
| `CODENDWMS` | Endereço p/ armazenagem/separação | I |  |
| `USACODBARRASCONCATWMS` | Utiliza cód. de barras concatenado | S | Veja opções na seção OPÇÕES |
| `VLRSTOPANT` | Vlr. do ST da operação anterior | S |  |
| `WMSUSAREGVOLFAT` | Utiliza registro de volumes no faturamento | S | Veja opções na seção OPÇÕES |
| `VLRSTFCPOPANT` | Vlr. ST FCP da operação anterior | S |  |
| `CODRESPRETC180` | Cód.ind. responsável p. retenção do ICMS-ST | S |  |
| `VLRUNITMERC` | Vlr. unitário do item | S |  |
| `VLRBASESTC180` | Vlr. unitário base ST | S |  |
| `VLRSTC180` | Vlr. unitário ST | S |  |
| `NOTAENTSOBRAWMS` | Nota modelo sobra estoque WMS (Entrada) | I |  |
| `NOTASAIPERDAWMS` | Nota modelo perda estoque WMS (Saída) | I |  |
| `TIPOCORTEWMS` | Tipo de corte na separação | S | Veja opções na seção OPÇÕES |
| `WMSLOCALAJEST` | Local para ajuste de estoque | I |  |
| `ENTAUTTARMAPA` | Entrega Automática de Mapas | S | Veja opções na seção OPÇÕES |
| `INTEGRAWMSPROD` | Utiliza Integração da Produção x WMS | S | Veja opções na seção OPÇÕES |
| `SERIEDEVWMS` | Série p/ devolução de mercadorias | S |  |
| `SERIETOPDIFMAIOR` | Série TOP diferença a maior(peso variável) | S |  |
| `TOPENTDIFPESOWMS` | TOP diferença a maior(peso variável) | I |  |
| `SERIETOPDIFMENOR` | Série TOP diferença a menor(peso variável) | S |  |
| `TOPSAIDADIFPESOWMS` | TOP diferença a menor(peso variável) | I |  |
| `TOPENTRADAWMS` | TOP de entrada de mercadorias | I |  |
| `TOPENVWMSAGRUP` | TOP pedido agrupado p/ enviar ao WMS (Expedição) | I |  |
| `TOPDEVOLUCAOWMS` | TOP p/ devolução de mercadorias | I |  |
| `CODENDSOBRA` | Cód. End. Sobra | I |  |
| `CODENDAVARIA` | Cód. End. Avaria | I |  |
| `CODENDPERDA` | Cód. End. Perda | I |  |
| `CODENDDIVERG` | Cód. End. Divergência | I |  |
| `WMSCODENDGAR` | Endereço especial de garantia | I |  |
| `UTILIZAEXPLOTE` | Utiliza explosão de lote no recebimento | S | Veja opções na seção OPÇÕES |
| `USARECPARCIAL` | Utiliza recebimento parcial? | S | Veja opções na seção OPÇÕES |
| `UTILIZATRICROSSDOCKING` | Utiliza triagem no Crossdocking | S | Veja opções na seção OPÇÕES |
| `WMSMULTIUSUCONF` | Múltiplos usuários na conferência de entrada | S | Veja opções na seção OPÇÕES |
| `QTDCONFENTWMS` | Qtd. padrão na conferência de entrada | I |  |
| `PROIBDIGCONFENT` | Proibir digitação de qtd. na conferência de entrada | S | Veja opções na seção OPÇÕES |
| `WMSUSAREGVOLREC` | Registra Volume na Conferência de Entrada | S | Veja opções na seção OPÇÕES |
| `INIBLOQREGCONF` | Inibe bloqueio do endereço no registro de conferência | S | Veja opções na seção OPÇÕES |
| `WMSCODENDFLUT` | Cód. End. Flutuante | I |  |
| `CODENDARMINDEF` | Cód. End. Armazenamento Indefinido | I |  |
| `WMSUSAETIQPAL` | Utiliza Etiqueta para Pálete | S | Veja opções na seção OPÇÕES |
| `ENDEMOVINDEF` | Endereço indefinido para movimentação | I |  |
| `USAMOVVERTWMS` | Utiliza Movimentação Vertical | S | Veja opções na seção OPÇÕES |
| `FRAGMENTAESTWMS` | Permitir estoque fragmentado | S | Veja opções na seção OPÇÕES |
| `WMSARMTOTALCOL` | Armazenar o total coletado no recebimento expresso | S | Veja opções na seção OPÇÕES |
| `REABCORRECAOWMS` | Gerar reabastecimento corretivo | S | Veja opções na seção OPÇÕES |
| `INIBEREABMAXPICKING` | Inibir o reabastecimento máximo do picking | S | Veja opções na seção OPÇÕES |
| `NROMAXPROD` | Nro. máximo de produtos no endereço | I |  |
| `CODENDCROSSDOCK` | Endereço CrossDocking | I |  |
| `MODESTCPAWMS` | Modelo Estorno WMS - Dev. Compra | I |  |
| `PERMOUTROUSUSEPPED` | Permite outro usuário continuar separação | S | Veja opções na seção OPÇÕES |
| `REABCOMPLETO` | Reabastecer somente quantidade completa do pulmão | S | Veja opções na seção OPÇÕES |
| `UTILIZAEXPLOTESEP` | Utiliza explosão de lote na separação | S | Veja opções na seção OPÇÕES |
| `WMSDOCASEPBALCAO` | Utiliza doca automaticamente separações balcão | S | Veja opções na seção OPÇÕES |
| `CODENDRETEXP` | Endereço para retorno de expedição | I |  |
| `CONSENTRPENDWMS` | Considerar armazenagens pendentes no envio para expedição | S | Veja opções na seção OPÇÕES |
| `ENTPENBALCAOWMS` | Envio ped. balcão considera entradas pendentes | S | Veja opções na seção OPÇÕES |
| `TRATOCWMS` | Tratamento p/falta de estoque no envio da OC | S | Veja opções na seção OPÇÕES |
| `CORTEFALTAWMS` | Cortar no MGE itens em falta no WMS | S | Veja opções na seção OPÇÕES |
| `UTILIZASEPPULMAO` | Utiliza separação pulmão | S | Veja opções na seção OPÇÕES |
| `WMSDOCAREP` | Permitir mais de uma OC na doca expedição | S | Veja opções na seção OPÇÕES |
| `SEPPULPARCIAL` | Utiliza separação parcial no pulmão | S | Veja opções na seção OPÇÕES |
| `WMSPERSEPPRODAP` | Permite separação por produto em área por pedido | S | Veja opções na seção OPÇÕES |
| `ENDECKTINDEF` | Endereço de checkout indefinido | I |  |
| `USASEPAGRUPROD` | Utiliza separação agrupada por produto | S | Veja opções na seção OPÇÕES |
| `PESMAXSEPAGRU` | Peso máx. do checkout por separação | F |  |
| `QTCHECKSEP` | Quantidade máx. de checkouts por separação | I |  |
| `VOLCHECKSEPROD` | Volumetria máx. do checkout por separação(M3) | F |  |
| `QTPEDSEPAGR` | Quantidade de pedidos por separação | I |  |
| `TRATSOBFINCONF` | Tratar sobra ao final da conferência? | S | Veja opções na seção OPÇÕES |
| `PROIBESCCHECKOUTPED` | Proibir escolha checkout na conferência do pedido | S | Veja opções na seção OPÇÕES |
| `WMSINFOPESODETVOL` | Informa peso no detalhamento de volume | S | Veja opções na seção OPÇÕES |
| `USAINFOADCONFPED` | Utiliza informação adicional na conferência do pedido? | S | Veja opções na seção OPÇÕES |
| `INIBELOTE` | Inibe solicitação lote na conferência pedido/saída | S | Veja opções na seção OPÇÕES |
| `IMPRESSORAETQVOL` | Impressora padrão da Etiqueta de Volume | S |  |
| `IMPETQVOL` | Impressão de etiqueta de volumes | I | Veja opções na seção OPÇÕES |
| `IMPETIQVOLCONF` | Imprimir etiquetas de volume na conferência | S | Veja opções na seção OPÇÕES |
| `IMPETIQSEPOC` | Imprime etiquetas de separação por OC | S | Veja opções na seção OPÇÕES |
| `WMSUSAIMPFECHAVOL` | Usa impressão de etiqueta ao fechar volume | S | Veja opções na seção OPÇÕES |
| `IMPRESSORAETQSEP` | Impressora padrão da etiqueta de separação | S |  |
| `CODMODRETESTWMS` | Modelo Retor. de Est. Gerencial WMS(Venda) | I |  |
| `CTACTBANLREGAPUR` | Contas contábeis analíticas para geração dos registros de apuração de PIS/COFINS | S | Veja opções na seção OPÇÕES |
| `TOKENIBPT` | Token IBPT | S |  |
| `CREDICMSCST60AM` | Creditar ICMS e ICMS ST de CT-e com CST 060 - Dec. 19671/99 AM | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPICMSFENVALBEM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | 1 - Considera a mesma tributação de ICMS aplicada ao item da nota |
| 2 | 2 - Considerar o valor do ICMS destacado no frete extra nota |

### Opções para campo ATIVO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Nao |
| S | Sim |

### Opções para campo ESTRNCREDICMSST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONTBAIBEMSUBIMPREC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USAVLRMEDTRANSFEMP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERCIAPCOMPEFD (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCICMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODSTPISCFBONIF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Operação Tributável com Alíquota Básica |
| 02 | 02-Operação Tributável com Alíquota Diferenciada |
| 03 | 03-Operação Tributável com Alíquota por Unidade de Medida de Produto |
| 04 | 04-Operação Tributável Monofásica - Revenda a Alíquota Zero |
| 05 | 05-Operação Tributável por Substituição Tributária |
| 06 | 06-Operação Tributável a Alíquota Zero |
| 07 | 07-Operação Isenta da Contribuição |
| 08 | 08-Operação sem Incidência da Contribuição |
| 09 | 09-Operação com Suspensão da Contribuição |
| 49 | 49-Outras Operações de Saída |
| 50 | 50-Operação com Direito a Crédito - Vinc.Exclus.Receita Tributada Mercado Interno |
| 51 | 51-Operação com Direito a Crédito - Vinc.Exclus.Receita Não-Tributada Mercado Interno |
| 52 | 52-Operação com Direito a Crédito - Vinc.Exclus. a Receita de Exportação |
| 53 | 53-Operação com Direito a Crédito - Vinc.Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 54 | 54-Operação com Direito a Crédito - Vinc.Receitas Tributadas no Mercado Interno e de Exportação |
| 55 | 55-Operação com Direito a Crédito - Vinc.Receitas Não Tributadas no Mercado Interno e de Exportação |
| 56 | 56-Operação com Direito a Crédito - Vinc.Receitas Tributadas e Não-Trib. no Mercado Int. e de Exp |
| 60 | 60-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita Tributada no Mercado Interno |
| 61 | 61-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita Não-Tributada no Mercado Interno |
| 62 | 62-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita de Exportação |
| 63 | 63-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 64 | 64-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas no Mercado Interno e de Exportação |
| 65 | 65-Crédito Presumido - Oper.Aquis.Vinc.Receitas Não-Tributadas no Mercado Interno e de Exportação |
| 66 | 66-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas e Não-Tributadas no Mercado Int e de Exp |
| 67 | 67-Crédito Presumido - Outras Operações |
| 70 | 70-Operação de Aquisição sem Direito a Crédito |
| 71 | 71-Operação de Aquisição com Isenção |
| 72 | 72-Operação de Aquisição com Suspensão |
| 73 | 73-Operação de Aquisição a Alíquota Zero |
| 74 | 74-Operação de Aquisição sem Incidência da Contribuição |
| 75 | 75-Operação de Aquisição por Substituição Tributária |
| 98 | 98-Outras Operações de Entrada |
| 99 | 99-Outras Operações |

### Opções para campo TRABCOMIPI (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESTIPIDEVCOM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IPIINCICMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRIBPISCFBONIF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCIRRF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCFUNRURAL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ICMSSCTTD (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EFDDIAVENC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 31 | Último Dia |

### Opções para campo CALCISS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isento |
| N | Não Tributado |
| S | Tributado |

### Opções para campo CSTIPIENT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Entrada c/Recuperação de Crédito |
| -1 | (-1)-Não sujeita ao IPI |
| 1 | 01-Entrada c/Alíquota zero |
| 2 | 02-Entrada Isenta |
| 3 | 03-Entrada Não Tributada |
| 4 | 04-Entrada Imune |
| 49 | 49-Outras Entradas |
| 5 | 05-Entrada c/Suspensão |

### Opções para campo CSTIPISAI (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| -1 | (-1)-Não sujeita ao IPI |
| 50 | 50-Saída Tributada |
| 51 | 51-Saída c/Alíquota zero |
| 52 | 52-Saída Isenta |
| 53 | 53-Saída Não Tributada |
| 54 | 54-Saída Imune |
| 55 | 55-Saída c/Suspensão |
| 99 | 99-Outras Saídas |

### Opções para campo TEMPIS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMCOFINS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EMITNFSENACIONAL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMCSSL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SALDOLIVQUINZ (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| D | Decendial |
| M | Mensal |
| Q | Quinzenal |

### Opções para campo SALDOLIVQUINZIPI (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| D | Decendial |
| M | Mensal |
| Q | Quinzenal |

### Opções para campo GERARLIVROS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GEROBSIPIREGENT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECMINTARE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo LIVRO1PARA1TGFITE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERAGNRE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCVLRAQUISBEM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | 1 - Seguindo as regras dos parâmetros |
| 2 | 2 - Valor do bem |
| 3 | 3 - Valor do bem sem ICMS operação própria |
| 4 | 4 - Valor do bem com ICMS diferencial de alíquotas |
| 5 | 5 - Valor do bem com ICMS diferencial de alíquotas, sem ICMS CIAP |

### Opções para campo REG54SEQ997ST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOIMPRESSORA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | ELEBRA/RIMA |
| 2 | EPSON |
| 3 | RIMA/ITAUTEC |
| 4 | ELGIN |
| 5 | OUTRAS |
| 6 | DESKJET |
| 7 | XEROX LASER |

### Opções para campo ALTCONTADOR (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EMITEEXPED (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERPROJ (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| C | Dezenal |
| D | Diária |
| M | Mensal |
| Q | Quinzenal |
| S | Semanal |

### Opções para campo PROJONLINE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODTRIB20RED (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| O | Outras |

### Opções para campo CODTRIB30 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| O | Outras |

### Opções para campo CODTRIB40ISENT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |

### Opções para campo CODTRIB41NAOTRIB (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| O | Outras |

### Opções para campo CODTRIB50SUSP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| O | Outras |

### Opções para campo CODTRIB51DIF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| O | Outras |

### Opções para campo CODTRIB60STANT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| O | Outras |

### Opções para campo CODTRIB70REDST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| O | Outras |
| X | Outras com redução em Isentas |

### Opções para campo CODTRIB90OUT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| O | Outras |

### Opções para campo NFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não usa |
| 1 | Produção |
| 2 | Homologação |

### Opções para campo TIPODANFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| P | Paisagem |
| R | Retrato |

### Opções para campo LAYOUTDANFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | Com IPI e sem Desconto |
| B | Com IPI e com Desconto |
| C | Sem IPI e com Desconto |

### Opções para campo VERSAONFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 401 | Versão NFe 2.0 |
| 502 | Versão NFe 2.0 e NFCe 3.10 |
| 503 | Versão NFe e NFCe 3.10 |
| 598 | Versão NFe 3.10 e NFCe 4.0 |
| 599 | Versão NFe 4.0 e NFCe 3.10 |
| 600 | Versão NFe e NFCe 4.00 |

### Opções para campo VERSAONT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 600 | Anterior |
| 9999 | Última (Nota Técnica 2021.004 - v 1.10) |

### Opções para campo IPINAOINCID (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| N | Nenhuma |
| O | Outras |
| P | Observação |

### Opções para campo STINCLUSA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| N | Nenhuma |
| O | Outras |

### Opções para campo CREDPIS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STINCLUSA70 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| N | Nenhuma |
| O | Outras |
| P | Observação |

### Opções para campo CREDCOFINS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRIORCODNAT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | TOP - Produto |
| 2 | Produto - TOP |

### Opções para campo PERFILEFD (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | Perfil A |
| B | Perfil B |
| C | Perfil C |

### Opções para campo INCENTCULT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOATIVIDADE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Industrial ou Equiparado a Industrial |
| 1 | Outros |

### Opções para campo NFSE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não usa |
| 1 | Produção |
| 2 | Homologação |

### Opções para campo REGIMEESPTRIBISS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | A - Empresa Individual de Responsabilidade Limitada (EIRELI) |
| C | C - Isenta de ISS |
| E | E - Não Incidência no Município |
| F | F - Imune |
| G | G - Tributável Fixo |
| H | H - Tributável S.N. |
| K | K - Exigibilidade Susp.Dec.J/Proc.A |
| M | M - Movimento mensal |
| N | N - Não Tributável |
| T | T - Tributável |
| 0 | 0 - Normal |
| 1 | 1 - Microempresa municipal |
| 2 | 2 - Estimativa |
| 3 | 3 - Sociedade de profissionais |
| 4 | 4 - Cooperativa |
| 5 | 5 - MEI (Simples Nacional) |
| 6 | 6 - ME EPP  (Simples Nacional) |
| 7 | 7 - Isenção Parcial |
| 8 | 8 - Média Empresa |
| 9 | 9 - Grande Empresa |

### Opções para campo COMPIPI (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BAIXAFINPREEMISSNFCE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODCLASSIFESTAB (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 00 | Industrial - Transformação |
| 01 | Industrial - Beneficiamento |
| 02 | Industrial - Montagem |
| 03 | Industrial - Acondicionamento ou Reacondicionamento |
| 04 | Industrial - Renovação ou Recondicionamento |
| 05 | Equiparado a industrial - Por opção |
| 06 | Equiparado a industrial - Importação Direta |
| 07 | Equiparado a industrial - Por lei específica |
| 08 | Equiparado a industrial - Não enquadrado nos códigos 05, 06 ou 07 |
| 09 | Outros |

### Opções para campo CODSTPISCFMULT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Operação Tributável com Alíquota Básica |
| 02 | 02-Operação Tributável com Alíquota Diferenciada |
| 03 | 03-Operação Tributável com Alíquota por Unidade de Medida de Produto |
| 04 | 04-Operação Tributável Monofásica - Revenda a Alíquota Zero |
| 05 | 05-Operação Tributável por Substituição Tributária |
| 06 | 06-Operação Tributável a Alíquota Zero |
| 07 | 07-Operação Isenta da Contribuição |
| 08 | 08-Operação sem Incidência da Contribuição |
| 09 | 09-Operação com Suspensão da Contribuição |
| 49 | 49-Outras Operações de Saída |
| 50 | 50-Operação com Direito a Crédito - Vinc.Exclus.Receita Tributada Mercado Interno |
| 51 | 51-Operação com Direito a Crédito - Vinc.Exclus.Receita Não-Tributada Mercado Interno |
| 52 | 52-Operação com Direito a Crédito - Vinc.Exclus. a Receita de Exportação |
| 53 | 53-Operação com Direito a Crédito - Vinc.Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 54 | 54-Operação com Direito a Crédito - Vinc.Receitas Tributadas no Mercado Interno e de Exportação |
| 55 | 55-Operação com Direito a Crédito - Vinc.Receitas Não Tributadas no Mercado Interno e de Exportação |
| 56 | 56-Operação com Direito a Crédito - Vinc.Receitas Tributadas e Não-Trib no Mercado Int. e de Exp |
| 60 | 60-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita Tributada no Mercado Interno |
| 61 | 61-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita Não-Tributada no Mercado Interno |
| 62 | 62-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita de Exportação |
| 63 | 63-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 64 | 64-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas no Mercado Interno e de Exportação |
| 65 | 65-Crédito Presumido - Oper.Aquis.Vinc.Receitas Não-Tributadas no Mercado Interno e de Exportação |
| 66 | 66-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas e Não-Tributadas no Mercado Int e de Exp |
| 67 | 67-Crédito Presumido - Outras Operações |
| 70 | 70-Operação de Aquisição sem Direito a Crédito |
| 71 | 71-Operação de Aquisição com Isenção |
| 72 | 72-Operação de Aquisição com Suspensão |
| 73 | 73-Operação de Aquisição a Alíquota Zero |
| 74 | 74-Operação de Aquisição sem Incidência da Contribuição |
| 75 | 75-Operação de Aquisição por Substituição Tributária |
| 98 | 98-Outras Operações de Entrada |
| 99 | 99-Outras Operações |

### Opções para campo CONTINGENCIANFCE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| C | EPEC |
| D | Perguntar ao usuário |
| G | Contingência Off-line |
| N | Não usar contingência |

### Opções para campo GERARTAXFINEMBNFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo IMPNFEEMISSPROP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NFESTANTCONSFINAL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Colocar zero |
| null | Colocar valor |

### Opções para campo NUMDOCR2020 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Nro. da NFS-e |
| null | Nro. do RPS |

### Opções para campo QRCODENFCEVERSAO2 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo QRCODENFCEVERSAO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Versão 2 |
| 3 | Versão 3 |

### Opções para campo TIPCTACTBEFD (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| C | Cadastros |
| T | Contabilização |

### Opções para campo TIPCTACTBEFDF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| C | Cadastros |
| T | Contabilização |

### Opções para campo TIPOENVIONFCE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | SEFAZ/Contingência |
| B | Preferir Contingência |
| C | Sempre Contingência |

### Opções para campo TRIBPISCFMULT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USASTEXTNOTARESTST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USATROCOCHECKOUT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BLQNFACOMPNFCPEND (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SUPRIMIREMAILDEST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODSTPISCFDESC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Operação Tributável com Alíquota Básica |
| 02 | 02-Operação Tributável com Alíquota Diferenciada |
| 03 | 03-Operação Tributável com Alíquota por Unidade de Medida de Produto |
| 04 | 04-Operação Tributável Monofásica - Revenda a Alíquota Zero |
| 05 | 05-Operação Tributável por Substituição Tributária |
| 06 | 06-Operação Tributável a Alíquota Zero |
| 07 | 07-Operação Isenta da Contribuição |
| 08 | 08-Operação sem Incidência da Contribuição |
| 09 | 09-Operação com Suspensão da Contribuição |
| 49 | 49-Outras Operações de Saída |
| 50 | 50-Operação com Direito a Crédito - Vinc.Exclus.Receita Tributada Mercado Interno |
| 51 | 51-Operação com Direito a Crédito - Vinc.Exclus.Receita Não-Tributada Mercado Interno |
| 52 | 52-Operação com Direito a Crédito - Vinc.Exclus. a Receita de Exportação |
| 53 | 53-Operação com Direito a Crédito - Vinc.Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 54 | 54-Operação com Direito a Crédito - Vinc.Receitas Tributadas no Mercado Interno e de Exportação |
| 55 | 55-Operação com Direito a Crédito - Vinc.Receitas Não Tributadas no Mercado Interno e de Exportação |
| 56 | 56-Operação com Direito a Crédito - Vinc.Receitas Tributadas e Não-Trib no Mercado Int. e de Exp |
| 60 | 60-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita Tributada no Mercado Interno |
| 61 | 61-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita Não-Tributada no Mercado Interno |
| 62 | 62-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita de Exportação |
| 63 | 63-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 64 | 64-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas no Mercado Interno e de Exportação |
| 65 | 65-Crédito Presumido - Oper.Aquis.Vinc.Receitas Não-Tributadas no Mercado Interno e de Exportação |
| 66 | 66-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas e Não-Tributadas no Mercado Int e de Exp |
| 67 | 67-Crédito Presumido - Outras Operações |
| 70 | 70-Operação de Aquisição sem Direito a Crédito |
| 71 | 71-Operação de Aquisição com Isenção |
| 72 | 72-Operação de Aquisição com Suspensão |
| 73 | 73-Operação de Aquisição a Alíquota Zero |
| 74 | 74-Operação de Aquisição sem Incidência da Contribuição |
| 75 | 75-Operação de Aquisição por Substituição Tributária |
| 98 | 98-Outras Operações de Entrada |
| 99 | 99-Outras Operações |

### Opções para campo CODSTPISCFJUROS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Operação Tributável com Alíquota Básica |
| 02 | 02-Operação Tributável com Alíquota Diferenciada |
| 03 | 03-Operação Tributável com Alíquota por Unidade de Medida de Produto |
| 04 | 04-Operação Tributável Monofásica - Revenda a Alíquota Zero |
| 05 | 05-Operação Tributável por Substituição Tributária |
| 06 | 06-Operação Tributável a Alíquota Zero |
| 07 | 07-Operação Isenta da Contribuição |
| 08 | 08-Operação sem Incidência da Contribuição |
| 09 | 09-Operação com Suspensão da Contribuição |
| 49 | 49-Outras Operações de Saída |
| 50 | 50-Operação com Direito a Crédito - Vinc.Exclus.Receita Tributada Mercado Interno |
| 51 | 51-Operação com Direito a Crédito - Vinc.Exclus.Receita Não-Tributada Mercado Interno |
| 52 | 52-Operação com Direito a Crédito - Vinc.Exclus. a Receita de Exportação |
| 53 | 53-Operação com Direito a Crédito - Vinc.Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 54 | 54-Operação com Direito a Crédito - Vinc.Receitas Tributadas no Mercado Interno e de Exportação |
| 55 | 55-Operação com Direito a Crédito - Vinc.Receitas Não Tributadas no Mercado Interno e de Exportação |
| 56 | 56-Operação com Direito a Crédito - Vinc.Receitas Tributadas e Não-Trib no Mercado Int. e de Exp |
| 60 | 60-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita Tributada no Mercado Interno |
| 61 | 61-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita Não-Tributada no Mercado Interno |
| 62 | 62-Crédito Presumido - Oper.Aquis.Vinc.Exclus.Receita de Exportação |
| 63 | 63-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 64 | 64-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas no Mercado Interno e de Exportação |
| 65 | 65-Crédito Presumido - Oper.Aquis.Vinc.Receitas Não-Tributadas no Mercado Interno e de Exportação |
| 66 | 66-Crédito Presumido - Oper.Aquis.Vinc.Receitas Tributadas e Não-Tributadas no Mercado Int e de Exp |
| 67 | 67-Crédito Presumido - Outras Operações |
| 68 | 70-Operação de Aquisição sem Direito a Crédito |
| 70 | 70-Operação de Aquisição sem Direito a Crédito |
| 71 | 71-Operação de Aquisição com Isenção |
| 72 | 72-Operação de Aquisição com Suspensão |
| 73 | 73-Operação de Aquisição a Alíquota Zero |
| 74 | 74-Operação de Aquisição sem Incidência da Contribuição |
| 75 | 75-Operação de Aquisição por Substituição Tributária |
| 98 | 98-Outras Operações de Entrada |
| 99 | 99-Outras Operações |

### Opções para campo TRIBPISCFDESC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRIBPISCFJUROS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo METCALCDIFICMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | Dif. de Alíq. – ICMS por dentro – sob diferença entre Alíquotas |
| B | Dif. entre Alíq. sobre Valor da BC |
| D | Dif. de Alíq. - ICMS por dentro, sem Red. da BC |
| E | Dif. de Alíq. - IPI - ICMS por dentro, sem Red. da BC |
| F | Dif. de Aliq. - Cálc. por Fórmula |
| G | Dif. de Alíq. sobre % Diferença das Alíquotas |
| I | Dif. de Alíq. - Cálculo Padrão |
| O | Dif. entre Alíq. sobre Valor da Operação |
| P | Dif. de Alíq. - ICMS por dentro, e com redução do valor de ST: |

### Opções para campo APLCALCDIFALIQFRT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIFALIQDESPACESS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIFALIQFCPINT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TPOEMPRESA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Empresa não participante de SCP como sócio ostensivo |
| 1 | 1 - Empresa participante de SCP como sócio ostensivo |
| 2 | 2 - SCP |

### Opções para campo COMPIPISEPICM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IGPERMCOMPPRODS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPICMSTOPENTSIMNAC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZAMDE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não utiliza |
| S | NF-e |
| T | NF-e/CT-e |

### Opções para campo INDESCRIT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Apuração com base nos registros de consolidação das operações por NF-e e ECF |
| 2 | 2 - Apuração com base nos registro individualizado de NF-e e ECF |

### Opções para campo TIPTRANSMNFSE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | Automática |
| M | Manual |

### Opções para campo INCENTFISCALISSQN (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONECTORNFSE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | ND Digital |
| S | Nativo do sistema |

### Opções para campo IMPCTEEMISPROP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TERACPCTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVIOSINCRONOCTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZADFETRANSP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TPAMBCTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não usa |
| 1 | Produção |
| 2 | Homologação |

### Opções para campo TPAMBNFCOM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não usa |
| 1 | Produção |
| 2 | Homologação |

### Opções para campo CONTINGENCIACTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | SVC |
| B | SVC/EPEC |
| C | EPEC |
| D | Perguntar ao usuário |
| E | Não usar contingência |

### Opções para campo TIPOENVIOCTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | SEFAZ/Contingência |
| B | Preferir contingência |
| C | Sempre Contingência |

### Opções para campo VERSAONTCTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 300 | Anterior |
| 9999 | Última (Nota Técnica 3.00a) |

### Opções para campo VERSAOCTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 200 | Versão CT-e 2.00 |
| 300 | Versão CT-e 3.00 |
| 400 | Versão CT-e 4.00 |

### Opções para campo INTERVALO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 15 | 15 minutos |
| 20 | 20 minutos |
| 30 | 30 minutos |
| 60 | 60 minutos |

### Opções para campo VALIDACPFCNPJ (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPODACTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Retrato |
| 2 | Paisagem |

### Opções para campo TPAMBMDFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não usa |
| 1 | Produção |
| 2 | Homologação |

### Opções para campo NATPESSOAJURIDICA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 00 | 00 - Pessoa jurídica em geral (não participante de SCP como sócia ostensiva) |
| 01 | 01 - Sociedade cooperativa (não participante de SCP como sócia ostensiva) |
| 02 | 02 - Entidade sujeita ao PIS/Pasep exclusivamente com base na Folha de Salários |
| 03 | 03 - Pessoa jurídica em geral participante de SCP como sócia ostensiva |
| 04 | 04 – Sociedade cooperativa participante de SCP como sócia ostensiva |
| 05 | 05 – Sociedade em Conta de Participação - SCP |

### Opções para campo RASTRESTOQUE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| E | Rastrear Doc. Fiscais e Não Fiscais |
| N | Não rastrear |
| S | Rastrear Doc. Fiscais |

### Opções para campo CONESTORIGPROD (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não controla |
| 0 | Para todos os produtos (Com rastreamento de estoque) |
| 1 | Verificar no produto |

### Opções para campo BANCOPIXCHECKOUT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | BANCO DO BRASIL (BB) |
| 341 | ITAÚ UNIBANCO |

### Opções para campo VLRLIQITEMNFCE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOATIVIDADEPISCOFINS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Industrial ou Equiparado a Industrial |
| 1 | 1 - Prestador de serviços |
| 2 | 2 - Atividade de comércio |
| 3 | 3 - Atividade financeira |
| 4 | 4 - Atividade imobiliária |
| 9 | 9 - Outros |

### Opções para campo TIRASERVLRCONTAB (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GRAVAROBSNOTA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOENVIONFCOM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | SEFAZ/Contingência |
| B | Preferir Contingência |
| C | Sempre Contingência |

### Opções para campo TIPOENVIONFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | SEFAZ/Contingência |
| B | Preferir Contingência |
| C | Sempre Contingência |

### Opções para campo GERADEDUCAOPF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AGRUPASERVFAT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMPREMIACAOESTADUAL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COMPLRESTITUICAOICMSST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| F | Restituição do ICMS/ST - Fato Gerador Presumido Não Realizado |
| N | Não se aplica |
| null | Complemento/Restituição ICMS/ST - Aspecto Quantitativo |

### Opções para campo MARCANOTRPS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSVLRLIQNFSE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TPLIGACAO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Monofásico |
| 2 | Bifásico |
| 3 | Trifásico |

### Opções para campo CODGRUPOTENSAO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 01 | A1 - Alta Tensão (230 KV ou mais) |
| 02 | A2 - Alta Tensão (88 KV a 138 KV) |
| 03 | A3 - Alta Tensão (69 KV) |
| 04 | A3a - Alta Tensão (30 KV a 44 KV) |
| 05 | A4 - Alta Tensão (2,3 KV a 25 KV) |
| 06 | AS - Alta Tensão Subterrâneo 06 |
| 07 | B1 - Residencial 07 |
| 08 | B1 - Residencial Baixa Renda 08 |
| 09 | B2 - Rural 09 |
| 10 | B2 - Cooperativa de Eletrificação Rural |
| 11 | B2 - Serviço Público de Irrigação |
| 12 | B3 - Demais Classes |
| 13 | B4a - Iluminação Pública - rede de distribuição |
| 14 | B4b - Iluminação Pública - bulbo de lâmpada |

### Opções para campo CLASCONS_ENERG (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 01 | Comercial |
| 02 | Consumo Próprio |
| 03 | Iluminação Pública |
| 04 | Industrial |
| 05 | Poder Público |
| 06 | Residencial |
| 07 | Rural |
| 08 | Serviço Público |

### Opções para campo TPLIGACAOINF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CLASCONS_GAS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 01 | Comercial |
| 02 | Consumo Próprio |
| 03 | Iluminação Pública |
| 04 | Industrial |
| 05 | Poder Público |
| 06 | Residencial |
| 07 | Rural |
| 08 | Serviço Público |

### Opções para campo CLASCONS_AGUA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 00 | 00 registro consolidando os documentos de consumo residencial até R$ 50,00 |
| 01 | 01 registro consolidando os documentos de consumo residencial de R$ 50,01 a R$ 100,00 |
| 02 | 02 registro consolidando os documentos de consumo residencial de R$ 100,01 a R$ 200,00 |
| 03 | 03 registro consolidando os documentos de consumo residencial de R$ 200,01 a R$ 300,00 |
| 04 | 04 registro consolidando os documentos de consumo residencial de R$ 300,01 a R$ 400,00 |
| 05 | 05 registro consolidando os documentos de consumo residencial de R$ 400,01 a R$ 500,00 |
| 06 | 06 registro consolidando os documentos de consumo residencial de R$ 500,01 a R$ 1000,00 |
| 07 | 07 registro consolidando os documentos de consumo residencial acima de R$ 1.000,01 |
| 20 | 20 registro consolidando os documentos de consumo comercial/industrial até R$ 50,00 |
| 21 | 21 registro consolidando os documentos de consumo comercial/industrial de R$ 50,01 a R$ 100,00 |
| 22 | 22 registro consolidando os documentos de consumo comercial/industrial de R$ 100,01 a R$ 200,00 |
| 23 | 23 registro consolidando os documentos de consumo comercial/industrial de R$ 200,01 a R$ 300,00 |
| 24 | 24 registro consolidando os documentos de consumo comercial/industrial de R$ 300,01 a R$ 400,00 |
| 25 | 25 registro consolidando os documentos de consumo comercial/industrial de R$ 400,01 a R$ 500,00 |
| 26 | 26 registro consolidando os documentos de consumo comercial/industrial de R$ 500,01 a R$ 1.000,00 |
| 27 | 27 registro por documento fiscal de consumo comercial/industrial acima de R$ 1.000,01 |
| 80 | 80 registro consolidando os documentos de consumo de órgão público |
| 90 | 90 registro consolidando os documentos de outros tipos de consumo até R$ 50,00 |
| 91 | 91 registro consolidando os documentos de outros tipos de consumo de R$ 50,01 a R$ 100,00 |
| 92 | 92 registro consolidando os documentos de outros tipos de consumo de R$ 100,01 a R$ 200,00 |
| 93 | 93 registro consolidando os documentos de outros tipos de consumo de R$ 200,01 a R$ 300,00 |
| 94 | 94 registro consolidando os documentos de outros tipos de consumo de R$ 300,01 a R$ 400,00 |
| 95 | 95 registro consolidando os documentos de outros tipos de consumo de R$ 400,01 a R$ 500,00 |
| 96 | 96 registro consolidando os documentos de outros tipos de consumo de R$ 500,01 a R$ 1.000,00 |
| 97 | 97 registro consolidando os documentos de outros tipos de consumo acima de R$ 1.000,01 |
| 99 | 99 registro por documento fiscal emitido |

### Opções para campo TPASSINANTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Comercial/Industrial |
| 2 | Poder Público |
| 3 | Residencial/Pessoa física |
| 4 | Público |
| 5 | Semi-Público |
| 6 | Outros |

### Opções para campo TPASSINANTEINF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONTINGENCIANFCOM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| D | Perguntar ao usuário |
| N | Não usar contingência |

### Opções para campo CONTINGENCIANFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| C | EPEC |
| D | Perguntar ao usuário |
| E | SVC |
| F | SVC/EPEC |
| N | Não usar contingência |

### Opções para campo FLEX (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GRAVAROBSPADRAO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VLRLIQITEMNFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODEPE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMREAICMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERNOTAENT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GRAVARSERIENOTA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRATARTRIBUT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRATARDIFPARC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USATRIBUTITENS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FRETESEPCONSTRANSP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FRETESEPSEMPRE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSOUTROSIMP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODTRIB53 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| O | Outras |

### Opções para campo CODTRIB61 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| I | Isentas |
| O | Outras |

### Opções para campo GERARPRODLIVENT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERARPRODORIGKIT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRATARTRIBUTDEFEMP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSDEVTEREVTR2050 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GEROBSFING4000 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GEROBSNOTAG4000 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCREDDIFCIAP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USADTFABLOTNFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USADTVALLOTNFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USANOMECOMPLITEM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMDENUESPONT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DENUNCESPCTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVRESPCONTNFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ISALIQINTSEXC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SERNAOTRIBBASEISS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVRESPCONTCTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VERSAOMDFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 100 | Versão MDFe 1.00 |
| 300 | Versão MDFe 3.00 |

### Opções para campo ENVMDFSINC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRANSPCARGA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Empresa transportadora de cargas (ETC) |
| 3 | Cooperativa transportadora de cargas (CTC) |

### Opções para campo REDICMSBCPISCONFINS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| D | Deduz para CT-e e NF-e |
| N | Não Deduz |
| O | Deduz para NF-e |
| S | Deduz para CT-e |
| T | Configurado pela TOP |

### Opções para campo REDISSBCPISCONF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| D | Deduz para NFS-e e NF-e |
| null | Não Deduz |
| O | Deduz para NF-e |
| S | Deduz para NFS-e |

### Opções para campo REDDIFALBCPISCOF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSREPICMSBASEPISCOF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AMBIENTEREINF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Produção |
| 2 | Produção restrita - dados reais |
| 3 | Produção restrita - dados fictícios |

### Opções para campo PARTCANALVERDE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRIBREINF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 01 | Empresa enquadrada no regime de tribut. Simples Nacional c/ tribut. previdenciária substit. |
| 02 | Empresa enquadrada no regime de tribut. Simples Nacional com tribut. previdenciária não substit. |
| 03 | Empresa enquadrada no regime de tribut. Simples Nacional c/tribut. previd. subst. e não subst. |
| 04 | MEI - Micro Empreendedor Individual |
| 06 | Agroindústria |
| 07 | Produtor Rural Pessoa Jurídica |
| 08 | Consórcio Simplificado de Produtores Rurais |
| 09 | Órgão Gestor de Mão de Obra |
| 10 | Entidade Sindical a que se refere a Lei 12.023/2009 |
| 11 | Associação desportiva que mantém clube de futebol profissional |
| 13 | Banco, caixa econômica, sociedade de credito 1° art. 22 da Lei 8.212/91. |
| 14 | Sindicatos em geral, exceto aquele classificado no código [10] |
| 21 | Pessoa Física, exceto Segurado Especial |
| 22 | Segurado Especial |
| 60 | Missão diplomática ou repartição consular de carreira estrangeira |
| 70 | Empresa de que trata o Decreto 5.436/2005 |
| 80 | Entidade Imune ou Isenta |
| 85 | Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas |
| 99 | Pessoas Jurídicas em Geral |

### Opções para campo ENTREGAECD (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SITEMPREINF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Situação Normal |
| 1 | Extinção |
| 2 | Fusão |
| 3 | Cisão |
| 4 | Incorporação |

### Opções para campo EMPADMPUBDIR (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESONERAFOLHACPRB (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VINCULOEFR (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Ente Federativo Responsável - EFR |
| 2 | Unidade Adm. Autônoma Vinculada a EFR |

### Opções para campo CAMCONVPREF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Cód. Natureza Oper. ISS |
| NR | Cód. Natureza Oper. ISS e Regime esp. tributação ISS |
| R | Regime esp. tributação ISS |

### Opções para campo CONSDEVEVTR2050 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERNOTAENTCANC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSIDBENEF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REDSTCOMPBCPISCOFINS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DEDICMSBCPISCOFINS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODTRIB90CREDDEB (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo TIPCONEXSMTPXML (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| S | Segura com SSL |
| T | Segura com TLS |

### Opções para campo GERARRETENCAO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Como pagamento (detPag) com 90 - sem pgto, e sem valor |
| 1 | Como pagamento (detPag) com 90 - sem pgto, e com valor |
| 2 | Como desconto da fatura e sem pagamento (detPag) |

### Opções para campo TIPGERINFGVEICGREB (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| E | Dentro do Estado |
| M | Dentro do Município |
| T | Todas as Operações |

### Opções para campo CONICMSMAJFCPINT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo GERLIVICMSEMPSN (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCICMSSTNAOCONT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo ENVEMAILCONF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROGAQUISALIM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VERSAONTMDFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 300 | Anterior (Nota Técnica 2020.001) |
| 9999 | Última (Nota Técnica 2021.002) |

### Opções para campo OBTSTANTMEDENT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IPITRIBUTDEFEMP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DEFCSTIPI00 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |
| 1 | Com Créd/Déb de imposto |
| 2 | Com Créd/Déb - Isentas |
| 3 | Com Créd/Déb - Outras |

### Opções para campo DEFCSTIPI01 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo DEFCSTIPI02 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo DEFCSTIPI03 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo DEFCSTIPI04 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo CALCPISCFSFIN (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USACUSTOMEDIOMPS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| G | Gerencial |
| N | Não considerar |
| S | Reposição |

### Opções para campo DEFCSTIPI05 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo USACUSMEDICMPRO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERCHAVEREFSIG (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDTIPLAYOUTK010 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | 1 - Leiaute completo |
| 0 | 0 - Leiaute simplificado |
| 2 | 2 - Leiaute restrito aos saldos de estoque |

### Opções para campo ENVINFISSSOMDEVIDO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DEFCSTIPI49 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |
| 1 | Com Créd/Déb de imposto |
| 2 | Com Créd/Déb - Isentas |
| 3 | Com Créd/Déb - Outras |

### Opções para campo SOMARFCPBCCIAP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOPIX (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | API (BB e Itaú) |
| N | NÃO USA |
| T | TEF |

### Opções para campo TIPDATAEVTSERV (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| E | Dt. Entrada/Saída |
| F | Dt. Faturamento |
| M | Dt. Movimento |
| null | Dt. Negociação |

### Opções para campo DEFCSTIPI50 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |
| 1 | Com Créd/Déb de imposto |
| 2 | Com Créd/Déb - Isentas |
| 3 | Com Créd/Déb - Outras |

### Opções para campo DEFCSTIPI51 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo DEFCSTIPI52 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo DEFCSTIPI53 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo DEFCSTIPI54 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo DEFCSTIPI55 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |

### Opções para campo DEFCSTIPI99 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Isentas |
| O | Outras |
| 1 | Com Créd/Déb de imposto |
| 2 | Com Créd/Déb - Isentas |
| 3 | Com Créd/Déb - Outras |

### Opções para campo ENVIOSINCRONONFE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo ENVIOSINCRONONFCE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo ATUALCBENEFFAT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não atualizar |
| 1 | Atualizar se não informado |
| 2 | Atualizar se diferente do cadastro |
| 3 | Sempre atualizar |

### Opções para campo ICMSNORMALDIFICMSSN (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MDFEDOCSEMISPROPRIA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ESCRITCOMPRAEMISSPROP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NFSEOBSITERPS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Padrão conforme prefeitura |
| 1 | Descrição dos itens de serviços |
| 2 | Descrição + obs. dos itens de serviços |
| 3 | Observação da nota |
| 4 | Observação + Natureza da nota |
| 5 | Descrição + obs. dos itens de serviços + obs. da nota |
| 6 | Descrição dos itens + $$$ + obs. da nota |

### Opções para campo REDPISBCPISCOFINS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| D | Deduz para CT-e e NF-e |
| null | Não Deduz |
| O | Deduz para NF-e |
| S | Deduz para CT-e |
| T | Configurado pela TOP |

### Opções para campo CONSIDQTCARCDESC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVLEITRANSPDESC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVLEITRANSPTOTOBS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERALCDPR (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOEXPLORACAO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Exploração individual |
| 2 | Condomínio |
| 3 | Imóvel arrendado |
| 4 | Parceria |
| 5 | Comodato |
| 6 | Outros |

### Opções para campo AMBIENTEGNRE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não usa |
| 1 | Produção |
| 2 | Homologação |

### Opções para campo VERSAOGNRE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 100 | 1.0 |
| 200 | 2.0 |

### Opções para campo DIRFPGEXT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIRFSITESP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCVENCGNREAPU (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIRFSOCOST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIRFDEPDECJUD (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIRFDEPFUNINV (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIRFPLPRIASS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIRFENTIMUNE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIRFPGFUNDPUB (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIRFNATDECL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 – Pessoa jurídica de direito privado |
| 1 | 1 - Órgãos, autarquias e fundações da administração pública federal |
| 2 | 2 - Órgãos, autarquias e fundações da adm. pública estadual, municipal ou do Distrito Federal |
| 3 | 3 - Empresa pública ou sociedade de economia mista federal |
| 4 | 4 - Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal |
| 8 | 8 - Entidade com alteração de natureza jurídica (uso restrito) |

### Opções para campo EMPCENTRALMOVFIN (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DEDUZFCPBCPISCOFINS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não Deduz |
| S | Deduz para NF-e |
| T | Configurar na TOP |

### Opções para campo USAINDPRESTOPFAT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DTOPMULTA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| D | Data da Baixa |
| U | Último dia do período da escrituração |

### Opções para campo DTOPJUROS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| D | Data da Baixa |
| U | Último dia do período da escrituração |

### Opções para campo ENVINUTNOTAEXC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCFETHAB (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCICMSAT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSDEVNFEREINF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NFECANEXTCANMES (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTFINOBRICMSSTREC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERCTECREDPISCOF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESRESTRFCPCST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESRESTRFCPSTCST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EFDTIPREENCHNOTA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| DIG_USU | Digitado pelo usuário |
| PREENCH_AUT | Gerar com número único |

### Opções para campo REDSTBCPISCOFINS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| D | Deduz para CT-e e NF-e |
| N | Não Deduz |
| O | Deduz para NF-e |
| S | Deduz para CT-e |
| T | Configurado pela TOP |

### Opções para campo ORIGDESCONTOS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Todos |
| 1 | Estoque e Financeiro |

### Opções para campo INTEGRARIPIFIN (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPDATAEVTPAG (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| B | Dt. Baixa |
| E | Dt. Entrada/Saída |
| F | Dt. Faturamento |
| M | Dt. Movimento |
| null | Dt. Negociação |

### Opções para campo TIPDATAEVTPAGXIR (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| B | Dt. Baixa |
| E | Dt. Entrada/Saída |
| F | Dt. Faturamento |
| M | Dt. Movimento |
| null | Dt. Negociação |

### Opções para campo GER0220UNDFORN (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESAPCPRODEPE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSDIFPARCOUTICMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERMULTPLACRES (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDUNIAO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não utiliza entidade vinculada a união |
| 0 | Não aplicável |
| 1 | Órgão, autarquias e fund. da admin. púb. fed. direta, soc. de econ. mista ou demais entidades... |

### Opções para campo TPOBSFING4000 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Observação Padrão |
| 2 | Histórico |

### Opções para campo TPOBSNOTAG4000 (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Observação |
| 2 | Observação Padrão |

### Opções para campo STATUS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Credenciais não Configuradas |
| 1 | Credenciais Configuradas |

### Opções para campo USAMEDDIAIMP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSIDERARRESCOMPLST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGAPURTRIBSN (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Reg. Apuração Trib. Fed. e Mun. pelo SN |
| 2 | 2 - Reg. Apuração Trib. Fed. pelo SN e ISS pela NFSe conforme legislação municipal |
| 3 | 3 - Reg. Apuração Trib. Fed. e Mun. pela NFSe conforme legislação Fed. e Mun. de cada tributo |

### Opções para campo GERLDPERTRI (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSRASTSERMED (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RUPTURAEST (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZAWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USACODBARRASCONCATWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSUSAREGVOLFAT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOCORTEWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| M | Maior Quantidade |
| N | Menor Quantidade |
| P | Proporcionalizado |

### Opções para campo ENTAUTTARMAPA (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTEGRAWMSPROD (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZAEXPLOTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USARECPARCIAL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZATRICROSSDOCKING (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSMULTIUSUCONF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROIBDIGCONFENT (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSUSAREGVOLREC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INIBLOQREGCONF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSUSAETIQPAL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USAMOVVERTWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FRAGMENTAESTWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSARMTOTALCOL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REABCORRECAOWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INIBEREABMAXPICKING (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMOUTROUSUSEPPED (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REABCOMPLETO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZAEXPLOTESEP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSDOCASEPBALCAO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSENTRPENDWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENTPENBALCAOWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRATOCWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CORTEFALTAWMS (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZASEPPULMAO (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSDOCAREP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SEPPULPARCIAL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSPERSEPPRODAP (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USASEPAGRUPROD (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| A | Sim, conforme área de separação |
| N | Não usa |
| S | Sim, conforme empresa |

### Opções para campo TRATSOBFINCONF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROIBESCCHECKOUTPED (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSINFOPESODETVOL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USAINFOADCONFPED (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INIBELOTE (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMPETQVOL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Ao fim da conferência |
| 1 | Ao colocar o produto na doca |

### Opções para campo IMPETIQVOLCONF (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMPETIQSEPOC (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo WMSUSAIMPFECHAVOL (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CTACTBANLREGAPUR (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CREDICMSCST60AM (Tabela: TGFEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFENFE
### Descrição: Eventos de Nota Fiscal Eletrônica

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TEXTOCORRECAO` | Texto Carta de Correção | C |  |
| `NUNOTA` | NUNOTA | I |  |
| `CODEVENTO` | CODEVENTO | I |  |
| `SEQEVENTO` | SEQEVENTO | I |  |
| `NULOTE` | NULOTE | I |  |
| `PROCESSADO` | PROCESSADO | S |  |
| `NROPROTAUT` | Nro. Protocolo de Autorização do Evento | S |  |

## Tabela: TGFESE
### Descrição: Entrada/Saída de Estoque

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DTREFERENCIA` | Data de Referência | H |  |
| `TIPMOV` | Tipo de Movimento | S |  |
| `CODTIPOPER` | Cód. Tipo de Operação | I |  |
| `CODPROD` | Cód. Produto | I |  |
| `CODEMP` | Cód. Empresa | I |  |
| `CODLOCALORIG` | Cód. Local de Origem | I |  |
| `CONTROLE` | Controle | S |  |
| `ATUALESTOQUE` | Atualiza Estoque | I |  |
| `ATUALESTTERC` | Atualiza Estoque de Terceiros | S |  |
| `QTDNEG` | Qtd. Negociada | F |  |
| `QTDENTRADAS` | Qtd. de Entradas | F |  |
| `QTDSAIDAS` | Qtd. Saídas | F |  |
| `CODEMPCONTPART` | Cód. Empresa Transferência | I |  |

## Tabela: TGFEST
### Descrição: Estoque

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `ESTDOCAWMS` | Estoque em docas de entrada do WMS | I |  |
| `CODEMP` | Empresa | I |  |
| `CODLOCAL` | Local | I |  |
| `CODPROD` | Cód. Prod. | I |  |
| `CONTROLE` | Controle | S |  |
| `ESTOQUE` | Estoque | F |  |
| `RESERVADO` | Reservado | F |  |
| `ESTMIN` | Estoque Mínimo | F |  |
| `ESTMAX` | Estoque Máximo | F |  |
| `CODBARRA` | Cód. de Barras | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `DTVAL` | Data de Validade | D |  |
| `CODPARC` | Parceiro | I |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `PERCPUREZA` | % Pureza | F |  |
| `PERCGERMIN` | % Germinação | F |  |
| `DTFABRICACAO` | Data de Fabricação | D |  |
| `STATUSLOTE` | Status Lote | S |  |
| `WMSBLOQUEADO` | Bloqueado no WMS | F |  |
| `CODAGREGACAO` | Cód. de Agregação | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPO (Tabela: TGFEST)
| Valor | Descrição |
|-------|-----------|
| P | Próprio |
| T | Terceiro |


## Tabela: TGFEXB
### Descrição: Extrato Bancário

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUEXB` | Cód. Extrato | I |  |
| `NROCTA` | Núm. Conta | S |  |
| `DTLANC` | Data Lançamento | D |  |
| `VALOR` | Valor | F |  |
| `NRODOC` | Núm. Documento | I |  |
| `CONCILIADO` | Conciliado | S | Veja opções na seção OPÇÕES |
| `CODCATEG` | Cód. Categoria | I |  |
| `CNPJ_CPF` | Cnpj/Cpf | S |  |
| `HIST` | Histórico | S |  |
| `CONVENIO` | Convênio | F |  |
| `CODBCO` | Banco | I |  |
| `RECDESP` | Receita/Despesa | I | Veja opções na seção OPÇÕES |
| `CODUSU` | Cód. Usuário Alteração | I |  |
| `NUIMPORT` | Núm. Importação | I |  |
| `TIPOTRANSACAO` | Tipo de transação | S |  |
| `DHALTER` | Data alteração | H |  |
| `FITID` | ID da Transação | S |  |
| `NUBCO` | Núm. Único Bancário | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo CONCILIADO (Tabela: TGFEXB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECDESP (Tabela: TGFEXB)
| Valor | Descrição |
|-------|-----------|
| -1 | Despesa |
| 1 | Receita |


## Tabela: TGFEXC
### Descrição: Tabela de Exeções

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPROD` | Produto | I |  |
| `CODUSUALTREG` | Cód. Usuário Alteração | I |  |
| `VLRANT` | Preço anterior | F |  |
| `VARIACAO` | Variação % | F |  |
| `DHALTREG` | Dt. Alteração | H |  |
| `NUTAB` | Tabela | I |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `VLRVENDA` | Preço | F |  |
| `CODLOCAL` | Local | I |  |
| `CONTROLE` | Controle | S |  |
| `AD_COMISSAO` | Comissao | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TGFEXC)
| Valor | Descrição |
|-------|-----------|
| P | Percentual |
| V | Valor |


## Tabela: TGFFAM
### Descrição: Família de Produtos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPRODPAI` | Produto pai | I |  |
| `CODPRODFILHO` | Produto filho | I |  |
| `COMPLDESC` | Complemento | S |  |
| `MARCA` | Marca | S |  |
| `REFERENCIA` | Referência | S |  |

## Tabela: TGFFCP
### Descrição: Fórmula de Composição do Produto

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPROD` | Produto | I |  |
| `CODLOCAL` | Local | I |  |
| `CONTROLE` | Controle | S |  |
| `VARIACAO` | Variação | I |  |
| `CICLOPRODUCAO` | Ciclo de produção | F |  |
| `UNIDCICLO` | Unidade do Ciclo | S | Veja opções na seção OPÇÕES |
| `MULTIPLOIDEAL` | Múltiplo Ideal | I |  |
| `PRODUCAOMIN` | Produção Mínima | F |  |
| `FORMPRINCIPAL` | Fórmula principal | S | Veja opções na seção OPÇÕES |
| `MARGLUCRO` | Margem de lucro | F |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `DESVIO` | Desvio Sup.(%) | F |  |
| `DESVIOINF` | Desvio Inf.(%) | F |  |
| `OBSERVACAO` | Observação | S |  |
| `MENORDTVAL` | Considerar Menor Dt. Validade ? | S | Veja opções na seção OPÇÕES |
| `REGMAPA` | Registrada no M.A.P.A? | S | Veja opções na seção OPÇÕES |
| `VARIACAOREL` | Variação Relacionada | I |  |
| `CODEST` | Estrutura de Produção | I |  |
| `CODPRC` | Cód. Processo | I |  |
| `IDPROC` | IDPROC | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo UNIDCICLO (Tabela: TGFFCP)
| Valor | Descrição |
|-------|-----------|
| D | Dias |
| E | Meses |
| H | Horas |
| M | Minutos |
| S | Segundos |

### Opções para campo FORMPRINCIPAL (Tabela: TGFFCP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVO (Tabela: TGFFCP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MENORDTVAL (Tabela: TGFFCP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGMAPA (Tabela: TGFFCP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFFIN
### Descrição: Financeiro

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUFIN` | Nro Único | I |  |
| `METODOCALCIRRF` | Método de Cálculo IRRF | S | Veja opções na seção OPÇÕES |
| `NUMOCORRENCIAS` | Nr. da Ocorrência Caixa | S |  |
| `NUCAIXA` | Núm. Caixa | I |  |
| `NUMNOTA` | Nro Nota | I |  |
| `SERIENOTA` | Série da Nota | S |  |
| `SANGDESPDV` | Sangria de despesa PDV | S | Veja opções na seção OPÇÕES |
| `CODPARC` | Parceiro | I |  |
| `CGC_CPF_PARC` | CNPJ / CPF | S |  |
| `CODEMP` | Empresa | I |  |
| `CONTABILIZADOPDD` | Título contabilizado PDD | S |  |
| `PERTENCEAC` | Pertence ao acerto de carga | S | Veja opções na seção OPÇÕES |
| `DESCRHISTAC` | Descrição histórico | S |  |
| `OBSERVACAOAC` | Observação | S |  |
| `RETORNADOAC` | Retornado | S | Veja opções na seção OPÇÕES |
| `STATUSLIB` | Status liberação | I | Veja opções na seção OPÇÕES |
| `RECDESP` | Receita/Despesa | I | Veja opções na seção OPÇÕES |
| `PROVISAO` | Provisão | S | Veja opções na seção OPÇÕES |
| `DTVENC` | Dt. Vencimento | D |  |
| `DTNEG` | Dt. Negociação | D |  |
| `DHBAIXA` | Data Baixa | D |  |
| `DHMOV` | Dt/Hr Movimentação | H |  |
| `DTBAIXAPREV` | Dt. Prevista p/ Baixa | H |  |
| `DTENTSAI` | Dt. Entrada e Saída | D |  |
| `CODPARCMATRIZ` | Cod. Parceiro Matriz | I |  |
| `NROCESSAOFDIC` | Nro. Cessao FDIC | S |  |
| `VLRDESDOBCALC` | Vlr do Desdobramento Calc | F |  |
| `CONTABILIZADO` | Contabilizado? | S | Veja opções na seção OPÇÕES |
| `VLRDESDOB` | Vlr do Desdobramento | F |  |
| `VLRDESC` | Vlr Desconto | F |  |
| `VLRATUAL` | Vlr. Atual | I |  |
| `VLRMULTA` | Vlr Multa | F |  |
| `VLRJURO` | Vlr Juros | F |  |
| `VLRVENDOR` | Vlr Vendor | F |  |
| `VLRALIBERAR` | Vlr. a liberar | F |  |
| `VLRBAIXA` | Vlr Baixa | F |  |
| `VLRLIQUIDO` | Valor Líquido | F |  |
| `DESDOBDUPL` | Desdob. Duplicata | S |  |
| `ATRASO` | Atraso (dias) | I |  |
| `HISTORICO` | Histórico | S |  |
| `CODHISTAC` | Histórico | I |  |
| `CODTIPOPER` | Tipo Operação | I |  |
| `CODTIPTIT` | Tipo de Título | I |  |
| `BASEICMS` | Base ICMS | F |  |
| `CODNAT` | Natureza | I |  |
| `CODCENCUS` | Centro Resultado | I |  |
| `CODPROJ` | Projeto | I |  |
| `NUMCONTRATO` | Nro Contrato | I |  |
| `REFATCON` | Ref. Faturamento do Contrato | D |  |
| `ORIGEM` | Origem | S | Veja opções na seção OPÇÕES |
| `CODVEND` | Vendedor | I |  |
| `CODCBE` | Acerto Benefício | I |  |
| `CODREGUA` | Régua | I |  |
| `AUTORIZADO` | Autorizado | S | Veja opções na seção OPÇÕES |
| `CARTA` | Nro Carta | I |  |
| `CODOBSPADRAO` | Observação padrão | I |  |
| `DTINITREFAPURACAO` | Data apuração | H |  |
| `VALORPRESENTE` | Valor Presente | F |  |
| `JUROSAVP` | Juros Ajuste do Valor Presente | F |  |
| `BLOQVAR` | Bloq. Calculo Variação | S | Veja opções na seção OPÇÕES |
| `NUCOMPENS` | Nro Compensação/Acerto | I |  |
| `INDRECEFDCONT` | Indicador de Receita (registro F525 - EFD Cont.) | S | Veja opções na seção OPÇÕES |
| `CODFUNC` | Funcionário | I |  |
| `INFCOMPLEFDCONT` | Informação complementar do Indic. comp. receita recebida | S |  |
| `CODCONTATO` | Contato | I |  |
| `PDD` | PDD | S | Veja opções na seção OPÇÕES |
| `CODIMOVELRURAL` | Imóvel Rural | I |  |
| `RECADIANTAMENTORURAL` | Receita de Adiantamentos | S | Veja opções na seção OPÇÕES |
| `CONCILIADO` | Conciliado | S | Veja opções na seção OPÇÕES |
| `DHCONCIL` | Dh. Conciliação | H |  |
| `IDTRANSACAOPIX` | TXID Pix | S |  |
| `ANTECIPADO` | Antecipado | S | Veja opções na seção OPÇÕES |
| `DTANTECIPACAO` | Dt. antecipação | D |  |
| `M2` | Metro Quadrado | F |  |
| `NUANTBANC` | Nro. único antecipação | I |  |
| `PRAZO` | Prazo | I |  |
| `CODMOEDA` | Moeda | I |  |
| `VLRVARCAMBIAL` | Variação Cambial | F |  |
| `VLRJUROCALC` | Juros Calculados | F |  |
| `VLRMOEDA` | Vlr Moeda | F |  |
| `VLRMULTACALC` | Multa Calculada | F |  |
| `TIPJURO` | Tipo Juro | S | Veja opções na seção OPÇÕES |
| `VLRTOTALCALC` | Total Calculado | F |  |
| `VLRTROCO` | Vlr Troco | F |  |
| `TIPMULTA` | Tipo Multa | S | Veja opções na seção OPÇÕES |
| `VLRMULTAEMBUT` | Vlr Multa Embutida | F |  |
| `VLRJUROEMBUT` | Vlr Juros Embutidos | F |  |
| `NUMTRANSF` | Nro da Transferência | I |  |
| `CODLANC` | Cód. Lançamento | I |  |
| `VLRJUROLIB` | Vlr Perdão de Juros | F |  |
| `VLRMULTALIB` | Vlr Perdão de Multa | F |  |
| `DHTIPOPERBAIXA` | Dt/Hr Tipo Operação | H |  |
| `VLRJURONEGOC` | Vlr Juros Negociados | F |  |
| `VLRMULTANEGOC` | Vlr Multa Negociada | F |  |
| `DESCRLANCBCO` | Desc. Lanc. Bancário | S |  |
| `CTABCOBAIXA` | Conta Baixa | S |  |
| `RECDESPFILTER` | Rec Desp p/ o Filtro | S |  |
| `CODUSUBAIXA` | Usuário Baixa | I |  |
| `RATEADO` | Rateado | S | Veja opções na seção OPÇÕES |
| `CODTIPOPERBAIXA` | Tipo Operação Baixa | I |  |
| `CODEMPBAIXA` | Emp. da Baixa | I |  |
| `VLRMOEDABAIXA` | Vlr Moeda na Baixa | F |  |
| `ORDEMCARGA` | Ordem de Carga | I |  |
| `VLRPROV` | Vlr Provisão Financeira | F |  |
| `CODVEICULO` | Veículo | I |  |
| `NURENEG` | Nro Renegociação | I |  |
| `RATEADOCAB` | Proveniente de nota rateada | S |  |
| `PARCRENEG` | Parcelas da Renegociação | S |  |
| `NUCKC` | Nro. Checkout | I |  |
| `VLRICMS` | Vlr ICMS | F |  |
| `SEQCAIXA` | Seq. Caixa | I |  |
| `MOSTRARENEG` | Mostrar Renegociados | S |  |
| `IDLOTEFDIC` | Identificador do Lote FDIC | I |  |
| `VLRCESSAO` | Vlr. Cessão FDIC | F |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Últ. Alteração | H |  |
| `DTCONTABBAIXA` | Dt. Contabilização Baixa | H |  |
| `VLRDESCEMBUT` | Vlr Desc. Embutido | F |  |
| `NUBCO` | Nro Único Bancário | I |  |
| `NUVERBA` | Nro. Verba | I |  |
| `VLRLANCORIG` | Valor lançamento | F |  |
| `PIXTEF` | Pix TEF | I |  |
| `DTPRAZO` | Dt. Prazo | D |  |
| `RECEBCARTAO` | Recebim. c/ cartão | S | Veja opções na seção OPÇÕES |
| `VLRDESCCALC` | Vlr. Desconto Calc. | F |  |
| `CODUSUCOBR` | CODUSUCOBR | I |  |
| `CODBCO` | Banco | I |  |
| `CODCTABCOINT` | Conta Bancária | I |  |
| `CODBARRA` | Código de Barras | S |  |
| `CODIGOBARRA` | Cód. Barras Receb. | S |  |
| `TPAGNFCE` | Tipo de pgto para NFC-e | S | Veja opções na seção OPÇÕES |
| `DESDOBRAMENTO` | Desdob. | S |  |
| `DTNEGFILTER` | Filtro p/ Dt Negociação | D |  |
| `NOSSONUM` | Nosso Número | S |  |
| `NUNOTA` | Nro Único Nota | I |  |
| `LINHADIGITAVEL` | Linha Dig. Receb. | S |  |
| `DHTIPOPER` | Dt/Hr Operação | H |  |
| `NUMREMESSA` | Nro Remessa | I |  |
| `NUMDUPL` | Nro Duplicata | I |  |
| `IDUNICO` | Identificador boleto rápido | I |  |
| `MONIOCOREM` | Monitora Ocorrência de Remessa | S | Veja opções na seção OPÇÕES |
| `ABATIMENTO` | Abatimento (Cob. Registrada) | F |  |
| `ABATIMENTOCAN` | Abatimento Cancelado (Cob. Registrada) | F |  |
| `EMVPIX` | PIX Copia e Cola | S |  |
| `DTCONTAB` | Dt. Contabilização | H |  |
| `NUPED` | Número Único do Pedido | I |  |
| `NUDEV` | Nro Único Devolução | I |  |
| `NUMNFSE` | Nro. NFS-e | S |  |
| `CHAVECTEREF` | Chave CT-e de referência | S |  |
| `NUCCR` | Nro do cartão de crédito | I |  |
| `CHAVECTE` | Chave CT-e | S |  |
| `CODCFO` | CFOP | I |  |
| `CODLST` | Tipo de Serviço | I |  |
| `OBRACONSTCIVIL` | Obra de Construção Civil | I | Veja opções na seção OPÇÕES |
| `CODOBRA` | Cód. da Obra | S |  |
| `CODCIDFIMCTE` | Cód. Cid. Fim CT-e | I |  |
| `CODCIDINICTE` | Cód. Cid. Inicio CT-e | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `DESCRTPAGNFCE` | Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros) | S |  |
| `CODTRIB` | Tributação CT-e | I | Veja opções na seção OPÇÕES |
| `NUMOS` | Nro da OS | I |  |
| `CLASSIFCESSAOOBRA` | Classificação Cessão M.d.Obra | I | Veja opções na seção OPÇÕES |
| `DTENTSAIINFO` | Data Extemporânea | D |  |
| `CODCC` | CODCC | I |  |
| `DIGSAFRA` | Dígito Safra | S |  |
| `REGESPTRIBUT` | Regime Especial de Tributação DES-BH | S |  |
| `NUAPONTA` | Nro Único Apontamento | I |  |
| `AD_DESCONTADO` | Descontado | S | Veja opções na seção OPÇÕES |
| `AD_DTPAGO` | Dt. Pagamento | D |  |
| `BASEIRF` | Base IRF | F |  |
| `AD_PAGO` | Pendente | S | Veja opções na seção OPÇÕES |
| `AD_COMISSIONAR` | Gerar Comissão | S | Veja opções na seção OPÇÕES |
| `ALIQICMS` | % ICMS | F |  |
| `BASEINSS` | Base INSS | F |  |
| `NUMBOR` | Nro Borderô | I |  |
| `INSSRETIDO` | INSS Retido | S | Veja opções na seção OPÇÕES |
| `IRFRETIDO` | IRRF Retido | S | Veja opções na seção OPÇÕES |
| `ISSRETIDO` | ISS Retido | S | Veja opções na seção OPÇÕES |
| `VLRINSS` | Vlr INSS | F |  |
| `VLRIRF` | Vlr IRF | F |  |
| `ATRASOINICIAL` | Atraso 1º Vencto (dias) | I |  |
| `VLRISS` | Vlr ISS | F |  |
| `PERCDESC` | Percentual de Desconto | F |  |
| `VLRJUROSMAISMULTA` | Juros + Multa | F |  |
| `PRAZOINICIAL` | Prazo 1º Vencto | I |  |
| `TIMVENDALOTE` | Contrato de venda de lote | I |  |
| `VLRCHEQUE` | Vlr Cheque | F |  |
| `TIPMARCCHEQ` | Tipo Marcação Cheque | S | Veja opções na seção OPÇÕES |
| `NOMEEMITENTE_CMC7` | Nome Emitente CMC7 | S |  |
| `CGC_CPF_CMC7` | CNPJ/CPF CMC7 | S |  |
| `CODBCO_CMC7` | Código Banco CMC7 | I |  |
| `AGENCIA_CMC7` | Agência CMC7 | S |  |
| `CONTA_CMC7` | Conta CMC7 | S |  |
| `DESCALINEACHEQDEV` | Alínea Dev. Cheque | S |  |
| `TIMVENDAIMV` | Contrato de venda do imóvel | I |  |
| `TIMRENEGIMV` | Renegociação da venda do imóvel | I |  |
| `AD_CTEAGR` | Ctes Agrupados | S |  |
| `CHEQUERASTREADO_CMC7` | Cheque rastreado | S |  |
| `AD_VLRPROD` | Vlr Produtos | F |  |
| `NUCHQ` | Nro. cheque | I |  |
| `AD_VLRCOM` | Valor Comissão | F |  |
| `AD_BASECOM` | Base comissão | F |  |
| `CHAVEPIX` | Chave Pix | S |  |
| `SUBTIPOVENDA` | Subtipo do Tipo de Título | F |  |
| `CARTAODESC` | Taxa Administradora | F |  |
| `AD_DTCARTORIO` | Dt. Cartório | D |  |
| `NUFTC` | Nro único da fatura | I |  |
| `VLRFATCARTAO` | Vlr. Fatura Cartão | F |  |
| `AD_DTVENCORI` | Vencimento Inicial | D |  |
| `AD_EMPCONTA` | Emp. da Conta | I |  |
| `CODRECEITA` | Código receita Darf | S |  |
| `DTREFERENCIA` | Período de referência | D |  |
| `AD_ORDERCARGA` | Ordem Carga NF | I |  |
| `DTINTEGRACAOIPI` | Data integração | D |  |
| `AD_COBAUTO` | Cobrança Automática | S | Veja opções na seção OPÇÕES |
| `AD_CONCILIACAO` | Conciliação | I |  |
| `AD_NOTACTE` | Notas do CTE | S |  |
| `TAXAVENDAMAIS` | Taxa Venda Mais | F |  |
| `DHAPROVACAOVENDAMAIS` | Dt. Aprovação | H |  |
| `CODOPERACAOVENDAMAIS` | Código da Operação | S |  |
| `VENDAMAIS` | Venda Mais | S | Veja opções na seção OPÇÕES |
| `NROLOTEGNRE` | Número Lote GNRE | I |  |
| `REJEICAOGNRE` | Motivo Rejeição GNRE | S |  |
| `STATUSGNRE` | Status GNRE | S |  |
| `CHAVENFEGNRE` | Chave de acesso NFe | S |  |
| `TIPAPURACAO` | Tipo Apuração | S | Veja opções na seção OPÇÕES |
| `VLRGNREDOIS` | Vlr GNRE dois | F |  |
| `PRORROGADO` | Prorrogado VM | S | Veja opções na seção OPÇÕES |
| `NVDTVENC` | Nova data de vencimento | D |  |
| `CODUSUPROR` | Prorrogado por | I |  |
| `PENDENTECRIARDESP` | Prorrogado VM | S |  |
| `DTPROR` | Prorrogado em | H |  |
| `CODPROR` | Cód. Prorrogação VM | S |  |
| `CUSTASPROCESSUAIS` | Custas Processuais? | S | Veja opções na seção OPÇÕES |
| `RECEBIDO` | Recebido | S | Veja opções na seção OPÇÕES |
| `AD_EMPRESA` | Empresa | I |  |
| `DEPOSITOJUDICIAL` | Depósito Judicial? | S | Veja opções na seção OPÇÕES |
| `AD_ADICIONAIS` | Dados Adicionais | S |  |
| `DESPADVOGADO` | Desp. com Advogado(s)? | S | Veja opções na seção OPÇÕES |
| `DESPCART` | Despesas c/ Cartório | F |  |
| `AD_CONFERENCIA` | Conferência | S |  |
| `AD_RAZAO` | Razao | S |  |
| `NUMPROCADMJUDIC` | Nº Processo Administrativo/Judicial | S |  |
| `AD_VENDEDOR` | Vendedor | S |  |
| `EXIGEISSQN` | Exigibilidade do ISSQN DES-BH | S |  |
| `MODELONFDES` | Modelo NF DES-BH | S |  |
| `NATUREZAOPERDES` | Natureza Oper. DES-BH | S | Veja opções na seção OPÇÕES |
| `SERIENFDES` | Série NF DES-BH | S |  |
| `MOTNAORETERISSQN` | Motivo de não Retenção ISSQN DES-BH | S |  |
| `SITESPECIALRESP` | Situação Especial de Responsabilidade DES-BH | S |  |
| `DTVENCINIC` | Dt. Venc. Inicial | H |  |
| `TIMDHGERREPPARCIAL` | Dh. Ger. Rep. Parcial | H |  |
| `TIMBLOQUEADA` | Bloqueada | S | Veja opções na seção OPÇÕES |
| `TIMVLRCORRMONET` | Vlr. Corr. Monetária | F |  |
| `TIMVLRJUROCONTRATO` | Vlr. Juro Contrato | F |  |
| `CODIPTU` | Conta IPTU | I |  |
| `TIMVLRALUGUEL` | Vlr. Aluguel | F |  |
| `TIMVLRAMORTCONTRATO` | Vlr. Amortização Contrato | F |  |
| `TIMDTIMPBOLLOCAL` | Dh. Imp. Local Boleto | H |  |
| `TIMDTREPPARCIAL` | Dt. Repasse Parcial | D |  |
| `TIMTIPOINTERMED` | Tipo de Intermediária | I |  |
| `TIMCONTALANC` | Conta Lançamento | I |  |
| `TIMESTAGIO` | Estágio | S |  |
| `TIMTXADMGERALU` | Tx Adm pela Parcela | S | Veja opções na seção OPÇÕES |
| `TIMREPPARCIAL` | Repasse Parcial | S | Veja opções na seção OPÇÕES |
| `TIMFINGARANTORIG` | Fin. Resp. Garantia | I |  |
| `TIMREPINTELIGENTE` | Usuário Rep. Inteligente | I |  |
| `TIMRESCISAOLOC` | Rescisão de Locação | I |  |
| `TIMORIGEM` | Tipo Parcela | S | Veja opções na seção OPÇÕES |
| `TIMDHGERREPASSE` | Dh. Ger. Repasse | H |  |
| `TIMORIGRENEG` | Repactuação | S | Veja opções na seção OPÇÕES |
| `TIMDATADEJUR` | Dt. Ida Jurídico | H |  |
| `TIMPARCELA` | Parcela | I |  |
| `TIMCONTRATOLOC` | Contrato de Locação | I |  |
| `TIMCONTRATOLTV` | Contrato de Venda Lotes | I |  |
| `TIMNEGOCIACAO` | Negociação | I |  |
| `TIMRENEGLOTE` | Renegociação Contrato | I |  |
| `TIMNUFINORIG` | Financeiro Origem | I |  |
| `TIMIMOVEL` | Imóvel | I |  |
| `TIMCONTRATOADM` | Contrato Adm. | I |  |
| `TIMDHBAIXA` | Dt. Pagamento | H |  |
| `TIMDTREPASSE` | Dt. Repasse | D |  |
| `TIMSAC` | Atendimento ao cliente (OS) | I |  |
| `TIMFECHAMENTO` | Fechamento Cond. | I |  |
| `TIMFECHAMENTOALU` | Fechamento Aluguel Perc. | I |  |
| `TIMCONTAREP` | Conta rep. prop. | I |  |
| `TIMDTIMPBOL` | Dt. Impressão Boleto | H |  |
| `TIMNOMEADVOGADO` | Advogado | S |  |
| `TIMNUMREG` | Sequência Banco | I |  |
| `TIMRENEGCANCLOTE` | Renegociado Por | I |  |
| `TIMRESCISAOLTV` | Rescisão de Contrato | I |  |
| `BAIXAAPI` | Baixa via API | S |  |
| `NROIMPORT` | Nro da importação | I |  |
| `NFCOMPLFIX` | Nf. Complemento Fixação | I |  |
| `NFENTSEQFIX` | Nf. Entrada Fixação/Sequência | S |  |
| `NUMENTSAFFIX` | Nro Nota Entrada Fixação | I |  |
| `SERIEENTSAFFIX` | Série Entrada Fixação | S |  |
| `NUMCOMPLFIX` | Nro Nota Complemento Fixação | I |  |
| `SERIENOTACOMPL` | Série Complemento Fixação | S |  |
| `TROCOPDV` | Vlr Troco | F |  |
| `NUMDOCARRECAD` | Nro Documento de arrecadação | S |  |
| `DH_IMPRESSAO` | Data Impressão | D |  |
| `AD_CONTBANC` | Conta Banc. | S |  |
| `VLRICMSXMLCTE` | Vlr ICMS_XML | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo METODOCALCIRRF (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| L | Por Deduções Legais |
| S | Por Desconto Simplificado |

### Opções para campo SANGDESPDV (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERTENCEAC (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RETORNADOAC (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSLIB (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| 1 | Pendente |
| 2 | Sem solicitação |
| 3 | Autorizado |
| 4 | Não autorizado |

### Opções para campo RECDESP (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| -1 | Despesa |
| 1 | Receita |

### Opções para campo PROVISAO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONTABILIZADO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ORIGEM (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| E | Estoque |
| F | Financeiro |
| P | Pessoal |

### Opções para campo AUTORIZADO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BLOQVAR (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDRECEFDCONT (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| 01 | 01- Clientes |
| 02 | 02- Administradora de cartão de débito/crédito |
| 03 | 03- Título de crédito - Duplicata, nota promissória, cheque, etc. |
| 04 | 04- Documento fiscal |
| 05 | 05- Item vendido (produtos e serviços) |
| 99 | 99-Outros |

### Opções para campo PDD (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECADIANTAMENTORURAL (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONCILIADO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANTECIPADO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPJURO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| 1 | Incluso |
| 2 | Extra Nota |

### Opções para campo TIPMULTA (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| 1 | Incluso |
| 2 | Extra Nota |

### Opções para campo RATEADO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECEBCARTAO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TPAGNFCE (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Dinheiro |
| 02 | 02-Cheque |
| 03 | 03-Cartão de Crédito |
| 04 | 04-Cartão de Débito |
| 05 | 05-Crédito Loja |
| 10 | 10-Vale Alimentação |
| 11 | 11-Vale Refeição |
| 12 | 12-Vale Presente |
| 13 | 13-Vale Combustível |
| 14 | 14-Duplicata Mercantil |
| 15 | 15-Boleto Bancário |
| 16 | 16-Depósito Bancário |
| 17 | 17-Pagamento Instantâneo (PIX) |
| 18 | 18-Transferência bancária, Carteira Digital |
| 19 | 19-Programa de fidelidade, Cashback, Crédito Virtual |
| 90 | 90-Sem pagamento |
| 99 | 99-Outros |

### Opções para campo MONIOCOREM (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OBRACONSTCIVIL (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Empreitada Total |
| 2 | 2 - Empreitada Parcial |

### Opções para campo CODTRIB (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Tributada integralmente |
| 02 | 02-Tributação monofásica própria sobre combustíveis |
| 10 | 10-Tributada e c/cobrança por substituição |
| 15 | 15-Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis |
| 20 | 20-Com redução de base de cálculo |
| 30 | 30-Isenta e não tribut.e c/cobrança por subst. |
| 40 | 40-Isenta |
| 41 | 41-Não tributada |
| 50 | 50-Suspensão |
| 51 | 51-Diferimento |
| 53 | 53-Tributação monofásica sobre combustíveis com recolhimento diferido |
| 60 | 60-ICMS cobrado anteriormente por substituição |
| 61 | 61-Tributação monofásica sobre combustíveis cobrada anteriormente |
| 70 | 70-Com redução de base e c/cobrança por subst. |
| 90 | 90-Outras |

### Opções para campo CLASSIFCESSAOOBRA (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| 100000001 | Limpeza, conservação ou zeladoria |
| 100000002 | Vigilância ou segurança |
| 100000003 | Construção civil |
| 100000004 | Serviços de natureza rural |
| 100000005 | Digitação |
| 100000006 | Preparação de dados para processamento |
| 100000007 | Acabamento |
| 100000008 | Embalagem |
| 100000009 | Acondicionamento |
| 100000010 | Cobrança |
| 100000011 | Coleta ou reciclagem de lixo ou de resíduos |
| 100000012 | Copa |
| 100000013 | Hotelaria |
| 100000014 | Corte ou ligação de serviços públicos |
| 100000015 | Distribuição |
| 100000016 | Treinamento e ensino |
| 100000017 | Entrega de contas e de documentos |
| 100000018 | Ligação de medidores |
| 100000019 | Leitura de medidores |
| 100000020 | Manutenção de instalações, de máquinas ou de equipamentos |
| 100000021 | Montagem |
| 100000022 | Operação de máquinas, de equipamentos e de veículos |
| 100000023 | Operação de pedágio ou de terminal de transporte |
| 100000024 | Operação de transporte de passageiros |
| 100000025 | Portaria, recepção ou ascensorista |
| 100000026 | Recepção, triagem ou movimentação de materiais |
| 100000027 | Promoção de vendas ou de eventos |
| 100000028 | Secretaria e expediente |
| 100000029 | Saúde |
| 100000030 | Telefonia ou telemarketing |
| 100000031 | Trabalho temporário na forma da Lei nº 6.019, de janeiro de 1974 |

### Opções para campo AD_DESCONTADO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| Nao | Não |

### Opções para campo AD_PAGO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| Nao | Não |

### Opções para campo AD_COMISSIONAR (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| nao | Não |

### Opções para campo INSSRETIDO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IRFRETIDO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ISSRETIDO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPMARCCHEQ (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| A | Nominal ao fornecedor |
| B | Agrupar nominal ao fornecedor |
| C | Nominal ao bco. de pgto. |
| D | Agrupar nominal ao bco de pagto |
| E | Não nominal |
| F | Agrupar não nominal |
| G | Nominal ao histórico |
| H | Agrupar nominal ao histórico |
| I | Sem emitir cheque |
| J | Nominal à empresa |
| K | Agrupar nominal à empresa |

### Opções para campo AD_COBAUTO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |

### Opções para campo VENDAMAIS (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPAPURACAO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| A | ICMS FCP Interno |
| B | ST FCP Interno |
| C | ICMS |
| D | ICMS DIFAL |
| F | ICMS FCP |
| S | ICMS ST |
| T | ICMS ST FCP |

### Opções para campo PRORROGADO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CUSTASPROCESSUAIS (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECEBIDO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DEPOSITOJUDICIAL (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESPADVOGADO (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NATUREZAOPERDES (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| A | A-Sem Dedução |
| B | B-Com Dedução |
| C | C-Isenta de ISSQN |
| D | D-Devolução/Simples Remessa |
| E | E-Não Incidência |
| F | F-Imune |
| G | G-Construção Civil |
| H | H-Regime Estimativa |
| I | I-Sociedade Profissional |
| J | J-Microempresa |
| K | K-Depósito em Juízo |
| L | L-Incentivo a Cultura |
| M | M-Inscrito na PBH |
| N | N-Turismo/Fundos |
| O | O-Intermed./Public. - Isento |
| P | P-Intermediação / Publicidade |
| Q | Q-Não Tributável |

### Opções para campo TIMBLOQUEADA (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMTXADMGERALU (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMREPPARCIAL (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMORIGEM (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| AC | Acumulada |
| AL | Aluguel |
| AR | Arras |
| AV | Avulsa |
| BA | Balão |
| CC | Condomínio Comum |
| CD | Parcela CDU |
| CM | Complemento |
| CP | Comissão Cancelada |
| CR | Compensar Rescisão |
| DC | Pagamento Comissão |
| DP | Devolução Provisão |
| DR | Devolução Real |
| DV | Financeiro Vinculado |
| EA | Extinta Aluguel |
| EN | Entrada |
| EV | Extinta Avulsa |
| FB | Financiado Banco |
| FC | Fechamento |
| FF | Fechamento Banco |
| FI | Financiamento |
| FP | Parceria |
| IT | ITU |
| JU | Juros |
| LT | Loteamento |
| MF | MFD |
| NR | Negociação Rescisão |
| OU | Outros |
| PC | Comissão |
| PD | Diferenciada |
| PI | Intermediária |
| PP | FPP |
| RB | Repasse ao Beneficiário |
| RL | Registro de Lote |
| RP | Repasse |

### Opções para campo TIMORIGRENEG (Tabela: TGFFIN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFFIN_EXC
### Descrição: TGFFIN_EXC

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Cód. Usuário | I |  |
| `INSSRETIDO` | INSS Retido | S |  |
| `IRFRETIDO` | IRF Retido | S |  |
| `DHEXCLUSAO` | Data Hora Exclusão | H |  |
| `CODUSUBAIXA` | Cód. Usuário Baixa | I |  |
| `CODBARRA` | Código de barras | S |  |
| `NUMREMESSA` | Número da remessa | I |  |
| `VLRBAIXA` | Valor da baixa | F |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `NUMNOTA` | Número da nota | I |  |
| `VLRISS` | Valor do ISS | F |  |
| `TIPMARCCHEQ` | Tipo marcação cheque | S |  |
| `BASEICMS` | Base ICMS | F |  |
| `DTVENCINIC` | Data vencimento inicial | H |  |
| `VLRPROV` | Valor da Provisão Financeira | F |  |
| `VLRVENDOR` | Valor do vendor | F |  |
| `DESDOBRAMENTO` | Desdobramento | S |  |
| `CODBCO` | Banco cobrança | I |  |
| `HOSTNAME` | HOSTNAME | S |  |
| `ISSRETIDO` | ISS Retido | S |  |
| `VLRCHEQUE` | Valor do Cheque | F |  |
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `RECDESP` | Receita ou Despesa | I |  |
| `DHTIPOPERBAIXA` | Data e hora operação baixa | H |  |
| `CODMOEDA` | Moeda | I |  |
| `USUARIO` | Usuário | S |  |
| `CODVEND` | Vendedor | I |  |
| `CODCENCUS` | Cód.Centro Resultado | I |  |
| `ALIQICMS` | Alíquota ICMS | F |  |
| `DESPCART` | Despesas com cartório | F |  |
| `NT_USERNAME` | NT_USERNAME | S |  |
| `NOSSONUM` | Nosso número | S |  |
| `CODTIPTIT` | Tipo de título | I |  |
| `NURENEG` | Número da Renegociação | I |  |
| `DHMOV` | Data e hora do movimento | H |  |
| `CODEMPBAIXA` | Empresa da baixa | I |  |
| `CODEMP` | Empresa | I |  |
| `NUNOTA` | Número único Nota | I |  |
| `CODPROJ` | Projeto | I |  |
| `DTCONTAB` | Data de Contabilização | H |  |
| `CODNAT` | Cód. Natureza | I |  |
| `NUMDUPL` | Número da duplicata | I |  |
| `NUFIN` | Número único Financeiro | I |  |
| `VLRJURO` | Valor do juro | F |  |
| `DESDOBDUPL` | Desdobramento duplicata | S |  |
| `AUTORIZADO` | Autorizado | S |  |
| `VLRMULTA` | Valor da multa | F |  |
| `CODTIPOPERBAIXA` | Cód.Tipo Operação baixa | I |  |
| `VLRDESC` | Valor do desconto | F |  |
| `VLRINSS` | Valor do INSS | F |  |
| `CARTAODESC` | Valor do desconto da administradora de cartões | F |  |
| `TIPMULTA` | Tipo de multa | S |  |
| `CARTA` | Carta | I |  |
| `VLRIRF` | Valor do IRF | F |  |
| `DTCONTABBAIXA` | Data da Contabilização da Baixa | H |  |
| `PROVISAO` | Provisão | S |  |
| `DTNEG` | Data da negociação | H |  |
| `DTENTSAI` | Data de Entrada e Saída da Nota | H |  |
| `NUBCO` | Número único bancário | I |  |
| `CODCTABCOINT` | Conta Bancária | I |  |
| `SERIENOTA` | Série da nota | S |  |
| `ORIGEM` | Origem | S |  |
| `TIPJURO` | Tipo de juro | S |  |
| `DHBAIXA` | Data e hora da baixa | H |  |
| `DTVENC` | Data do vencimento | H |  |
| `VLRDESDOB` | Valor do desdobramento | F |  |
| `DHTIPOPER` | Data e hora operação | H |  |
| `NUDEV` | Número único devolução | I |  |
| `RATEADO` | Rateado | S |  |
| `HISTORICO` | Histórico | S |  |

## Tabela: TGFFNF
### Descrição: Frete para Nota Financeiro

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUFIN` | Número no Financeiro | I |  |
| `NUNOTA` | Número da Nota | I |  |
| `VLRFRETE` | Valor do frete | F |  |
| `TIPFRETE` | Tipo do frete | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPFRETE (Tabela: TGFFNF)
| Valor | Descrição |
|-------|-----------|
| N | Extra nota |
| S | Incluso |


## Tabela: TGFFOC
### Descrição: Fórmulas de Comissão

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODFORM` | Código | I |  |
| `DESCRFORM` | Descrição | S |  |
| `VENDAREGPROP` | Venda região própria | S |  |
| `HISTREGPROP` | Histórico região própria | I |  |
| `CODEVENTO` | Cód. Evento | I |  |
| `TIPINTEGRA` | Tipo de  Integração | S | Veja opções na seção OPÇÕES |
| `HISTREGTERC` | Histórico região terceiros | I |  |
| `HISTSUPREGPROP` | Hist Sup região própria | I |  |
| `HISTSUPREGTERC` | Hist Sup região terceiros | I |  |
| `HISTSUPTERCREG` | Hist Sup terceiros região | I |  |
| `HISTTERCREG` | Histórico terceiros região | I |  |
| `SUPREGPROP` | Supervisor região própria | S |  |
| `SUPREGTERC` | Supervisor região terceiros | S |  |
| `SUPTERCREG` | Supervisor terceiros região | S |  |
| `VENDAREGTERC` | Venda região terceiros | S |  |
| `VENDATERCREG` | Venda terceiros região | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPINTEGRA (Tabela: TGFFOC)
| Valor | Descrição |
|-------|-----------|
| F | Financeiro |
| N | Nenhuma |
| P | Folha |


## Tabela: TGFFRE
### Descrição: Acerto de Frete

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUACERTO` | Número do acerto | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `NUNOTA` | Número da Nota | F |  |
| `NUFIN` | Número do financeiro | F |  |
| `NUFINORIG` | Número único Financeiro Origem | F |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DHALTER` | Data de Alteração | H |  |
| `TIPACERTO` | Tipo de Acerto | S |  |

## Tabela: TGFFSN
### Descrição: Faixas do Simples Nacional

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUANEXO` | Nro. do Anexo | I |  |
| `NUFAIXA` | Nro. da Faixa | I |  |
| `RECBRUTAINI` | Receita Bruta Inicial | F |  |
| `RECBRUTAFIN` | Receita Bruta Final | F |  |
| `ALIQUOTA` | Alíquota | F |  |
| `PARCDEDUZIR` | Parcela a Deduzir | F |  |
| `IRPJ` | % IRPJ | F |  |
| `CSLL` | % CSLL | F |  |
| `COFINS` | % COFINS | F |  |
| `PISPASEP` | % PIS/PASEP | F |  |
| `CPP` | % CPP | F |  |
| `ICMS` | % ICMS | F |  |
| `IPI` | % IPI | F |  |
| `ISS` | % ISS | F |  |

## Tabela: TGFGRU
### Descrição: Grupos de Produtos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TIPOIMPOSTO` | Tipo de Imposto | S |  |
| `CODGRUPAI` | Grupo pai | I |  |
| `CODGRUPOPROD` | Cód. do Grupo Produto | I |  |
| `DESCRGRUPOPROD` | Descrição | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `ANALITICO` | Analítico | S | Veja opções na seção OPÇÕES |
| `APRPRODVDA` | Apresenta produtos desse grupo na venda consultiva? | S | Veja opções na seção OPÇÕES |
| `VISIVELAPPOS` | Apresentar produtos no aplicativo de Ordem de Serviço | S | Veja opções na seção OPÇÕES |
| `GRUPOICMS` | Grupo de ICMS | I |  |
| `PERCCMTNAC` | % Carga Média Trib. Nacional | F |  |
| `PERCCMTFED` | % Carga Média Trib. Federal | F |  |
| `PERCCMTEST` | % Carga Média Trib. Estadual | F |  |
| `PERCCMTMUN` | % Carga Média Trib. Municipal | F |  |
| `PERCCMTIMP` | % Carga Média Trib. Importação | F |  |
| `VALEST` | Valida estoque | S | Veja opções na seção OPÇÕES |
| `SOLCOMPRA` | Solicita Compra | S | Veja opções na seção OPÇÕES |
| `PEDIRLIB` | Pedir confirmação de liberação | S | Veja opções na seção OPÇÕES |
| `AGRUPALOCVALEST` | Agrupar local na validação de estoque | S | Veja opções na seção OPÇÕES |
| `CODNAT` | Cód. Natureza | I |  |
| `CODPROJ` | Projeto | I |  |
| `CODCENCUS` | Cód.Centro Resultado | I |  |
| `CODRFA` | Regra armazenagem | I |  |
| `PARTICMETA` | Participação na meta | F |  |
| `LIMCURVA_C` | Limite Curva C | F |  |
| `PERCMETA` | Meta percentual | F |  |
| `IMAGEM` | Imagem | B |  |
| `PERCMETACONTRIB` | Meta contribuição | F |  |
| `QTDEXPOSICAO` | Quantidade em exposição | F |  |
| `COMCURVA_B` | Comissão curva B | F |  |
| `AREAOCUPUNID` | Área ocupada por unidade | I |  |
| `METAQTD` | Meta quantitativa | F |  |
| `COMCURVA_A` | Comissão curva A | F |  |
| `LIMCURVA_B` | Limite Curva B | F |  |
| `GRAU` | Grau | I |  |
| `COMCURVA_C` | Comissão curva C | F |  |
| `CODCTACTBEFD` | Conta Contábil para EFD | I |  |
| `AD_TAXCOMMIN` | Taxa Mínima | F |  |
| `AD_TAXCOMMAX` | Taxa Máxima | F |  |
| `CONSGRUPRODCAT42` | Considerar grupo de produto/serviço na geração da Cat 42? | S | Veja opções na seção OPÇÕES |
| `DHALTER` | Dt. Alteração | H |  |
| `AD_DESCONTO` | Porcentagem de desconto | F |  |
| `AD_VENDEDOR` | Vendedor | S |  |
| `CODUSU` | Cód. Usuário Alteração | I |  |
| `CALRUPTURAESTOQUE` | Calcula Ruptura de Estoque? | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANALITICO (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APRPRODVDA (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VISIVELAPPOS (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALEST (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| A | Pela Empresa, mas aceita |
| E | Pela Empresa |
| G | Pela soma de todas as Empresas |
| L | Empresa/Local |
| N | Não valida |
| S | Pelo Grupo de Empresas |

### Opções para campo SOLCOMPRA (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PEDIRLIB (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AGRUPALOCVALEST (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSGRUPRODCAT42 (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALRUPTURAESTOQUE (Tabela: TGFGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFHBC
### Descrição: Históricos Lançamentos Bancários

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODLANC` | Código | I |  |
| `DESCRLANCBCO` | Descrição | S |  |
| `TIPLANC` | Tipo do Lançamento | I | Veja opções na seção OPÇÕES |
| `ACEITADEV` | Aceita Devolução Individual? | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPLANC (Tabela: TGFHBC)
| Valor | Descrição |
|-------|-----------|
| -1 | Débito |
| 1 | Crédito |

### Opções para campo ACEITADEV (Tabela: TGFHBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFHGR
### Descrição: Histórico de Geração de Remessa Bancária

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUTGFHGR` | Número único | I |  |
| `NUREMESSA` | Número remessa | I |  |
| `VLRTOTALREM` | Valor Total da Remessa | F |  |
| `NOMEARQ` | Nome arquivo | S |  |
| `QTDTITPROC` | Qtd. títulos processados | I |  |
| `DHGERACAO` | Data e hora remessa | H |  |
| `CODIGOLAYOUT` | Layout | I |  |
| `CODCTABCOINT` | Conta Bancária | I |  |
| `ARQUIVO` | Arquivo | C |  |

## Tabela: TGFHICM
### Descrição: Histórico de Alíquota ICMS

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `UFORIG` | UF origem | I |  |
| `UFDEST` | UF destino | I |  |
| `TIPRESTRICAO` | Tipo de Restrição | S | Veja opções na seção OPÇÕES |
| `CODRESTRICAO` | Cód. restrição | I |  |
| `DESCRRESTRICAO` | Descrição Restrição | S |  |
| `TIPRESTRICAO2` | Tipo de Restrição 2 | S | Veja opções na seção OPÇÕES |
| `CODRESTRICAO2` | Cód. restrição 2 | I |  |
| `DESCRRESTRICAO2` | Descrição Restrição 2 | S |  |
| `ALIQUOTA` | Alíquota | F |  |
| `REDBASE` | Redução da Base | F |  |
| `PERCMINSUBTRIB` | Percentual Mínimo ST (RIOLOG) | F |  |
| `ALIQFRETE` | Alíquota do Frete | F |  |
| `REDBASEFRETE` | Redução da Base do Frete | F |  |
| `MARGLUCRO` | Margem de Lucro | F |  |
| `CODTRIB` | Tributação | I | Veja opções na seção OPÇÕES |
| `CODOBSPADRAO` | Observação Padrão | I |  |
| `ALIQSUBTRIB` | Aliquota Débito de ST | F |  |
| `REPREDBASE` | Repassar Redução do Imposto para o cliente? | S | Veja opções na seção OPÇÕES |
| `ALIQICMSLIMITECALCST` | Alíq. Limite créd. ICMS p/ dedução no Valor ST | F |  |
| `REDBASEST` | Redução de Base ST | F |  |
| `CODTAB` | Tabela | I |  |
| `DHALTER` | Data Alteração | D |  |
| `USUARIO` | Usuário | S |  |
| `MAIORBASEST` | Maior Base ST | S | Veja opções na seção OPÇÕES |
| `REPICMS` | Repassar ICMS | S | Veja opções na seção OPÇÕES |
| `CONSIDIPIVLROPPROP` | Considerar IPI na comparação conforme portaria Sutri860 | S | Veja opções na seção OPÇÕES |
| `REDICMS` | Redução ICMS | S | Veja opções na seção OPÇÕES |
| `CALCSTCONSUTRI` | Calcular ST Conforme Portaria Sutri860 | S | Veja opções na seção OPÇÕES |
| `BASESTRED` | Base ST Redução | S | Veja opções na seção OPÇÕES |
| `NAOCONSIDMVA` | Considera Pauta para a base de cálculo do ICMS ST | S | Veja opções na seção OPÇÕES |
| `MAIORBASEICMS` | Usar a maior base para ICMS | S | Veja opções na seção OPÇÕES |
| `STSUTRI4302014MG` | Calcular ST conforme portaria Sutri 430/2014 - MG | S | Veja opções na seção OPÇÕES |
| `OUTORGA` | Outorga | F |  |
| `CONVPRODUZ` | Convênio Produzir | S | Veja opções na seção OPÇÕES |
| `PAUTAVLRSTFIXO` | Pauta de Valor Fixo do Item - CE | S | Veja opções na seção OPÇÕES |
| `CODTABICMS` | Tabela c/base p/ICMS | I |  |
| `BASICMMOD` | Modalidade BC ICMS | I | Veja opções na seção OPÇÕES |
| `REPREDBASE2` | Redução da BASE | S | Veja opções na seção OPÇÕES |
| `BASICMSTMOD` | Modalidade BC ICMS ST | I | Veja opções na seção OPÇÕES |
| `CODTABSTANT` | Tabela c/Base ST Operação Anterior: | I |  |
| `CODTABSTUFDEST` | Tabela c/Base ST em Favor da UF de Destino | I |  |
| `ALIQUFDEST` | Alíquota Estado Destino | F |  |
| `MVASTUFDEST` | Margem Lucro (MVA) UF Destino | F |  |
| `BASESTUFDEST` | Base ST UF Destino por | S | Veja opções na seção OPÇÕES |
| `CODANTECIPST` | Cód.Antecipação ST | S | Veja opções na seção OPÇÕES |
| `CSOSN` | Cód. situação op. Simples nacional (CSON) | I | Veja opções na seção OPÇÕES |
| `ZERAR` | Usar Vlr.ICMS na ST, anotar Base/Vlr na Obs.item e zerar Base/Vlr do ICMS? | S | Veja opções na seção OPÇÕES |
| `STCAT137SP` | Calcular ST p/ Medicamentos - CAT-SP | S | Veja opções na seção OPÇÕES |
| `PROEMPREGO` | Optante pelo Regime Especial do Pró-Emprego (Resolução n° 257/2008 - SEF) | S | Veja opções na seção OPÇÕES |
| `CODMOTDESONERAICMS` | Cód.Mot.Desoneração ICMS | I | Veja opções na seção OPÇÕES |
| `REPPERCBASEICMS` | % da Base ICMS | F |  |
| `ZERARSTNEG` | Zerar valor da substituição tributária quando negativo | S | Veja opções na seção OPÇÕES |
| `CUSCOMICMSBASEST` | Usar último custo de entrada com ICMS como base p/ST | S | Veja opções na seção OPÇÕES |
| `CALCSTEXTRANOTA` | Calcula ST extra nota com base em MVA na VENDA (Não utilizar em compras) | S | Veja opções na seção OPÇÕES |
| `TABCFOP` | Tabela de CFOPs | S |  |
| `IDALIQ` | Cód. Alíq. ICMS | I |  |
| `CALCMVAAJUSTADO` | Calcular MVA Ajustado | S | Veja opções na seção OPÇÕES |
| `ALIQINTDEST` | Alíq. Interna Destino | F |  |
| `PERCICMSFCP` | % ICMS FCP | F |  |
| `PERCREDBASEDEST` | % Redução Base Destino | F |  |
| `TIPCALCDIFAL` | Tipo de Cálculo do DIFAL | I | Veja opções na seção OPÇÕES |
| `ALIQESTRANGEIRA` | Alíquota de Origem Estrangeira | F |  |
| `ICMSUFORIGDIFEMIT` | ICMS devido à UF de origem da prestação, quando diferente da UF do emitente | S | Veja opções na seção OPÇÕES |
| `DESCONSIDERAREDBASE` | Para redução da base de cálculo p/ produtos de origem estrangeira | S | Veja opções na seção OPÇÕES |
| `SEQUENCIA` | Sequência | I |  |
| `CODTABSTPMPF` | Tabela p/ Base ST - PMPF | I |  |
| `CODTABSTFARPOP` | Tabela p/ Base ST - Farmácia Popular | I |  |
| `TIPCALCFCPSTESPEC` | Tipo de Cálculo de FCP Específico | I | Veja opções na seção OPÇÕES |
| `TIPCALCSTESPEC` | Tipo de Cálculo de ST Específico | I | Veja opções na seção OPÇÕES |
| `MVASIMPLIFICADO` | MVA Simplificado | S | Veja opções na seção OPÇÕES |
| `PERCCARGATRIBMEDIA` | Percentual Carga Trib. Média | F |  |
| `ALIQICMSESPST` | Alíquota de ICMS Específico para o cálculo de ST | F |  |
| `CALCREPREDST` | Cálculo de Desoneração ICMS/ST por Dentro, conforme Resolução SEFAZ nº 13/2019 | S | Veja opções na seção OPÇÕES |
| `CODMOTDESONERAST` | Cód. Mot. Desoneração do ICMS ST | I | Veja opções na seção OPÇÕES |
| `PERCICMSFCPINT` | % ICMS FCP Interno | F |  |
| `ZERARDIFALREM` | Zerar Valor do ICMS DIFAL do Remetente | S | Veja opções na seção OPÇÕES |
| `BASEFCPINT` | Base para cálculo do FCP Interno | S | Veja opções na seção OPÇÕES |
| `PERCSTFCPINT` | % ST FCP Interno | F |  |
| `ALIQADREMICMS` | Alíquota ad rem ICMS | F |  |
| `MVAORIGINAL` | Usar MVA original quando carga trib. inferior à alíq. interestadual? | S | Veja opções na seção OPÇÕES |
| `CODFORMBASDIFAL` | Fórmula para Cálculo da Base do DIFAL e do FCP | I |  |
| `PERCICMSMONORET` | % Destino ICMS Monofásico Retido | F |  |
| `CODFORMCALCDIFAL` | Fórmula para Cálculo do DIFAL | I |  |
| `PERCALIQADREMICMS` | % Redução Alíquota ad rem ICMS | F |  |
| `REPDIFALFCP` | ICMS DIFAL (Não Contribuinte) | S | Veja opções na seção OPÇÕES |
| `MOTREDADREM` | Motivo Redução do ad rem | I | Veja opções na seção OPÇÕES |
| `PERCTRAVAMED` | Porcentagem de trava para medicamentos | F |  |
| `CODBEN` | Código do Benefício | S |  |
| `CODFORMBASICM` | Fórmula para cálculo da base de ICMS | I |  |
| `PERCREDPR` | Percentual do Crédito Presumido | F |  |
| `PERCPMPF` | Percentual PMPF | F |  |
| `REDBASEESTRANGEIRA` | Redução da Base para Origem Estrangeira | F |  |
| `CARACTRIB` | Característica tributável | S | Veja opções na seção OPÇÕES |
| `ALIQICMSEFET` | Alíquota Interna (CST 60) | F |  |
| `FINALIDADE` | Destinação da mercadoria adquirida | S | Veja opções na seção OPÇÕES |
| `PERCMULTCALCDP` | % Diferença Positiva | F |  |
| `ICMSDIFPOSITIVA` | Utilizar diferença positiva | S | Veja opções na seção OPÇÕES |
| `MARGLUCROEST` | Margem Lucro (MVA) para origem estrangeira | F |  |
| `PERCREDBASEICMSEFET` | Perc. Red. Base | F |  |
| `CALCSTLIVRECOM` | Calcular ICMS ST Zona Franca/Ýrea de livre comércio | S | Veja opções na seção OPÇÕES |
| `CALCREPREDDENTRO` | Calculo Desoneração ICMS por dentro | S | Veja opções na seção OPÇÕES |
| `DESICMSSN` | Desonera ICMS do Simples Nacional | S | Veja opções na seção OPÇÕES |
| `FORMAREPICMS` | FORMAREPICMS | S | Veja opções na seção OPÇÕES |
| `CALCDIFICMSDENTRO` | Cálculo Diferimento Por Dentro | S | Veja opções na seção OPÇÕES |
| `REGRACALCBCICMSAT` | Regra p/ cálculo da base ICMS AT | S | Veja opções na seção OPÇÕES |
| `CODFORMBCICMSAT` | Fórmula para Cálculo da Base do ICMS AT | I |  |
| `ALIQICMSAT` | Alíquota ICMS AT (%) | F |  |
| `ALIQICMSATIMP` | Alíquota ICMS AT produto importado (%) | F |  |
| `ALIQICMSATINT` | Alíquota de ICMS Interna (%) | F |  |
| `REGRADEDICMSAT` | Deduzir do ICMS AT | S | Veja opções na seção OPÇÕES |
| `PERCUSAQUDECPE` | Percentual/Coeficiente sobre Custo Aquisição - PE | F |  |
| `PERCUSAQUDECPEEST` | Percentual/Coeficiente sobre Custo Aquisição - PE - Origem Estrangeira | F |  |
| `TIPCUSAQUDECPE` | Tipo de custo Custo Decreto 38.296/PE | S | Veja opções na seção OPÇÕES |
| `ALIQICMSCARGTRIBRED` | Alíquota da Carga Tributária Reduzida (ICMS) (%) | F |  |
| `ALIQSTCARGTRIBRED` | Alíquota da Carga Tributária Reduzida (ST) (%) | F |  |
| `CALPERREDBASEICMS` | Calcular % de Redução BC ICMS Lei 9.025/2020 | S | Veja opções na seção OPÇÕES |
| `CALPERREDBASEST` | Calcular % de Redução BC ICMS ST Lei 9.025/2020 | S | Veja opções na seção OPÇÕES |
| `CALCSTDECPR` | Calcular ST conforme Decreto 4.520/2020 - PR | S | Veja opções na seção OPÇÕES |
| `CONSPMVABCICM` | Considera Pauta + MVA para a base de cálculo do ICMS ST | S | Veja opções na seção OPÇÕES |
| `CREDPRESDECPR` | % Crédito Presumido Decreto 4.520/2020 - PR | F |  |
| `CALCREDPREICMCON` | Calcular % de Crédito Presumido de ICMS ST Convênio ICMS 106/1996 | S | Veja opções na seção OPÇÕES |
| `FORMCALFCPDIFAL` | Fórmula para o Cálculo do FCP do DIFAL | I |  |
| `PERCREDPREICMCON` | Percentual de Crédito Presumido de ICMS ST Convênio ICMS 106/1996 | F |  |
| `CODFORMVA` | Fórmula para calcular MVA Ajustada | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPRESTRICAO (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| A | por tipo de transporte de importação |
| B | por capítulo do NCM |
| C | por cidade origem |
| D | por cidade destino |
| E | por grupo de ICMS do parceiro |
| F | por posição do NCM |
| G | por grupo de produtos |
| H | por NCM |
| I | por grupo de ICMS do produto |
| J | por grupo. ICMS do grupo de produto |
| K | Grupo de ICMS 2 |
| L | Produtor Rural |
| M | Código da Empresa |
| N | consumidor |
| O | por TOP |
| P | por produto |
| Q | por Finalidade da Operação |
| R | por TARE |
| S | sem exceção |
| T | por perfil principal |
| U | por CFOP |
| X | consumidor contribuinte |

### Opções para campo TIPRESTRICAO2 (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| A | por tipo de transporte de importação |
| B | por capítulo do NCM |
| C | por cidade origem |
| D | por cidade destino |
| E | por grupo de ICMS do parceiro |
| F | por posição do NCM |
| G | por grupo de produtos |
| H | por NCM |
| I | por grupo de ICMS do produto |
| J | por grupo. ICMS do grupo de produto |
| K | Grupo de ICMS 2 |
| M | Código da Empresa |
| O | por TOP |
| P | por produto |
| Q | por Finalidade da Operação |
| R | por TARE |
| S | sem exceção |
| T | por perfil principal |
| U | por CFOP |

### Opções para campo CODTRIB (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Tributada integralmente |
| 02 | 02-Tributação monofásica própria sobre combustíveis |
| 10 | 10-Tributada e c/cobrança por substituição |
| 15 | 15-Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis |
| 20 | 20-Com redução de base de cálculo |
| 30 | 30-Isenta e não tribut.e c/cobrança por subst. |
| 40 | 40-Isenta |
| 41 | 41-Não tributada |
| 50 | 50-Suspensão |
| 51 | 51-Diferimento |
| 53 | 53-Tributação monofásica sobre combustíveis com recolhimento diferido |
| 60 | 60-ICMS cobrado anteriormente por substituição |
| 61 | 61-Tributação monofásica sobre combustíveis cobrada anteriormente |
| 70 | 70-Com redução de base e c/cobrança por subst. |
| 90 | 90-Outras |

### Opções para campo REPREDBASE (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MAIORBASEST (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REPICMS (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSIDIPIVLROPPROP (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REDICMS (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCSTCONSUTRI (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASESTRED (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| D | Desconsiderar IPI p/ Redução |
| N | Desconsidera |
| S | Considerar IPI p/ Redução |

### Opções para campo NAOCONSIDMVA (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MAIORBASEICMS (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STSUTRI4302014MG (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONVPRODUZ (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PAUTAVLRSTFIXO (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASICMMOD (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 1 | Pauta (Valor) |
| 2 | Preço Tabelado Máx. (Valor) |
| 3 | Valor da Operação |

### Opções para campo REPREDBASE2 (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASICMSTMOD (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 0 | Preço tabelado ou Máximo Sugerido |
| 1 | Lista Negativa (Valor) |
| 2 | Lista Positiva (Valor) |
| 3 | Lista Neutra (Valor) |
| 4 | Margem Valor Agregado (%) |
| 5 | Pauta (Valor) |
| 6 | Valor da Operação |

### Opções para campo BASESTUFDEST (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| P | Pauta |
| V | Valor do Produto |

### Opções para campo CODANTECIPST (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| A | A-ST informada pelo substituto/substituído que não incorra em nenhuma das situações anteriores |
| N | N-(Não Usa) Operação não envolve ST |
| 1 | 1-Pgto de ST efetuado pelo destinatário quando não efetuado ou efetuado a menor pelo substituto |
| 2 | 2-Antecip. tribut. efetuada pelo destinatário apenas como complemento do diferencial de alíquota |
| 3 | 3-Antecip. tribut. com MVA efetuada pelo destinatário sem encerrar a fase de tributação |
| 4 | 4-Antecip. tribut. com MVA efetuada pelo destinatário encerrando a fase de tributação |
| 5 | 5-Substituição tributária interna motivada por regime especial de tributação |
| 6 | 6-ICMS pago na importação |

### Opções para campo CSOSN (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 101 | 101-Tributada pelo Simples Nacional com permissão de crédito |
| 102 | 102-Tributada pelo Simples Nacional sem permissão de crédito |
| 103 | 103-Isenção do ICMS no Simples Nacional para faixa de receita bruta |
| 201 | 201-Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por ST |
| 202 | 202-Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por ST |
| 203 | 203-Isenção do ICMS no Simples Nacional para faixa de receita bruta e com cobrança do ICMS por ST |
| 300 | 300-Imune |
| 400 | 400-Não tributada pelo Simples Nacional |
| 500 | 500-ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação |
| 900 | 900-Outros |

### Opções para campo ZERAR (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STCAT137SP (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROEMPREGO (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODMOTDESONERAICMS (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 1 | 1-Táxi |
| 10 | 10-Deficiente Condutor (Convênio ICMS 38/12) |
| 11 | 11-Deficiente Não Condutor (Convênio ICMS 38/12) |
| 12 | 12-Órgão de Fomento e Desenv. Agropecuário |
| 16 | 16-Olimpíadas Rio 2016 |
| 2 | 2-Deficiente Físico (Desativado) |
| 3 | 3-Produtor Agropecuário |
| 4 | 4-Frotista/Locadora |
| 5 | 5-Diplomático/Consular |
| 6 | 6-Utilitários e Motocicletas da Amazônia Ocidental e Ýreas de Livre Comércio |
| 7 | 7-SUFRAMA |
| 8 | 8-Venda a Órgãos Públicos |
| 9 | 9-Outros |
| 90 | 90-Solicitado pelo Fisco |

### Opções para campo ZERARSTNEG (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CUSCOMICMSBASEST (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCSTEXTRANOTA (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCMVAAJUSTADO (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| A | Pelo MVA da Alíquota |
| F | Pelo MVA da Alíquota considerando % ST FCP Interno |
| N | Não Calcular |
| P | Pela Fórmula |
| S | Pelo MVA Padrão do Produto/Empresa |

### Opções para campo TIPCALCDIFAL (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Sem considerar redução da Base |
| 1 | 1 - Com redução da base aplicada na base |
| 10 | 10 - Cálculo da base, valor do DIFAL e do FCP por fórmula |
| 2 | 2 - Com redução da base aplicada na alíquota |
| 3 | 3 - ICMS Interestadual calculado sob a BC do DIFAL |
| 4 | 4 - Cálculo do DIFAL com ICMS Destino por dentro |
| 5 | 5 - Cálculo do DIFAL Convênio 142/2018 |
| 6 | 6 - Cálculo do DIFAL com a redução do ICMS Próprio |
| 7 | 7 - ICMS Difal base dupla UF Sergipe |
| 8 | 8 - Base de cálculo do DIFAL e do FCP por fórmula |
| 9 | 9 - Cálculo do DIFAL com ICMS Destino por dentro - Base Dupla |

### Opções para campo ICMSUFORIGDIFEMIT (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCONSIDERAREDBASE (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Redução de Base |
| S | Desconsiderar redução |
| Z | Redução de Base Estrangeira |

### Opções para campo TIPCALCFCPSTESPEC (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| null | 0 - Não específico (Regra Geral) |
| 1 | 1 - FECOP ST Majorado (CE) |

### Opções para campo TIPCALCSTESPEC (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Não específico (Regra Geral) |
| 1 | 1 - Calcular ST p/ Medicamentos - CAT-SP |
| 10 | 10 - Calcular ST Via Pauta sem dedução do ICMS próprio |
| 11 | 11 - Calcular ST (Alíq. Limite créd. ICMS p/ dedução no Valor ST) |
| 12 | 12 - Calcular ST (Dif.Alíq. por dentro), BC ST COM Red.ICMS COM FCP |
| 13 | 13 - Realizar cálc de ICMS para reduc no ST com alíq espec e utilizando o mesmo % de redução do ST |
| 14 | 14 - Cálculo ICMS e ICMS/ST - Decreto 38.296/PE |
| 15 | 15 - Calcular ST P/ Medicamentos - CAT-40/SP |
| 16 | 16 - Cálculo ICMS/ST - DIFAL - Decreto 40.230/2020 - PB |
| 17 | 17 - Calcular ST - Lei nº 15730/PE |
| 18 | 18 - Cálculo ICMS ST e FCP (ICMS de Destino por Dentro) - Protocolo ICMS 104/2008 - AL |
| 19 | 19 - Cálculo ST SUFRAMA com Desoneração Simples Nacional |
| 2 | 2 - Calcular ST (Dif.Alíq. por dentro), BC ST SEM Red.ICMS |
| 20 | 20 - Calcular ICMS-ST com BC Reduzida por PIS/COFINS Desonerados e ICMS Operação |
| 3 | 3 - Calcular ST com Incentivos SUFRAMA e Redução da BC |
| 4 | 4 - Calcular ST (Dif.Alíq. por dentro), BC ST COM Red.ICMS |
| 5 | 5 - Calcular ST Simplificado (Carga Média) |
| 6 | 6 - Calcular ST sem dedução do ICMS Próprio |
| 7 | 7 - Calcular ST (Dif.Alíq. Convênio 142/2018 - CFC) |
| 8 | 8 - Calcular ST (Dif. Aliq. Considerando FCP e Redução de Base de ST) |
| 9 | 9 - Implementação Futura |

### Opções para campo MVASIMPLIFICADO (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCREPREDST (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODMOTDESONERAST (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 12 | Órgão de fomento e desenvolvimento agropecuário |
| 3 | Uso na agropecuária |
| 9 | Outros |

### Opções para campo ZERARDIFALREM (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASEFCPINT (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| B | Base do ICMS |
| null | Valor da Operação |

### Opções para campo MVAORIGINAL (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REPDIFALFCP (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MOTREDADREM (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Transporte coletivo de passageiros |
| 9 | 9 - Outros |

### Opções para campo CARACTRIB (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 0 | Industrial |
| 1 | Distribuidor |
| 2 | Atacadista |
| 3 | Varejista |
| 4 | Pessoa Jurídica não Contribuinte do ICMS |
| 6 | Produtor Rural Pessoa Física |
| 7 | Pessoa Jurídica não Contribuinte do ICMS |
| 8 | Pessoa Física não Contribuinte do ICMS |

### Opções para campo FINALIDADE (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 0 | Revenda |
| 1 | Insumo |
| 2 | Uso e Consumo Ou Ativo Imobilizado |

### Opções para campo ICMSDIFPOSITIVA (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo CALCSTLIVRECOM (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCREPREDDENTRO (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESICMSSN (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FORMAREPICMS (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| null | Destacar valores e deduzir do total da nota |
| 1 | Destacar valores e não deduzir do total da nota |

### Opções para campo CALCDIFICMSDENTRO (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGRACALCBCICMSAT (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| 0 | Cálculo por dentro |
| 1 | Cálculo (Valor líquido do produto + IPI) |
| 2 | Fórmula personalizada |

### Opções para campo REGRADEDICMSAT (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| null | Sem dedução |
| 1 | Deduzir ICMS normal |
| 2 | Deduzir ICMS-ST |
| 3 | Deduzir ICMS normal e ICMS-ST |

### Opções para campo TIPCUSAQUDECPE (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| E | Último Custo de Entrada Com ICMS |
| G | Último Custo Médio Gerencial |
| L | Último Custo Gerencial |
| M | Último Custo Médio Com ICMS |
| null | Não se Aplica |
| R | Último Custo de Reposição |
| S | Último Custo de Entrada Sem ICMS |
| V | Último Custo Variável |
| Z | Último Custo Médio Sem ICMS |

### Opções para campo CALPERREDBASEICMS (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALPERREDBASEST (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCSTDECPR (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSPMVABCICM (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCREDPREICMCON (Tabela: TGFHICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFHIFE
### Descrição: Histórico de Alíquotas Pis Cofins Cssl

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NOMEIMP` | Nome do imposto | S |  |
| `GRUPOIMP` | Grupo | S |  |
| `CODEMP` | Empresa | I |  |
| `CODPARC` | Parceiro | I |  |
| `CODTIPOPER` | Tipo Operação | I |  |
| `ENTSAI` | Tipo | S | Veja opções na seção OPÇÕES |
| `PERCVLR` | Tipo alíquota | S | Veja opções na seção OPÇÕES |
| `ALIQ` | Alíquota | F |  |
| `ID` | ID | I |  |
| `REDBASE` | % Red. base | F |  |
| `IVA` | IVA | F |  |
| `ALIQCRED` | Alíq. p/ crédito | F |  |
| `RETEMFIN` | Retém no financeiro | S | Veja opções na seção OPÇÕES |
| `CODTAB` | Tabela c/base p/ ST | I |  |
| `CST` | Cód. sit. tributária | I | Veja opções na seção OPÇÕES |
| `VLRPAUTA` | Valor pauta | F |  |
| `VLRPAUTACRED` | Valor pauta cred. | F |  |
| `IPIINCBASE` | IPI incide na base de cálculo | S | Veja opções na seção OPÇÕES |
| `PRODSEMTRIB` | Produto sem tributação | S | Veja opções na seção OPÇÕES |
| `ALIQSUFRAMA` | Alíquota Suframa | F |  |
| `USUARIO` | Usuário | S |  |
| `DHALTER` | Data Alteração | D |  |

## OPÇÕES DE CAMPOS

### Opções para campo ENTSAI (Tabela: TGFHIFE)
| Valor | Descrição |
|-------|-----------|
| A | Ambas |
| E | Entrada |
| S | Saída |

### Opções para campo PERCVLR (Tabela: TGFHIFE)
| Valor | Descrição |
|-------|-----------|
| P | Percentual |
| V | Valor |

### Opções para campo RETEMFIN (Tabela: TGFHIFE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CST (Tabela: TGFHIFE)
| Valor | Descrição |
|-------|-----------|
| 1 | 01 - Alíquota Normal (Cumulativo/Não Cumulativo) |
| 2 | 02 - Alíquota Diferenciada |
| 3 | 03 - Alíquota por Unidade de produto |
| 4 | 04 - Monofásica (Alíquota Zero) |
| 49 | 49 - Outras Operações de Saída |
| 5 | 05 - Operação Tributável por Substituição Tributária |
| 50 | 50 - Direito a Créd.- Vinc.Exclusiv.a Receita Tribut.no Merc.Interno |
| 51 | 51 - Direito a Créd.- Vinc.Exclusiv.a Receita Não Tribut.no Merc.Interno |
| 52 | 52 - Direito a Créd.- Vinc.Exclusiv.a Receita de Export. |
| 53 | 53 - Direito a Créd.- Vinc.a Receitas Tribut.e Não-Tribut.no Merc.Interno |
| 54 | 54 - Direito a Créd.- Vinc.a Receitas Tribut.no Merc.Interno e de Export |
| 55 | 55 - Direito a Créd.- Vinc.a Receitas Não-Tribut.no Merc.Interno e de Export. |
| 56 | 56 - Direito a Créd.- Vinc.a Receitas Tribut.e Não-Tribut.no Merc.Interno, e de Export. |
| 6 | 06 - Alíquota Zero |
| 60 | 60 - Créd.Presumido - Aquisição Vinc.Exclusiv.a Receita Tribut.no Merc.Interno |
| 61 | 61 - Créd.Presumido - Aquisição Vinc.Exclusiv.a Receita Não-Tribut.no Merc.Interno |
| 62 | 62 - Créd.Presumido - Aquisição Vinc.Exclusiv.a Receita de Export. |
| 63 | 63 - Créd.Presumido - Aquisição Vinc.a Receitas Tribut.e Não-Tribut.no Merc.Interno |
| 64 | 64 - Créd.Presumido - Aquisição Vinc.a Receitas Tribut.no Merc.Interno e de Export. |
| 65 | 65 - Créd.Presumido - Aquisição Vinc.a Receitas Não-Tribut.no Merc.Interno e de Export. |
| 66 | 66 - Créd.Presumido - Aquisição Vinc.a Receitas Tribut.e Não-Tribut.no Merc.Interno, e de Export. |
| 67 | 67 - Créd.Presumido - Outras Operações |
| 7 | 07 - Isenta |
| 70 | 70 - Aquisição sem Direito a Créd. |
| 71 | 71 - Aquisição com Isenção |
| 72 | 72 - Aquisição com Suspensão |
| 73 | 73 - Aquisição a Alíquota Zero |
| 74 | 74 - Aquisição sem Incidência da Contribuição |
| 75 | 75 - Aquisição por Substituição Tributária |
| 8 | 08 - Sem Incidência |
| 9 | 09 - Com Suspensão |
| 98 | 98 - Outras Entradas |
| 99 | 99 - Outras |

### Opções para campo IPIINCBASE (Tabela: TGFHIFE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODSEMTRIB (Tabela: TGFHIFE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFHISS
### Descrição: Tabela de ISS

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDALIQ` | Código Alíquota | I |  |
| `CODCID` | Cidade | I |  |
| `ID` | ID | I |  |
| `CODPROD` | Serviço | I |  |
| `CODEMP` | Empresa | I |  |
| `PERCINSS` | Percentual de ISS | F |  |
| `CODTRIBISS` | Cód. Tributação ISS | I | Veja opções na seção OPÇÕES |
| `PERCDEDUCAO` | Perc. de dedução na base do ISS | F |  |
| `TIPODEDUCAO` | Tipo de dedução de base do ISS | S | Veja opções na seção OPÇÕES |
| `CODTRIBMUNISS` | Cod. Trib. Município | S |  |
| `CODLST` | Tipo de Serviço | I |  |
| `DHALTER` | Data Alteração | D |  |
| `USUARIO` | Usuário | S |  |
| `NAOCALCULA` | Não Calcula | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo CODTRIBISS (Tabela: TGFHISS)
| Valor | Descrição |
|-------|-----------|
| 0 | 00 - Tributado |
| 1 | 01 - Tributado com ISS Retido |
| 6 | 06 - Isento |
| 7 | 07 - Não Tributado |

### Opções para campo TIPODEDUCAO (Tabela: TGFHISS)
| Valor | Descrição |
|-------|-----------|
| M | Materiais |
| P | Por percentual |
| S | Sub-Empreito |

### Opções para campo NAOCALCULA (Tabela: TGFHISS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFICM
### Descrição: Alíquotas de ICMS

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `UFORIG` | UF origem | I |  |
| `UFDEST` | UF destino | I |  |
| `TIPRESTRICAO` | Tipo de Restrição | S | Veja opções na seção OPÇÕES |
| `CODRESTRICAO` | Cód. restrição | I |  |
| `DESCRRESTRICAO` | Descrição Restrição | S |  |
| `TIPRESTRICAO2` | Tipo de Restrição 2 | S | Veja opções na seção OPÇÕES |
| `CODRESTRICAO2` | Cód. restrição 2 | I |  |
| `DESCRRESTRICAO2` | Descrição Restrição 2 | S |  |
| `ALIQUOTA` | Alíquota | F |  |
| `REDBASE` | Redução da Base | F |  |
| `PERCMINSUBTRIB` | Percentual Mínimo ST (RIOLOG) | F |  |
| `ALIQFRETE` | Alíquota do Frete | F |  |
| `REDBASEFRETE` | Redução da Base do Frete | F |  |
| `ALIQCONSFIN` | Alíquota suportada pelo Consumidor Final | F |  |
| `MARGLUCRO` | Margem de Lucro | F |  |
| `CODTRIB` | Tributação | I | Veja opções na seção OPÇÕES |
| `CODOBSPADRAO` | Observação Padrão | I |  |
| `ALIQSUBTRIB` | Aliquota Débito de ST | F |  |
| `ALIQICMSLIMITECALCST` | Alíq. Limite créd. ICMS p/ dedução no Valor ST | F |  |
| `REPREDBASE` | Repassar Redução do Imposto para o cliente? | S | Veja opções na seção OPÇÕES |
| `REDBASEST` | Redução de Base ST | F |  |
| `CODTAB` | Tabela | I |  |
| `MAIORBASEST` | Maior Base ST | S | Veja opções na seção OPÇÕES |
| `REPICMS` | Repassar ICMS | S | Veja opções na seção OPÇÕES |
| `REDICMS` | Redução ICMS | S | Veja opções na seção OPÇÕES |
| `CONSIDIPIVLROPPROP` | Considerar IPI na comparação conforme portaria Sutri860 | S | Veja opções na seção OPÇÕES |
| `CALCSTCONSUTRI` | Calcular ST Conforme Portaria Sutri860 | S | Veja opções na seção OPÇÕES |
| `BASESTRED` | Base ST Redução | S | Veja opções na seção OPÇÕES |
| `NAOCONSIDMVA` | Considera Pauta para a base de cálculo do ICMS ST | S | Veja opções na seção OPÇÕES |
| `MAIORBASEICMS` | Usar a maior base para ICMS | S | Veja opções na seção OPÇÕES |
| `OUTORGA` | Outorga | F |  |
| `STSUTRI4302014MG` | Calcular ST conforme portaria Sutri 430/2014 - MG | S | Veja opções na seção OPÇÕES |
| `PAUTAVLRSTFIXO` | Pauta de Valor Fixo do Item - CE | S | Veja opções na seção OPÇÕES |
| `CONVPRODUZ` | Convênio Produzir | S | Veja opções na seção OPÇÕES |
| `CODTABICMS` | Tabela c/base p/ICMS | I |  |
| `BASICMMOD` | Modalidade BC ICMS | I | Veja opções na seção OPÇÕES |
| `REPREDBASE2` | Redução da BASE | S | Veja opções na seção OPÇÕES |
| `BASICMSTMOD` | Modalidade BC ICMS ST | I | Veja opções na seção OPÇÕES |
| `CODTABSTANT` | Tabela c/Base ST Operação Anterior: | I |  |
| `CODTABSTUFDEST` | Tabela c/Base ST em Favor da UF de Destino | I |  |
| `ALIQUFDEST` | Alíquota Estado Destino | F |  |
| `MVASTUFDEST` | Margem Lucro (MVA) UF Destino | F |  |
| `BASESTUFDEST` | Base ST UF Destino por | S | Veja opções na seção OPÇÕES |
| `CODANTECIPST` | Cód.Antecipação ST | S | Veja opções na seção OPÇÕES |
| `CSOSN` | Cód. situação op. Simples nacional (CSON) | I | Veja opções na seção OPÇÕES |
| `ZERAR` | Usar Vlr.ICMS na ST, anotar Base/Vlr na Obs.item e zerar Base/Vlr do ICMS? | S | Veja opções na seção OPÇÕES |
| `STCAT137SP` | Calcular ST p/ Medicamentos - CAT-SP | S | Veja opções na seção OPÇÕES |
| `PROEMPREGO` | Optante pelo Regime Especial do Pró-Emprego (Resolução n° 257/2008 - SEF) | S | Veja opções na seção OPÇÕES |
| `CODMOTDESONERAICMS` | Cód.Mot.Desoneração ICMS | I | Veja opções na seção OPÇÕES |
| `REPPERCBASEICMS` | % da Base ICMS | F |  |
| `ZERARSTNEG` | Zerar valor da substituição tributária quando negativo | S | Veja opções na seção OPÇÕES |
| `CUSCOMICMSBASEST` | Usar último custo de entrada com ICMS como base p/ST | S | Veja opções na seção OPÇÕES |
| `CALCSTEXTRANOTA` | Calcula ST extra nota com base em MVA na VENDA (Não utilizar em compras) | S | Veja opções na seção OPÇÕES |
| `TABCFOP` | Tabela de CFOPs | S |  |
| `IDALIQ` | Cód. Alíq. ICMS | I |  |
| `CALCMVAAJUSTADO` | Calcular MVA Ajustado | S | Veja opções na seção OPÇÕES |
| `ALIQINTDEST` | Alíq. Interna Destino | F |  |
| `PERCICMSFCP` | % ICMS FCP | F |  |
| `PERCREDBASEDEST` | % Redução Base Destino | F |  |
| `TIPCALCDIFAL` | Tipo de Cálculo do DIFAL | I | Veja opções na seção OPÇÕES |
| `ALIQESTRANGEIRA` | Alíquota de Origem Estrangeira | F |  |
| `ICMSUFORIGDIFEMIT` | ICMS devido à UF de origem da prestação, quando diferente da UF do emitente | S | Veja opções na seção OPÇÕES |
| `DESCONSIDERAREDBASE` | Para redução da base de cálculo p/ produtos de origem estrangeira | S | Veja opções na seção OPÇÕES |
| `SEQUENCIA` | Sequência | I |  |
| `CODTABSTPMPF` | Tabela p/ Base ST - PMPF | I |  |
| `TIPCALCFCPSTESPEC` | Tipo de Cálculo de FCP Específico | I | Veja opções na seção OPÇÕES |
| `TIPCALCSTESPEC` | Tipo de Cálculo de ST Específico | I | Veja opções na seção OPÇÕES |
| `CODTABSTFARPOP` | Tabela p/ Base ST - Farmácia Popular | I |  |
| `MVASIMPLIFICADO` | MVA Simplificado | S | Veja opções na seção OPÇÕES |
| `PERCCARGATRIBMEDIA` | Percentual Carga Trib. Média | F |  |
| `PERCICMSFCPINT` | % ICMS FCP Interno | F |  |
| `ZERARDIFALREM` | Zerar Valor do ICMS DIFAL do Remetente | S | Veja opções na seção OPÇÕES |
| `CALCALIFCPST` | Aplicar a aliquota de FCP no cálculo de Desoneração ICMS/ST por Dentro | S | Veja opções na seção OPÇÕES |
| `CALCREPREDST` | Cálculo de Desoneração ICMS/ST por Dentro, conforme Resolução SEFAZ nº 13/2019 | S | Veja opções na seção OPÇÕES |
| `CODMOTDESONERAST` | Cód. Mot. Desoneração do ICMS ST | I | Veja opções na seção OPÇÕES |
| `ALIQICMSESPST` | Alíquota de ICMS Específico para o cálculo de ST | F |  |
| `BASEFCPINT` | Base para cálculo do FCP Interno | S | Veja opções na seção OPÇÕES |
| `PERCSTFCPINT` | % ST FCP Interno | F |  |
| `ALIQADREMICMS` | Alíquota ad rem ICMS | F |  |
| `MVAORIGINAL` | Usar MVA original quando carga trib. inferior à alíq. interestadual? | S | Veja opções na seção OPÇÕES |
| `CODFORMBASDIFAL` | Fórmula para Cálculo da Base do DIFAL e do FCP | I |  |
| `PERCICMSMONORET` | % Destino ICMS Monofásico Retido | F |  |
| `REPDIFALFCP` | ICMS DIFAL (Não Contribuinte) | S | Veja opções na seção OPÇÕES |
| `PERCALIQADREMICMS` | % Redução Alíquota ad rem ICMS | F |  |
| `CODFORMCALCDIFAL` | Fórmula para Cálculo do DIFAL | I |  |
| `PERCTRAVAMED` | Porcentagem de trava para medicamentos | F |  |
| `MOTREDADREM` | Motivo Redução do ad rem | I | Veja opções na seção OPÇÕES |
| `CODBEN` | Código do Benefício | S |  |
| `CODFORMBASICM` | Fórmula para cálculo da base de ICMS | I |  |
| `PERCREDPR` | Percentual do Crédito Presumido | F |  |
| `REDBASEESTRANGEIRA` | Redução da Base para Origem Estrangeira | F |  |
| `PERCPMPF` | Percentual PMPF | F |  |
| `CARACTRIB` | Característica tributável | S | Veja opções na seção OPÇÕES |
| `ALIQICMSEFET` | Alíquota Interna (CST 60) | F |  |
| `PERCMULTCALCDP` | % Diferença Positiva | F |  |
| `FINALIDADE` | Destinação da mercadoria adquirida | S | Veja opções na seção OPÇÕES |
| `ICMSDIFPOSITIVA` | Utilizar diferença positiva | S | Veja opções na seção OPÇÕES |
| `MARGLUCROEST` | Margem Lucro (MVA) para origem estrangeira | F |  |
| `PERCREDBASEICMSEFET` | Perc. Red. Base | F |  |
| `CALCSTLIVRECOM` | Calcular ICMS ST Zona Franca/Ýrea de livre comércio | S | Veja opções na seção OPÇÕES |
| `CALCREPREDDENTRO` | Calculo Desoneração ICMS por dentro | S | Veja opções na seção OPÇÕES |
| `FORMAREPICMS` | FORMAREPICMS | S | Veja opções na seção OPÇÕES |
| `DESICMSSN` | Desonera ICMS do Simples Nacional | S | Veja opções na seção OPÇÕES |
| `CALCDIFICMSDENTRO` | Cálculo Diferimento Por Dentro | S | Veja opções na seção OPÇÕES |
| `REGRACALCBCICMSAT` | Regra p/ cálculo da base ICMS AT | S | Veja opções na seção OPÇÕES |
| `CODFORMBCICMSAT` | Fórmula para Cálculo da Base do ICMS AT | I |  |
| `ALIQICMSAT` | Alíquota ICMS AT (%) | F |  |
| `ALIQICMSATIMP` | Alíquota ICMS AT produto importado (%) | F |  |
| `ALIQICMSATINT` | Alíquota de ICMS Interna (%) | F |  |
| `REGRADEDICMSAT` | Deduzir do ICMS AT | S | Veja opções na seção OPÇÕES |
| `PERCUSAQUDECPE` | Percentual/Coeficiente sobre Custo Aquisição - PE | F |  |
| `PERCUSAQUDECPEEST` | Percentual/Coeficiente sobre Custo Aquisição - PE - Origem Estrangeira | F |  |
| `TIPCUSAQUDECPE` | Tipo de custo Custo Decreto 38.296/PE | S | Veja opções na seção OPÇÕES |
| `ALIQICMSCARGTRIBRED` | Alíquota da Carga Tributária Reduzida (ICMS) (%) | F |  |
| `ALIQSTCARGTRIBRED` | Alíquota da Carga Tributária Reduzida (ST) (%) | F |  |
| `CALPERREDBASEICMS` | Calcular % de Redução BC ICMS Lei 9.025/2020 | S | Veja opções na seção OPÇÕES |
| `CALPERREDBASEST` | Calcular % de Redução BC ICMS ST Lei 9.025/2020 | S | Veja opções na seção OPÇÕES |
| `CALCSTDECPR` | Calcular ST conforme Decreto 4.520/2020 - PR | S | Veja opções na seção OPÇÕES |
| `CONSPMVABCICM` | Considera Pauta + MVA para a base de cálculo do ICMS ST | S | Veja opções na seção OPÇÕES |
| `CREDPRESDECPR` | % Crédito Presumido Decreto 4.520/2020 - PR | F |  |
| `FORMCALFCPDIFAL` | Fórmula para o Cálculo do FCP do DIFAL | I |  |
| `CALCREDPREICMCON` | Calcular % de Crédito Presumido de ICMS ST Convênio ICMS 106/1996 | S | Veja opções na seção OPÇÕES |
| `PERCREDPREICMCON` | Percentual de Crédito Presumido de ICMS ST Convênio ICMS 106/1996 | F |  |
| `CODFORMVA` | Fórmula para calcular MVA Ajustada | I |  |
| `DTFIMVIGENCIA` | Fecha de Fin de Vigencia | D |  |
| `DTINICIOVIGENCIA` | Fecha de Vigencia | D |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPRESTRICAO (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| A | por tipo de transporte de importação |
| B | por capítulo do NCM |
| C | por cidade origem |
| D | por cidade destino |
| E | por grupo de ICMS do parceiro |
| F | por posição do NCM |
| G | por grupo de produtos |
| H | por NCM |
| I | por grupo de ICMS do produto |
| J | por grupo. ICMS do grupo de produto |
| K | Grupo de ICMS 2 |
| L | Produtor Rural |
| M | Código da Empresa |
| N | consumidor |
| O | por TOP |
| P | por produto |
| Q | por Finalidade da Operação |
| R | por TARE |
| S | sem exceção |
| T | por perfil principal |
| U | por CFOP |
| X | consumidor contribuinte |

### Opções para campo TIPRESTRICAO2 (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| A | por tipo de transporte de importação |
| B | por capítulo do NCM |
| C | por cidade origem |
| D | por cidade destino |
| E | por grupo de ICMS do parceiro |
| F | por posição do NCM |
| G | por grupo de produtos |
| H | por NCM |
| I | por grupo de ICMS do produto |
| J | por grupo. ICMS do grupo de produto |
| K | Grupo de ICMS 2 |
| M | Código da Empresa |
| O | por TOP |
| P | por produto |
| Q | por Finalidade da Operação |
| R | por TARE |
| S | sem exceção |
| T | por perfil principal |
| U | por CFOP |

### Opções para campo CODTRIB (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Tributada integralmente |
| 02 | 02-Tributação monofásica própria sobre combustíveis |
| 10 | 10-Tributada e c/cobrança por substituição |
| 15 | 15-Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis |
| 20 | 20-Com redução de base de cálculo |
| 30 | 30-Isenta e não tribut.e c/cobrança por subst. |
| 40 | 40-Isenta |
| 41 | 41-Não tributada |
| 50 | 50-Suspensão |
| 51 | 51-Diferimento |
| 53 | 53-Tributação monofásica sobre combustíveis com recolhimento diferido |
| 60 | 60-ICMS cobrado anteriormente por substituição |
| 61 | 61-Tributação monofásica sobre combustíveis cobrada anteriormente |
| 70 | 70-Com redução de base e c/cobrança por subst. |
| 90 | 90-Outras |

### Opções para campo REPREDBASE (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MAIORBASEST (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REPICMS (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REDICMS (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSIDIPIVLROPPROP (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCSTCONSUTRI (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASESTRED (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| D | Desconsiderar IPI p/ Redução |
| N | Desconsidera |
| S | Considerar IPI p/ Redução |

### Opções para campo NAOCONSIDMVA (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MAIORBASEICMS (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STSUTRI4302014MG (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PAUTAVLRSTFIXO (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONVPRODUZ (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASICMMOD (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 1 | Pauta (Valor) |
| 2 | Preço Tabelado Máx. (Valor) |
| 3 | Valor da Operação |

### Opções para campo REPREDBASE2 (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASICMSTMOD (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 0 | Preço tabelado ou Máximo Sugerido |
| 1 | Lista Negativa (Valor) |
| 2 | Lista Positiva (Valor) |
| 3 | Lista Neutra (Valor) |
| 4 | Margem Valor Agregado (%) |
| 5 | Pauta (Valor) |
| 6 | Valor da Operação |

### Opções para campo BASESTUFDEST (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| P | Pauta |
| V | Valor do Produto |

### Opções para campo CODANTECIPST (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| A | A-ST informada pelo substituto/substituído que não incorra em nenhuma das situações anteriores |
| N | N-(Não Usa) Operação não envolve ST |
| 1 | 1-Pgto de ST efetuado pelo destinatário quando não efetuado ou efetuado a menor pelo substituto |
| 2 | 2-Antecip. tribut. efetuada pelo destinatário apenas como complemento do diferencial de alíquota |
| 3 | 3-Antecip. tribut. com MVA efetuada pelo destinatário sem encerrar a fase de tributação |
| 4 | 4-Antecip. tribut. com MVA efetuada pelo destinatário encerrando a fase de tributação |
| 5 | 5-Substituição tributária interna motivada por regime especial de tributação |
| 6 | 6-ICMS pago na importação |

### Opções para campo CSOSN (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 101 | 101-Tributada pelo Simples Nacional com permissão de crédito |
| 102 | 102-Tributada pelo Simples Nacional sem permissão de crédito |
| 103 | 103-Isenção do ICMS no Simples Nacional para faixa de receita bruta |
| 201 | 201-Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por ST |
| 202 | 202-Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por ST |
| 203 | 203-Isenção do ICMS no Simples Nacional para faixa de receita bruta e com cobrança do ICMS por ST |
| 300 | 300-Imune |
| 400 | 400-Não tributada pelo Simples Nacional |
| 500 | 500-ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação |
| 900 | 900-Outros |

### Opções para campo ZERAR (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STCAT137SP (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROEMPREGO (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODMOTDESONERAICMS (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 1 | 1-Táxi |
| 10 | 10-Deficiente Condutor (Convênio ICMS 38/12) |
| 11 | 11-Deficiente Não Condutor (Convênio ICMS 38/12) |
| 12 | 12-Órgão de Fomento e Desenv. Agropecuário |
| 16 | 16-Olimpíadas Rio 2016 |
| 2 | 2-Deficiente Físico (Desativado) |
| 3 | 3-Produtor Agropecuário |
| 4 | 4-Frotista/Locadora |
| 5 | 5-Diplomático/Consular |
| 6 | 6-Utilitários e Motocicletas da Amazônia Ocidental e Ýreas de Livre Comércio |
| 7 | 7-SUFRAMA |
| 8 | 8-Venda a Órgãos Públicos |
| 9 | 9-Outros |
| 90 | 90-Solicitado pelo Fisco |

### Opções para campo ZERARSTNEG (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CUSCOMICMSBASEST (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCSTEXTRANOTA (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| M | Com base na Pauta acrescida de MVA |
| N | Não se aplica |
| P | Com base na Pauta |
| S | Com base em MVA |

### Opções para campo CALCMVAAJUSTADO (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| A | Pelo MVA da Alíquota |
| F | Pelo MVA da Alíquota considerando % ST FCP Interno |
| N | Não Calcular |
| P | Pela Fórmula |
| S | Pelo MVA Padrão do Produto/Empresa |

### Opções para campo TIPCALCDIFAL (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Sem considerar redução da Base |
| 1 | 1 - Com redução da base aplicada na base |
| 10 | 10 - Cálculo da base, valor do DIFAL e do FCP por fórmula |
| 2 | 2 - Com redução da base aplicada na alíquota |
| 3 | 3 - ICMS Interestadual calculado sob a BC do DIFAL |
| 4 | 4 - Cálculo do DIFAL com ICMS Destino por dentro |
| 5 | 5 - Cálculo do DIFAL Convênio 142/2018 |
| 6 | 6 - Cálculo do DIFAL com a redução do ICMS Próprio |
| 7 | 7 - ICMS Difal base dupla UF Sergipe |
| 8 | 8 - Base de cálculo do DIFAL e do FCP por fórmula |
| 9 | 9 - Cálculo do DIFAL com ICMS Destino por dentro - Base Dupla |

### Opções para campo ICMSUFORIGDIFEMIT (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCONSIDERAREDBASE (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Redução de Base |
| S | Desconsiderar redução |
| Z | Redução de Base Estrangeira |

### Opções para campo TIPCALCFCPSTESPEC (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| null | 0 - Não específico (Regra Geral) |
| 1 | 1 - FECOP ST Majorado (CE) |

### Opções para campo TIPCALCSTESPEC (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Não específico (Regra Geral) |
| 1 | 1 - Calcular ST p/ Medicamentos - CAT-SP |
| 10 | 10 - Calcular ST Via Pauta sem dedução do ICMS próprio |
| 11 | 11 - Calcular ST (Alíq. Limite créd. ICMS p/ dedução no Valor ST) |
| 12 | 12 - Calcular ST (Dif.Alíq. por dentro), BC ST COM Red.ICMS COM FCP |
| 13 | 13 - Realizar cálc de ICMS para reduc no ST com alíq espec e utilizando o mesmo % de redução do ST |
| 14 | 14 - Cálculo ICMS e ICMS/ST - Decreto 38.296/PE |
| 15 | 15 - Calcular ST P/ Medicamentos - CAT-40/SP |
| 16 | 16 - Cálculo ICMS/ST - DIFAL - Decreto 40.230/2020 - PB |
| 17 | 17 - Calcular ST - Lei nº 15730/PE |
| 18 | 18 - Cálculo ICMS ST e FCP (ICMS de Destino por Dentro) - Protocolo ICMS 104/2008 - AL |
| 19 | 19 - Cálculo ST SUFRAMA com Desoneração Simples Nacional |
| 2 | 2 - Calcular ST (Dif.Alíq. por dentro), BC ST SEM Red.ICMS |
| 20 | 20 - Calcular ICMS-ST com BC Reduzida por PIS/COFINS Desonerados e ICMS Operação |
| 3 | 3 - Calcular ST com Incentivos SUFRAMA e Redução da BC |
| 4 | 4 - Calcular ST (Dif.Alíq. por dentro), BC ST COM Red.ICMS |
| 5 | 5 - Calcular ST Simplificado (Carga Média) |
| 6 | 6 - Calcular ST sem dedução do ICMS Próprio |
| 7 | 7 - Calcular ST (Dif.Alíq. Convênio 142/2018 - CFC) |
| 8 | 8 - Calcular ST (Dif. Aliq. Considerando FCP e Redução de Base de ST) |
| 9 | 9 - Implementação Futura |

### Opções para campo MVASIMPLIFICADO (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ZERARDIFALREM (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCALIFCPST (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCREPREDST (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODMOTDESONERAST (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 12 | Órgão de fomento e desenvolvimento agropecuário |
| 3 | Uso na agropecuária |
| 9 | Outros |

### Opções para campo BASEFCPINT (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| B | Base do ICMS |
| null | Valor da Operação |

### Opções para campo MVAORIGINAL (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REPDIFALFCP (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MOTREDADREM (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Transporte coletivo de passageiros |
| 9 | 9 - Outros |

### Opções para campo CARACTRIB (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 0 | Industrial |
| 1 | Distribuidor |
| 2 | Atacadista |
| 3 | Varejista |
| 4 | Produtor Rural Pessoa Jurídica |
| 6 | Produtor Rural Pessoa Física |
| 7 | Pessoa Jurídica não Contribuinte do ICMS |
| 8 | Pessoa Física não Contribuinte do ICMS |

### Opções para campo FINALIDADE (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 0 | Revenda |
| 1 | Insumo |
| 2 | Uso e Consumo Ou Ativo Imobilizado |

### Opções para campo ICMSDIFPOSITIVA (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo CALCSTLIVRECOM (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCREPREDDENTRO (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FORMAREPICMS (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| null | Destacar valores e deduzir do total da nota |
| 1 | Destacar valores e não deduzir do total da nota |

### Opções para campo DESICMSSN (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCDIFICMSDENTRO (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGRACALCBCICMSAT (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| 0 | Cálculo por dentro |
| 1 | Cálculo (Valor líquido do produto + IPI) |
| 2 | Fórmula personalizada |

### Opções para campo REGRADEDICMSAT (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| null | Sem dedução |
| 1 | Deduzir ICMS normal |
| 2 | Deduzir ICMS-ST |
| 3 | Deduzir ICMS normal e ICMS-ST |

### Opções para campo TIPCUSAQUDECPE (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| E | Último Custo de Entrada Com ICMS |
| G | Último Custo Médio Gerencial |
| L | Último Custo Gerencial |
| M | Último Custo Médio Com ICMS |
| null | Não se Aplica |
| R | Último Custo de Reposição |
| S | Último Custo de Entrada Sem ICMS |
| V | Último Custo Variável |
| Z | Último Custo Médio Sem ICMS |

### Opções para campo CALPERREDBASEICMS (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALPERREDBASEST (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCSTDECPR (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSPMVABCICM (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCREDPREICMCON (Tabela: TGFICM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFICNF
### Descrição: Contingências por Nota

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Cód. Usuário | I |  |
| `CODEMP` | Empresa | I |  |
| `TPEMISNFCOM` | Emissão NFCom | I | Veja opções na seção OPÇÕES |
| `TPEMISNFE` | Emissão NF-e | I | Veja opções na seção OPÇÕES |
| `TIPMOV` | Tipo de Movimento | S | Veja opções na seção OPÇÕES |
| `DTNEG` | Dt.Negociação | D |  |
| `NUMNOTA` | Nro. Nota | I |  |
| `SERIENOTA` | Série da nota | S |  |
| `VLRNOTA` | Valor da Nota | F |  |
| `STATUSNOTA` | Status da Nota | S | Veja opções na seção OPÇÕES |
| `CODPARC` | Cód.Parceiro | I |  |
| `NOMEPARC` | Parceiro | S |  |
| `NUCONTING` | Nro. Contingência | I |  |
| `NUNOTA` | Nro. Único Nota | I |  |
| `DHALTER` | Dh. Alter | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo TPEMISNFCOM (Tabela: TGFICNF)
| Valor | Descrição |
|-------|-----------|
| 2 | Contingência Offline |

### Opções para campo TPEMISNFE (Tabela: TGFICNF)
| Valor | Descrição |
|-------|-----------|
| 2 | Danfe de Segurança |
| 3 | S.C.Amb.Nac. |
| 4 | DPEC |
| 9 | Conting.Off-Line NFC-e |

### Opções para campo TIPMOV (Tabela: TGFICNF)
| Valor | Descrição |
|-------|-----------|
| B | B-Movimento bancário |
| C | C-Compra |
| D | D-Devolução de venda |
| E | E-Devolução de compra |
| F | F-Produção |
| G | G-Pagamento |
| I | I-Financeiro |
| J | J-Pedido de Requisição |
| K | K-Pedido de Transferência |
| L | L-Devolução de Requisição |
| M | M-Devolução de Transf. |
| N | N-Entradas |
| O | O-Pedido de compra |
| P | P-Pedido de venda |
| Q | Q-Requisição |
| R | R-Recebimento |
| T | T-Transferência |
| V | V-Venda |
| Z | Z-Modelo |
| 1 | 1-NF Depósito |
| 2 | 2-PD Devol. / Procuração / Warrant |
| 3 | 3-Saídas |
| 4 | 4-Faturamento |
| 8 | 8-RD8 |

### Opções para campo STATUSNOTA (Tabela: TGFICNF)
| Valor | Descrição |
|-------|-----------|
| A | Atendimento |
| L | Confirmada |
| P | Pendente |


## Tabela: TGFIFE
### Descrição: Aliquotas (PIS, Confins e CSLL)

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NOMEIMP` | Nome do imposto | S |  |
| `IDALIQ` | Código Alíquota | I |  |
| `GRUPOIMP` | Grupo | S |  |
| `CODEMP` | Empresa | I |  |
| `CODPARC` | Parceiro | I |  |
| `CODTIPOPER` | Tipo Operação | I |  |
| `ENTSAI` | Tipo | S | Veja opções na seção OPÇÕES |
| `PERCVLR` | Tipo alíquota | S | Veja opções na seção OPÇÕES |
| `ALIQ` | Alíquota | F |  |
| `REDBASE` | % Red. base | F |  |
| `IVA` | IVA | F |  |
| `ALIQCRED` | Alíq. p/ crédito | F |  |
| `RETEMFIN` | Retém no financeiro | S | Veja opções na seção OPÇÕES |
| `CODTAB` | Tabela c/base p/ ST | I |  |
| `CST` | Cód. sit. tributária | I | Veja opções na seção OPÇÕES |
| `VLRPAUTA` | Valor pauta | F |  |
| `VLRPAUTACRED` | Valor pauta cred. | F |  |
| `IPIINCBASE` | IPI incide na base de cálculo | S | Veja opções na seção OPÇÕES |
| `PRODSEMTRIB` | Produto sem tributação | S | Veja opções na seção OPÇÕES |
| `ALIQSUFRAMA` | Alíquota Suframa | F |  |
| `SOMARPISCOFINSST` | Indica se o valor do PIS/COFINS ST compõe o valor total da NF-e | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ENTSAI (Tabela: TGFIFE)
| Valor | Descrição |
|-------|-----------|
| A | Ambas |
| E | Entrada |
| S | Saída |

### Opções para campo PERCVLR (Tabela: TGFIFE)
| Valor | Descrição |
|-------|-----------|
| P | Percentual |
| V | Valor |

### Opções para campo RETEMFIN (Tabela: TGFIFE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CST (Tabela: TGFIFE)
| Valor | Descrição |
|-------|-----------|
| 1 | 01 - Alíquota Normal (Cumulativo/Não Cumulativo) |
| 2 | 02 - Alíquota Diferenciada |
| 3 | 03 - Alíquota por Unidade de produto |
| 4 | 04 - Monofásica (Alíquota Zero) |
| 49 | 49 - Outras Operações de Saída |
| 5 | 05 - Operação Tributável por Substituição Tributária |
| 50 | 50 - Direito a Créd.- Vinc.Exclusiv.a Receita Tribut.no Merc.Interno |
| 51 | 51 - Direito a Créd.- Vinc.Exclusiv.a Receita Não Tribut.no Merc.Interno |
| 52 | 52 - Direito a Créd.- Vinc.Exclusiv.a Receita de Export. |
| 53 | 53 - Direito a Créd.- Vinc.a Receitas Tribut.e Não-Tribut.no Merc.Interno |
| 54 | 54 - Direito a Créd.- Vinc.a Receitas Tribut.no Merc.Interno e de Export |
| 55 | 55 - Direito a Créd.- Vinc.a Receitas Não-Tribut.no Merc.Interno e de Export. |
| 56 | 56 - Direito a Créd.- Vinc.a Receitas Tribut.e Não-Tribut.no Merc.Interno, e de Export. |
| 6 | 06 - Alíquota Zero |
| 60 | 60 - Créd.Presumido - Aquisição Vinc.Exclusiv.a Receita Tribut.no Merc.Interno |
| 61 | 61 - Créd.Presumido - Aquisição Vinc.Exclusiv.a Receita Não-Tribut.no Merc.Interno |
| 62 | 62 - Créd.Presumido - Aquisição Vinc.Exclusiv.a Receita de Export. |
| 63 | 63 - Créd.Presumido - Aquisição Vinc.a Receitas Tribut.e Não-Tribut.no Merc.Interno |
| 64 | 64 - Créd.Presumido - Aquisição Vinc.a Receitas Tribut.no Merc.Interno e de Export. |
| 65 | 65 - Créd.Presumido - Aquisição Vinc.a Receitas Não-Tribut.no Merc.Interno e de Export. |
| 66 | 66 - Créd.Presumido - Aquisição Vinc.a Receitas Tribut.e Não-Tribut.no Merc.Interno, e de Export. |
| 67 | 67 - Créd.Presumido - Outras Operações |
| 7 | 07 - Isenta |
| 70 | 70 - Aquisição sem Direito a Créd. |
| 71 | 71 - Aquisição com Isenção |
| 72 | 72 - Aquisição com Suspensão |
| 73 | 73 - Aquisição a Alíquota Zero |
| 74 | 74 - Aquisição sem Incidência da Contribuição |
| 75 | 75 - Aquisição por Substituição Tributária |
| 8 | 08 - Sem Incidência |
| 9 | 09 - Com Suspensão |
| 98 | 98 - Outras Entradas |
| 99 | 99 - Outras |

### Opções para campo IPIINCBASE (Tabela: TGFIFE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODSEMTRIB (Tabela: TGFIFE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SOMARPISCOFINSST (Tabela: TGFIFE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFIIF
### Descrição: Impostos Item de Financeiro

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `SEQUENCIA` | Sequência | I |  |
| `CODIMP` | Imposto | I | Veja opções na seção OPÇÕES |
| `TIPBASE` | Incidência | S | Veja opções na seção OPÇÕES |
| `NUFIN` | Nro Único Fin. | I |  |
| `NUNOTA` | Nro. Único Nota | I |  |
| `BASE` | Base | F |  |
| `BASERED` | Base Cálc.Reduzida | F |  |
| `ALIQUOTA` | Alíquota | F |  |
| `VALOR` | Valor | F |  |
| `CST` | CST | I |  |
| `DIGITADO` | Digitado | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo CODIMP (Tabela: TGFIIF)
| Valor | Descrição |
|-------|-----------|
| 6 | PIS |
| 7 | COFINS |

### Opções para campo TIPBASE (Tabela: TGFIIF)
| Valor | Descrição |
|-------|-----------|
| D | Desconto |
| J | Juro |
| M | Multa |
| V | Valor Desdobramento |

### Opções para campo DIGITADO (Tabela: TGFIIF)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFIMA
### Descrição: Aliquotas de impostos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TIPO` | Tipo | S |  |
| `CODIGO` | Código | I |  |
| `CODIMP` | Imposto | I |  |
| `IMPNOTA` | Na Nota | I | Veja opções na seção OPÇÕES |
| `IMPFINORIGFIN` | No Financeiro Origem Financeiro | I | Veja opções na seção OPÇÕES |
| `IMPFINORIGEST` | No Financeiro Origem Estoque | I | Veja opções na seção OPÇÕES |
| `TPIRRFEXT` | Tributação IRRF - Exterior REINF | I | Veja opções na seção OPÇÕES |
| `CALCULAR` | Calcular | S | Veja opções na seção OPÇÕES |
| `CODRECEITA` | Código da Receita | S |  |
| `ALIQUOTA` | Alíquota | F |  |
| `TIPIMP` | Tipo do Imposto | I | Veja opções na seção OPÇÕES |
| `REDBASE` | Redução da Base de Imposto | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo IMPNOTA (Tabela: TGFIMA)
| Valor | Descrição |
|-------|-----------|
| 0 | Já Incluso |
| -1 | Subtrair |
| 1 | Somar |
| 2 | Nenhum |

### Opções para campo IMPFINORIGFIN (Tabela: TGFIMA)
| Valor | Descrição |
|-------|-----------|
| -1 | Subtrair |
| 2 | Nenhum |

### Opções para campo IMPFINORIGEST (Tabela: TGFIMA)
| Valor | Descrição |
|-------|-----------|
| -1 | Subtrair |
| 2 | Nenhum |

### Opções para campo TPIRRFEXT (Tabela: TGFIMA)
| Valor | Descrição |
|-------|-----------|
| 10 | 10 - Retenção do IRRF - alíquota padrão |
| 11 | 11 - Retenção do IRRF - alíquota da tabela progressiva |
| 12 | 12 - Retenção do IRRF - alíquota diferenciada (países com tributação favorecida) |
| 13 | 13 - Retenção do IRRF - alíquota limitada conforme cláusula em convênio |
| 30 | 30 - Retenção do IRRF - outras hipóteses |

### Opções para campo CALCULAR (Tabela: TGFIMA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPIMP (Tabela: TGFIMA)
| Valor | Descrição |
|-------|-----------|
| 0 | Já Incluso |
| -1 | Subtrair |
| 1 | Somar |


## Tabela: TGFIMC
### Descrição: Cadastro de Imposto

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `F600EFD` | Gerar reg. F600 p/EFD Contribuições | S | Veja opções na seção OPÇÕES |
| `DESCRICAO` | Descrição do Imposto | S |  |
| `REGRA` | Tipo | S | Veja opções na seção OPÇÕES |
| `NOMEIMP` | Nome do Imposto | S |  |
| `CODCTACTB2` | Conta Contábil 2 | I |  |
| `CODIMP` | Código | I |  |
| `CODCTACTB1` | Conta Contábil 1 | I |  |
| `USARPRECOCUSTO` | Usar Preço de Custo | S | Veja opções na seção OPÇÕES |
| `TIPOIMPOSTO` | Tipo Imposto | I | Veja opções na seção OPÇÕES |
| `CODTAB` | Tab.p/Pauta | I |  |
| `IMPBAIXAPARCIAL` | Destaque do Imposto | S | Veja opções na seção OPÇÕES |
| `GRUPOVLRMIN` | Grupo Vlr Mínimo | S |  |
| `CONSIDERARIMP` | Considerar Impostos | S | Veja opções na seção OPÇÕES |
| `IMPFRETE` | Proporcionalizar imposto dos itens ao Frete | S | Veja opções na seção OPÇÕES |
| `BASEIMPFIN` | Base do Imposto no Financeiro | S | Veja opções na seção OPÇÕES |
| `CODREC` | Código Receita (Darf) | S |  |
| `REGCALCIMPRET` | Registrar cálculo quando o imposto retido for inferior ao valor mínimo? | S | Veja opções na seção OPÇÕES |
| `CALCBASDIA` | Calcular com Base Diária? | S |  |
| `VLRMAXINSS` | Valor Maxímo INSS | F |  |
| `ACUMBASEICMS` | Acumular na Base ICMS? | S |  |
| `VLRMIN` | Valor Mínimo do Imposto | F |  |
| `CALCBASEMENSAL` | Calcular com Base Mensal? | S |  |
| `ACUMBASEIPI` | Acumular na Base IPI? | S |  |
| `ATIVO` | Ativo | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo F600EFD (Tabela: TGFIMC)
| Valor | Descrição |
|-------|-----------|
| E | Entrada |
| N | Não Gerar |
| S | Saída |
| U | Usar da TOP |

### Opções para campo REGRA (Tabela: TGFIMC)
| Valor | Descrição |
|-------|-----------|
| N | apenas os que tenham a coluna "calcular" MARCADA |
| S | todos, EXCETO os com a coluna "calcular" DESMARCADA |

### Opções para campo USARPRECOCUSTO (Tabela: TGFIMC)
| Valor | Descrição |
|-------|-----------|
| E | Último Custo de Entrada Com ICMS |
| G | Último Custo Médio Gerencial |
| L | Último Custo Gerencial |
| M | Último Custo Médio Com ICMS |
| P | Preço da Nota |
| R | Último Custo de Reposição |
| S | Último Custo de Entrada Sem ICMS |
| T | Valor de Pauta |
| W | Valor Total + ST |
| X | Valor Total + IPI |
| Y | Valor Total + IPI + ST |
| Z | Último Custo Médio Sem ICMS |

### Opções para campo TIPOIMPOSTO (Tabela: TGFIMC)
| Valor | Descrição |
|-------|-----------|
| 0 | OUTROS |
| 1 | ICMS |
| 10 | GILRAT |
| 11 | SENAR |
| 2 | ST |
| 3 | IPI |
| 4 | ISS |
| 5 | INSS |
| 6 | PIS |
| 7 | COFINS |
| 8 | IRF |
| 9 | CSLL |

### Opções para campo IMPBAIXAPARCIAL (Tabela: TGFIMC)
| Valor | Descrição |
|-------|-----------|
| B | Destaca imposto na baixa |
| D | Destaca imposto na pendência |
| P | Proporcionaliza o imposto na baixa |

### Opções para campo CONSIDERARIMP (Tabela: TGFIMC)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| F | Financeiro |
| N | Nota |

### Opções para campo IMPFRETE (Tabela: TGFIMC)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo BASEIMPFIN (Tabela: TGFIMC)
| Valor | Descrição |
|-------|-----------|
| D | Valor do documento |
| null | Valor do pagamento |

### Opções para campo REGCALCIMPRET (Tabela: TGFIMC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFIMN
### Descrição: GF Imposto na Nota

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro Único Nota | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `CODIMP` | Imposto | I |  |
| `TIPIMP` | Tipo Imposto | I | Veja opções na seção OPÇÕES |
| `CODCID` | Cód. Cidade | I |  |
| `BASE` | Base | F |  |
| `ALIQUOTA` | Alíquota | F |  |
| `VALOR` | Valor | F |  |
| `DIGITADO` | Digitado | S | Veja opções na seção OPÇÕES |
| `TIPOINSSESPECIAL` | Tipo de INSS Especial | S | Veja opções na seção OPÇÕES |
| `PERCINSSESPECIAL` | % INSS Especial | F |  |
| `VLRINSSESPECIAL` | Vlr. INSS Especial | F |  |
| `CODRECEITA` | Cód. Receita | S |  |
| `TPIRRFEXT` | Tributação IRRF - Exterior REINF | I | Veja opções na seção OPÇÕES |
| `CODNATREND` | Código Natureza de Rendimento | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPIMP (Tabela: TGFIMN)
| Valor | Descrição |
|-------|-----------|
| 0 | Incluso |
| -1 | Retido |
| 1 | Somar |

### Opções para campo DIGITADO (Tabela: TGFIMN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOINSSESPECIAL (Tabela: TGFIMN)
| Valor | Descrição |
|-------|-----------|
| 1 | INSS 15 anos |
| 2 | INSS 20 anos |
| 3 | INSS 25 anos |

### Opções para campo TPIRRFEXT (Tabela: TGFIMN)
| Valor | Descrição |
|-------|-----------|
| 10 | 10 - Retenção do IRRF - Alíquota padrão |
| 11 | 11 - Retenção do IRRF - Alíquota da tabela progressiva |
| 12 | 12 - Retenção do IRRF - Alíquota diferenciada (países com tributação favorecida) |
| 13 | 13 - Retenção do IRRF - Alíquota limitada conforme cláusula em convênio |
| 30 | 30 - Retenção do IRRF - Outras hipóteses |


## Tabela: TGFINCT
### Descrição: Relação de Itens do CTe

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Nota | I |  |
| `SEQNOTA` | Sequência NF-e | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `QUANTIDADE` | Quantidade | F |  |
| `DESCPROD` | Descrição do Produto | S |  |
| `UNIDADE` | Unidade | S |  |
| `VALUNIT` | Valor Unitário | F |  |
| `VALTOTAL` | Valor Total | F |  |

## Tabela: TGFIPI
### Descrição: Alíquotas de IPI

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODFISIPI` | Código Fiscal (NPC, NBM) | S |  |
| `CODIPI` | Código do IPI | I |  |
| `DESCRICAO` | Descrição | S |  |
| `VLRPAUTA` | Valor de Pauta | F |  |
| `PERCENTUAL` | Percentual | F |  |
| `CODEXNCM` | Cód. Exceção NCM | I |  |
| `PERCREDVLRIPI` | % Redução de Vlr. IPI | F |  |
| `CODEXII` | Cód. Exceção II | I |  |
| `ALIQII` | Aliq. II | F |  |
| `PERCPIS` | % PIS | F |  |
| `PERCCOFINS` | % COFINS | F |  |
| `PERCCSSL` | % CSLL | F |  |
| `ALIQICMS` | Alíquota ICMS | F |  |
| `CSTIPIENT` | Cód.Sit.Trib.IPI Entrada | I | Veja opções na seção OPÇÕES |
| `CSTIPISAI` | Cód.Sit.Trib.IPI Saída | I | Veja opções na seção OPÇÕES |
| `CODENQIPIENT` | Cód. Enq. Legal IPI Entrada | I |  |
| `CODENQIPISAI` | Cód. Enq. Legal IPI Saída | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo CSTIPIENT (Tabela: TGFIPI)
| Valor | Descrição |
|-------|-----------|
| 0 | 00 - Entrada c/Recuperação de Crédito |
| 1 | 01 - Entrada c/Alíquota zero |
| 2 | 02 - Entrada Isenta |
| 3 | 03 - Entrada Não Tributada |
| 4 | 04  -Entrada Imune |
| 49 | 49 - Outras Entradas |
| 5 | 05 - Entrada c/Suspensão |

### Opções para campo CSTIPISAI (Tabela: TGFIPI)
| Valor | Descrição |
|-------|-----------|
| 50 | 50-Saída Tributada |
| 51 | 51 - Saída c/Alíquota zero |
| 52 | 52 - Saída Isenta |
| 53 | 53 - Saída Não Tributada |
| 54 | 54 - Saída Imune |
| 55 | 55 - Saída c/Suspensão |
| 99 | 99 - Outras Saídas |


## Tabela: TGFISS
### Descrição: Tabela de ISS

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDALIQ` | Código Alíquota | I |  |
| `CODCID` | Cidade | I |  |
| `CODPROD` | Serviço | I |  |
| `CODEMP` | Empresa | I |  |
| `PERCINSS` | Percentual de ISS | F |  |
| `CODTRIBISS` | Cód. Tributação ISS | I | Veja opções na seção OPÇÕES |
| `PERCDEDUCAO` | Perc. de dedução na base do ISS | F |  |
| `TIPODEDUCAO` | Tipo de dedução de base do ISS | S | Veja opções na seção OPÇÕES |
| `CODTRIBMUNISS` | Cod. Trib. Município | S |  |
| `CODLST` | Tipo de Serviço | I |  |
| `NAOCALCULA` | Não Calcula | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo CODTRIBISS (Tabela: TGFISS)
| Valor | Descrição |
|-------|-----------|
| 0 | 00 - Tributado |
| 1 | 01 - Tributado com ISS Retido |
| 6 | 06 - Isento |
| 7 | 07 - Não Tributado |

### Opções para campo TIPODEDUCAO (Tabela: TGFISS)
| Valor | Descrição |
|-------|-----------|
| M | Materiais |
| P | Por percentual |
| S | Sub-Empreito |

### Opções para campo NAOCALCULA (Tabela: TGFISS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFITC
### Descrição: Ítens da Cotação

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTACPA` | Nro. do Item na Nota do Pedido | I |  |
| `CODPROD` | Produto | I |  |
| `SEQNOTACPA` | Sequencia da nota de compra | I |  |
| `COMPLDESC` | Complemento | S |  |
| `CODPARC` | Parceiro | I |  |
| `CODVOL` | Volume | S |  |
| `DTCOLETAPRECO` | Data Coleta | H |  |
| `TIPOCOLPRECO` | Coleta de preço | S | Veja opções na seção OPÇÕES |
| `QTDCOTADA` | Quantidade | F |  |
| `PRAZOVALPROP` | Prazo Validade | I |  |
| `PRECOMOE` | Preço em moeda | F |  |
| `PRECO` | Preço | F |  |
| `CODMOEDA` | Moeda | I |  |
| `VLRMOEDA` | Valor Moeda | I |  |
| `CONDPAGT` | Condição de pagamento | S | Veja opções na seção OPÇÕES |
| `PRAZOPARC` | Intervalo pagamento | I |  |
| `QTDPARCPAGT` | Parcelas | I |  |
| `VLRACRESC` | Valor do Acréscimo | F |  |
| `PERCACRESC` | % Acréscimo | F |  |
| `VLRDESCMOE` | Vlr. Desc. Moeda | F |  |
| `VLRDESC` | Valor do Desconto | F |  |
| `TOTALPRODUTO` | Total | F |  |
| `PERCDESC` | % Desconto | F |  |
| `DTLIMPRECO` | Data limite preço | D |  |
| `IPI` | IPI unitário | F |  |
| `ICMS` | ICMS Unitário | F |  |
| `FRETE` | Frete Unitário | F |  |
| `OUTROS` | Outros | F |  |
| `TAXAJURO` | Taxa Juro | F |  |
| `PRAZOMEDIO` | Prazo Médio | I |  |
| `PRAZOENTREGA` | Prazo Entrega | I |  |
| `QUALPROD` | Qual. Produto | I |  |
| `MODFRETE` | Modalidade de frete | S | Veja opções na seção OPÇÕES |
| `CONFIABFORN` | Conf. Fornecedor | I |  |
| `GARANTIA` | Garantia | I |  |
| `FATMINIMO` | Fat. Mínimo | F |  |
| `SITUACAO` | Situação | S | Veja opções na seção OPÇÕES |
| `MELHOR` | Melhor Cotação | S | Veja opções na seção OPÇÕES |
| `RESULTCOT` | Resultado | F |  |
| `CODTIPVENDA` | Tipo Negociação | I |  |
| `CODLOCAL` | Local | I |  |
| `OBSMOTCANC` | Observação Motivo de Cancelamento | S |  |
| `CODMOTCAN` | Código Motivo de Cancelamento | I |  |
| `CUSMEDICM` | Custo com ICMS Calc. | F |  |
| `CUSSEMICM` | Custo sem ICMS Calc. | F |  |
| `ULTCUSREP` | Último Custo Reposição | F |  |
| `CUSREP` | Custo Reposição Calc. | F |  |
| `ULTCUSVAR` | Último Custo Variável | F |  |
| `CUSGER` | Custo Gerencial Calc. | F |  |
| `ULTCUSGER` | Último Custo Gerencial | F |  |
| `CUSVARIAVEL` | Custo Variável Calc. | F |  |
| `PRECOCALC` | Preço Calculado | F |  |
| `VLRSUBST` | Valor S.T. | F |  |
| `ALIQIPI` | % IPI | F |  |
| `ALIQICMS` | % ICMS | F |  |
| `CONTROLE` | Controle | S |  |
| `DIFERENCIADOR` | Diferenciador | I |  |
| `DTENVIOCOT` | Dt. envio da cotação | D |  |
| `NUMEROOS` | Número OS Gub. | I |  |
| `USURESP` | Usuário responsável | I |  |
| `MELHORFORNEC` | Melhor Fornecedor | I |  |
| `NUMCOTACAO` | Número da cotação | I |  |
| `MELHORPRECO` | Melhor preço | F |  |
| `CUSTOFINAL` | Custo Final | F |  |
| `EMPRESA` | Empresa | I |  |
| `CODNAT` | Natureza | I |  |
| `CODPROJ` | Projeto | I |  |
| `CENTRESULT` | Centro de Resultado | I |  |
| `FORNECAPROVADO` | Fornecedor aprovado | I |  |
| `STATUSENVIO` | Status de envio | S |  |
| `QUALATEND` | Qual. Atendimento | I |  |
| `DHINICIAL` | Data inicial da cotação | H |  |
| `STATUSPRECIFICACAO` | Status de precificação | S |  |
| `DTMOEDA` | Data Moeda | H |  |
| `TOTALPARCEIROS` | Quantidade total de fornecedores | I |  |
| `STATUSPRODCOT` | Situação do produto | S | Veja opções na seção OPÇÕES |
| `CABECALHO` | Cabeçalho | S | Veja opções na seção OPÇÕES |
| `SEQITEMCOT` | Numero item cotacação | I |  |
| `DTLIMITE` | Dt. limite | D |  |
| `ULTVLRUNITCOMP` | Último Vlr. Unit. Compra | F |  |
| `MARCA` | Marca | S |  |
| `CODPRODESP` | Produto específico | I |  |
| `DIFALIQICMS` | Diferença de aliq. ICMS | F |  |
| `DHFINAL` | Data final da cotação | H |  |
| `CODCONTATO` | Contato | I |  |
| `OBS` | Observação | S |  |
| `DHENTREGA` | Data Entrega | H |  |
| `USUSOL` | Usuário comprador | I |  |
| `VALPROPOSTA` | Validade Proposta | I |  |
| `RESPMINCOT` | Respostas mínimas p/ cotação | I |  |
| `PRODDECQTD` | Decimais para qtd | I |  |
| `PRODDECVLR` | Decimais para valor | I |  |
| `PRODAGRUPMIN` | Agrupamento mínimo | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOCOLPRECO (Tabela: TGFITC)
| Valor | Descrição |
|-------|-----------|
| MANUAL | Manual |
| ONLINE | Online |

### Opções para campo CONDPAGT (Tabela: TGFITC)
| Valor | Descrição |
|-------|-----------|
| P | Parcelada |
| V | À Vista |
| Z | A Prazo |

### Opções para campo MODFRETE (Tabela: TGFITC)
| Valor | Descrição |
|-------|-----------|
| C | Por conta do emitente (CIF) |
| D | Transp. próprio pelo destinatário |
| F | Por conta do destinatário (FOB) |
| R | Transp. próprio pelo remetente |
| S | Sem frete |
| T | Por conta de terceiros |

### Opções para campo SITUACAO (Tabela: TGFITC)
| Valor | Descrição |
|-------|-----------|
| A | Aprovada |
| C | Recusada |
| E | Enviada |
| F | Faturada |
| G | Negociar |
| N | Reprovada |
| P | Pendente |
| R | Respondida |

### Opções para campo MELHOR (Tabela: TGFITC)
| Valor | Descrição |
|-------|-----------|
| I | Empate |
| N | Não |
| S | Sim |

### Opções para campo STATUSPRODCOT (Tabela: TGFITC)
| Valor | Descrição |
|-------|-----------|
| A | Aprovada |
| C | Cancelada |
| E | Enviada |
| F | Fechada |
| O | Aberta |
| P | Precificada |

### Opções para campo CABECALHO (Tabela: TGFITC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFITE
### Descrição: Itens de Entrada e Saída de Produto

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `RESERVADO` | Qtd. Reservada | F |  |
| `STATUSPROC` | Situação Atual da Produção | S | Veja opções na seção OPÇÕES |
| `IDDESCPARCERIA` | Id de desconto da parceria | F |  |
| `VLRDESCPARCERIA` | Valor cupom desconto parceria | F |  |
| `ALIQFUNTTEL` | Alíquota FUNTTEL | F |  |
| `ALIQFUST` | Alíquota FUST | F |  |
| `BASEFUNTTEL` | Base FUNTTEL | F |  |
| `BASEFUST` | Base FUST | F |  |
| `VLRFUNTTEL` | Valor FUNTTEL | F |  |
| `VLRFUST` | Valor FUST | F |  |
| `CODBARRAPDV` | Cód. de Barras | S |  |
| `OPERATUAL` | Operação Atual da Produção | S |  |
| `NROPROCESSO` | Nro do Processo Judicial/Adm (ISS) | S |  |
| `CODPROD` | Produto | I |  |
| `CODVOLPAD` | Unidade padrão | S |  |
| `COMPLDESC` | Complemento | S |  |
| `CODEMP` | Cód.Empresa | I |  |
| `NUNOTA` | Nro único | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `REFFORN` | Referência do Fornecedor | S |  |
| `REFERENCIA` | Referência do produto | S |  |
| `ESTOQUE` | Estoque | F |  |
| `QTDPENDENTE` | Qtd. pendente | F |  |
| `CODNATREND` | Código Natureza de Rendimento | I |  |
| `QTDNEG` | Quantidade | F |  |
| `QTDFORMULA` | Qtd. fórmula | F |  |
| `QTDCONFERIDA` | Qtd. corte | F |  |
| `VLRUNIT` | Vlr. unitário | F |  |
| `VLRTOT` | Vlr. total | F |  |
| `VLRTOTMOE` | Vlr. Tot. Moeda | F |  |
| `PERCDESC` | % desconto | F |  |
| `CODVOL` | Unidade | S |  |
| `CODVEND` | Vendedor | I |  |
| `CODLOCALORIG` | Local origem | I |  |
| `CODLOCALDEST` | Local destino | I |  |
| `CONTROLE` | Controle | S |  |
| `CONTROLEDEST` | Controle destino | S |  |
| `BASEICMS` | Base ICMS | F |  |
| `ALIQICMS` | Alíq. ICMS | F |  |
| `VLRICMS` | Vlr. ICMS | F |  |
| `BASEIPI` | Base do IPI | F |  |
| `ALIQIPI` | Alíq. IPI | F |  |
| `VLRIPI` | Vlr. IPI | F |  |
| `BASESUBSTIT` | Base substituição | F |  |
| `VLRSUBST` | Vlr. substituição | F |  |
| `CODTRIB` | Tributação | I | Veja opções na seção OPÇÕES |
| `CODEXEC` | Executante | I |  |
| `ATUALESTOQUE` | Atualiza estoque | I |  |
| `DTVIGOR` | Última Dt. Vigor | D |  |
| `VLRSUGERIDO` | Vlr. Sugerido | F |  |
| `CODCFO` | CFOP | I |  |
| `CODOBSPADRAO` | Obs Padrão | I |  |
| `CUSTO` | Custo | F |  |
| `FATURAR` | Faturar | S | Veja opções na seção OPÇÕES |
| `M3` | Metro Cúbico | F |  |
| `NUTAB` | Tabela | I |  |
| `OBSERVACAO` | Observação | S |  |
| `PENDENTE` | Pendente | S | Veja opções na seção OPÇÕES |
| `QTDENTREGUE` | Qtd. entregue | F |  |
| `RESERVA` | Reserva | S |  |
| `PERCREDVLRIPI` | % Redução de Vlr. IPI | F |  |
| `STATUSNOTA` | Status da Nota | S |  |
| `USOPROD` | Uso do Produto | S | Veja opções na seção OPÇÕES |
| `VLRCUS` | Vlr. custos | F |  |
| `VLRDESC` | Vlr. desconto | F |  |
| `VLRDESCMOE` | Vlr. Desc. Moeda | F |  |
| `VLRDESCBONIF` | Bonificação | F |  |
| `VLRREPRED` | Vlr. redução | F |  |
| `VLRTOTLIQ` | Total líq. | F |  |
| `VLRTOTLIQMOE` | Total líq. Moeda | F |  |
| `VLRUNITLIQ` | Preço líq. | F |  |
| `VLRUNITMOE` | Vlr. Unit. Moeda | F |  |
| `VLRUNITLIQMOE` | Preço Líq. Moeda | F |  |
| `ALIQICMSRED` | Alíq. ICMS Reduzida | F |  |
| `CODMOTDESONERAST` | Cód. Mot. Desoneração do ICMS ST | I | Veja opções na seção OPÇÕES |
| `CODPARCEXEC` | Cód. Parceiro Exec | I |  |
| `BASESUBSTSEMRED` | Base ST S/Redução | F |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Dt. Alteração | H |  |
| `SOLCOMPRA` | Solic. compra | S | Veja opções na seção OPÇÕES |
| `CODTRIBISS` | Cód. trib. ISS | I |  |
| `CODCFPS` | Cód. CFPS | I |  |
| `ALIQISS` | Alíq. ISS | F |  |
| `ATUALESTTERC` | Estoque terc. | S |  |
| `TERCEIROS` | Terceiros | S | Veja opções na seção OPÇÕES |
| `PERCDESCBONIF` | % desc. bonif. | F |  |
| `ENDIMAGEM` | End. imagem | S |  |
| `ALTURA` | Altura | F |  |
| `LARGURA` | Largura | F |  |
| `ESPESSURA` | Espessura | F |  |
| `CODCAV` | Cód. cavalete | I |  |
| `CODPROC` | Cód. processo | I |  |
| `QTDPECA` | Qtd. peça | F |  |
| `PRECOBASE` | Preço base | F |  |
| `VLRACRESCDESC` | Vlr. acresc./desc. | F |  |
| `VLRRETENCAO` | Vlr. retenção | F |  |
| `CSTIPI` | C.S.T IPI | I | Veja opções na seção OPÇÕES |
| `CODENQIPI` | Cód. Enq. Legal IPI | I |  |
| `PERCCOM` | % comissão | F |  |
| `VLRCOM` | Vlr. comissão | F |  |
| `ALTPRECO` | Alt. Preço Igual | S | Veja opções na seção OPÇÕES |
| `QTDFIXADA` | Qtd. fixada | F |  |
| `PERCCOMGER` | % comiss. Gerente | F |  |
| `VLRCOMGER` | Comiss. gerente | F |  |
| `QTDWMS` | Qtd. WMS | F |  |
| `BASICMMOD` | Mod. Base ICMS | I |  |
| `BASICMSTMOD` | Mod. Base ICMS ST | I |  |
| `CODPROMO` | Cód. promoção | I |  |
| `QTDFAT` | Qtd. faturada | F |  |
| `VLRPROMO` | Vlr. Promoção | F |  |
| `BASESTUFDEST` | Base ST UF Destino | F |  |
| `QTDVOL` | Base Cálc. Amostragem | I |  |
| `VLRLIQPROM` | Vlr. liq. promoção | F |  |
| `ALIQSTFCPSTANT` | Alíquota da ST de oper. ant. | F |  |
| `ORIGEMBUSCA` | Origem da busca | S | Veja opções na seção OPÇÕES |
| `PRODUTOPESQUISADO` | Produto pesquisado | I |  |
| `ALIQSTEXTRANOTA` | Alíquota ST Extra Nota | F |  |
| `BASESTEXTRANOTA` | Base ST Extra Nota | F |  |
| `PERCDESCFORNECEDOR` | % Desconto Fornecedor | F |  |
| `TIPENTREGA` | Tipo entrega | S | Veja opções na seção OPÇÕES |
| `QTDTRIBEXPORT` | Qtd. tributação para exportação | F |  |
| `PERCPUREZA` | % Pureza | F |  |
| `CODDOCARRECAD` | Cód. Mod. Documento de arrecadação | I | Veja opções na seção OPÇÕES |
| `NUMDOCARRECAD` | Número Documento de arrecadação | S |  |
| `TIPOSEPARACAO` | Tipo de separação | S | Veja opções na seção OPÇÕES |
| `PERCGERMIN` | % Germinação | F |  |
| `VLRICMSUFDEST` | Vlr. ICMS UF Destino | F |  |
| `CODESPECST` | Código Especificador ST | I |  |
| `VLRSUBSTUNITORIG` | Vlr. ST unitário do pedido de origem | F |  |
| `CODLOCALTERC` | Local terceiros | I |  |
| `GERAPRODUCAO` | Necessidade de Produção | S | Veja opções na seção OPÇÕES |
| `NUMEROOS` | Número OS Gub. | I |  |
| `NUFOP` | Finalidade da Operação | I |  |
| `PRECOBASEQTD` | Preço base qtd. | F |  |
| `BASESTANT` | Base ST ant. | F |  |
| `CODVOLPARC` | Cód. Volume Parceiro | S |  |
| `GRUPOTRANSG` | Grupo transg. | I |  |
| `IDALIQICMS` | Cód. Alíq. ICMS | I |  |
| `VLRUNITLOC` | Vlr. Unit. Locação | F |  |
| `PRODUTONFE` | Produto para NF-e | S |  |
| `VLRICMSDIFERIDO` | Vlr. ICMS Diferido | F |  |
| `VLRPTOPUREZA` | Vlr.Ponto Pureza | F |  |
| `IDALIQICMSDIFICMS` | Cód. Alíq. Dif. ICMS | I |  |
| `GTINNFE` | GTINNFE | S |  |
| `GTINTRIBNFE` | GTINTRIBNFE | S |  |
| `STATUSLOTE` | Status do Lote | S | Veja opções na seção OPÇÕES |
| `NUPROMOCAO` | Nro. Promoção | I |  |
| `CODANTECIPST` | Cód.Antecipação ST | S | Veja opções na seção OPÇÕES |
| `NUMCONTRATO` | Contrato | I |  |
| `DTINICIO` | Dt.Prev.Entrega | D |  |
| `PERCDESCPROM` | % desc. promoção | F |  |
| `VLRUNITDOLAR` | Vlr.Unitário em Dólar | F |  |
| `BASEISS` | Base do ISS | F |  |
| `VLRISS` | Vlr. ISS | F |  |
| `VARIACAOFCP` | Variação da Fórmula | I |  |
| `VLRTROCA` | Vlr. Troca | F |  |
| `VLRSTEXTRANOTA` | Valor ST Extra Nota | F |  |
| `BASEICMSSTFRETE` | Base do ICMS/ST do Frete | F |  |
| `PERCDESCDIGITADO` | % desc. digitado | F |  |
| `ICMSSTFRETE` | Vlr. ICMS/ST sobre o frete | F |  |
| `PERCDESCTGFDES` | % desc. promoção | F |  |
| `VLRDESCDIGITADO` | Vlr. desc. digitado | F |  |
| `NUMPEDIDO2` | Número Pedido | S |  |
| `SEQPEDIDO2` | Seq. no Pedido | S |  |
| `CODMOTDESONERAICMS` | Cód.Mot.Desoneração ICMS | I | Veja opções na seção OPÇÕES |
| `PERCDESCBASE` | Desc. p/ Preço Base | F |  |
| `VLRSUBSTANT` | Vlr. do ICMS da  ST da oper. ant. | F |  |
| `BASESUBSTITANT` | Base de Cálc. da ST de oper. ant. | F |  |
| `VLRICMSANT` | Vlr ICMS destacado da oper. própria de oper. ant. | F |  |
| `ORIGPROD` | Origem do Produto | S | Veja opções na seção OPÇÕES |
| `CODTPA` | Tipo Atendimento | I |  |
| `CSOSN` | Cód. situação op. Simples nacional (CSON) | I | Veja opções na seção OPÇÕES |
| `NRSERIERESERVA` | Nro série | S |  |
| `QTDUNIDPAD` | Qtd. unid. padrão | F |  |
| `VLRUNIDPAD` | Vlr. unid. padrão | F |  |
| `MARCA` | Marca | S |  |
| `AD_NUTABORIG` | NUTABORIG | I |  |
| `CODIGONFCOM` | Cod. Item NFCom | S |  |
| `NCM` | NCM | S |  |
| `AD_VLRTAB` | VLRTAB | F |  |
| `INDDEVOLUCAONFCOM` | Indicador de devolução | S | Veja opções na seção OPÇÕES |
| `PESOBRUTO` | Peso bruto | F |  |
| `AD_COMISSAOEX` | Comissao Vend ite | F |  |
| `PESOLIQ` | Peso líq. | F |  |
| `BASESUBSTITUNITORIG` | Base ST unitária do pedido de origem | F |  |
| `AD_TIPMOV` | Tipo Movimento | S |  |
| `SEQUENCIAFISCAL` | Sequência Fiscal | I |  |
| `AD_CHKSTATUS` | Status | S |  |
| `CODAGREGACAO` | Cód. de Agregação | S |  |
| `AD_CHKMOTIVO` | MOTIVO | S | Veja opções na seção OPÇÕES |
| `INDESCALA` | Indicador de Escala Relevante | S | Veja opções na seção OPÇÕES |
| `AD_CHKTIPO` | TIPO | S |  |
| `AD_MARCA_ITEM` | Marca Produto | S |  |
| `CNPJFABRICANTE` | CNPJ do Fabricante da Mercadoria | S |  |
| `CODBENEFNAUF` | Cód. de Benefício Fiscal na UF | S |  |
| `BASESTFCPINTANT` | Base ST FCP Interno Anterior | F |  |
| `PERCSTFCPINTANT` | % ST FCP Interno Anterior | F |  |
| `VLRSTFCPINTANT` | Vlr. ST FCP Interno Anterior | F |  |
| `AD_SALDO` | Qtd. Perda | F |  |
| `VLRTOTLIQREF` | Vlr. Tot.Líq. Desejado | F |  |
| `VLRVENDAPROMO` | Vlr. Venda Promoção | F |  |
| `AD_TOTDESC` | Total com desconto | F |  |
| `VLRREPREDSEMDESC` | Vlr. redução sem desconto | F |  |
| `AD_RESULCONTAB` | Re. Contab | F |  |
| `AD_RESULFIN` | Re Finan | F |  |
| `AD_PERCOM` | % Com | F |  |
| `BASECALCSTEXTRANOTA` | Base de Cálculo ST Extra Nota | F |  |
| `REDBASEST` | Redução da Base ST | F |  |
| `MARGLUCRO` | Margem de Lucro | F |  |
| `AD_PERCONTAB` | %Contabil | F |  |
| `AD_SDABERTO` | Saldo total aberto | F |  |
| `IDALIQICMSAT` | Cod. Aliq. ICMS AT | I |  |
| `BASEICMSAT` | Base de ICMS AT | F |  |
| `ALIQICMSAT` | Alíquota ICMS AT | F |  |
| `ALIQINTERICMSAT` | Alíquota ICMS Interna AT | F |  |
| `VLRICMSAT` | Valor de ICMS AT | F |  |
| `ALIQFETHAB` | Alíquota FETHAB | F |  |
| `PERCUSAQUDECPE` | Percentual/Coeficiente sobre Custo Aquisição - PE | F |  |
| `VLRREPREDST` | Vlr. redução ST | F |  |
| `VLRFETHAB` | Vlr. FETHAB | F |  |
| `VLRCUSAQUDECPE` | Valor Custo Aquisição - PE | F |  |
| `AD_CODCENCUS` | Centro de Resultado | I |  |
| `PERCUSAQUDECPEEST` | Percentual/Coeficiente sobre Custo Aquisição - PE - Origem Estrangeira | F |  |
| `CODSIT08EFD` | Considerar a situação do documento '08' nos EFDs | S | Veja opções na seção OPÇÕES |
| `TIPUTILCOM` | Tipo de Utilização | I | Veja opções na seção OPÇÕES |
| `UNIDADE` | Unidade do Parceiro | S |  |
| `CODFCI` | Código da FCI | S |  |
| `AD_ULTVLR` | Último Valor | F |  |
| `AD_PRELIQ` | Preço Liq, | F |  |
| `IDALIQISS` | Código Alíquota ISS | I |  |
| `AD_PERDESC` | % desc. | F |  |
| `CODIPI` | Código do IPI | I |  |
| `INDREPDES` | Indicador Repasse Desoneração | S | Veja opções na seção OPÇÕES |
| `AD_NCFDEV` | Cód Defeito | I |  |
| `AD_DESCMAX` | Desconto Máximo | F |  |
| `CODEND` | Endereço WMS | I |  |
| `AD_QTDA` | Quantidade A | I |  |
| `AD_QTDB` | Quantidade B | I |  |
| `AD_QTDC` | Quantidade C | I |  |
| `AD_EXCLUIR` | Excluir | I |  |
| `AD_NUMCAD` | NUM CAD | I |  |
| `AD_SEQ` | SEQ | I |  |
| `AD_ESTOQ` | Estoq. | F |  |
| `AD_TIPCOL` | Tip Colab | I |  |
| `AD_PORCST` | %ST | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo STATUSPROC (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| A | Em Andamento |
| C | Cancelado |
| C2 | Cancelando |
| F | Finalizado |
| P | Em Planejamento |
| P2 | Planejado |
| R | Criado |
| S | Suspenso |
| S2 | Suspendendo |

### Opções para campo CODTRIB (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Tributada integralmente |
| 02 | 02-Tributação monofásica própria sobre combustíveis |
| 10 | 10-Tributada e c/cobrança por substituição |
| 15 | 15-Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis |
| 20 | 20-Com redução de base de cálculo |
| 30 | 30-Isenta e não tribut.e c/cobrança por subst. |
| 40 | 40-Isenta |
| 41 | 41-Não tributada |
| 50 | 50-Suspensão |
| 51 | 51-Diferimento |
| 53 | 53-Tributação monofásica sobre combustíveis com recolhimento diferido |
| 60 | 60-ICMS cobrado anteriormente por substituição |
| 61 | 61-Tributação monofásica sobre combustíveis cobrada anteriormente |
| 70 | 70-Com redução de base e c/cobrança por subst. |
| 90 | 90-Outras |

### Opções para campo FATURAR (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PENDENTE (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USOPROD (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| B | Brinde |
| C | Consumo |
| D | Revenda (por fórmula) |
| E | Embalagem |
| F | Brinde (NF) |
| I | Imobilizado |
| M | Matéria prima |
| O | Outros insumos |
| P | Em Processo |
| R | Revenda |
| S | Serviço |
| T | Terceiros |
| V | Venda (fabricação própria) |
| 1 | Subproduto |
| 2 | Prod.Intermediário |
| 4 | Demonstração |

### Opções para campo CODMOTDESONERAST (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 12 | Fomento agropecuário |
| 3 | Uso na agropecuária |
| 9 | Outros |

### Opções para campo SOLCOMPRA (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TERCEIROS (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CSTIPI (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Entrada c/Recuperação de Crédito |
| -1 | (-1)-Não sujeita ao IPI |
| 1 | 01-Entrada c/Alíquota zero |
| 2 | 02-Entrada Isenta |
| 3 | 03-Entrada Não Tributada |
| 4 | 04-Entrada Imune |
| 49 | 49-Outras Entradas |
| 5 | 05-Entrada c/Suspensão |
| 50 | 50-Saída c/Recuperação de Crédito |
| 51 | 51-Saída c/Alíquota zero |
| 52 | 52-Saída Isenta |
| 53 | 53-Saída Não Tributada |
| 54 | 54-Saída Imune |
| 55 | 55-Saída c/Suspensão |
| 99 | 99-Outras Saídas |

### Opções para campo ALTPRECO (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| B | Atualiza menor |
| M | Atualiza maior |
| N | Não Atualiza |

### Opções para campo ORIGEMBUSCA (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| A | Produto alternativo |
| G | Busca Geral |
| S | Produto sugerido |

### Opções para campo TIPENTREGA (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| B | Retirar no estoque |
| C | Retirar no caixa |
| E | Encomenda |

### Opções para campo CODDOCARRECAD (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 0 | Documento Estadual de Arrecadação |
| 1 | GNRE |

### Opções para campo TIPOSEPARACAO (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| N | Não separa |
| S | Separa na mesma empresa |

### Opções para campo GERAPRODUCAO (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSLOTE (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| A | Aguardando Aprovação |
| N | Nenhum |
| P | Aprovado |
| Q | Quarentena |
| R | Reprovado |

### Opções para campo CODANTECIPST (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| A | A-ST informada pelo substituto/substituído que não incorra em nenhuma das situações anteriores |
| N | N-(Não Usa) Operação não envolve ST |
| 1 | 1-Pgto de ST efetuado pelo destinatário quando não efetuado ou efetuado a menor pelo substituto |
| 2 | 2-Antecip. tribut. efetuada pelo destinatário apenas como complemento do diferencial de alíquota |
| 3 | 3-Antecip. tribut. com MVA efetuada pelo destinatário sem encerrar a fase de tributação |
| 4 | 4-Antecip. tribut. com MVA efetuada pelo destinatário encerrando a fase de tributação |
| 5 | 5-Substituição tributária interna motivada por regime especial de tributação |
| 6 | 6-ICMS pago na importação |

### Opções para campo CODMOTDESONERAICMS (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 1 | Táxi |
| 16 | Olimpíadas Rio 2016 |
| 2 | Deficiente Físico |
| 3 | Produtor Agropecuário |
| 4 | Frotista/Locadora |
| 5 | Diplomático/Consular |
| 6 | Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio |
| 7 | SUFRAMA |
| 8 | Venda a Órgãos Públicos |
| 9 | Outros |
| 90 | Solicitado pelo Fisco |

### Opções para campo ORIGPROD (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 |
| 1 | 1-Estrangeira, importação direta, exceto a indicada no código 6 |
| 2 | 2-Estrangeira, adquirida no mercado interno, exceto a indicada no código 7 |
| 3 | 3-Nacional, mercadoria ou bem com conteúdo de importação superior a 40% e inferior ou igual a 70% |
| 4 | 4-Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos |
| 5 | 5-Nacional, mercadoria ou bem com conteúdo de importação inferior ou igual a 40% |
| 6 | 6-Estrangeira, importação direta, sem similar nacional, constante em lista da CAMEX |
| 7 | 7-Estrangeira, adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX |
| 8 | 8-Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% |

### Opções para campo CSOSN (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 101 | 101-Tributada pelo Simples Nacional com permissão de crédito |
| 102 | 102-Tributada pelo Simples Nacional sem permissão de crédito |
| 103 | 103-Isenção do ICMS no Simples Nacional para faixa de receita bruta |
| 201 | 201-Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por ST |
| 202 | 202-Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por ST |
| 203 | 203-Isenção do ICMS no Simples Nacional para faixa de receita bruta e com cobrança do ICMS por ST |
| 300 | 300-Imune |
| 400 | 400-Não tributada pelo Simples Nacional |
| 500 | 500-ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação |
| 900 | 900-Outros |

### Opções para campo INDDEVOLUCAONFCOM (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AD_CHKMOTIVO (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 1 | 01 - QUEBRA |
| 10 | 10 - RETRAÇÃO |
| 11 | 11 - OUTROS |
| 12 | 12 - DEFEITO FURAÇÃO PARAFUSO CX |
| 13 | 13 - DEFEITO FURO POÇO |
| 14 | 14 - CLIENTE SE RECUSOU A RECEBER |
| 15 | 15 - FURO DA VÁLVULA CUBA |
| 16 | 16 - Mau Funcionamento |
| 17 | 17 - Trinca do pé |
| 18 | 18 - RACHO NA ROLHA |
| 19 | 19 - ENCAIXE TAMPA CAIXA IRIS |
| 2 | 02 - FALTA |
| 3 | 03 - PÉ QUEBRADO |
| 4 | 04 - TRINCA |
| 5 | 05 - PEÇA SUJA |
| 6 | 06 - LANÇAMENTO DIVERGENTE |
| 7 | 07 - DEFORMAÇÃO FUNDIÇÃO |
| 8 | 08 - FALTA DE ACABAMENTO |
| 9 | 09 - SUJEIRA NO ESMALTE |

### Opções para campo INDESCALA (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| N | Produzido em Escala NÃO Relevante |
| null | Não se aplica |
| S | Produzido em Escala Relevante |

### Opções para campo CODSIT08EFD (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPUTILCOM (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Telefonia |
| 2 | 2 - Comunicação de dados |
| 3 | 3 - TV por Assinatura |
| 4 | 4 - Provimento de acesso à Internet |
| 5 | 5 - Multimídia |
| 6 | 6 - Outros |
| 7 | 7 - Vários |

### Opções para campo INDREPDES (Tabela: TGFITE)
| Valor | Descrição |
|-------|-----------|
| 0 | Valor do ICMS desonerado não deduz do valor do item  / total da NF-e. |
| 1 | Valor do ICMS desonerado deduz do valor do item / total da NF-e |


## Tabela: TGFITE_EXC
### Descrição: Itens de Notas Excluídas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `VLRDESCPARCERIA` | Valor cupom desconto parceria | F |  |
| `IDDESCPARCERIA` | Id de desconto da parceria | F |  |
| `NUTAB` | NUTAB | I |  |
| `NUNOTA` | NUNOTA | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `CODEMP` | CODEMP | I |  |
| `CODPROD` | Produto | I |  |
| `CODLOCALORIG` | Local de Origem | I |  |
| `CONTROLE` | Controle | S |  |
| `USOPROD` | USOPROD | S |  |
| `CODCFO` | CODCFO | I |  |
| `QTDNEG` | Qtd. Negociada | F |  |
| `QTDENTREGUE` | QTDENTREGUE | F |  |
| `QTDCONFERIDA` | QTDCONFERIDA | F |  |
| `VLRUNIT` | Vlr. Unitário | F |  |
| `VLRTOT` | Vlr. Total | F |  |
| `VLRCUS` | Vlr. Custo | F |  |
| `BASEIPI` | BASEIPI | F |  |
| `VLRIPI` | VLRIPI | F |  |
| `BASEICMS` | BASEICMS | F |  |
| `VLRICMS` | VLRICMS | F |  |
| `VLRDESC` | VLRDESC | F |  |
| `BASESUBSTIT` | BASESUBSTIT | F |  |
| `VLRSUBST` | VLRSUBST | F |  |
| `ALIQICMS` | ALIQICMS | F |  |
| `ALIQIPI` | ALIQIPI | F |  |
| `PENDENTE` | PENDENTE | S |  |
| `CODVOL` | Volume | S |  |
| `CODTRIB` | CODTRIB | I |  |
| `ATUALESTOQUE` | ATUALESTOQUE | I |  |
| `OBSERVACAO` | OBSERVACAO | S |  |
| `RESERVA` | RESERVA | S |  |
| `STATUSNOTA` | STATUSNOTA | S |  |
| `CODOBSPADRAO` | CODOBSPADRAO | I |  |
| `CODVEND` | CODVEND | I |  |
| `CODEXEC` | CODEXEC | I |  |
| `FATURAR` | FATURAR | S |  |
| `NT_USERNAME` | NT_USERNAME | S |  |
| `HOSTNAME` | HOSTNAME | S |  |
| `DHEXCLUSAO` | Dt. Exclusão | H |  |
| `USUARIO` | USUARIO | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `VLRREPRED` | VLRREPRED | F |  |
| `VLRDESCBONIF` | VLRDESCBONIF | F |  |
| `PERCDESC` | PERCDESC | F |  |
| `PROGRAMA` | PROGRAMA | S |  |
| `CODCFPS` | CODCFPS | I |  |
| `PRODUTONFE` | PRODUTONFE | S |  |
| `GTINNFE` | GTINNFE | S |  |
| `GTINTRIBNFE` | GTINTRIBNFE | S |  |
| `CODESPECST` | Código Especificador ST | I |  |
| `CODAGREGACAO` | Cód. de Agregação | S |  |
| `INDESCALA` | Indicador de Escala Relevante | S | Veja opções na seção OPÇÕES |
| `CNPJFABRICANTE` | CNPJ do Fabricante da Mercadoria | S |  |
| `CODBENEFNAUF` | Cód. de Benefício Fiscal na UF | S |  |
| `BASESTFCPINTANT` | Base ST FCP Interno Anterior | F |  |
| `PERCSTFCPINTANT` | % ST FCP Interno Anterior | F |  |
| `VLRSTFCPINTANT` | Vlr. ST FCP Interno Anterior | F |  |
| `BASECALCSTEXTRANOTA` | Base de Cálculo ST Extra Nota | F |  |
| `REDBASEST` | Redução da Base ST | F |  |
| `MARGLUCRO` | Margem de Lucro | F |  |
| `CODMOTDESONERAST` | Cód. Mot. Desoneração do ICMS ST | I |  |
| `QTDTRIBEXPORT` | Qtd. Tributação para Exportação | F |  |
| `ALIQSTFCPSTANT` | Alíquota ST/FCP ST Ant. | F |  |
| `AD_CODCENCUS` | Centro de Resultado | I |  |
| `PERCUSAQUDECPE` | Percentual/Coeficiente sobre Custo Aquisição - PE | F |  |
| `VLRCUSAQUDECPE` | Valor Custo Aquisição - PE | F |  |
| `TIPUTILCOM` | Tipo de Utilização | I | Veja opções na seção OPÇÕES |
| `CODFCI` | Código da FCI | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo INDESCALA (Tabela: TGFITE_EXC)
| Valor | Descrição |
|-------|-----------|
| N | Produzido em Escala NÃO Relevante |
| null | Não se aplica |
| S | Produzido em Escala Relevante |

### Opções para campo TIPUTILCOM (Tabela: TGFITE_EXC)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Telefonia |
| 2 | 2 - Comunicação de dados |
| 3 | 3 - TV por Assinatura |
| 4 | 4 - Provimento de acesso à Internet |
| 5 | 5 - Multimídia |
| 6 | 6 - Outros |


## Tabela: TGFITR
### Descrição: Itens Regra

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DESCINSTSECINI` | Desc. Instância Secundária Inicial | S |  |
| `DESCDINSTPRINCFIN` | Desc. Instância Principal Final | S |  |
| `DESCINSTPRINC` | Desc. Instância Principal | S |  |
| `CODREGRA` | Código Regra | I |  |
| `DESCINSTSECFIN` | Desc. Instância Secundária Final | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `CODINSTPRINC` | Cód. Instância Principal | I |  |
| `CODINSTPRINCFIN` | Cód. Instância Principal Final | I |  |
| `CODINSTSECINI` | Cód. Instância Secundária Inicial | I |  |
| `CODINSTSECFIN` | Cód. Instância Secundária Final | I |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Data Alteração | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFITR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFIXN
### Descrição: Importação de XML de Notas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `DIASEMISSAOCALC` | Dias Emissão Doc | S |  |
| `CODEMP` | Código da Empresa | I |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `CODVEND` | Cód. Comprador | I |  |
| `SITUACAOMDE` | Situação  da manifestação | S | Veja opções na seção OPÇÕES |
| `IMPORTADOMDE` | Importado pelo DF-e | S | Veja opções na seção OPÇÕES |
| `SITUACAONFE` | Situação NF-e | S | Veja opções na seção OPÇÕES |
| `TEMXML` | Possui o XML | S | Veja opções na seção OPÇÕES |
| `VLRNOTA` | Valor da Nota | F |  |
| `DHEMISS` | Dh. Emissão | H |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `CONFIG` | CONFIG | C |  |
| `DHPROCESS` | Dh. Processamento | H |  |
| `XML` | XML | C |  |
| `CODUSUPROC` | Usuário Processamento | I |  |
| `CODUSUIMP` | Usuário Importação | I |  |
| `DHIMPORT` | Dh. Importação | H |  |
| `NUMNOTA` | Nro Nota | I |  |
| `NUARQUIVO` | Código | I |  |
| `CHAVEACESSO` | Chave Acesso | S |  |
| `DETALHESIMPORTACAO` | Detalhes | S |  |
| `NOMEARQUIVO` | Arquivo | S |  |
| `STATUS` | Status | I | Veja opções na seção OPÇÕES |
| `STATUSWMS` | Status WMS | I | Veja opções na seção OPÇÕES |
| `NUNOTA` | Nro Único da Nota | I |  |
| `NUFIN` | Nro. Financeiro | I |  |
| `TIPIMPCTE` | Tipo de Importação CT-e | S | Veja opções na seção OPÇÕES |
| `DTVENC` | Dt. Vencimento | D |  |
| `CODPARCCOLETACTE` | Parceiro Coleta CT-e | I |  |
| `CODPARCENTREGACTE` | Parceiro Entrega CT-e | I |  |
| `TIPONFE` | Tipo NF-e | S | Veja opções na seção OPÇÕES |
| `SITUACAOCTE` | Situação CT-e | S | Veja opções na seção OPÇÕES |
| `PAPELCTE` | Papel no CT-e | S | Veja opções na seção OPÇÕES |
| `ULTEVEDFE` | Último Evento DF-e | S |  |
| `OBSERVACAODFE` | Justificativa DF-e | S |  |
| `DOCSREF` | Docs Referenciados | C |  |
| `TIPOCTE` | Tipo CTe | S | Veja opções na seção OPÇÕES |
| `TOMADORCTE` | Tomador CT-e | S | Veja opções na seção OPÇÕES |
| `TIPOMANIFDFE` | Tipo Manifestação DF-e | I | Veja opções na seção OPÇÕES |
| `SERIEDOC` | Série Doc | I |  |
| `CODPARCDEST` | Cód. Parceiro Destinatário | I |  |
| `NATUREZAOPER` | Descrição Nat. Operação | S |  |
| `DTAUTORIZACAO` | Dh. Autorização | H |  |
| `PLACAVEIC` | Placa Veículo | S |  |
| `CNPJTRANSP` | Cnpj Transportadora | S |  |
| `CODPARCTRANSP` | Cód. Parceiro Transportadora | I |  |
| `CNPJPARC` | Cnpj Parceiro | S |  |
| `CNPJREMET` | Cnpj Remetente | S |  |
| `CODPARCREMET` | Cód. Parceiro Remetente | I |  |
| `CNPJDEST` | Cnpj Destinatário | S |  |
| `CNPJEXPED` | Cnpj Expedidor | S |  |
| `CODPARCEXPED` | Cód. Parceiro Expedidor | I |  |
| `CNPJRECEB` | Cnpj Recebedor | S |  |
| `CODPARCRECEB` | Cód. Parceiro Recebedor | I |  |
| `ENTSAINFE` | Entrada/Saida NF-e | S | Veja opções na seção OPÇÕES |
| `CFOPXML` | CFOP's XML | S |  |
| `DTCONFIRMACAO` | Dh. Confirmação | H |  |
| `XNOMEEMIT` | Nome do Emitente | S |  |
| `XNOMEDEST` | Nome do Destinatário | S |  |
| `XNOMETRANSP` | Nome da Transportadora | S |  |
| `XNOMETOMA` | Nome do Tomador | S |  |
| `NUMCOTACAO` | Nro. da Cotação | I |  |
| `DHPROCAG` | Dh. Proc Agenda | H |  |
| `CODCENCUS` | Código do Centro de Resultado | I |  |
| `CODNAT` | Cód. Natureza | I |  |
| `CODPROJ` | Projeto | I |  |
| `CODTIPVENDA` | Tipo de Negociação | I |  |
| `QTDPROCAG` | Qtd. Proc Adenda | I |  |
| `AD_TOPREF` | Tipo de operação(TOP) | S |  |
| `AD_PARC` | Parceiro Nota | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo SITUACAOMDE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| 0 | Sem Manifestação do Destinatário |
| 1 | Operação confirmada |
| 2 | Desconhecida |
| 3 | Operação não Realizada |
| 4 | Ciência |
| 5 | Aguardando Evento |
| 6 | Erro ao Registrar Evento |
| 7 | Prest. serv. em desacordo |

### Opções para campo IMPORTADOMDE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SITUACAONFE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| 1 | Uso autorizado |
| 2 | Uso denegado |
| 3 | NF-e cancelada |

### Opções para campo TEMXML (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPO (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| C | CT-e |
| N | NF-e |
| O | CT-e OS |

### Opções para campo STATUS (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| 0 | Pendente |
| 1 | Cancelado |
| 2 | Importado |
| 3 | Inválido |
| 4 | Com divergência |
| 5 | Confirmado |

### Opções para campo STATUSWMS (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| 0 | Pedido parcialmente cortado |
| 1 | Enviado totalmente |
| 2 | Enviado parcialmente |
| 3 | Não enviado |
| 4 | Não Controlado pelo WMS |
| 5 | Pedido totalmente cortado |

### Opções para campo TIPIMPCTE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| C | Cancelamento |
| D | Documento Anterior |
| E | Emissão Própria |
| T | Terceiros |

### Opções para campo TIPONFE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| A | NF-e Ajuste |
| B | NF-e Destinada a Transporte |
| C | NF-e Complementar Emissão Própria |
| D | Devolução de mercadoria |
| E | NF-e Devolução de Venda Emissão Própria |
| J | NF-e Ajuste Emissão Própria |
| L | NF-e Devolução de Compra Emissão Própria |
| N | NF-e Normal Compra |
| O | NF-e Complementar |
| P | NF-e Normal Compra Emissão Própria |
| V | NF-e Normal Venda Emissão Própria |

### Opções para campo SITUACAOCTE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| A | Uso autorizado |
| C | CT-e cancelado |
| D | Uso denegado |
| E | Uso EPEC |

### Opções para campo PAPELCTE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| C | Recebedor |
| D | Destinatário |
| E | Expedidor |
| null | Indefinido |
| R | Remetente |
| T | Tomador |

### Opções para campo TIPOCTE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| 0 | CT-e Normal |
| 1 | CT-e de Complemento de Valores |
| 2 | CT-e de Anulação |
| 3 | CT-e Substituto |

### Opções para campo TOMADORCTE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| A | Não se aplica |
| N | Não |
| S | Sim |

### Opções para campo TIPOMANIFDFE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| 1 | Ciência da operação |
| 2 | Confirmar operação |
| 3 | Desconhecer operação |
| 4 | Operação não realizada |
| 5 | Desacordo da prestação de serviço |

### Opções para campo ENTSAINFE (Tabela: TGFIXN)
| Valor | Descrição |
|-------|-----------|
| 0 | Entrada |
| 1 | Saída |


## Tabela: TGFLAY
### Descrição: Layout da Nota

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NULAYOUT` | Nro. Layout | I |  |
| `LAYOUT` | Layout | C |  |
| `DESCRICAO` | Descrição | S |  |
| `TIPMOV` | Tipo de movimento | S |  |
| `PADRAO` | Padrão | S | Veja opções na seção OPÇÕES |
| `MODULO` | MODULO | I |  |
| `USARCHECKOUTPROD` | Usar checkout de produtos | S | Veja opções na seção OPÇÕES |
| `TIPREC` | Tipo de recebimento | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo PADRAO (Tabela: TGFLAY)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USARCHECKOUTPROD (Tabela: TGFLAY)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFLIC
### Descrição: Liberação Cascata

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `EVENTO` | Evento | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Data Alteração | H |  |
| `ORDEM` | Ordem | I |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `VLRMIN` | Vlr.Mínimo | F |  |
| `VLRMAX` | Vlr.Máximo | F |  |
| `CODUSULIB` | Usuário Aprovação | I |  |
| `ENVIAREMAIL` | Enviar Notificação | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TGFLIC)
| Valor | Descrição |
|-------|-----------|
| U | Usuário |
| 1 | Grau 1 do CR |
| 2 | Grau 2 do CR |
| 3 | Grau 3 do CR |
| 4 | Grau 4 do CR |

### Opções para campo ENVIAREMAIL (Tabela: TGFLIC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFLNF
### Descrição: LoteNotaFiscalEletronica

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NULOTE` | Nro. Lote | I |  |
| `NUMRECEB` | Nro.Receb.Lote NF-e | S |  |
| `DHRECEB` | Dt.Receb.Lote NF-e | H |  |
| `OBSERVACAO` | Observação | S |  |
| `GUID` | Guid | S |  |
| `NUMLOTEPROVEDOR` | NUMLOTEPROVEDOR | I |  |

## Tabela: TGFLOC
### Descrição: Locais

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODLOCAL` | Cód. Local | I |  |
| `DESCRLOCAL` | Descrição | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `ANALITICO` | Analítico | S | Veja opções na seção OPÇÕES |
| `CODTAB` | Tabela de preço | I |  |
| `VLRCUS` | Valor de custo | F |  |
| `VLRVENDA` | Valor de venda | F |  |
| `INCSOBREIRF` | Incide sobre IRF | S | Veja opções na seção OPÇÕES |
| `CODLOCALPAI` | Local Pai | I |  |
| `GRAU` | Grau | I |  |
| `VALESTINDEP` | Val.Est.Independente | S | Veja opções na seção OPÇÕES |
| `DIASPRODUCAO` | Prazo de entrega (em dias) | I |  |
| `CAPACIDADEPRODUCAO` | Capacidade de Produção | F |  |
| `DOMINGO` | Domingo | S | Veja opções na seção OPÇÕES |
| `SEGUNDA` | Segunda | S | Veja opções na seção OPÇÕES |
| `TERCA` | Terça | S | Veja opções na seção OPÇÕES |
| `QUARTA` | Quarta | S | Veja opções na seção OPÇÕES |
| `QUINTA` | Quinta | S | Veja opções na seção OPÇÕES |
| `SEXTA` | Sexta | S | Veja opções na seção OPÇÕES |
| `SABADO` | Sábado | S | Veja opções na seção OPÇÕES |
| `CODPARC` | Cód. Parceiro | I |  |
| `ACEITANOVAPROD` | Aceita Novas Produções | S | Veja opções na seção OPÇÕES |
| `UTILIZAWMS` | Controlado pelo WMS | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANALITICO (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INCSOBREIRF (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALESTINDEP (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DOMINGO (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SEGUNDA (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TERCA (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo QUARTA (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo QUINTA (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SEXTA (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SABADO (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ACEITANOVAPROD (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZAWMS (Tabela: TGFLOC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFMAR
### Descrição: Marcas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Código | I |  |
| `DESCRICAO` | Descrição | S |  |

## Tabela: TGFMBC
### Descrição: Movimento Bancário

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPDV` | Cod. PDV | I |  |
| `SALDO` | Saldo | F |  |
| `NUCAIXA` | Núm. Caixa | I |  |
| `NUBCOCP` | Núm. Banco | I |  |
| `CODCTABCOCONTRA` | Cód. conta bancária | I |  |
| `ORIGMOV` | Tipo de Movimento | S | Veja opções na seção OPÇÕES |
| `NUMTRANSF` | Número | I |  |
| `DTLANC` | Dt. Lançamento | D |  |
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `NUMDOC` | Núm. Documento | I |  |
| `VLRLANC` | Vlr. Lançamento | F |  |
| `HISTORICO` | Histórico | S |  |
| `CODCTABCOINT` | Conta Origem | I |  |
| `CODLANC` | Lanç. Origem | I |  |
| `CODCTABCOINTDEST` | Conta Destino | I |  |
| `CODLANCDEST` | Lanç. Destino | I |  |
| `CONCILIADO` | Conciliado | S | Veja opções na seção OPÇÕES |
| `CONCILIADODEST` | Conciliado Destino | S | Veja opções na seção OPÇÕES |
| `VLRMOEDA` | Vlr. Moeda | F |  |
| `VLRLANC_DESTINO` | Vlr. Lanç. Destino | F |  |
| `RECDESP` | Receita/Despesa | I | Veja opções na seção OPÇÕES |
| `NUBCO` | Núm. Único Bancário | I |  |
| `DTINCLUSAO` | Dt. Inclusão | H |  |
| `DHTIPOPER` | Dh. Operação | H |  |
| `DTCONTAB` | Dt. Contabilização | H |  |
| `PREDATA` | Pré-Data | H |  |
| `DHCONCILIACAO` | Dh. Conciliação | H |  |
| `CODUSU` | Cód. Usuário | I |  |
| `CONTABILIZADO` | Contabilizado? | S | Veja opções na seção OPÇÕES |
| `TALAO` | Talão | I |  |
| `DTALTER` | Dt. Alteração | H |  |
| `VLRTROCO` | Vlr. Troco | F |  |
| `VLRCHEQUE` | Vlr. Cheque | F |  |
| `NROIMPORT` | Nro da importação | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo ORIGMOV (Tabela: TGFMBC)
| Valor | Descrição |
|-------|-----------|
| A | Aplicação |
| D | Depósito |
| F | Financeiro |
| R | Resgate |
| S | Saque |
| T | Transferência |

### Opções para campo CONCILIADO (Tabela: TGFMBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONCILIADODEST (Tabela: TGFMBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECDESP (Tabela: TGFMBC)
| Valor | Descrição |
|-------|-----------|
| -1 | Despesa |
| 1 | Receita |

### Opções para campo CONTABILIZADO (Tabela: TGFMBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFMDFE
### Descrição: MDF-e

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUVIAG` | Nro. Viagem | I |  |
| `SEQMDFE` | Sequência do manifesto | I |  |
| `NUMMDFE` | Nro. MDF-e | I |  |
| `STATUSMDFE` | Status MDF-e | S | Veja opções na seção OPÇÕES |
| `NUMALEATORIO` | Nro. Aleatório | I |  |
| `CHAVEMDFE` | Chave MDF-e | S |  |
| `NRORECIBO` | Nro. Recibo | S |  |
| `DHRECIBO` | Dt. e Hora do Recbto. | H |  |
| `DHEMISS` | Dt. e Hora da emissão | H |  |
| `TIPEMISS` | Tipo de emissão | S | Veja opções na seção OPÇÕES |
| `UFINICIAL` | UF de Coleta | I |  |
| `MUNINICIAL` | Municipio de Coleta | I |  |
| `UFFINAL` | UF de Descarregamento | I |  |
| `DHALTER` | Data de Alteração | H |  |
| `MUNFINAL` | Municipio de Descarregamento | I |  |
| `CODUSU` | CODUSU | I |  |
| `XML` | XML | C |  |
| `NULOTEMDFE` | Nro. Lote | I |  |
| `XMLPROTAUT` | XMLPROTAUT | C |  |
| `XMLENVCLI` | XMLENVCLI | C |  |
| `UNMED` | Unidade de Medida | S | Veja opções na seção OPÇÕES |
| `PESOBRUTOTOT` | Peso Bruto Total | F |  |
| `USAPESOBRUTONFE` | Considerar Peso Bruto Total para NF-e | S | Veja opções na seção OPÇÕES |
| `CODCIDENCERRAMENTO` | Cód. Cidade Encerramento | I |  |
| `CODPORTOEMBARQUE` | Cód. Porto Embarque | S |  |
| `CODPORTODESTINO` | Cód. Porto Destino | S |  |
| `QRCODE` | QRCODE | S |  |
| `CODPORTOTRANSBORDO` | Cód. Porto Transbordo | S |  |
| `TIPONAVEGACAO` | Tipo Navegação | I | Veja opções na seção OPÇÕES |
| `IRINNAVIO` | Nº IRIN | S |  |
| `TPCARGA` | Tipo de Carga | S | Veja opções na seção OPÇÕES |
| `DESCPROD` | Descrição do Produto | S |  |
| `EAN` | EAN | S |  |
| `NCM` | NCM | S |  |
| `CEPCAR` | CEP | S |  |
| `LATCAR` | Latitude | F |  |
| `LONGCAR` | Longitude | F |  |
| `CEPDESCAR` | CEP | S |  |
| `LATDESCAR` | Latitude | F |  |
| `LONDESGCAR` | Longitude | F |  |
| `INDCARREGPOST` | Indicativo de Carregamento Posterior | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo STATUSMDFE (Tabela: TGFMDFE)
| Valor | Descrição |
|-------|-----------|
| 0 | Não transmitido |
| 1 | Enviado |
| 2 | Aguardando autorização |
| 3 | Autorizado |
| 4 | Aguardando correção |
| 5 | Cancelado |
| 6 | Encerrado |
| 7 | Denegado |
| 8 | Com erro de validação |
| 9 | Enviado em contingência |

### Opções para campo TIPEMISS (Tabela: TGFMDFE)
| Valor | Descrição |
|-------|-----------|
| 1 | Normal |
| 2 | Contingência |

### Opções para campo UNMED (Tabela: TGFMDFE)
| Valor | Descrição |
|-------|-----------|
| 01 | KG |
| 02 | TON |

### Opções para campo USAPESOBRUTONFE (Tabela: TGFMDFE)
| Valor | Descrição |
|-------|-----------|
| N | Nao |
| S | Sim |

### Opções para campo TIPONAVEGACAO (Tabela: TGFMDFE)
| Valor | Descrição |
|-------|-----------|
| 0 | Interior |
| 1 | Cabotagem |

### Opções para campo TPCARGA (Tabela: TGFMDFE)
| Valor | Descrição |
|-------|-----------|
| 01 | Granel sólido |
| 02 | Granel líquido |
| 03 | Frigorificada |
| 04 | Conteinerizada |
| 05 | Carga Geral |
| 06 | Neogranel |
| 07 | Perigosa (granel sólido) |
| 08 | Perigosa (granel líquido) |
| 09 | Perigosa (carga frigorificada) |
| 10 | Perigosa (conteineirazada) |
| 11 | Perigosa (carga geral) |

### Opções para campo INDCARREGPOST (Tabela: TGFMDFE)
| Valor | Descrição |
|-------|-----------|
| N | Nao |
| S | Sim |


## Tabela: TGFMDFESEG
### Descrição: Seguro MDF-e

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUVIAG` | Nro. Viagem | I |  |
| `SEQMDFE` | Sequência do manifesto | I |  |
| `NUMAPOLICE` | Nro. Apólice | S |  |
| `CODPARCSEG` | Seguradora | I |  |
| `CODPARCRESPSEG` | Responsável do seguro | I |  |

## Tabela: TGFMET
### Descrição: Metas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODMETA` | CODMETA | I |  |
| `DTREF` | DTREF | H |  |
| `CODEMP` | CODEMP | I |  |
| `CODPROD` | CODPROD | I |  |
| `CODGRUPOPROD` | CODGRUPOPROD | I |  |
| `CODLOCAL` | CODLOCAL | I |  |
| `CODPROJ` | CODPROJ | I |  |
| `CODCENCUS` | Cód.Centro Resultado | I |  |
| `CODNAT` | Cód. Natureza | I |  |
| `CODREG` | CODREG | I |  |
| `CODGER` | CODGER | I |  |
| `CODVEND` | CODVEND | I |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `CODUF` | CODUF | I |  |
| `CODCID` | Cód. Cidade | I |  |
| `CODPAIS` | CODPAIS | I |  |
| `CODTIPPARC` | CODTIPPARC | I |  |
| `CONTROLE` | CONTROLE | S |  |
| `MARCA` | MARCA | S |  |
| `QTDPREV` | QTDPREV | F |  |
| `PREVREC` | PREVREC | F |  |
| `PREVDESP` | PREVDESP | F |  |
| `QTDREAL` | QTDREAL | F |  |
| `REALREC` | REALREC | F |  |
| `REALDESP` | REALDESP | F |  |
| `PERCENTUAL` | PERCENTUAL | F |  |
| `SUPLEMENTODESP` | SUPLEMENTODESP | F |  |
| `ANTECIPDESP` | ANTECIPDESP | F |  |
| `TRANSFDESP` | TRANSFDESP | F |  |
| `TRANSFSALDODESP` | TRANSFSALDODESP | F |  |
| `REDUCAODESP` | REDUCAODESP | F |  |
| `COMPROMISSODESP` | COMPROMISSODESP | F |  |
| `ANALITICO` | ANALITICO | S |  |
| `TIPOMSG` | TIPOMSG | S |  |
| `PERCAVISO` | PERCAVISO | F |  |
| `DIA` | DIA | I |  |
| `SEMANAMES` | SEMANAMES | I |  |
| `TOTALAUTINV` | TOTALAUTINV | F |  |
| `CODVOL` | CODVOL | S |  |

## Tabela: TGFMIX
### Descrição: Modelo de Importação de XML

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Empresa | I |  |
| `CODNATOP` | Natureza da Operação | S |  |
| `PESQCODNATOP` | Pesquisa da nat. da operação | S | Veja opções na seção OPÇÕES |
| `NUNOTA` | Modelo de notas e pedidos | I |  |
| `PADRAO` | Padrão | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo PESQCODNATOP (Tabela: TGFMIX)
| Valor | Descrição |
|-------|-----------|
| B | Começando com |
| C | Contendo |
| E | Igual |
| T | Terminando com |

### Opções para campo PADRAO (Tabela: TGFMIX)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFMME
### Descrição: Motorista MDF-e

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUVIAG` | Nro. Viagem | I |  |
| `CODPARC` | Motorista | I |  |

## Tabela: TGFMMS
### Descrição: GF Movimento Mensal Sintético

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DTAM` | Data ano e mês | H |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `CODGRUPOPROD` | Grupo Produtos | I |  |
| `CODEMP` | Empresa | I |  |
| `TIPMOV` | Tipo de Movimento | S |  |
| `MES` | Mês | I |  |
| `ANO` | Ano | I |  |
| `VLRMOV` | Valor do movimento | F |  |
| `GRUPO` | Grupo | S |  |

## Tabela: TGFMODTOP
### Descrição: Modelos da TOP

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DESCRICAO` | Descrição | S |  |
| `DHALTER` | Dh. alteração | D |  |
| `TIPMOV` | Tipo movimento | S |  |
| `MODELO` | Modelo | C |  |
| `NUMODTOP` | Nro. único | I |  |
| `HASH` | Hash | S |  |

## Tabela: TGFMON
### Descrição: GF Modelo para notas fiscais

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CAMINHO` | Caminho | S |  |
| `CODMODNF` | Modelo | I |  |
| `CAMINHOSW` | Caminho Rep. Arquivos | S |  |
| `NOME` | Nome | S |  |
| `TIPOIMPRESSORA` | Tipo de impressora | S | Veja opções na seção OPÇÕES |
| `NURFE` | Número do relatório modelo | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOIMPRESSORA (Tabela: TGFMON)
| Valor | Descrição |
|-------|-----------|
| 1 | ELEBRA/RIMA |
| 2 | EPSON |
| 3 | RIMA/ITAUTEC |
| 4 | ELGIN |
| 5 | OUTRAS |
| 6 | DESKJET |
| 7 | XEROX LASER |


## Tabela: TGFNAS
### Descrição: TGFNAS

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODMUNFIS` | Município Fiscal | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `CODNATOPER` | Natureza da Operação | S |  |
| `DESCRNATOPER` | Descrição | S |  |

## Tabela: TGFNAT
### Descrição: Natureza de Receitas e Despesas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODNAT` | Cód. Natureza | I |  |
| `DESCRNAT` | Descrição | S |  |
| `ATIVA` | Ativa | S | Veja opções na seção OPÇÕES |
| `ANALITICA` | Analítica | S | Veja opções na seção OPÇÕES |
| `INCRESULT` | Incide no resultado | S | Veja opções na seção OPÇÕES |
| `CODCTACTB` | Conta contábil | I |  |
| `CODCTACTB2` | Conta contábil 2 | I |  |
| `CODHISTCTB` | Cód. Histórico 1 | I |  |
| `CODHISTCTB2` | Cód. Histórico 2 | I |  |
| `GRUPOMKP` | Grupo MKP | S |  |
| `SUBGRUPOMKP` | Sub Grupo MKP | S |  |
| `DECVLR` | Decimal para Valor | I |  |
| `GRAU` | Grau | I |  |
| `CODNATPAI` | Cód. Natureza Pai | I |  |
| `CODCENCUS` | Cód.Centro Resultado | I |  |
| `FORMULA` | Fórmula | S |  |
| `CODSERVUNICO` | Serviço único faturamento | I |  |
| `CODGRUPONAT` | Grupo da Natureza | I |  |
| `TIPNAT` | Tipo de natureza | S | Veja opções na seção OPÇÕES |
| `CSTPIS` | Cód. Sit. Tribut. PIS | I | Veja opções na seção OPÇÕES |
| `CODCTACTBEFD` | Conta Contábil para EFD | I |  |
| `ALIQPIS` | Alíquota de PIS | F |  |
| `CSTCOFINS` | Cód. Sit. Tribut. COFINS | I | Veja opções na seção OPÇÕES |
| `ALIQCOFINS` | Alíquota de COFINS | F |  |
| `NATBCCRED` | Natureza da Base de Cálculo do Crédito de PIS/COFINS | S | Veja opções na seção OPÇÕES |
| `REGIMEEFD` | Regime (EFD PIS/COFINS) | S | Veja opções na seção OPÇÕES |
| `GERALCDPR` | Gera informações para o Livro Caixa Digital Produtor Rural | S | Veja opções na seção OPÇÕES |
| `NATEFDCONTM410M810` | Cod. Natureza (PIS/COFINS M410/M810) | I |  |
| `RECADIANTRURAL` | Receita de Adiantamentos para o Livro Caixa Digital Produtor Rural | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVA (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANALITICA (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INCRESULT (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPNAT (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| D | Despesa |
| R | Receita |

### Opções para campo CSTPIS (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Operação Tributável com Alíquota Básica |
| 02 | 02-Operação Tributável com Alíquota Diferenciada |
| 03 | 03-Operação Tributável com Alíquota por Unidade de Medida de Produto |
| 04 | 04-Operação Tributável Monofásica - Revenda a Alíquota Zero |
| 05 | 05-Operação Tributável por Substituição Tributária |
| 06 | 06-Operação Tributável a Alíquota Zero |
| 07 | 07-Operação Isenta da Contribuição |
| 08 | 08-Operação sem Incidência da Contribuição |
| 09 | 09-Operação com Suspensão da Contribuição |
| 49 | 49-Outras Operações de Saída |
| 50 | 50-Operação com Direito a Crédito - Vinc. Exclus. Receita Tributada Mercado Interno |
| 51 | 51-Operação com Direito a Crédito - Vinc. Exclus. Receita Não-Tributada Mercado Interno |
| 52 | 52-Operação com Direito a Crédito - Vinc. Exclus. a Receita de Exportação |
| 53 | 53-Operação com Direito a Crédito - Vinc. Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 54 | 54-Operação com Direito a Crédito - Vinc. Receitas Tributadas no Mercado Interno e de Exportação |
| 55 | 55-Operação com Direito a Crédito - Vinc. Receitas Não Tributadas no Mercado Interno e de Exportação |
| 56 | 56-Op. c/ Direito a Créd.-Vinc.Receitas Tributadas e Não-Tributadas no Mercado Int. e de Exportação |
| 60 | 60-Crédito Presumido - Oper. Aquis. Vinc. Exclus. Receita Tributada no Mercado Interno |
| 61 | 61-Crédito Presumido - Oper. Aquis. Vinc. Exclus. Receita Não Tributada no Mercado Interno |
| 62 | 62-Crédito Presumido - Oper. Aquis. Vinc. Exclus. Receita de Exportação |
| 63 | 63-Crédito Presumido - Oper. Aquis. Vinc. Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 64 | 64-Crédito Presumido - Oper. Aquis. Vinc. Receitas Tributadas no Mercado Interno e de Exportação |
| 65 | 65-Crédito Presumido - Oper. Aquis. Vinc. Receitas Não-Tributadas no Mercado Interno e de Exportação |
| 66 | 66-Créd. Presumido-Oper.Aquis.Vinc.Receitas Tributadas e Não-Tribut. no Mercado Int. e de Exportação |
| 67 | 67 - Crédito Presumido - Outras Operações |
| 70 | 70 - Operação de Aquisição sem Direito a Crédito |
| 71 | 71 - Operação de Aquisição com Isenção |
| 72 | 72 - Operação de Aquisição com Suspensão |
| 73 | 73 - Operação de Aquisição a Alíquota Zero |
| 74 | 74 - Operação de Aquisição sem Incidência da Contribuição |
| 75 | 75 - Operação de Aquisição por Substituição Tributária |
| 98 | 98 - Outras Operações de Entrada |
| 99 | 99-Outras Operações |

### Opções para campo CSTCOFINS (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Operação Tributável com Alíquota Básica |
| 02 | 02-Operação Tributável com Alíquota Diferenciada |
| 03 | 03-Operação Tributável com Alíquota por Unidade de Medida de Produto |
| 04 | 04-Operação Tributável Monofásica - Revenda a Alíquota Zero |
| 05 | 05-Operação Tributável por Substituição Tributária |
| 06 | 06-Operação Tributável a Alíquota Zero |
| 07 | 07-Operação Isenta da Contribuição |
| 08 | 08-Operação sem Incidência da Contribuição |
| 09 | 09-Operação com Suspensão da Contribuição |
| 49 | 49-Outras Operações de Saída |
| 50 | 50-Operação com Direito a Crédito - Vinc. Exclus. Receita Tributada Mercado Interno |
| 51 | 51-Operação com Direito a Crédito - Vinc. Exclus. Receita Não-Tributada Mercado Interno |
| 52 | 52-Operação com Direito a Crédito - Vinc. Exclus. a Receita de Exportação |
| 53 | 53-Operação com Direito a Crédito - Vinc. Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 54 | 54-Operação com Direito a Crédito - Vinc. Receitas Tributadas no Mercado Interno e de Exportação |
| 55 | 55-Operação com Direito a Crédito - Vinc. Receitas Não Tributadas no Mercado Interno e de Exportação |
| 56 | 56-Op. c/ Direito a Créd.-Vinc.Receitas Tributadas e Não-Tribut. no Mercado Interno e de Exportação |
| 60 | 60-Crédito Presumido - Oper. Aquis. Vinc. Exclus. Receita Tributada no Mercado Interno |
| 61 | 61-Crédito Presumido - Oper. Aquis. Vinc. Exclus. Receita Não Tributada no Mercado Interno |
| 62 | 62-Crédito Presumido - Oper. Aquis. Vinc. Exclus. Receita de Exportação |
| 63 | 63-Crédito Presumido - Oper. Aquis. Vinc. Receitas Tributadas e Não-Tributadas no Mercado Interno |
| 64 | 64-Crédito Presumido - Oper. Aquis. Vinc. Receitas Tributadas no Mercado Interno e de Exportação |
| 65 | 65-Crédito Presumido - Oper. Aquis. Vinc. Receitas Não-Tributadas no Mercado Interno e de Exportação |
| 66 | 66-Créd. Presumido-Oper.Aquis.Vinc.Receitas Tributadas e Não-Tribut. no Mercado Int. e de Exportação |
| 67 | 67 - Crédito Presumido - Outras Operações |
| 70 | 70 - Operação de Aquisição sem Direito a Crédito |
| 71 | 71 - Operação de Aquisição com Isenção |
| 72 | 72 - Operação de Aquisição com Suspensão |
| 73 | 73 - Operação de Aquisição a Alíquota Zero |
| 74 | 74 - Operação de Aquisição sem Incidência da Contribuição |
| 75 | 75 - Operação de Aquisição por Substituição Tributária |
| 98 | 98 - Outras Operações de Entrada |
| 99 | 99-Outras Operações |

### Opções para campo NATBCCRED (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Aquisição de bens para revenda |
| 02 | 02-Aquisição de bens utilizados como insumo |
| 03 | 03-Aquisição de serviços utilizados como insumo |
| 04 | 04-Energia elétrica e térmica, inclusive sob a forma de vapor |
| 05 | 05-Aluguéis de prédios |
| 06 | 06-Aluguéis de máquinas e equipamentos |
| 07 | 07-Armazenagem de mercadoria e frete na operação de venda |
| 08 | 08-Contraprestações de arrendamento mercantil |
| 09 | 09-Máq., equip. e outros bens incorporados ao ativo imobilizado(créd. sobre encargos de depreciação) |
| 10 | 10-Máq., equip. e outros bens incorporados ao ativo imobilizado(créd. c/ base no valor de aquisição) |
| 11 | 11-Amortização e Depreciação de edificações e benfeitorias em imóveis |
| 12 | 12-Devolução de Vendas Sujeitas à Incidência Não-Cumulativa |
| 13 | 13-Outras Operações com Direito a Crédito |
| 14 | 14-Atividade de Transporte de Cargas - Subcontratação |
| 15 | 15-Atividade Imobiliária - Custo Incorrido de Unidade Imobiliária |
| 16 | 16-Atividade Imobiliária - Custo Orçado de unidade não concluída |
| 17 | 17-Atividade Prest. Serv. de Limp., Conserv. e Manut. - V.T., V.R. ou V.A., fardamento ou uniforme |
| 18 | 18-Estoque de Abertura de Bens |

### Opções para campo REGIMEEFD (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| A | Regime de Caixa |
| B | Regime de Competência (Dt.Negociação) |
| C | Regime de Competência (Dt.Entrada/Saída) |

### Opções para campo GERALCDPR (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECADIANTRURAL (Tabela: TGFNAT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFNCE
### Descrição: Coleta e Entrega por Nota

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nota | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `TIPOTRANSP` | Tipo transporte | I | Veja opções na seção OPÇÕES |
| `CODPARC` | Cód. Parceiro | I |  |
| `CGC_CPF` | CNPJ/CPF | S |  |
| `INSCESTAD` | Insc. estadual | S |  |
| `CODMUNFIS` | Mun. domicilio fiscal | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TGFNCE)
| Valor | Descrição |
|-------|-----------|
| C | Coleta |
| E | Entrega |

### Opções para campo TIPOTRANSP (Tabela: TGFNCE)
| Valor | Descrição |
|-------|-----------|
| 0 | Rodoviário |
| 1 | Ferroviário |
| 2 | Aquaviário |
| 3 | Dutoviário |
| 4 | Aéreo |
| 5 | Rodo-Ferroviário |
| 9 | Outros |


## Tabela: TGFNCM
### Descrição: CODNCM

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODNCM` | NCM | S |  |
| `DSNCM` | Descrição | S |  |
| `DINIVIGENCIA` | Data Início Vigência | D |  |
| `DFIMVIGENCIA` | Data Fim Vigência | D |  |
| `CATEGORIA` | Categoria | S |  |
| `DSUNITRIBUTACAO` | Descrição Unidade de Tributação | S |  |
| `UNITRIBUTACAO` | Unidade de Tributação | S |  |
| `IPI` | IPI | S |  |

## Tabela: TGFNCT
### Descrição: Notas Conhecimento Transporte

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Único CT-e | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `NUMERO` | Nro. Doc. | S |  |
| `DTEMISSAO` | Dh. Emissão | H |  |
| `SERIE` | Série | S |  |
| `VLRNOTA` | Valor da Nota | F |  |
| `CODMODDOC` | Modelo Documento | I |  |
| `BASEICMS` | Base ICMS | F |  |
| `VLRICMS` | Valor ICMS | F |  |
| `BASEST` | Base Substit. | F |  |
| `VLRST` | Valor Substit. | F |  |
| `VLRTOTPROD` | Valor Total dos Produtos | F |  |
| `CFOP` | CFOP | I |  |
| `CHAVENFE` | Chave NF-e | S |  |
| `DESCRDOC` | Descrição | S |  |
| `SEGCODBAR` | Segundo Código de Barras | S |  |
| `PESOB` | Peso Bruto | F |  |
| `PESOL` | Peso Líquido | F |  |

## Tabela: TGFNCTE
### Descrição: Arquivos XML de CTe

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Único da Nota | I |  |
| `CHAVECTE` | Chave CT-e | S |  |
| `XML` | XML | C |  |
| `XMLPROTAUTCTE` | XMLPROTAUTCTE | C |  |
| `XMLENVCLI` | XMLENVCLI | C |  |
| `XMLCANC` | XMLCANC | C |  |
| `XMLCANCPROTAUT` | XMLCANCPROTAUT | C |  |
| `XMLCANCENVCLI` | XMLCANCENVCLI | C |  |
| `XMLENVCARTA` | XMLENVCARTA | C |  |
| `XMLENVCARTROTAUT` | XMLENVCARTROTAUT | C |  |
| `XMLENVCARTENVCLI` | XMLENVCARTENVCLI | C |  |
| `QRCODE` | QRCODE | S |  |
| `XMLENVEPEC` | XMLENVEPEC | C |  |
| `XMLPROTAUTEPEC` | XMLPROTAUTEPEC | C |  |
| `XMLPROTCANC` | XMLPROTCANC | C |  |
| `XMLENVCLICANC` | XMLENVCLICANC | C |  |

## Tabela: TGFNFE
### Descrição: Arquivos XML de NFe

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `XMLENVCARTA` | Xml Envio Carta de Correção | C |  |
| `NUNOTA` | NUNOTA | I |  |
| `XMLCANC` | XMLCANC | C |  |
| `XMLPROTCANC` | XMLPROTCANC | C |  |
| `XMLENVCLICANC` | XMLENVCLICANC | C |  |
| `XMLENVCLICARTA` | Xml de Distribuição da Carta de Correção | C |  |
| `XMLPROTAUTCARTA` | Xml de Autorização de Carta de Correção | C |  |
| `CHAVENFE` | CHAVENFE | S |  |
| `XML` | XML | C |  |
| `XMLPROTAUTNOT` | XMLPROTAUTNOT | C |  |
| `XMLENVCLI` | XMLENVCLI | C |  |
| `QRCODE` | QRCODE | S |  |
| `XMLENVEPEC` | XMLENVEPEC | C |  |
| `XMLPROTAUTEPEC` | XMLPROTAUTEPEC | C |  |
| `XMLENVCANCPRORROG` | Xml de envio do Cancelamento do Evento de Prorrogação de Prazo de Suspensão do Icms | C |  |
| `XMLENVPRORROG` | Xml de envio do Evento de Prorrogação de Prazo de Suspensão do Icms | C |  |
| `XMLENVCLICANCPRORROG` | XMLENVCLICANCPRORROG | C |  |
| `XMLENVCLIPRORROG` | XMLENVCLIPRORROG | C |  |
| `XMLPROTAUTCANCPRORROG` | Xml de Autorização do Cancelamento do Evento de Prorrogação de Prazo de Suspensão do Icms | C |  |
| `XMLPROTAUTPRORROG` | Xml de Autorização do Evento de Prorrogação de Prazo de Suspensão do Icms | C |  |

## Tabela: TGFNFENT
### Descrição: Nota Técnica NFe

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Empresa | I |  |
| `ATIVONT` | Ativo | S | Veja opções na seção OPÇÕES |
| `VERSAONT` | Versão Nota Técnica | S | Veja opções na seção OPÇÕES |
| `DTENTPROD` | Data de Produção | H |  |
| `DTENTHOMOLOG` | Data de Homologação | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVONT (Tabela: TGFNFENT)
| Valor | Descrição |
|-------|-----------|
| N | Nao |
| S | Sim |

### Opções para campo VERSAONT (Tabela: TGFNFENT)
| Valor | Descrição |
|-------|-----------|
| 0 | Anterior |
| 1 | Nota Técnica 2021.004 - v1.10 |
| 10 | Nota Técnica 2018.005 - v.1.40 |
| 11 | Nota Técnica 2024.003 - v1.01 |
| 12 | Nota Técnica 2024.003 - v1.03 |
| 2 | Nota Técnica 2021.004 - v1.30 |
| 3 | Nota Técnica 2020.005 - v1.21 |
| 4 | Nota Técnica 2022.003 - v.1.00 |
| 5 | Nota Técnica 2023.001 - v.1.20 |
| 6 | Nota Técnica 2023.004 - v.1.11 |
| 7 | Nota Técnica 2023.005 - v.1.00 |
| 8 | Nota Técnica 2019.001 - v.1.64 |
| 9 | Nota Técnica 2024.001 - v.1.10 |


## Tabela: TGFNMDFE
### Descrição: Notas MDF-e

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Único da Nota | I |  |
| `ORDEMCARGA` | Ordem de Carga | I |  |
| `NUVIAG` | Nro. Viagem | I |  |
| `CODEMP` | Cód. Empresa | I |  |
| `RAZAOSOCIAL` | Descrição da empresa | S |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `RAZAOSOCIALPARC` | Descrição do parceiro | S |  |
| `VLRNOTA` | Valor da nota | F |  |
| `NUMNOTA` | Nro. Nota | I |  |
| `PESOBRUTO` | Peso Bruto | F |  |
| `SEQMDFE` | Sequência do manifesto | I |  |
| `INDREENTREGA` | Id. Reentrega | S | Veja opções na seção OPÇÕES |
| `STATUSENVIO` | Status de Envio | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo INDREENTREGA (Tabela: TGFNMDFE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSENVIO (Tabela: TGFNMDFE)
| Valor | Descrição |
|-------|-----------|
| D | Não enviado |
| null | Normal |
| P | Por evento |


## Tabela: TGFNTA
### Descrição: Nome das Tabelas de Preço

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DECVENDA` | Casas decimais | I |  |
| `CODTAB` | Código | I |  |
| `CODREG` | Região | I |  |
| `NOMETAB` | Nome | S |  |
| `OBS` | Observação | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `CODTIPPARC` | Perfil | I |  |
| `CODTABFLEX` | Tabela p/ Flex | I |  |
| `INTEGRAECONECT` | Integrar com EConect | S | Veja opções na seção OPÇÕES |
| `CODMOEDA` | Moeda | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFNTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTEGRAECONECT (Tabela: TGFNTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFNUM
### Descrição: Controle de Numeração

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `ARQUIVO` | Arquivo | S |  |
| `CODEMP` | Empresa | I |  |
| `SERIE` | Série | S |  |
| `CODMODDOC` | Mod.Doc.Fiscal | I | Veja opções na seção OPÇÕES |
| `AUTOMATICO` | Numeração Automática | S | Veja opções na seção OPÇÕES |
| `ULTCOD` | Último Código | I |  |
| `ULTNOTATALAO` | Último número do talão | I |  |
| `QTDAVISO` | Qtd. p/Aviso Poucas Notas | I |  |
| `TOTITENSNOTA` | Quantidade de itens na nota | I |  |
| `TOTSERVNOTA` | Quantidade de serviços da nota | I |  |
| `MODNOTAFIS` | Modelo | I |  |
| `TIPOIMPRESSORA` | Tipo Impressora | S | Veja opções na seção OPÇÕES |
| `IMPNOTA` | Caminho/Impressora | S |  |
| `DIASAVISO` | Dias para aviso | I |  |
| `DTVAL` | Dt. Validade | H |  |
| `CODMAQ` | Máquina | I |  |
| `NOMEARQ` | Nome | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo CODMODDOC (Tabela: TGFNUM)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Sem Modelo |
| 1 | 01-Nota Fiscal |
| 10 | 10-Conhecimento Aéreo |
| 11 | 11-Conhecimento de Transporte Ferroviário de Cargas |
| 13 | 13-Bilhete de Passagem Rodoviário |
| 14 | 14-Bilhete e Passagem Aquaviário |
| 15 | 15-Bilhete de Passagem e Nota de Bagagem |
| 16 | 16-Bilhete de Passagem Ferroviário |
| 17 | 17-Despacho de Transporte |
| 18 | 18-Resumo Movimento Diário |
| 2 | 02-Nota Fiscal de Venda a Consumidor |
| 20 | 20-Ordem de Coleta de Carga |
| 21 | 21-Nota Fiscal de Serviço de Comunicação |
| 22 | 22-Nota Fiscal de Serviço de Telecomunicações |
| 23 | 23-GNRE |
| 24 | 24-Autorização de Carregamento de Transporte |
| 25 | 25-Manifesto de Carga |
| 26 | 26-Conhecimento de Transporte Multimodal de Cargas |
| 27 | 27-Nota Fiscal de Transporte Ferroviário De Carga |
| 28 | 28-Nota Fiscal/Conta de Fornecimento de Gás Canalizado |
| 29 | 29-Nota Fiscal/Conta De Fornecimento D''água Canalizada |
| 3 | 03-Nota Fiscal de Entrada |
| 4 | 04-Nota Fiscal de Produtor |
| 55 | 55-Nota Fiscal Eletrônica |
| 57 | 57-Conhecimento Transporte Rodoviário Eletrônico |
| 58 | 58-Manifesto de Documentos Fiscais Eletrônico |
| 59 | 59-Cupom Fiscal Eletrônico |
| 6 | 06-Nota Fiscal Conta de Energia Elétrica |
| 62 | 62-Nota Fiscal Eletrônica de Serviços de Comunicação |
| 63 | 63-Bilhete de Passagem Eletrônico |
| 65 | 65-Nota Fiscal Eletrônica de Venda a Consumidor |
| 66 | 66 - Nota Fiscal de Energia Elétrica Eletrônica |
| 67 | 67-Conhecimento Transporte Eletrônico Outros Serviços |
| 7 | 07-Nota Fiscal de Serviço de Transporte |
| 8 | 08-Conhecimento de Transporte Rodoviário de Cargas |
| 9 | 09-Conhecimento de Transporte Aquaviário de Cargas |
| 901 | 1B-Nota Fiscal Avulsa |
| 902 | 8B-Conhecimento de Transporte de Cargas Avulso |

### Opções para campo AUTOMATICO (Tabela: TGFNUM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOIMPRESSORA (Tabela: TGFNUM)
| Valor | Descrição |
|-------|-----------|
| 1 | ELEBRA/RIMA |
| 2 | EPSON |
| 3 | RIMA/ITAUTEC |
| 4 | ELGIN |
| 5 | OUTRAS |
| 6 | DESKJET |
| 7 | XEROX LASER |
| 8 | GENÉRICA |


## Tabela: TGFOBS
### Descrição: Observações para Notas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODOBSPADRAO` | Código | I |  |
| `DTALTER` | Data | D |  |
| `OBSERVACAO` | Observação | S |  |
| `QTDLINHAS` | Qtde de Linhas | I |  |
| `NROPROCESSO` | Num. Processo | S |  |
| `ORIGPROCESSO` | Origem Processo | I | Veja opções na seção OPÇÕES |
| `VINCDOCARREC` | Vincular DAE/GNRE | S | Veja opções na seção OPÇÕES |
| `GERAREFD` | Geração no EFD | S | Veja opções na seção OPÇÕES |
| `COMPLEMENTOEFD` | Carrega Complemento p/ EFD | S | Veja opções na seção OPÇÕES |
| `CODREFINFCOMPL` | Código de referência à informação complementar | S |  |
| `OPERESSACOMP` | Operação com Ressarcimento/Complemento de ST | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ORIGPROCESSO (Tabela: TGFOBS)
| Valor | Descrição |
|-------|-----------|
| 0 | Sefaz |
| 1 | Justiça Federal |
| 2 | Justiça Estadual |
| 3 | Secex/RFB |
| 9 | Outros |

### Opções para campo VINCDOCARREC (Tabela: TGFOBS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERAREFD (Tabela: TGFOBS)
| Valor | Descrição |
|-------|-----------|
| I | Informação Complementar do Documento Fiscal |
| N | Não Gerar |
| O | Observação do Lançamento Fiscal |

### Opções para campo COMPLEMENTOEFD (Tabela: TGFOBS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OPERESSACOMP (Tabela: TGFOBS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFOMDF
### Descrição: TGFOMDF

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUVIAG` | Nro. Viagem | I |  |
| `SEQMDFE` | Sequência do manifesto | I |  |
| `DHOCOR` | Dt. e Hora da Ocorrência | H |  |
| `CODUSU` | Usuário | I |  |
| `OCORRENCIAS` | Ocorrências | C |  |

## Tabela: TGFORD
### Descrição: Ordens de Carga

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TOTALCARGA` | Total da carga | F |  |
| `CODEMP` | Empresa | I |  |
| `ORDEMCARGA` | Ordem de carga | I |  |
| `TEMTRANSBORDO` | Transbordo | S | Veja opções na seção OPÇÕES |
| `DTINIC` | Data início | D |  |
| `DTPREVSAIDA` | Data prevista para saída | D |  |
| `CODVEICULO` | Veículo | I |  |
| `CODREG` | Região | I |  |
| `CODPARCTRANSP` | Parceiro Transportadora | I |  |
| `CODPARCMOTORISTA` | Parceiro Motorista | I |  |
| `CODPARCORIG` | Parceiro Origem da Rota | I |  |
| `NROFROTA` | Nro. da Frota | I |  |
| `ROTEIRO` | Roteiro | S |  |
| `CODDOCA` | Doca p/ separação | I |  |
| `ENTSAI` | Tipo de OC | S | Veja opções na seção OPÇÕES |
| `TIPCARGA` | Tipo de Carga | S | Veja opções na seção OPÇÕES |
| `SITUACAO` | Situação | S | Veja opções na seção OPÇÕES |
| `TIPEMBALAGEM` | Tipo de Embalagem | S | Veja opções na seção OPÇÕES |
| `KMINIC` | Km Inicial | F |  |
| `KMFIN` | Km Final | F |  |
| `HORASAIDA` | Hora da saída | H |  |
| `PESOMAX` | Peso máximo | F |  |
| `M3MAX` | Metros Cúbicos Máximo | F |  |
| `VINCROT` | Gerar vinculação automática da rota para ordem de carga | S | Veja opções na seção OPÇÕES |
| `TIPCALCFRETE` | Tipo de Cálculo de Frete | I | Veja opções na seção OPÇÕES |
| `TIPDIST` | Tipo de Distância p/ Valor Manual/Tabela | S | Veja opções na seção OPÇÕES |
| `CODROTA` | Rota | I |  |
| `VLRFRETE` | Valor do Frete | F |  |
| `CODLOCAL` | Local | I |  |
| `CODPARCDEST` | Parceiro Destino da Rota | I |  |
| `SEQCARGA` | Sequência Carga | I |  |
| `ORDEMCARGAPAI` | Ordem Carga Pai | I |  |
| `CODTIPOPERTRANSB` | Tipo Operação | I |  |
| `DHINICIALPESAGEM` | Data e hora inicial Pesagem | H |  |
| `DHFINALPESAGEM` | Data e hora final Pesagem | H |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Data de Alteração | H |  |
| `DTALTERROTCAT` | Data Alteração Erro Rotas | H |  |
| `FRETECALC` | Frete Cálculo | S |  |
| `NUFINACERTO` | Número Financeiro Acerto | I |  |
| `VLRDIFACERTO` | Valor diferença acerto | F |  |
| `NUCAIXA` | Número do Caixa | I |  |
| `CODUSURETORNO` | Cód. Usuário Retorno | I |  |
| `DTRETORNO` | Data de Retorno | H |  |
| `QTDENTREGA` | Qtd. Entrega | I |  |
| `STATUSAVAL` | Avaliação de Veículo/Motorista | S | Veja opções na seção OPÇÕES |
| `OBSMOTORISTA` | Observações | S |  |
| `JUSTIFICATIVA` | Justificativa de escolha-Veículo/Motorista | S |  |
| `IDORDEMCARGA` | Cód. Barras | S |  |
| `ENVIOWMS` | Enviado p/ WMS | S | Veja opções na seção OPÇÕES |
| `PRIORIDADE` | Prioridade | I |  |
| `NUVIAG` | Número da Viagem | I |  |
| `AD_MANIFESTO` | Manifesto | I |  |
| `CODEMPPAI` | Empresa Pai | I |  |
| `AD_DATA_CHEGADA` | Data Chegada | D |  |
| `AD_TOTPECAS` | Total Peças | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo TEMTRANSBORDO (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENTSAI (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| E | Entrada |
| S | Saída |

### Opções para campo TIPCARGA (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| F | Fechada |
| R | Fracionada |

### Opções para campo SITUACAO (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| A | Aberta |
| F | Fechada |

### Opções para campo TIPEMBALAGEM (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| C | Caixas |
| G | Granel |
| P | Paletizada |

### Opções para campo VINCROT (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCALCFRETE (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Escolha Manual |
| 1 | 1 - Valor por Fórmula/Rateio por Peso |
| 2 | 2 - Valor por Fórmula/Rateio por Valor |
| 3 | 3 - Valor por Fórmula/Ganho Logístico |
| 4 | 4 - Valor por Rota/Rateio por Peso |
| 5 | 5 - Valor por Rota/Rateio por Valor |
| 6 | 6 - Valor Manual/Rateio por Peso |
| 7 | 7 - Valor Manual/Rateio por Valor |
| 8 | 8 - Valor Fixo Mensal Tabela |

### Opções para campo TIPDIST (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| A | entre Parceiros ou Cidades |
| C | entre Cidades |
| N | Não calcular Distancia |
| P | entre Parceiros |

### Opções para campo STATUSAVAL (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| N | Aguardando nova avaliação |
| null | Aguardando avaliação |
| S | Avaliado |

### Opções para campo ENVIOWMS (Tabela: TGFORD)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFPAEM
### Descrição: Grupo ICMS/ISS por Empresa

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Empresa | I |  |
| `GRUPOICMS` | Grupo de ICMS | I |  |
| `CODTAB` | Tabela preço | I |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `INDPRECOEMBUT` | Percentual | F |  |
| `FORMULA` | Fórmula | S |  |
| `CLASSIFICMS` | Classificação de ICMS | S | Veja opções na seção OPÇÕES |
| `RETEMISS` | Retém ISS | S | Veja opções na seção OPÇÕES |
| `AD_GRUPOICMS` | Grupo ICMS do Parceiro | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo CLASSIFICMS (Tabela: TGFPAEM)
| Valor | Descrição |
|-------|-----------|
| C | Consumidor Final |
| I | Isento de ICMS |
| P | Produtor rural |
| R | Revendedor |
| T | Usar a da TOP |
| X | Consumidor Contribuinte |
| Z | Usar do Parceiro |

### Opções para campo RETEMISS (Tabela: TGFPAEM)
| Valor | Descrição |
|-------|-----------|
| N | Não Retem ISS |
| S | Retem ISS |
| Z | Verificar no Parceiro |


## Tabela: TGFPAP
### Descrição: Interação Parceiro Produto

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPARC` | Cód. Parceiro | I |  |
| `CODPROD` | Produto | I |  |
| `CODPROPARC` | Cod. Produto Equivalente | S |  |
| `DESCRPROPARC` | Descrição do Produto Equivalente | S |  |
| `UNIDADEPARC` | Unidade | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `PRAZOENT` | Prazo para entrega | I |  |
| `CODBARRA` | Cód.Barra | S |  |
| `DUM14` | Cód. Barra DUN-14 | S |  |
| `CONTROLE` | Controle | S |  |
| `UNIDADE` | Unidade do Parceiro | S |  |
| `UNIDADELOTE` | Unidade do Lote | S |  |
| `MULTIPCPA` | Multipl. Compra | F |  |
| `CODBARRAPARC` | Cód. Barras Parceiro | S |  |
| `CODEMP` | Código Empresa | I |  |

## Tabela: TGFPAR
### Descrição: Parceiros

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPARC` | Cód. Parceiro | I |  |
| `PROVACRESCCAC` | Provisão do carrinho | F |  |
| `SALDODISPCAC` | Saldo disponivel do carrinho | F |  |
| `DESCRROTA` | Descrição da Rota | S |  |
| `NOMEPARC` | Nome Parceiro | S |  |
| `RAZAOSOCIAL` | Razão social | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `TIPPESSOA` | Tipo de pessoa | S | Veja opções na seção OPÇÕES |
| `CLIENTE` | Cliente | S | Veja opções na seção OPÇÕES |
| `FORNECEDOR` | Fornecedor | S | Veja opções na seção OPÇÕES |
| `VENDEDOR` | Vendedor | S | Veja opções na seção OPÇÕES |
| `USUARIO` | Usuário | S | Veja opções na seção OPÇÕES |
| `TRANSPORTADORA` | Transportadora | S | Veja opções na seção OPÇÕES |
| `AGENCIA` | Agência | S | Veja opções na seção OPÇÕES |
| `CTAADIANT` | Conta Adiantamento | S | Veja opções na seção OPÇÕES |
| `MOTORISTA` | Motorista | S | Veja opções na seção OPÇÕES |
| `MEDICO` | Médico | S | Veja opções na seção OPÇÕES |
| `AGRONOMO` | Agrônomo | S | Veja opções na seção OPÇÕES |
| `CODPARCGRUECONOMICO` | Cód. Grupo Econômico | I |  |
| `CODPARCMATRIZ` | Matriz | I |  |
| `CODGRUPO` | Grupo Cobrança | I |  |
| `CODVEND` | Vend. Preferencial | I |  |
| `CODASSESSOR` | Assessor do Parceiro | I |  |
| `CODBCO` | Banco | I |  |
| `CODAGE` | Agência bancária | S |  |
| `NOMEAGE` | Nome da agência | S |  |
| `CODCTABCO` | Conta bancária parceiro | S |  |
| `AGRUPAR` | Agrupar Pagamentos na geração p/Banco | S | Veja opções na seção OPÇÕES |
| `CODCTABCOINT` | Conta bancária empresa | I |  |
| `CGC_CPF` | CNPJ / CPF | S |  |
| `CODTIPPARC` | Perfil Principal | I |  |
| `IDENTINSCESTAD` | Insc. Estadual / Identidade | S |  |
| `TIMDATACI` | Dt. Cart. Identidade | D |  |
| `INSCESTADNAUF` | Insc. Estadual na UF | S |  |
| `CEI` | Cad. Específico do INSS - CEI | S |  |
| `TIMMAE` | Mãe | S |  |
| `DIASEM` | Dia Visita | I | Veja opções na seção OPÇÕES |
| `TIMPAI` | Pai | S |  |
| `TIMPROFISSAO` | Prof. / Ramo Atividade | I |  |
| `SELECIONADO` | Seleção | S |  |
| `TIMSENHASITE` | Senha do Site | S |  |
| `INSCMUN` | Cad.Mun.Contribuintes | S |  |
| `CODUNIMED` | Cód. Unimed | S |  |
| `TIMSENHADESC` | Conf. Senha | S |  |
| `CEP` | CEP | S |  |
| `TIMREFERENCIA01` | Referência 01 | S |  |
| `TIMREFERENCIA02` | Referência 02 | S |  |
| `CODEND` | Endereço | I |  |
| `NUMEND` | Número | S |  |
| `COMPLEMENTO` | Complemento | S |  |
| `CODBAI` | Bairro | I |  |
| `CODCID` | Cód. Cidade | I |  |
| `CODREG` | Região | I |  |
| `CAIXAPOSTAL` | Caixa Postal | S |  |
| `TELEFONE` | Telefone | S |  |
| `RAMAL` | Ramal | I |  |
| `ENVIPEDEMAILTOP` | Envio email de pedido / nota | S | Veja opções na seção OPÇÕES |
| `FAX` | Celular/Fax | S |  |
| `EMAIL` | Email | S |  |
| `EVENDA` | Email p/ pedido de venda | S | Veja opções na seção OPÇÕES |
| `ECOMPRA` | Email p/ pedido de compra | S | Veja opções na seção OPÇÕES |
| `DTCAD` | Data cadastramento | D |  |
| `CODUSU` | Cód. Usuário Alteração | I |  |
| `DTALTER` | Data alteração | H |  |
| `DTNASC` | Data nascimento/Fundação | D |  |
| `IMPLAUDOLOTE` | Imprime laudo lote | S | Veja opções na seção OPÇÕES |
| `SITUACAO` | Situação | S | Veja opções na seção OPÇÕES |
| `TIMTELEFONE01` | Telefone 01 | S |  |
| `DTULTCONTATO` | Dt. Último contato | H |  |
| `TIMTELEFONE02` | Telefone 02 | S |  |
| `PRAZOCONTATO` | Prazo p/ contato | I |  |
| `PRAZOPAG` | Prazo médio pagamento | I |  |
| `TOLERINADIMP` | Tolerância p/ inadimplência | I |  |
| `CODTAB` | Tabela de Preço | I |  |
| `GRUPOAUTOR` | Grupo de autorização | S |  |
| `LIMCRED` | Limite de crédito | F |  |
| `LIMCREDMENSAL` | Limite crédito mensal | F |  |
| `BLOQUEAR` | Bloquear venda a prazo | S | Veja opções na seção OPÇÕES |
| `MOTBLOQ` | Motivo de Bloqueio | S |  |
| `DESCBONIF` | Desconto bonificado | S | Veja opções na seção OPÇÕES |
| `DESCFIN` | % Desc. Financeiro | F |  |
| `TIPOFATUR` | Tipo de faturamento | S | Veja opções na seção OPÇÕES |
| `PERCCUSVAR` | % de Custo Variável | F |  |
| `DIASVARPAGTO` | Antecipação/Atraso recebimento(em dias) | I |  |
| `CONTACESSO` | Informações adicionais | S |  |
| `QTDMAXTITVENCIDOS` | Qtd. máx. de títulos vencidos | I |  |
| `CLASSIFICMS` | Classificação ICMS | S | Veja opções na seção OPÇÕES |
| `CSTIPIENT` | Código Sit.Trib.IPI Entrada | I | Veja opções na seção OPÇÕES |
| `CSTIPISAI` | Código Sit.Trib.IPI Saída | I | Veja opções na seção OPÇÕES |
| `CODENQIPIENT` | Código Enq. Legal IPI Entrada | I |  |
| `CODENQIPISAI` | Código Enq. Legal IPI Saída | I |  |
| `INDNATRET` | Natureza da Retenção na Fonte | S | Veja opções na seção OPÇÕES |
| `CODCTACTB` | Conta contábil 1 | I |  |
| `CODCTACTB2` | Conta contábil 2 | I |  |
| `CODCTACTB3` | Conta contábil 3 | I |  |
| `CODCTACTB4` | Conta contábil 4 | I |  |
| `CODTABST` | Tabela c/base p/S.T.na venda | I |  |
| `MODELONFDES` | Modelo da nota fiscal | S |  |
| `SERIENFDES` | Série da Nota Fiscal | S |  |
| `NATUREZAOPERDES` | Tipo de Negócio | S |  |
| `IPIINCICMS` | IPI incide no cálculo do ICMS | S | Veja opções na seção OPÇÕES |
| `TEMIPI` | Tem IPI | S | Veja opções na seção OPÇÕES |
| `CALCINSS` | Calcula FUNRURAL/INSS | S | Veja opções na seção OPÇÕES |
| `PERCREDINSS` | % a ser subtraído da Alíquota do FUNRURAL/INSS | F |  |
| `INDCOMERCIALIZACAO` | Indicador de Comercialização | S | Veja opções na seção OPÇÕES |
| `INDAQUISICAO` | Indicador de Aquisição | S | Veja opções na seção OPÇÕES |
| `RETEMINSS` | Calcula IRF | S | Veja opções na seção OPÇÕES |
| `RETEMISS` | Retém ISS | S | Veja opções na seção OPÇÕES |
| `TARE` | Tare | S | Veja opções na seção OPÇÕES |
| `CALCFETHAB` | Calcular FETHAB | S | Veja opções na seção OPÇÕES |
| `INAPLICPRODEPE` | Parceiro elegível à inaplicabilidade do PRODEPE? | S | Veja opções na seção OPÇÕES |
| `INTEGRAECONECT` | Integração EConect | S | Veja opções na seção OPÇÕES |
| `DESCSTIVA` | Considera desconto no cálculo de ST por IVA | S | Veja opções na seção OPÇÕES |
| `SENHAECONECT` | Senha | S |  |
| `PRODUTORTEMNF` | Produtor tem NF | S | Veja opções na seção OPÇÕES |
| `PRAZOPARCECONECT` | Prazos | S |  |
| `CODEMP` | Empresa | I |  |
| `TIPGERBOLCENT` | Geração de boleto nas centrais | S | Veja opções na seção OPÇÕES |
| `TIPLOTACAO` | Tipo de Lotação | S | Veja opções na seção OPÇÕES |
| `EXIGENOMEPARC` | Usar razão social no Boleto Rápido | S | Veja opções na seção OPÇÕES |
| `TRUNCPARCELA` | Truncar valores no parcelamento | S | Veja opções na seção OPÇÕES |
| `ARREDPRIMEIRAPARC` | Ajusta arredondamento na 1ª parcela | S | Veja opções na seção OPÇÕES |
| `NUFOP` | Finalidade da Operação | I |  |
| `DESCONSIDESCBASE` | Desconsiderar desconto da nota/item na base de cálculo dos impostos ISS e IRF | S | Veja opções na seção OPÇÕES |
| `ATUNUVERSAO` | Atualizar versão | S |  |
| `NUVERSAO` | Versão | I |  |
| `PARCSUBSTISS` | Substituto Tributário - ISS | S | Veja opções na seção OPÇÕES |
| `CODCONTATOPADCOT` | Contato padrão para cotação | I |  |
| `ENQART227` | Enquadro no Art. 227. para cálculo de IPI? | S | Veja opções na seção OPÇÕES |
| `INTERVANALISCRED` | Intervalo p/ análise de crédito | I |  |
| `VENDAMIN` | Venda Mínima | F |  |
| `TIMCARTREGIMEBENSV` | Regime de Casamento | S | Veja opções na seção OPÇÕES |
| `TIMCORRESPBANCARIO` | Corr. Bancário | S | Veja opções na seção OPÇÕES |
| `TIMFAIXASALARIAL` | Faixa Salarial | S | Veja opções na seção OPÇÕES |
| `TIMPROPRIETA` | Proprietário | S | Veja opções na seção OPÇÕES |
| `TIPANEXONFE` | Tipo do anexo | S | Veja opções na seção OPÇÕES |
| `BASEPRAZOECONECT` | Partir de | I | Veja opções na seção OPÇÕES |
| `TRANSPPROPRIA` | Transportadora própria | S | Veja opções na seção OPÇÕES |
| `DTULTNEGOC` | Última negociação | H |  |
| `PARCELAMECONECT` | Parcelamentos | S |  |
| `RETEMCOFINS` | Retém COFINS | S | Veja opções na seção OPÇÕES |
| `BASEPARCELECONECT` | Partir de | I | Veja opções na seção OPÇÕES |
| `EMAILNOTIFENTREGA` | E-mail p/ notificação de entrega | S |  |
| `OBSERVACOES` | Observações | S |  |
| `VLRLIQITEMNFE` | Considera valor líquido do item na NF-e (geração do XML e imp.Danfe) | S | Veja opções na seção OPÇÕES |
| `DIAFECHAECONECT` | Dia Fechamento | I |  |
| `VLRLIQITEMNFCE` | Considera valor líquido do item na NFC-e (geração do XML e imp.Danfe) | S | Veja opções na seção OPÇÕES |
| `RETEMCSL` | Retém CSL | S | Veja opções na seção OPÇÕES |
| `DIAPAGTOECONECT` | Dia Pagamento | I |  |
| `RETEMPIS` | Retém PIS | S | Veja opções na seção OPÇÕES |
| `TIMCORRETOR` | Corretor | S | Veja opções na seção OPÇÕES |
| `PERFILECONECT` | Perfil | S | Veja opções na seção OPÇÕES |
| `TIPOSPARC` | Tipo | S |  |
| `TIMTIPOMORADIA` | Tipo de Moradia | S | Veja opções na seção OPÇÕES |
| `MOTNAORETERISSQN` | Motivo de não Retenção ISSQN | S |  |
| `TIMFIADOR` | Fiador | S | Veja opções na seção OPÇÕES |
| `SITESPECIALRESP` | Situação Especial de Responsabilidade | S |  |
| `TIMQUERCOMPRAR` | Quer Comprar | S | Veja opções na seção OPÇÕES |
| `DTEMISNFEFORN` | Data de Inicio para Emissão de NFe | D |  |
| `TIMCOMPRADOR` | Comprador | S | Veja opções na seção OPÇÕES |
| `TIMPROPVENDA` | Prop. Venda | S | Veja opções na seção OPÇÕES |
| `CODANT` | Código no SGE | I |  |
| `EMAILDANFE` | Enviar DANFE por e-mail? | S | Veja opções na seção OPÇÕES |
| `ENVIADANFEREDESPACHO` | Enviar DANFE/XML por e-mail para Redespacho (Recebedor)? | S | Veja opções na seção OPÇÕES |
| `TIMINQUILINO` | Inquilino | S | Veja opções na seção OPÇÕES |
| `HOMEPAGE` | HomePage | S |  |
| `TIMCARTORIO` | Cartório | I |  |
| `ALUNO` | Aluno | S | Veja opções na seção OPÇÕES |
| `TIMBAIRROCOMPRA` | Bairro da Compra | I |  |
| `TIMORGAO` | Orgão | S |  |
| `PROFESSOR` | Professor | S | Veja opções na seção OPÇÕES |
| `TERMACORD` | Tem Termo de Acordo p/ CT-e? | S | Veja opções na seção OPÇÕES |
| `CONSIDTOTITENSTRIB` | Considerar valor total dos itens mais valor total tributado para tags vTprest e vRec? | S | Veja opções na seção OPÇÕES |
| `EMAILNFE` | E-mail p/ envio NF-e/NFS-e/CT-e | S |  |
| `CHAVEPIX` | Chave Pix | S |  |
| `TIMESTADOCIVIL` | Estado Civil | S | Veja opções na seção OPÇÕES |
| `IDESTRANGEIRO` | Identificação de Estrangeiro | S |  |
| `SITCADSEFAZ` | Situação Cadastral SEFAZ | I | Veja opções na seção OPÇÕES |
| `DHCADSEFAZ` | Data/Hora da Última Consulta SEFAZ | H |  |
| `COMOCONHECEU` | Como nos conheceu | S |  |
| `TIMAINVESTIR` | Investimento | F |  |
| `CODCRED` | Crédito | I |  |
| `TIMOUTTELS` | Outras Informações de Contato | S |  |
| `QTDMAXPEDCPA` | Qtd máx itens por pedido | I |  |
| `TIMNACIONALIDAD` | Nacionalidade | I |  |
| `CODROTA` | Rota | I |  |
| `SIMPLES` | Optante pelo Simples Nacional? | S | Veja opções na seção OPÇÕES |
| `SEXO` | Sexo | S | Veja opções na seção OPÇÕES |
| `VALDESCGRDCAR` | Validar Desc. Grande Carga? | S | Veja opções na seção OPÇÕES |
| `FLEX` | Usar Créd.Flex? | S | Veja opções na seção OPÇÕES |
| `SALDODISP` | Saldo Disponível | F |  |
| `RETSTVENDA` | Retirar ST do preço de venda do item | S | Veja opções na seção OPÇÕES |
| `CODEMPPREF` | Empresa Preferencial | I |  |
| `VLRMINPEDCPA` | Vlr mín por pedido | F |  |
| `ENTREGAENDCONTATO` | Utiliza endereço de entrega do contato | S | Veja opções na seção OPÇÕES |
| `EXIGCONTATOENTCAB` | Exigir Contato de Entrega no cabeçalho | S | Veja opções na seção OPÇÕES |
| `AD_REDE` | Rede | S |  |
| `CODLOCALPADRAO` | Local padrão para produtos | I |  |
| `CPFPRODRURAL` | CPF Prod. Rural | S |  |
| `TIPJURO` | Tipo de juro | S | Veja opções na seção OPÇÕES |
| `AD_EMAILCONF` | Email Confirmado? | S | Veja opções na seção OPÇÕES |
| `USATABCRFORN` | Usa Tabela p/ compra por CR? | S | Veja opções na seção OPÇÕES |
| `AD_ESTADO` | Estado(UF) | S |  |
| `PERCMULTA` | % de multa | F |  |
| `PERCJURO` | % de juro (diário) | F |  |
| `TIPOGERBOLETO` | Tipo geração boleto | S | Veja opções na seção OPÇÕES |
| `ALIQISSRETSIMPLES` | Alíquota ISS Ret/Simples | F |  |
| `POTENCIALNEG` | Potencial de compra | F |  |
| `LATITUDE` | Latitude | S |  |
| `IMPAGRUPFIN` | Impedir agrupamento de boletos | S | Veja opções na seção OPÇÕES |
| `LONGITUDE` | Longitude | S |  |
| `PERCDESCESPECIAL` | % Desc. Especial | F |  |
| `MEIRJ` | Micro empresário individual | S | Veja opções na seção OPÇÕES |
| `SITCCF` | Situação no CCF | S | Veja opções na seção OPÇÕES |
| `SITRECEITA` | Situação na Receita Federal | S | Veja opções na seção OPÇÕES |
| `SITSINTEGRA` | Situação no Sintegra | S | Veja opções na seção OPÇÕES |
| `STATUSEDZ` | Status envio EDZ | S | Veja opções na seção OPÇÕES |
| `OPERLOGIST` | Operador logístico | S | Veja opções na seção OPÇÕES |
| `CODUSUCOBR` | Cód. Usuário Cobrador | I |  |
| `APLICLEITRANSP` | Aplicar a lei da transparência | S | Veja opções na seção OPÇÕES |
| `ESTABTRANSP` | Estabelecimento p/ fins de transporte | S | Veja opções na seção OPÇÕES |
| `AD_TRAVACOM` | Trava Comissão em % | F |  |
| `SITCADRF` | Situação Cadastral ReceitaWS | I | Veja opções na seção OPÇÕES |
| `DHCADRF` | Data/Hora da Última Consulta ReceitaWS | H |  |
| `UNIDIMPORT` | Unidade para considerar na importação | I | Veja opções na seção OPÇÕES |
| `ORGPUBLNFSE` | Orgão público (NFS-e) | S | Veja opções na seção OPÇÕES |
| `ASSOCIACAODESP` | Associação Desportiva | S | Veja opções na seção OPÇÕES |
| `MODELONOTACOMPRA` | Modelo para Importação de XML Compra | I |  |
| `PARCINTER` | Parceiro com Interdependência | S | Veja opções na seção OPÇÕES |
| `PROVACRESC` | Provisão acréscimo | F |  |
| `EMAILNFSE` | E-mail específico p/ envio NFS-e | S |  |
| `EMAILCTE` | E-mail específico p/ envio CT-e | S |  |
| `CNAE` | CNAE principal do contribuinte | S |  |
| `INDCREDNFE` | Contribuinte credenciado a emitir NF-e | I | Veja opções na seção OPÇÕES |
| `INDCREDCTE` | Contribuinte credenciado a emitir CTe | I | Veja opções na seção OPÇÕES |
| `DTINIATIV` | Início da Atividade do Contribuinte | D |  |
| `DTULTSIT` | Última mod. da situação cadastral | D |  |
| `DTBAIXA` | Data da baixa do contribuinte | D |  |
| `REGAPUR` | Regime de apuração | S |  |
| `INDOPCCP` | Tributação Contr.Previdenciária (Prod.Rural) | I | Veja opções na seção OPÇÕES |
| `AD_CONF` | Conferência | S | Veja opções na seção OPÇÕES |
| `CODIDENTCONS` | Código de identificação do consumidor ou assinante | I |  |
| `UTILIZANUCADPARC` | Utilizar código de identificação do consumidor ou assinante? | S | Veja opções na seção OPÇÕES |
| `AD_VENDDESC` | Valor do pedido para 3% desconto | F |  |
| `DESCONSDESCINSS` | Desconsiderar desconto da nota/item na base de cálculo do INSS | S | Veja opções na seção OPÇÕES |
| `AD_DESC_2G` | Descontar 2G | S |  |
| `TIPCLIENTESERVCOM` | Tipo Cliente de Serviços de Comunicação | I | Veja opções na seção OPÇÕES |
| `AD_CODNAT` | Natureza | I |  |
| `CONSPARCADRCST` | Considerar parceiro no registro 1210 e 1220 da ADRC-ST (PR) | S | Veja opções na seção OPÇÕES |
| `DEDUZIPIBCPISCF` | Deduzir valor de IPI da BC do PIS e COFINS | S | Veja opções na seção OPÇÕES |
| `GRUPOPISCOFINS` | Grupo PIS/COFINS | I |  |
| `REGISTROANS` | Registro ANS | I |  |
| `REDE` | Nome da Rede na operação com TEF | S |  |
| `ORGAOPUB` | Órgão Público | S | Veja opções na seção OPÇÕES |
| `AD_MAE` | Mãe | S |  |
| `AD_CODPIS` | PIS | F |  |
| `TPCOMPRAGOV` | Tipo de Compra Governamental | S | Veja opções na seção OPÇÕES |
| `AD_ULTNOTA` | Ult. Nota | I |  |
| `AD_NOMFANTASISA` | Nome Fantasia | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPPESSOA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| F | Física |
| J | Jurídica |

### Opções para campo CLIENTE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FORNECEDOR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VENDEDOR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USUARIO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRANSPORTADORA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AGENCIA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CTAADIANT (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MOTORISTA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MEDICO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AGRONOMO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AGRUPAR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIASEM (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| null | Indefinido |
| 1 | Domingo |
| 2 | Segunda |
| 3 | Terça |
| 4 | Quarta |
| 5 | Quinta |
| 6 | Sexta |
| 7 | Sábado |

### Opções para campo ENVIPEDEMAILTOP (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| A | Automático |
| M | Manual |

### Opções para campo EVENDA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| C | Contato |
| N | Não envia |
| P | Parceiro |

### Opções para campo ECOMPRA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| C | Contato |
| N | Não envia |
| P | Parceiro |

### Opções para campo IMPLAUDOLOTE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SITUACAO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| B | Bom |
| E | Excelente |
| O | Ótimo |
| P | Péssimo |
| R | Regular |

### Opções para campo BLOQUEAR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCBONIF (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| J | Na Nota/Pedido |
| L | Livre |
| P | Proibido |
| S | Em separado |

### Opções para campo TIPOFATUR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| L | Livre |
| M | Mensal |
| Q | Quinzenal |
| S | Semanal |

### Opções para campo CLASSIFICMS (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| C | Consumidor Final Não Contribuinte |
| I | Isento de ICMS |
| P | Produtor Rural |
| R | Revendedor |
| T | Usar a da TOP |
| X | Consumidor Final Contribuinte |

### Opções para campo CSTIPIENT (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Entrada c/Recuperação de Crédito |
| -1 | (-1)-Não sujeita ao IPI |
| 1 | 01-Entrada c/Alíquota zero |
| 2 | 02-Entrada Isenta |
| 3 | 03-Entrada Não Tributada |
| 4 | 04-Entrada Imune |
| 49 | 49-Outras Entradas |
| 5 | 05-Entrada c/Suspensão |

### Opções para campo CSTIPISAI (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| -1 | (-1)-Não sujeita ao IPI |
| 50 | 50-Saída Tributada |
| 51 | 51-Saída c/Alíquota zero |
| 52 | 52-Saída Isenta |
| 53 | 53-Saída Não Tributada |
| 54 | 54-Saída Imune |
| 55 | 55-Saída c/Suspensão |
| 99 | 99-Outras Saídas |

### Opções para campo INDNATRET (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 01 | 01 - Retenção por Órgãos, Autarquias e Fundações Federais |
| 02 | 02 - Retenção por outras Entidades Adm.Pública Federal |
| 03 | 03 - Retenção por Pessoas Jurídicas de Direito Privado |
| 04 | 04 - Recolhimento por Sociedade Cooperativa |
| 05 | 05 - Retenção por Fabricante de Máquinas e Veículos |
| 99 | 99 - Outras Retenções |

### Opções para campo IPIINCICMS (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMIPI (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCINSS (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDCOMERCIALIZACAO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 1 | Com. da Produção por Prod. Rural PJ ou Agroindústria, exceto para PAA |
| 2E | Com. da Produção efetuada por Prod. Rural PF à Consumidor Final ou Prod. Rural PF |
| 3E | Com. da Produção por Prod. Rural PF/Seg. Especial – Vendas a PJ (exceto PAA) ou a PF |
| 7 | Com. da Produção com Isenção de Contrib. Prev., de acordo com a Lei n° 13.606/2018 |
| 8 | Com. da Produção para Entidade do Programa de Aquisição de Alimentos - PAA |
| 8E | Com. da Produção de PF/Seg. Especial a Entidade no PAA |
| 9 | Comercialização direta da Produção no Mercado Externo |
| 9E | Comercialização da Produção no Mercado Externo |

### Opções para campo INDAQUISICAO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 1 | 1-Aquisição da produção de produtor rural pessoa física ou segurado especial em geral |
| 2 | 2-Aquisição da produção de produtor rural PF ou segurado especial em geral por Entidade do PAA |
| 3 | 3-Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA |
| 4 | 4-Aquisição de produção de produtor rural pessoa física ou segurado especial em geral |
| 5 | 5-Aquisição de produção de produtor rural pessoa física ou segurado especial por entidade do PAA |
| 6 | 6-Aquisição de produção de produtor rural pessoa jurídica por entidade do PAA - Produção isenta |
| 7 | 7-Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação |

### Opções para campo RETEMINSS (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RETEMISS (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TARE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCFETHAB (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INAPLICPRODEPE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTEGRAECONECT (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCSTIVA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODUTORTEMNF (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPGERBOLCENT (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| A | Imprimir e Enviar e-mail |
| E | Enviar e-mail |
| I | Imprimir |

### Opções para campo TIPLOTACAO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 2 | Obra de Construção Civil - Empreitada Parcial ou Subempreitada |
| 3 | PF Tomadora de Serviços prestados mediante cessão de MOB, exceto contratante de cooperativa |
| 4 | PJ Tomadora de Serv prest mediante cessão de MOB, exceto contratante de cooperativa, lei 8.212/1991 |
| 5 | PJ Tomadora Serv prest por cooperados intermédio cooperativa de trab, exceto ent beneficente/isenta |
| 6 | Entidade beneficente/isenta Tom de Serv prest por cooperados por intermédio de cooperativa de trab |
| 7 | PF tomadora de Serv prest por Cooperados por intermédio de Cooperativa de Trabalho |
| 8 | Operador Portuário tomador de serviços de trabalhadores avulsos |
| 9 | Contratante de trabalhadores avulsos não portuários por intermédio de Sindicato |

### Opções para campo EXIGENOMEPARC (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRUNCPARCELA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ARREDPRIMEIRAPARC (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCONSIDESCBASE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PARCSUBSTISS (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENQART227 (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMCARTREGIMEBENSV (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| CPB | Comunhão parcial de bens |
| CUB | Comunhão universal de bens |
| OU | Outros |
| PFA | Participação final nos aquestos |
| STB | Separação total de bens |

### Opções para campo TIMCORRESPBANCARIO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMFAIXASALARIAL (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| AC20 | Acima de 20 Salários Mínimos |
| AT01 | Até 01 Salário Mínimo |
| AT02A03 | De 02 a 03 Salários Mínimos |
| AT05A10 | De 05 a 10 Salários Mínimos |
| AT10A20 | De 10 a 20 Salários Mínimos |
| NI | Não informado |

### Opções para campo TIMPROPRIETA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPANEXONFE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| X | Arquivo normal (Extensão XML) |
| Z | Arquivo compactado (Extensão ZIP) |

### Opções para campo BASEPRAZOECONECT (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 0 | Não se aplica |
| 1 | Fora dia |
| 2 | Próximo dia útil |
| 3 | Fora Semana |
| 4 | Fora Dezena |
| 5 | Fora Quinzena |
| 6 | Fora Mês |

### Opções para campo TRANSPPROPRIA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RETEMCOFINS (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASEPARCELECONECT (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 0 | Não se aplica |
| 1 | Fora dia |
| 2 | Próximo dia útil |
| 3 | Fora Semana |
| 4 | Fora Dezena |
| 5 | Fora Quinzena |
| 6 | Fora Mês |

### Opções para campo VLRLIQITEMNFE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| E | Conforme empresa |
| N | Não |
| S | Sim |

### Opções para campo VLRLIQITEMNFCE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| E | Conforme empresa |
| N | Não |
| S | Sim |

### Opções para campo RETEMCSL (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RETEMPIS (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMCORRETOR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERFILECONECT (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| A | Pode ultrapassar limite |
| B | Somente até limite |
| C | Cliente sem limite |

### Opções para campo TIMTIPOMORADIA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| AL | Alugada |
| FI | Financiada |
| NI | Não Informada |
| OU | Outros |
| PR | Própria |
| SR | Sem Resposta |

### Opções para campo TIMFIADOR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMQUERCOMPRAR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMCOMPRADOR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMPROPVENDA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EMAILDANFE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVIADANFEREDESPACHO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMINQUILINO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALUNO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROFESSOR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TERMACORD (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSIDTOTITENSTRIB (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMESTADOCIVIL (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| CA | Casado(a) |
| DE | Desquitado(a) |
| DI | Divorciado(a) |
| NI | Não Informado |
| OU | Outros(as) |
| SJ | Sep. Judicialmente |
| SO | Solteiro(a) |
| UE | União Estável |
| VI | Viuvo(a) |

### Opções para campo SITCADSEFAZ (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Habilitado |
| 1 | Habilitado |

### Opções para campo SIMPLES (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SEXO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| F | Feminino |
| M | Masculino |

### Opções para campo VALDESCGRDCAR (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FLEX (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RETSTVENDA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| A | Sim e considerar despesas acessórias |
| N | Não |
| S | Sim |

### Opções para campo ENTREGAENDCONTATO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGCONTATOENTCAB (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPJURO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| C | Composto |
| S | Simples |

### Opções para campo AD_EMAILCONF (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 1 | OK |

### Opções para campo USATABCRFORN (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOGERBOLETO (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| E | Enviar e-mail |
| I | Imprimir |
| P | Preparar |

### Opções para campo IMPAGRUPFIN (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MEIRJ (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SITCCF (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| A | Regular |
| B | Restrição |
| I | Indefinida |

### Opções para campo SITRECEITA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| A | Regular |
| B | Restrição |
| I | Indefinida |

### Opções para campo SITSINTEGRA (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| A | Regular |
| B | Restrição |
| I | Indefinida |

### Opções para campo STATUSEDZ (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| E | Enviado |
| P | Pendente |
| R | Recebido |

### Opções para campo OPERLOGIST (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APLICLEITRANSP (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ESTABTRANSP (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| C | Comercial |
| G | Geradora/Distribuidora de Energia Elétrica |
| I | Industrial |
| N | Não contribuinte |
| P | Produtor Rural |
| S | Prestador de Serviço de Comunicação |
| T | Prestador de Serviço de Transporte |

### Opções para campo SITCADRF (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Habilitado |
| 1 | Habilitado |

### Opções para campo UNIDIMPORT (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 1 | Unidade Comercial |
| 2 | Unidade Tributável |

### Opções para campo ORGPUBLNFSE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ASSOCIACAODESP (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PARCINTER (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDCREDNFE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 0 | Não credenciado para emissão da NF-e |
| 1 | Credenciado |
| 2 | Credenciado com obrigatoriedade para todas operações |
| 3 | Credenciado com obrigatoriedade parcial |
| 4 | A SEFAZ não fornece a informação |

### Opções para campo INDCREDCTE (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 0 | Não credenciado para emissão da CT-e |
| 1 | Credenciado |
| 2 | Credenciado com obrigatoriedade para todas operações |
| 3 | Credenciado com obrigatoriedade parcial |
| 4 | A SEFAZ não fornece a informação |

### Opções para campo INDOPCCP (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 0 | Não se aplica |
| 1 | Sobre a comercialização da produção |
| 2 | Sobre a folha de pagamento |

### Opções para campo AD_CONF (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| NAO | Não |
| SIM | Sim |

### Opções para campo UTILIZANUCADPARC (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCONSDESCINSS (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCLIENTESERVCOM (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 1 | 01 - Comercial |
| 2 | 02 - Industrial |
| 3 | 03 - Residencial/Pessoa Física |
| 4 | 04 - Produtor Rural |
| 5 | 05 - Órgão da administração..., nos termos do Convênio ICMS 107/95 |
| 6 | 06 - Prestador de serviço de telecomunicação..., nos termos do Convênio ICMS 17/13 |
| 7 | 07 - Missões Diplomáticas, Repartições Consulares..., nos termos do Convênio ICMS 158/94 |
| 8 | 08 - Igrejas e Templos de qualquer natureza |
| 99 | 99 - Outros não especificados anteriormente |

### Opções para campo CONSPARCADRCST (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DEDUZIPIBCPISCF (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ORGAOPUB (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TPCOMPRAGOV (Tabela: TGFPAR)
| Valor | Descrição |
|-------|-----------|
| 1 | União |
| 2 | Estado |
| 3 | DF |
| 4 | Município |


## Tabela: TGFPDF
### Descrição: TABLE TGFPDF

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | NUNOTA | I |  |
| `PDFDANFESIMPLIF` | PDFDANFESIMPLIF | B |  |
| `PDFDANFE` | PDFDANFE | B |  |
| `TIPO` | TIPO | S |  |

## Tabela: TGFPDI
### Descrição: Percentuais de Partilha DIFAL

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DTINICIO` | Data Início Partilha | D |  |
| `PERCPARTDIFAL` | Percentual de Partilha DIFAL | F |  |

## Tabela: TGFPEM
### Descrição: Empresa produtos e impostos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Empresa | I |  |
| `CODPROD` | Produto | I |  |
| `GRUPOICMS` | Grupo de ICMS | I |  |
| `TEMICMS` | Tem ICMS | S | Veja opções na seção OPÇÕES |
| `TIPSUBST` | Tipo de substituição | S | Veja opções na seção OPÇÕES |
| `USOPROD` | Uso do Produto | S | Veja opções na seção OPÇÕES |
| `TIPOITEMSPED` | Tipo do item p/ SPED | S | Veja opções na seção OPÇÕES |
| `CODICMSFAST` | Alíquota ICMS do Fast Service | F |  |
| `CODPRODROI` | Produto | S |  |
| `DESCMAX` | Descrição | F |  |
| `USAIDPALETE` | Usa Pálete Identificado | S | Veja opções na seção OPÇÕES |
| `PERCREDBASEICMSEFET` | Perc. Red. Base Icms Efetivo | F |  |
| `ALIQICMSINTEFD` | Alíquota Interna de ICMS | F |  |
| `LEADTIME` | Lead time de compra | I |  |
| `CALCDIFAL` | Calcular DIFAL ? | S | Veja opções na seção OPÇÕES |
| `ORIGPROD` | Origem do Produto | S | Veja opções na seção OPÇÕES |
| `TEMIPICOMPRA` | IPI na Entrada | S | Veja opções na seção OPÇÕES |
| `TEMIPIVENDA` | IPI na Saída | S | Veja opções na seção OPÇÕES |
| `CSTIPIENT` | Código Sit.Trib.IPI Entrada | I | Veja opções na seção OPÇÕES |
| `CSTIPISAI` | Código Sit.Trib.IPI Saída | I | Veja opções na seção OPÇÕES |
| `CODENQIPIENT` | Código Enq. Legal IPI Entrada | I |  |
| `CODENQIPISAI` | Código Enq. Legal IPI Saída | I |  |
| `CAT1799SPRES` | Ressarcimento de ST (CAT-17/99) | S | Veja opções na seção OPÇÕES |
| `TIPCONTEST` | Tipo de Controle de Estoque | S | Veja opções na seção OPÇÕES |
| `USALOTEDTFAB` | Usa Data de Fabricação | S | Veja opções na seção OPÇÕES |
| `USALOTEDTVAL` | Usa Data de Validade | S | Veja opções na seção OPÇÕES |
| `LOCALIZACAO` | Localização | S |  |
| `ESTMAX` | Estoque Máximo | F |  |
| `ESTMIN` | Estoque Mínimo | F |  |
| `GRUPOICMS2` | Grupo de ICMS 2 | I |  |
| `MVAPADRAO` | MVA Padrão | F |  |
| `ALIQGERAL` | Alíquota Geral | F |  |
| `CODLOCALPAD` | Local Padrão | I |  |
| `CODESPECST` | Código Especificador ST | I |  |
| `PERCCMTNAC` | % Carga Média Trib. Nacional | F |  |
| `PERCCMTFED` | % Carga Média Trib. Federal | F |  |
| `PERCCMTEST` | % Carga Média Trib. Estadual | F |  |
| `PERCCMTIMP` | % Carga Média Trib. Importação | F |  |
| `TEMRASTROLOTE` | Tem Rastro do Lote | S | Veja opções na seção OPÇÕES |
| `CODCTACTBEFD` | Conta Contábil para EFD | I |  |
| `RASTSTULTENTRADA` | Usa Rastro/ST pela Ult. Entrada | S | Veja opções na seção OPÇÕES |
| `OBTSTANTMEDENT` | Obtém ST Anterior pela média das entradas? | S | Veja opções na seção OPÇÕES |
| `CODFCI` | Código da FCI | S |  |
| `VLRCOMERC` | Valor de Comercialização - (R$) | F |  |
| `VLRPARCIMPEXT` | Valor da Parcela Importada do Exterior - (R$) | F |  |
| `GRADEPADRAO` | Grade Padrão | C |  |
| `IDGRADE` | Grade Produto | I |  |
| `ENQREINTEGRA` | Enquadrado no Reintegra/Prev. | I | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TEMICMS (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPSUBST (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| A | Subst. na compra e na venda |
| C | Revenda com subst. tributária (cálculo de Subst. na compra) |
| N | Não tem |
| P | Venda com subst. tributária (cálculo de Subst. na venda) |

### Opções para campo USOPROD (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| B | Brinde |
| C | Consumo |
| D | Revenda (por Fórmula) |
| E | Embalagem |
| F | Brinde (NF) |
| I | Imobilizado |
| M | Matéria Prima |
| O | Outros insumos |
| P | Em Processo |
| R | Revenda |
| T | Terceiros |
| V | Venda (Fabricação Própria) |
| 1 | Subproduto |
| 2 | Prod.Intermediário |
| 4 | Demonstração |

### Opções para campo TIPOITEMSPED (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| null | Utilizar do "Uso do Produto" |
| 00 | Mercadoria para revenda |
| 01 | Matéria-Prima |
| 02 | Embalagem |
| 03 | Produtos em Processo |
| 04 | Produto Acabado |
| 05 | Subproduto |
| 06 | Produto Intermediário |
| 07 | Material de Uso e Consumo |
| 08 | Ativo Imobilizado |
| 09 | Serviços |
| 10 | Outros Insumos |
| 99 | Outras |

### Opções para campo USAIDPALETE (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCDIFAL (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ORIGPROD (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 |
| 1 | 1-Estrangeira, importação direta, exceto a indicada no código 6 |
| 2 | 2-Estrangeira, adquirida no mercado interno, exceto a indicada no código 7 |
| 3 | 3-Nacional, mercadoria ou bem com conteúdo de importação superior a 40% e inferior ou igual a 70% |
| 4 | 4-Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos |
| 5 | 5-Nacional, mercadoria ou bem com conteúdo de importação inferior ou igual a 40% |
| 6 | 6-Estrangeira, importação direta, sem similar nacional, constante em lista da CAMEX |
| 7 | 7-Estrangeira, adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX |
| 8 | 8-Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% |

### Opções para campo TEMIPICOMPRA (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| C | Conforme cadastro |
| N | Não tem IPI |
| S | Tem IPI |

### Opções para campo TEMIPIVENDA (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| C | Conforme cadastro |
| N | Não tem IPI |
| S | Tem IPI |

### Opções para campo CSTIPIENT (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| 00 | 00-Entrada c/Recuperação de Crédito |
| 01 | 01-Entrada c/Alíquota zero |
| 02 | 02-Entrada Isenta |
| 03 | 03-Entrada Não Tributada |
| 04 | 04-Entrada Imune |
| 05 | 05-Entrada c/Suspensão |
| -1 | (-1)-Não sujeita ao IPI |
| 49 | 49-Outras Entradas |

### Opções para campo CSTIPISAI (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| -1 | (-1)-Não sujeita ao IPI |
| 50 | 50-Saída Tributada |
| 51 | 51-Saída c/Alíquota zero |
| 52 | 52-Saída Isenta |
| 53 | 53-Saída Não Tributada |
| 54 | 54-Saída Imune |
| 55 | 55-Saída c/Suspensão |
| 99 | 99-Outras Saídas |

### Opções para campo CAT1799SPRES (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCONTEST (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| G | Grade |
| L | Número do lote |
| N | Sem controle adicional |
| P | Parceiro |
| V | Data da validade |

### Opções para campo USALOTEDTFAB (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USALOTEDTVAL (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMRASTROLOTE (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RASTSTULTENTRADA (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OBTSTANTMEDENT (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENQREINTEGRA (Tabela: TGFPEM)
| Valor | Descrição |
|-------|-----------|
| 1 | Gerar |
| 2 | Não Gerar |


## Tabela: TGFPJBH
### Descrição: Historico boletos rapido

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | USUARIO ALTERAÇÃO | I |  |
| `DTALT` | DATA MOVIMENTO | H |  |
| `SITREGBOL` | SITUAÇÃO BOLETO | S | Veja opções na seção OPÇÕES |
| `MOTIVO` | MOTIVO | S |  |
| `IDUNICO` | Nº IDENTIFICAÇÃO BOLETO | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo SITREGBOL (Tabela: TGFPJBH)
| Valor | Descrição |
|-------|-----------|
| A | Aguardando cancelamento |
| B | Baixado |
| C | Cancelado |
| E | Enviado |
| P | Pendente |
| R | Rejeitado |


## Tabela: TGFPPA
### Descrição: Parceiro Contato e Tipo de Parceiro

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPARC` | Cód. Parceiro | I |  |
| `CODTIPPARC` | Perfil | I |  |
| `CODCONTATO` | Contato | I |  |

## Tabela: TGFPPG
### Descrição: Gestao Fiscal Parcelas de Pagamento

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DIGVENDA` | Opção de digitação | S | Veja opções na seção OPÇÕES |
| `PRAZO` | Prazo | I |  |
| `PERCENTUAL` | Percentual | F |  |
| `CODBCOPAD` | Banco | I |  |
| `CODCENCUSPAD` | Centro Resultado Padrão | I |  |
| `CODNATPAD` | Natureza Padrão | I |  |
| `CODTIPTITPAD` | Tipo de Título | I |  |
| `CODCTABCOINT` | Conta Bancária | I |  |
| `TIPOEMP` | Tipo de Empresa | S | Veja opções na seção OPÇÕES |
| `CODEMP` | Empresa | I |  |
| `TIPOPAR` | Tipo de Parceiro | S | Veja opções na seção OPÇÕES |
| `CODPARC` | Parceiro | I |  |
| `FORMULA` | Fórmula | S |  |
| `CODPROJPAD` | Projeto | I |  |
| `BAIXA` | Baixa na confirmação | S | Veja opções na seção OPÇÕES |
| `CODTIPVENDA` | Tipo de Negociação | I |  |
| `TEXTOCENTRAL` | Texto parcela | S |  |
| `COR` | Cor da fonte | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `TIPRECDESP` | Tipo de Receita/Despesa | S |  |
| `DTFIX` | Vencto fixo | H |  |
| `BASEPRAZO` | Base do prazo | I | Veja opções na seção OPÇÕES |
| `VENCNAOUTIL` | Vencimento não útil | I | Veja opções na seção OPÇÕES |
| `SOMAPRAZOCLIENTE` | Soma prazo de cliente | S | Veja opções na seção OPÇÕES |
| `USARDTENTSAIGNRE` | Usar Dt. Entrada/Saída para vencimento da GNRE? | S | Veja opções na seção OPÇÕES |
| `PARCEXCLUSIVAFCPST` | Parcela exclusiva FCP-ST | S | Veja opções na seção OPÇÕES |
| `TIPOFIN` | Tipo de Financeiro (REC/DESP) | S | Veja opções na seção OPÇÕES |
| `AD_COMISSIONAR` | Gera comissão | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo DIGVENDA (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Digita |
| 1 | Digitar Data e Valor |
| 2 | Digitar Somente Data |
| 3 | Digitar Prazo e Valor |
| 4 | Digitar Somente Prazo |
| 5 | Digitar Somente Valor |

### Opções para campo TIPOEMP (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| C | C - Constante |
| E | E - Empresa |
| N | N - Negociação |
| X | X - Constante Exclusiva |

### Opções para campo TIPOPAR (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| C | C - Constante |
| D | D - Digita |
| N | N - Nota |
| T | T - Transportadora |
| V | V - Vendedor |
| X | X - Constante Exclusiva |

### Opções para campo BAIXA (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASEPRAZO (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| 0 | A partir do dia |
| -1 | Usar do Tipo de Negociação |
| 1 | Fora a semana |
| 2 | Fora a dezena |
| 3 | Fora a quinzena |
| 4 | Fora o mês |
| 5 | Quinzena/Fim mês |

### Opções para campo VENCNAOUTIL (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| 0 | Vencimento original |
| 1 | Antecipa vencimento se dia não útil |
| 2 | Posterga vencimento se dia não útil |

### Opções para campo SOMAPRAZOCLIENTE (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USARDTENTSAIGNRE (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PARCEXCLUSIVAFCPST (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOFIN (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| N | N - Usar da Natureza Padrão |
| T | T - Usar da TOP |

### Opções para campo AD_COMISSIONAR (Tabela: TGFPPG)
| Valor | Descrição |
|-------|-----------|
| nao | Não |


## Tabela: TGFPRC
### Descrição: Processo

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NROUNICO` | Nro. Único | I |  |
| `MSGRESULT` | Resultado | C |  |
| `IDPROC` | Cód. Processo | S |  |
| `TIPO` | Tipo | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `STATUS` | Status | S | Veja opções na seção OPÇÕES |
| `DHINI` | Data Início | H |  |
| `DHFIM` | Data Fim | H |  |
| `PARAMS` | Parâmetros | S |  |
| `XMLRESULT` | XMLRESULT | C |  |

## OPÇÕES DE CAMPOS

### Opções para campo STATUS (Tabela: TGFPRC)
| Valor | Descrição |
|-------|-----------|
| C | Cancelado |
| E | Erro |
| F | Finalizado |
| X | Em execução |


## Tabela: TGFPRI
### Descrição: Prioridades da restriçaõ ICMS

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `PRIORIDADE` | Prioridade | I |  |
| `TIPRESTRICAO1` | Tipo de Restrição 1 | S | Veja opções na seção OPÇÕES |
| `TIPRESTRICAO2` | Tipo de Restrição 2 | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPRESTRICAO1 (Tabela: TGFPRI)
| Valor | Descrição |
|-------|-----------|
| A | por tipo de transporte de importação |
| B | por capítulo do NCM |
| C | por cidade origem |
| D | por cidade destino |
| E | por grupo de ICMS do parceiro |
| F | por posição do NCM |
| G | por grupo de produtos |
| H | por NCM |
| I | por grupo de ICMS do produto |
| J | por grupo de ICMS do grupo de produto |
| K | Grupo de ICMS 2 |
| L | Produtor Rural |
| M | Código da Empresa |
| N | CONSUMIDOR |
| O | por TOP |
| P | por produto |
| Q | por Finalidade da Operação |
| R | por TARE |
| S | sem exceção |
| T | por perfil principal |
| U | por CFOP |
| X | Consumidor Contribuinte |

### Opções para campo TIPRESTRICAO2 (Tabela: TGFPRI)
| Valor | Descrição |
|-------|-----------|
| A | por tipo de transporte de importação |
| B | por capítulo do NCM |
| C | por cidade origem |
| D | por cidade destino |
| E | por grupo de ICMS do parceiro |
| F | por posição do NCM |
| G | por grupo de produtos |
| H | por NCM |
| I | por grupo de ICMS do produto |
| J | por grupo de ICMS do grupo de produto |
| K | Grupo de ICMS 2 |
| L | Produtor Rural |
| M | Código da Empresa |
| N | CONSUMIDOR |
| O | por TOP |
| P | por produto |
| Q | por Finalidade da Operação |
| R | por TARE |
| S | sem exceção |
| T | por perfil principal |
| U | por CFOP |
| X | Consumidor Contribuinte |


## Tabela: TGFPRO
### Descrição: Produtos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPROD` | Código | I |  |
| `ARMAZELOTE` | Armazena por Lote | S | Veja opções na seção OPÇÕES |
| `ONEROSO` | Oneroso | S | Veja opções na seção OPÇÕES |
| `CORFUNDOCONSPRECO` | Cor do Fundo | I |  |
| `CODFAB` | Cód. Fabricante | I |  |
| `CORFONTCONSPRECO` | Cor da Fonte | I |  |
| `CONTROLADO` | Controlado | S | Veja opções na seção OPÇÕES |
| `TIPO` | Tipo | S |  |
| `IDENCOSME` | Identificação de Cosmecêutico | S | Veja opções na seção OPÇÕES |
| `DESCRPROD` | Descrição | S |  |
| `IDENCORRELATO` | Identificação de Correlato | S | Veja opções na seção OPÇÕES |
| `DESCRPRODNFE` | Descrição para NFE | S |  |
| `CODPAT` | Princ. Ativo Medicamento | I |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `PRODFALTA` | Produto em Falta | S | Veja opções na seção OPÇÕES |
| `DTALTER` | Data de Alteração | H |  |
| `REFMERCMED` | Referência no Mercado de Medicamento | S | Veja opções na seção OPÇÕES |
| `RENDIMENTO` | Rendimento | S |  |
| `IDENOTC` | Identificação de OTC | S | Veja opções na seção OPÇÕES |
| `COMPLDESC` | Complemento | S |  |
| `IDENPORTARIA` | Identificação de Portaria | S |  |
| `CODGRUPOPROD` | Grupo | I |  |
| `STATUSMED` | Status do produto | I | Veja opções na seção OPÇÕES |
| `CODVOL` | Unidade padrão | S |  |
| `LISTALPM` | Lista de Procedimentos Médicos | S | Veja opções na seção OPÇÕES |
| `CODPARCFORN` | Parceiro Fornecedor preferencial | I |  |
| `TERMOLABIL` | Termolábil | S | Veja opções na seção OPÇÕES |
| `REFFORN` | Referência do Fornecedor | S |  |
| `TEMPMINIMA` | Temperatura Mínima em ºC | I |  |
| `FABRICANTE` | Fabricante | S |  |
| `TEMPMAXIMA` | Temperatura Máxima em ºC | I |  |
| `REFERENCIA` | Referência | S |  |
| `CODCPR` | Classificação | I |  |
| `LOCALIZACAO` | Localização | S |  |
| `SEQSPR` | Sub-Classificação | I |  |
| `SELECIONADO` | Seleção | S |  |
| `CODCAT` | Categoria | I |  |
| `TEMPOSERV` | Tempo Estimado | H |  |
| `SEQSCA` | Sub-Categoria | I |  |
| `MARCA` | Marca | S |  |
| `CODMARCA` | Marca | I |  |
| `CODTER` | Classe Terapêutica | I |  |
| `SEQSTE` | Sub-Terapêutica | I |  |
| `LOCAL` | Local | S | Veja opções na seção OPÇÕES |
| `USALOCAL` | Usa local | S | Veja opções na seção OPÇÕES |
| `ESTMIN` | Estoque Mínimo | F |  |
| `ESTMAX` | Estoque Máximo | F |  |
| `PROMOCAO` | Promoção | S | Veja opções na seção OPÇÕES |
| `DESCMAX` | % Desconto Máximo | F |  |
| `GRUPODESCPROD` | Grupo Desconto | S |  |
| `TEMCOMISSAO` | Calcular comissão | S | Veja opções na seção OPÇÕES |
| `COMVEND` | % Comissão vendedor | F |  |
| `COMGER` | % Comissão gerente | F |  |
| `CODMOEDA` | Moeda p/ preço | I |  |
| `TIPLANCNOTA` | Digitação na nota | S | Veja opções na seção OPÇÕES |
| `PESOBRUTO` | Peso bruto | F |  |
| `ARREDPRECO` | Múltiplo p/ Preço | F |  |
| `HOMEPAGE` | Home Page | S |  |
| `DECVLR` | Decimais para o valor | I |  |
| `DECQTD` | Decimais para quantidade | I |  |
| `ORIGPROD` | Origem do produto | S | Veja opções na seção OPÇÕES |
| `ENDIMAGEM` | Endereço da Imagem | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `MULTIPVENDA` | Multiplicador para venda | F |  |
| `DECCUSTO` | Decimais para o custo | I |  |
| `CODFORMPREC` | Fórmula de precificação | I |  |
| `CODFILTRO` | Filtro p/ Cálc.Custo baseado no Financeiro | I |  |
| `CODFILTROREQ` | Filtro p/ Cálc.Custo baseado na Requisição | I |  |
| `MEDAUX` | Medida auxiliar | F |  |
| `HRDOBRADA` | Hora Dobrada | S | Veja opções na seção OPÇÕES |
| `TEMISS` | Tem ISS | S | Veja opções na seção OPÇÕES |
| `TEMIRF` | Tem IRF | S | Veja opções na seção OPÇÕES |
| `PERCIRF` | % IRF | F |  |
| `REDBASEIRF` | % Red. Base IRF | F |  |
| `PRAZOVAL` | Prazo validade/tolerância | I |  |
| `MARGLUCRO` | % Margem de lucro | F |  |
| `TIPCONTEST` | Tipo de controle de estoque | S | Veja opções na seção OPÇÕES |
| `USOPROD` | Usado como | S | Veja opções na seção OPÇÕES |
| `PERCAUMENTCUSTO` | % Aviso Var. Custo | F |  |
| `TIPOITEMSPED` | Tipo do item p/ SPED | S | Veja opções na seção OPÇÕES |
| `CALCFUNTTELPRO` | Calcular FUNTTEL? | S | Veja opções na seção OPÇÕES |
| `BLOQVENDAFRAC` | Bloquear venda fracionada? | S | Veja opções na seção OPÇÕES |
| `TITCONTEST` | Título Controle de estoque | S |  |
| `CALCFUSTPRO` | Calcular FUST? | S | Veja opções na seção OPÇÕES |
| `SERVDESPNTRIB` | Tratar serviço como despesa não tributável no JSON? | S | Veja opções na seção OPÇÕES |
| `SERVPRESTTER` | Serviço prestado por terceiro? | S | Veja opções na seção OPÇÕES |
| `ALERTAESTMIN` | Alerta estoque mínimo | S | Veja opções na seção OPÇÕES |
| `ALIQFETHAB` | Alíquota FETHAB | F |  |
| `CODVOLCOMPRA` | Unid. Compra | S |  |
| `CODPRODROI` | Número do Item (Portaria 384/01) | S |  |
| `AGRUPMIN` | Agrupamento mínimo | F |  |
| `CODGENERO` | Gênero | I |  |
| `CODVOLFETHAB` | Unidade Padrão p/ FETHAB | S |  |
| `CODCENCUS` | Centro Resultado | I |  |
| `CARACTERISTICAS` | Características | S |  |
| `PRODINTERNO` | Considerar na Integração Impostos | S | Veja opções na seção OPÇÕES |
| `IMAGEM` | Imagem | B |  |
| `CODPROJ` | Projeto | I |  |
| `GERIMPNRETREINFAQ` | Gera Imposto não-retido evento 2055 da EFD-Reinf? | S | Veja opções na seção OPÇÕES |
| `PERCINSSESPECIAL` | % INSS Especial | F |  |
| `TIPOINSSESPECIAL` | Tipo de INSS Especial | S | Veja opções na seção OPÇÕES |
| `PERCENTSEPPUL` | Percentual para separação pulmão(0-100) | F |  |
| `TEMCIAP` | Atualizar CIAP? | S | Veja opções na seção OPÇÕES |
| `CODFILTROCTA` | Filtro p/ Cálc.Custo baseado em Lanç. Contábeis | I |  |
| `DESVIOMAXTOLCONFSEP` | Desvio máximo tolerado na conferência da separação | I |  |
| `DESVIOMINTOLCONFSEP` | Desvio mínimo tolerado na conferência da separação | I |  |
| `REGISTRARPESO` | Registrar peso | S | Veja opções na seção OPÇÕES |
| `FRAGMENTALOTE` | Fragmenta lote no envio para separação | S | Veja opções na seção OPÇÕES |
| `INCPESOBRUTO` | Incremento de peso bruto | F |  |
| `INCPESOLIQUIDO` | Incremento de peso líquido | F |  |
| `NURFE` | Modelo de etiqueta | I |  |
| `ATUNUVERSAO` | Atualizar versão | S |  |
| `INTEGRAFOX` | Integra com Sankhya Checkout | I |  |
| `NUVERSAO` | Versão | I |  |
| `GRADEPADRAO` | Grade Pradão | C |  |
| `TAMANHOMEDIOPECA` | Tamanho médio por peça (metros) | I |  |
| `ORDEMMEDIDA` | Ordem medida | F |  |
| `TIPOCONTAGEM` | Tipo de Contagem | S | Veja opções na seção OPÇÕES |
| `QTDEMB` | Quantidade de embalagens | I |  |
| `M3` | Metros Cúbicos | F |  |
| `PESOLIQ` | Peso líquido | F |  |
| `CODNAT` | Natureza | I |  |
| `APRESDETALHE` | Apresenta tela de detalhes | S | Veja opções na seção OPÇÕES |
| `INTEGRAECONECT` | Integrar com EConect | S | Veja opções na seção OPÇÕES |
| `CODVTP` | Meio de transporte | I |  |
| `COMERCIALIZACAOAGRI` | Comercialização Agrícola? | S | Veja opções na seção OPÇÕES |
| `MODETIQSEPWMS` | Modelo de etiqueta para separação | I |  |
| `IMPETIQSEPWMS` | Imprime etiqueta para separação | S | Veja opções na seção OPÇÕES |
| `MOTIVOINCEXC` | Filtro para motivos SubOS | S | Veja opções na seção OPÇÕES |
| `UTILIZAENDFLUT` | Utiliza endereço flutuante | S | Veja opções na seção OPÇÕES |
| `MAXMULTECONECT` | Máx. Multiplicador | I |  |
| `UTILSMARTCARD` | Utiliza SmartCard? | S | Veja opções na seção OPÇÕES |
| `QTDIDENTIF` | Qtd. identificadores | I |  |
| `TIPOIDENTIF` | Tipo identificador | S | Veja opções na seção OPÇÕES |
| `LISCONTEST` | Lista Controle de estoque | S |  |
| `IMPLAUDOLOTE` | Imprime laudo por lote | S | Veja opções na seção OPÇÕES |
| `CODGAR` | Extensão de garantia | I |  |
| `TEMMEDICAO` | Realiza controle por medição | S | Veja opções na seção OPÇÕES |
| `DESCMAXFLEX` | % Desconto Máximo Flex | F |  |
| `VISIVELAPPOS` | Apresentar no aplicativo de Ordem de Serviço | S | Veja opções na seção OPÇÕES |
| `DIMENSOES` | Informar dimensões | S | Veja opções na seção OPÇÕES |
| `CODPRODSUBKIT` | Código do Produto Substituto do Kit | I |  |
| `PERCQUEBRATEC` | % Quebra Técnica | F |  |
| `TIPOKIT` | Tipo de Kit | S | Veja opções na seção OPÇÕES |
| `CODCONFKIT` | Código Configuração Kit | I |  |
| `DESCVENCONSUL` | Desconsiderar nos result. venda consultiva | S | Veja opções na seção OPÇÕES |
| `PERCTOLPESOMENORSEP` | % de tolerância de peso a menor na separação | F |  |
| `CODLST` | Tipo de Serviço | I |  |
| `OBRACONSTCIVIL` | Obra de Construção Civil | I | Veja opções na seção OPÇÕES |
| `CODLOCALPADRAO` | Local Padrão | I |  |
| `CLASSIFCESSAOOBRA` | Classificação Cessão M.d.Obra | I | Veja opções na seção OPÇÕES |
| `CODGPROD` | Grupo Produção | I |  |
| `FIXOAGENDA` | Fixar na agenda | S | Veja opções na seção OPÇÕES |
| `SERFATURCON` | Série para faturamento em contratos | S |  |
| `TOPFATURCON` | TOP para faturamento em contratos | I |  |
| `EXIGELASTROCAMADAS` | Exige Lastro e Camadas | S | Veja opções na seção OPÇÕES |
| `USALOTEDTFAB` | Utiliza data de Fabricação | S | Veja opções na seção OPÇÕES |
| `USALOTEDTVAL` | Utiliza data de Validade | S | Veja opções na seção OPÇÕES |
| `CONTROLMEDIC` | Realiza controle por medição | S | Veja opções na seção OPÇÕES |
| `DTSUBST` | Data da Substituição do Produto | H |  |
| `CODPRODSUBST` | Código do Produto Substituto | I |  |
| `USACONTPESOVAR` | Produto controlado por peso variável | S | Veja opções na seção OPÇÕES |
| `PERCTOLPESOMAIOR` | % de tolerância de peso a maior no recebimento | F |  |
| `PERCTOLPESOMAIORSEP` | % de tolerância de peso a maior na separação | F |  |
| `PERCTOLPESOMENOR` | % de tolerância de peso a menor no recebimento | F |  |
| `CODPARCCONSIG` | Parceiro Consignante | I |  |
| `CODCOMP` | Componente do Serviço | I |  |
| `CODVOLPESOVAR` | Unidade de separação para produtos com peso variável | S |  |
| `DESVIOMAX` | % Desvio Máximo | F |  |
| `LOTECOMPMINIMO` | Compra Mínima | F |  |
| `ESTSEGQTD` | Estoque de Segurança | F |  |
| `ESTSEGDIAS` | Estoque de Segurança (dias úteis) | I |  |
| `DTALTERESQ` | Data de Alteração (Estoque de Segurança) | H |  |
| `LOTECOMPRAS` | Lote de Compra (dias úteis) | I |  |
| `AGRUPCOMPMINIMO` | Agrupamento Mínimo | F |  |
| `ARREDAGRUP` | Arredondamento para Agrupamento | F |  |
| `ESTMAXQTD` | Estoque Máximo | F |  |
| `ESTMAXDIAS` | Estoque Máximo (dias úteis) | I |  |
| `DTALTEREMQ` | Data de Alteração (Estoque Máximo) | H |  |
| `APLICASAZO` | Aplica Sazonalidade | S | Veja opções na seção OPÇÕES |
| `PADRAO` | Produto padrão | S | Veja opções na seção OPÇÕES |
| `ACRESCMAX` | % Acréscimo Máximo | F |  |
| `APLICACAO` | Aplicações | I |  |
| `APRESFORM` | Apresenta em fórmulas de composição | S | Veja opções na seção OPÇÕES |
| `BALANCA` | Utiliza balança | S | Veja opções na seção OPÇÕES |
| `CALCULOGIRO` | Calcular giro pelo agendador | S | Veja opções na seção OPÇÕES |
| `CARENCIA` | Carência (dias) | I |  |
| `CLASSEAGT` | Classe do agrotóxico | I |  |
| `CLASSETOX` | Classe tóxica | I |  |
| `CODBARBALANCA` | Cód.Barras Balança por Unidade | S | Veja opções na seção OPÇÕES |
| `CODBARCOMP` | Conferência por Codigo de Barras Composto | S | Veja opções na seção OPÇÕES |
| `CODFORMAPONTA` | Fórmula Apontamento | I |  |
| `CODPAIS` | País de origem | I |  |
| `CODPRODAGRUPAPT` | Produto/Serviço p/ agrupar apontamento | I |  |
| `CODPRODAGRUPAPTENC` | Produto/Serviço p/ agrupar apontamento de encarregado | I |  |
| `CODREGMAPA` | Registro no M.A.P.A | S |  |
| `CODRFA` | Regra armazenagem | I |  |
| `CODTRIBMUNISS` | Cód. Trib. Município NFS-e | S |  |
| `CODVOLPLAN` | Unid. Planejamento | S |  |
| `CODVOLRES` | Unidade para Resumo de Entrega | S |  |
| `CODVOLKANBAN` | Unidade de movimentação padrão | S |  |
| `COMPONOBRIG` | Validação de componentes | S | Veja opções na seção OPÇÕES |
| `CONCENTRACAO` | Concentração | S |  |
| `CONFCEGAPESO` | Conferência cega por peso | S | Veja opções na seção OPÇÕES |
| `CONFERE` | Confere por Cód. Barra | S | Veja opções na seção OPÇÕES |
| `CONVERVOL` | Conversão de Volume | F |  |
| `DIASEXPEDICAO` | Dias para Expedição | I |  |
| `DOSAGEM` | Dosagem indicada | F |  |
| `DOSAGEMPOR` | Qtd.Hectares/dosagem | F |  |
| `DTVALDIF` | Dt.Val. diferentes na armazenagem | S | Veja opções na seção OPÇÕES |
| `ENDMODROTULO` | Endereço do Modelo do Rótulo | S |  |
| `EXCLUIRCONF` | Excluir do processo de conferência | S | Veja opções na seção OPÇÕES |
| `EXIGEBENEFIC` | Exige beneficiamento | S |  |
| `FATTOTAL` | Faturar Total | S | Veja opções na seção OPÇÕES |
| `FLEX` | FLEX | S |  |
| `CODNBS` | Código NBS | I |  |
| `FORMULACAO` | Formulação | S |  |
| `AD_EMPRESA` | Empresa | I |  |
| `GERAPLAPROD` | Plan. Produção pelo Est. Mínimo | S | Veja opções na seção OPÇÕES |
| `AD_GRUPOCOM` | Grupo de Comissões | S | Veja opções na seção OPÇÕES |
| `GRUPOQUIMICO` | Grupo químico | I |  |
| `GRUPOTRANSG` | Grupo transg. | I |  |
| `IMPETIQCONF` | Imprime etiqueta de volumes na conferência | S | Veja opções na seção OPÇÕES |
| `IMPORDEMCORTE` | Imprime ordem de corte | S | Veja opções na seção OPÇÕES |
| `INFPUREZA` | Informa % Pureza e % Germinação | S | Veja opções na seção OPÇÕES |
| `INTERVALO` | Intervalo (dias) | I |  |
| `LARGURA` | Largura | F |  |
| `LASTRO` | Lastro | I |  |
| `LEADTIME` | Lead time de compra | I |  |
| `MANEJOINT` | Manejo integrado | S |  |
| `MODOAPLIC` | Modo de aplicação | S |  |
| `NOTIFCONF` | Notificação para conferência | S |  |
| `OBSETIQUETA` | Observação | S |  |
| `PERMCOMPPROD` | Permite comprar este produto? | S | Veja opções na seção OPÇÕES |
| `QTDNFLAUDOSINT` | Qtd. Notas entre laudos internos | I |  |
| `RASTRESTOQUE` | Rastreamento de Estoques | S | Veja opções na seção OPÇÕES |
| `CONESTORIGPROD` | Controla estoque por origem de produto | S | Veja opções na seção OPÇÕES |
| `RECEITUARIO` | Exige receituário agronômico | S |  |
| `RECUPAVARIA` | Recuperação de Avaria? | S | Veja opções na seção OPÇÕES |
| `REGRAWMS` | Regras de WMS | S | Veja opções na seção OPÇÕES |
| `REMETER` | Remeter? | S | Veja opções na seção OPÇÕES |
| `RENDIMENTOHA` | Dosagem/Ha Planejamento | F |  |
| `SHELFLIFE` | Shelf life | I |  |
| `SHELFLIFEMIN` | Shelf life mín. em recebimentos | I |  |
| `SOLCOMPRA` | Solicita compra? | S | Veja opções na seção OPÇÕES |
| `TAMLOTE` | Tamanho Lote | I |  |
| `TAMSERIE` | Tamanho Série | I |  |
| `TIPCONTESTWMS` | Usa controle adicional no WMS ? | S |  |
| `TIPSERNFE` | Tipo de série para NF-e | S | Veja opções na seção OPÇÕES |
| `UNIDADE` | Unid. de Medida | S |  |
| `UNIDMINARMAZ` | Unid. Min. Armazenagem WMS | S |  |
| `USACODBARRASQTD` | Cód.Barras com quantidade | S | Veja opções na seção OPÇÕES |
| `USAIMPAGRUPMIN` | Imprimir Etiqueta de Volume por Agrupamento Mínimo | S | Veja opções na seção OPÇÕES |
| `AD_CODFABRICANTE` | Cód. Fabricante | I |  |
| `AD_DESCABREV` | Abreviatura Descrição | S |  |
| `USASERIEFAB` | Exige Nro de Série do Fabricante | S | Veja opções na seção OPÇÕES |
| `ALIQNAC` | ALIQNAC | F |  |
| `USASERIESEPWMS` | Coletar Série na Conferência de Expedição do WMS? | S | Veja opções na seção OPÇÕES |
| `ALIQIMP` | ALIQIMP | F |  |
| `USASTATUSLOTE` | Usa Status de Lote | S | Veja opções na seção OPÇÕES |
| `UTILIZAWMS` | Controlado pelo WMS | S | Veja opções na seção OPÇÕES |
| `AD_PERPERDA` | Percentual de Perda | F |  |
| `VOLDOSAGEM` | Unidade dosagem | S |  |
| `VALCAPM3` | Validar capac.produção diária em M3 | S |  |
| `VALCBGLOBAL` | Valida Cód. Barra de Nro Série Global | S | Veja opções na seção OPÇÕES |
| `VENCOMPINDIV` | Aceitar venda fora do KIT | S | Veja opções na seção OPÇÕES |
| `VOLDOSAGEMPOR` | Volume dosagem por | S |  |
| `QTDAGRUPAMENTOMTZ` | Qtd. multiplicador Compra | F |  |
| `NATUREZAOPERDES` | Natureza da Operação de Declaração Eletrônica de Serviços | S |  |
| `CODAREASEP` | Cód.Área Separação | I |  |
| `AD_SUBPRODUTO` | Subproduto | S |  |
| `CNAE` | CNAE | I |  |
| `NROPROCESSO` | Nro do Processo Judicial/Adm (ISS) | S |  |
| `CAMADAS` | Camadas | I |  |
| `ESPESSURA` | Espessura/Profundidade | F |  |
| `ALTURA` | Altura | F |  |
| `CIENTIFICO` | Nome científico | S |  |
| `CODAUTCODIF` | Autorização CODIF | S |  |
| `CODCOS` | Status OS | I |  |
| `CULTURA` | Nome da cultura | S |  |
| `CODANP` | Código ANP | I |  |
| `EPOCAAPLIC` | Época de aplicação | S |  |
| `PRINCATIVO` | Princípio ativo | I |  |
| `NOMETAB` | Nome da tabela | S |  |
| `STATUSINCEXC` | Filtro para status SubOS | S | Veja opções na seção OPÇÕES |
| `TEMRASTROLOTE` | Tem Rastro do Lote | S | Veja opções na seção OPÇÕES |
| `CODANVISA` | Cód. ANVISA | S |  |
| `DESCRANP` | Descrição ANP | S |  |
| `PERCMISTGLP` | Percentual de mistura GLP | F |  |
| `PERCINDMISTURA` | Percentual do Índice de Mistura | F |  |
| `PERCMISTGNN` | Percentual de mistura de Gás Natural Nacional | F |  |
| `PERCMISTGNI` | Percentual de mistura de Gás Natural Importado | F |  |
| `VLRPARTIDAGLP` | Valor de Partida GLP | F |  |
| `CODIDCNAE` | Código ID CNAE | I |  |
| `CODSERVTELECOM` | Cód. Serviço de Telecomunicação | I |  |
| `MOTISENCAOANVISA` | Motivo Isenção Anvisa | S |  |
| `CODIGONFCOM` | Cód. Item NFCom | S |  |
| `IDGRADE` | Modelo de Grade | I |  |
| `STATUSNCM` | NCM Válido | S | Veja opções na seção OPÇÕES |
| `TIPUTILCOM` | Tipo de Utilização | I | Veja opções na seção OPÇÕES |
| `INDTIPREFBCICMSST` | Indicador de Tipo de Referência da BC do ICMS ST | S | Veja opções na seção OPÇÕES |
| `CODCTACTB` | Conta contábil 1 | I |  |
| `CODCTACTB2` | Conta contábil 2 | I |  |
| `CODCTACTB3` | Conta contábil 3 | I |  |
| `CODCTACTB4` | Conta contábil 4 | I |  |
| `WMSPRODRASTSERMED` | Produto rastreado por série e controle de medicamento | S | Veja opções na seção OPÇÕES |
| `APURAPRODEPE` | Cód. Apur. Inc. PRODEPE/FUNCRESCE | S | Veja opções na seção OPÇÕES |
| `INDESPPRODEPE` | Indicador Esp. Inc. PRODEPE/FUNCRESCE | S | Veja opções na seção OPÇÕES |
| `IDENTIMOB` | Identificação do Imobilizado | I | Veja opções na seção OPÇÕES |
| `UTILIMOB` | Utilização do Imobilizado | I | Veja opções na seção OPÇÕES |
| `CODNATREND` | Código Natureza Rendimento | I |  |
| `AD_CODAGRUP` | COD AGRUPAR | I |  |
| `TPIRRFEXT` | Tributação IRRF - Exterior REINF | I | Veja opções na seção OPÇÕES |
| `TEMICMS` | Calcular ICMS? | S | Veja opções na seção OPÇÕES |
| `CALCDIFAL` | Calcular DIFAL ? | S | Veja opções na seção OPÇÕES |
| `ICMSGERENCIA` | Considerar débito ICMS nas consultas gerenciais? | S | Veja opções na seção OPÇÕES |
| `OBTSTANTMEDENT` | Obtém ST Anterior pela média das entradas? | S | Veja opções na seção OPÇÕES |
| `TEMINSS` | Tem INSS? | S | Veja opções na seção OPÇÕES |
| `ALIQGERAL` | Alíquota Geral | F |  |
| `CODICMSFAST` | Alíquota ICMS do Fast Service | F |  |
| `ALIQICMSINTEFD` | Alíquota Interna de ICMS | F |  |
| `GRUPOICMS` | Grupo ICMS | I |  |
| `GRUPOICMS2` | Grupo de ICMS 2 | I |  |
| `MVAPADRAO` | MVA Padrão | F |  |
| `PERCREDBASEICMSEFET` | Perc. Red. Base Icms Efetivo | F |  |
| `PERCINSS` | % INSS | F |  |
| `MVAAJUSTADO` | % MVA Ajustado | F |  |
| `REDBASEINSS` | % Red. Base INSS | F |  |
| `NUMITEMREA` | Nro.Item REA/ICMS | I |  |
| `CODTAB` | Tabela c/ base p/ substituição na venda | I |  |
| `CLASSUBTRIB` | Classificação Substituição Tributária | I | Veja opções na seção OPÇÕES |
| `TIPOSN` | Tipo de Partilha/Anexo | I | Veja opções na seção OPÇÕES |
| `TIPSUBST` | Tipo de substituição | S | Veja opções na seção OPÇÕES |
| `CODESPECST` | CEST - Código Especificador ST | I |  |
| `CODAGREGACAO` | Cód. de Agregação | S |  |
| `CODBENEFNAUF` | Cód. de Benefício Fiscal na UF | S |  |
| `CODEXNCM` | Cód. Exceção NCM | I |  |
| `CODBARTRIBDIFGTIN` | Código de Barras da Un. Trib. diferente do padrão GTIN | S |  |
| `CODBARDIFGTIN` | Código de Barras diferente do padrão GTIN | S |  |
| `CNPJFABRICANTE` | CNPJ do Fabricante da Mercadoria | S |  |
| `PERCCMTEST` | % Carga Média Trib. Estadual | F |  |
| `PERCCMTFED` | % Carga Média Trib. Federal | F |  |
| `PERCCMTIMP` | % Carga Média Trib. Importação | F |  |
| `PERCCMTMUN` | % Carga Média Trib. Municipal | F |  |
| `PERCCMTNAC` | % Carga Média Trib. Nacional | F |  |
| `NCM` | NCM | S |  |
| `PRODUTONFE` | Cód. Produto p/ NF-e/NFC-e/CF-e | I | Veja opções na seção OPÇÕES |
| `TIPGTINNFE` | EAN/GTIN Produto p/ NF-e | I | Veja opções na seção OPÇÕES |
| `INDESCALA` | Indicador de Escala Relevante | S | Veja opções na seção OPÇÕES |
| `DESDESCCALCPIS` | Desconsiderar desconto no cálculo de PIS/COFINS? | S | Veja opções na seção OPÇÕES |
| `CALRUPTURAESTOQUE` | Calcula Ruptura de Estoque? | S | Veja opções na seção OPÇÕES |
| `TEMCREDPISCOFINSDEPR` | Tem Créd. PIS/COFINS sobre Deprec. mensal? | S | Veja opções na seção OPÇÕES |
| `NATEFDCONTM410M810` | Cód. Natureza (PIS/COFINS M410/M810) | I |  |
| `GRUPOCOFINS` | Grupo COFINS | S |  |
| `GRUPOPIS` | Grupo PIS | S |  |
| `GRUPOCSSL` | Grupo CSLL | S |  |
| `TEMIPICOMPRA` | Tem IPI na compra? | S | Veja opções na seção OPÇÕES |
| `TEMIPIVENDA` | Tem IPI na venda? | S | Veja opções na seção OPÇÕES |
| `CODENQIPIENT` | Código Enq. Legal IPI Entrada | I |  |
| `CODENQIPISAI` | Código Enq. Legal IPI Saída | I |  |
| `CODIPI` | IPI | I |  |
| `CSTIPIENT` | Código Sit.Trib.IPI Entrada | I | Veja opções na seção OPÇÕES |
| `CSTIPISAI` | Código Sit.Trib.IPI Saída | I | Veja opções na seção OPÇÕES |
| `PARTICIPAADRCST` | Considerar geração da ADRC-ST (PR)? | S | Veja opções na seção OPÇÕES |
| `PRODALIADRCST` | Produto alimentício conforme art. 119 do Anexo IX do RICMS/2017 PR? | S | Veja opções na seção OPÇÕES |
| `PRODSUJFECOP` | Produto sujeito ao FECOP? | S | Veja opções na seção OPÇÕES |
| `ALIQFECOP` | Alíquota FECOP | F |  |
| `MVAORIGINALADRCST` | MVA Original para ADRC-ST (PR) | F |  |
| `DESCPRODDRCST` | Desconsiderar produto na geração da DRCST? | S | Veja opções na seção OPÇÕES |
| `MVAORIGINALDRCST` | MVA Original para DRCST | F |  |
| `CONSPRODCAT42` | Considerar produto na geração da Cat 42? | S | Veja opções na seção OPÇÕES |
| `CAT1799SPRES` | Ressarcimento de ST (CAT-17/99)? | S | Veja opções na seção OPÇÕES |
| `ALIQINTERNACAT42` | Alíquota interna para CAT42 | F |  |
| `ENQREINTEGRA` | Enquadrado no Reintegra/Prev.? | S | Veja opções na seção OPÇÕES |
| `AP1RCTEGO` | Produto constante no apêndice I do RCTE/GO? | S | Veja opções na seção OPÇÕES |
| `CODATIVREINTEGRA` | Código Atividade Reintegra | S |  |
| `CODCPRB` | Cód. Atividade CPRB (Reintegra/Prev.) | S |  |
| `CODCTACTBEFD` | Conta Contábil para EFD | I |  |
| `CODFCI` | Código da FCI | S |  |
| `CODFCICALC` | Código da FCI | S |  |
| `VLRPARCIMPEXT` | Valor da Parcela Importada do Exterior - (R$) | F |  |
| `VLRPARCIMPEXTCALC` | Valor da Parcela Importada do Exterior - (R$) | F |  |
| `VLRCOMERC` | Valor de Comercialização - (R$) | F |  |
| `VLRCOMERCCALC` | Valor de Comercialização - (R$) | F |  |
| `OPEINTFETHAB` | Resp. pelo Recolhimento em Operações Internas | S | Veja opções na seção OPÇÕES |
| `OPEINTESTFETHAB` | Resp. pelo Recolhimento em Operações Interestaduais | S | Veja opções na seção OPÇÕES |
| `OPEEXPFETHAB` | Resp. pelo Recolhimento em Operações de Exportação | S | Veja opções na seção OPÇÕES |
| `AD_DESCAGR` | Descrição Agrupada | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo ARMAZELOTE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ONEROSO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONTROLADO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IDENCOSME (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IDENCORRELATO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODFALTA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REFMERCMED (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IDENOTC (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSMED (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 0 | Não classificado |
| 1 | Retirado do Mercado |
| 2 | Descontinuado |
| 3 | Não Faz Mais Parte do Mix |

### Opções para campo LISTALPM (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TERMOLABIL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo LOCAL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USALOCAL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROMOCAO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMCOMISSAO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPLANCNOTA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| A | Quant. e Valor Unitário |
| Q | Quantidade |
| T | Valor Total |
| U | Valor Unitário |
| V | Quant. e Valor Total |

### Opções para campo ORIGPROD (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 |
| 1 | 1-Estrangeira, importação direta, exceto a indicada no código 6 |
| 2 | 2-Estrangeira, adquirida no mercado interno, exceto a indicada no código 7 |
| 3 | 3-Nacional, mercadoria ou bem com conteúdo de importação superior a 40% e inferior ou igual a 70% |
| 4 | 4-Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos |
| 5 | 5-Nacional, mercadoria ou bem com conteúdo de importação inferior ou igual a 40% |
| 6 | 6-Estrangeira, importação direta, sem similar nacional, constante em lista da CAMEX |
| 7 | 7-Estrangeira, adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX |
| 8 | 8-Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% |

### Opções para campo HRDOBRADA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMISS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| I | Isento |
| N | Não tributado |
| S | Tributado |

### Opções para campo TEMIRF (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCONTEST (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| E | Série |
| G | Grade |
| I | Livre |
| L | Número do lote |
| N | Sem controle adicional |
| P | Parceiro |
| S | Lista |
| V | Data da validade |

### Opções para campo USOPROD (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| B | Brinde |
| C | Consumo |
| D | Revenda (por fórmula) |
| E | Embalagem |
| F | Brinde (NF) |
| I | Imobilizado |
| M | Matéria prima |
| O | Outros insumos |
| P | Em Processo |
| R | Revenda |
| T | Terceiros |
| V | Venda (fabricação própria) |
| 1 | Subproduto |
| 2 | Prod.Intermediário |
| 4 | Demonstração |

### Opções para campo TIPOITEMSPED (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| null | Utilizar do "Usado como" |
| 00 | Mercadoria para revenda |
| 01 | Matéria-Prima |
| 02 | Embalagem |
| 03 | Produtos em Processo |
| 04 | Produto Acabado |
| 05 | Subproduto |
| 06 | Produto Intermediário |
| 07 | Material de Uso e Consumo |
| 08 | Ativo Imobilizado |
| 09 | Serviços |
| 10 | Outros Insumos |
| 99 | Outras |

### Opções para campo CALCFUNTTELPRO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BLOQVENDAFRAC (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCFUSTPRO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SERVDESPNTRIB (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SERVPRESTTER (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALERTAESTMIN (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODINTERNO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Código de barras |
| S | Código do produto |

### Opções para campo GERIMPNRETREINFAQ (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOINSSESPECIAL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 1 | INSS 15 anos |
| 2 | INSS 20 anos |
| 3 | INSS 25 anos |

### Opções para campo TEMCIAP (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGISTRARPESO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| A | Pela balança |
| AM | Balança/manual |
| M | Manualmente |
| N | Não Registrar |

### Opções para campo FRAGMENTALOTE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOCONTAGEM (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| C | Contagem cumulativa |
| D | Considerar configuração |
| P | Contagem única por produto |
| Q | Contagem cumulativa com qtd |

### Opções para campo APRESDETALHE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTEGRAECONECT (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COMERCIALIZACAOAGRI (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMPETIQSEPWMS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| P | Sim (por produto) |
| S | Sim (por unidade) |

### Opções para campo MOTIVOINCEXC (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| E | Exceção (Não pode ser usado com) |
| I | Restrição (Só pode ser usado com) |
| N | Nenhum |

### Opções para campo UTILIZAENDFLUT (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILSMARTCARD (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOIDENTIF (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| SERIAL | Número serial |

### Opções para campo IMPLAUDOLOTE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMMEDICAO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VISIVELAPPOS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIMENSOES (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOKIT (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| D | Composição Padrão |
| P | Composição Personalizada |

### Opções para campo DESCVENCONSUL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OBRACONSTCIVIL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Empreitada Total |
| 2 | 2 - Empreitada Parcial |

### Opções para campo CLASSIFCESSAOOBRA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 100000001 | Limpeza, conservação ou zeladoria |
| 100000002 | Vigilância ou segurança |
| 100000003 | Construção civil |
| 100000004 | Serviços de natureza rural |
| 100000005 | Digitação |
| 100000006 | Preparação de dados para processamento |
| 100000007 | Acabamento |
| 100000008 | Embalagem |
| 100000009 | Acondicionamento |
| 100000010 | Cobrança |
| 100000011 | Coleta ou reciclagem de lixo ou de resíduos |
| 100000012 | Copa |
| 100000013 | Hotelaria |
| 100000014 | Corte ou ligação de serviços públicos |
| 100000015 | Distribuição |
| 100000016 | Treinamento e ensino |
| 100000017 | Entrega de contas e de documentos |
| 100000018 | Ligação de medidores |
| 100000019 | Leitura de medidores |
| 100000020 | Manutenção de instalações, de máquinas ou de equipamentos |
| 100000021 | Montagem |
| 100000022 | Operação de máquinas, de equipamentos e de veículos |
| 100000023 | Operação de pedágio ou de terminal de transporte |
| 100000024 | Operação de transporte de passageiros |
| 100000025 | Portaria, recepção ou ascensorista |
| 100000026 | Recepção, triagem ou movimentação de materiais |
| 100000027 | Promoção de vendas ou de eventos |
| 100000028 | Secretaria e expediente |
| 100000029 | Saúde |
| 100000030 | Telefonia ou telemarketing |
| 100000031 | Trabalho temporário na forma da Lei nº 6.019, de janeiro de 1974 |

### Opções para campo FIXOAGENDA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGELASTROCAMADAS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USALOTEDTFAB (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USALOTEDTVAL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONTROLMEDIC (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USACONTPESOVAR (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APLICASAZO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PADRAO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APRESFORM (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BALANCA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCULOGIRO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| E | Não |
| G | Sim |

### Opções para campo CODBARBALANCA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODBARCOMP (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COMPONOBRIG (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| I | Qtd.Iguais |
| N | Opcional |
| S | Obrigatório |

### Opções para campo CONFCEGAPESO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONFERE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DTVALDIF (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| M | Apenas datas dentro do mesmo mês |
| N | Nunca aceitar datas diferentes |
| Q | Apenas datas dentro da mesma quinzena |
| S | Apenas datas dentro da mesma semana |
| X | Aceitar datas diferentes |

### Opções para campo EXCLUIRCONF (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FATTOTAL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERAPLAPROD (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AD_GRUPOCOM (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 1 | Extra |
| 2 | Comercial |
| 4 | Promoção - 12,74% |
| 5 | Promoção - 17,06% |
| 6 | Promoção - 20% |

### Opções para campo IMPETIQCONF (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMPORDEMCORTE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INFPUREZA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMCOMPPROD (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RASTRESTOQUE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| C | Rastrear com Controle |
| L | Rastrear com Controle e Local |
| N | Sem rastreamento |
| O | Rastrear com Local |
| S | Rastrear |

### Opções para campo CONESTORIGPROD (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECUPAVARIA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGRAWMS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| F | FIFO |
| O | Ordem |

### Opções para campo REMETER (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| D | Dependente |
| N | Não |
| S | Sim |

### Opções para campo SOLCOMPRA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPSERNFE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| F | Fabricante |
| P | Padrão |

### Opções para campo USACODBARRASQTD (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USAIMPAGRUPMIN (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USASERIEFAB (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USASERIESEPWMS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USASTATUSLOTE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZAWMS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALCBGLOBAL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VENCOMPINDIV (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSINCEXC (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| E | Exceção (Não pode ser usado com) |
| I | Restrição (Só pode ser usado com) |
| N | Nenhum |

### Opções para campo TEMRASTROLOTE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSNCM (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPUTILCOM (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Telefonia |
| 2 | 2 - Comunicação de dados |
| 3 | 3 - TV por Assinatura |
| 4 | 4 - Provimento de acesso à Internet |
| 5 | 5 - Multimídia |
| 6 | 6 - Outros |
| 7 | 7 - Vários |

### Opções para campo INDTIPREFBCICMSST (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Base de cálculo referente ao preço tabelado ou preço máximo sugerido |
| 1 | 1 - Base cálculo – Margem de valor agregado |
| 2 | 2 - Base de cálculo referente à Lista Negativa |
| 3 | 3 - Base de cálculo referente à Lista Positiva |
| 4 | 4 - Base de cálculo referente à Lista Neutra |

### Opções para campo WMSPRODRASTSERMED (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APURAPRODEPE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 01 | Sem incentivo |
| 02 | Com incentivo |

### Opções para campo INDESPPRODEPE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 01 | Sem incentivo |
| 02 | Com incentivo |

### Opções para campo IDENTIMOB (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 1 | Edif.e Benfeitorias em Imóveis Próprios |
| 2 | Edif.e Benfeitorias em Imóveis de Terceiros |
| 3 | Instalações |
| 4 | Máquinas |
| 5 | Equipamentos |
| 6 | Veículos |
| 99 | Outros |

### Opções para campo UTILIMOB (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 1 | Produção de Bens Destinados a Venda |
| 2 | Prestação de Serviços |
| 3 | Locação a Terceiros |
| 9 | Outros |

### Opções para campo TPIRRFEXT (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 10 | 10 - Retenção do IRRF - alíquota padrão |
| 11 | 11 - Retenção do IRRF - alíquota da tabela progressiva |
| 12 | 12 - Retenção do IRRF - alíquota diferenciada (países com tributação favorecida) |
| 13 | 13 - Retenção do IRRF - alíquota limitada conforme cláusula em convênio |
| 30 | 30 - Retenção do IRRF - outras hipóteses |

### Opções para campo TEMICMS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCDIFAL (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ICMSGERENCIA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OBTSTANTMEDENT (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMINSS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CLASSUBTRIB (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 1 | Açucar de cana |
| 10 | Tintas e vernizes e outras mercadorias |
| 11 | Veículos automotores |
| 12 | Outros |
| 13 | Lâmina de Barbear, Aparelho de Barbear Descart.e Isqueiro |
| 14 | Peças, componentes e acessórios de produtos autopropulsados |
| 15 | Materiais de construção, acabamento, bricolagem ou adorno |
| 16 | Ferramentas |
| 17 | Material de Limpeza |
| 18 | Material Elétrico |
| 19 | Máquinas e aparelhos mecânicos, elétricos, eletromecânicos e automáticos |
| 2 | Carne bovina, bufalina e suína |
| 20 | Máquinas e Ferramentas |
| 3 | Cerveja/chope/refr., água mineral/pot. envasada e gelo |
| 4 | Cigarros e outros produtos derivados do fumo |
| 5 | Cimento |
| 6 | Derivados de petróleo, lubrificantes e outros produtos |
| 7 | Medicamentos e outros produtos |
| 8 | Pneumáticos, câmaras de ar e protetores de borracha |
| 9 | Sorvetes |

### Opções para campo TIPOSN (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 1 | Anexo I - Comércio |
| 2 | Anexo II - Indústria |
| 3 | Anexo III - Rec. de locação de bens/móveis e prest. de serv. não relac. no § 5o-C do art. 18 da Lei |
| 4 | Anexo IV - Rec. decorrentes da prest. de serv. relacionados no § 5o-C do art. 18 da Lei |
| 5 | Serviços de Atividades Físicas, Computação, Adm. e Loc. de Imóveis de Terceiros, Outros |
| 6 | Serviços da Atividade Intelectual como Medicina, Consultorias, Engenharia, Outros |
| 7 | Anexo V - Rec. decorrentes da prest. de serv. relacionados no § 5o-I do art. 18 da Lei |

### Opções para campo TIPSUBST (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| A | Subst. na compra e na venda |
| C | Revenda com subst. tributária (cálculo de Subst. na compra) |
| N | Não tem |
| P | Venda com subst. tributária (cálculo de Subst. na venda) |

### Opções para campo PRODUTONFE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 0 | Código do Produto |
| 1 | Referência |

### Opções para campo TIPGTINNFE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Informar |
| 1 | Código do Produto |
| 2 | Referência |
| 3 | Código de Barras Estoque |
| 4 | Cód.Barras da Unid.Alternativa ou a Referência |

### Opções para campo INDESCALA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Produzido em Escala NÃO Relevante |
| null | Não se aplica |
| S | Produzido em Escala Relevante |

### Opções para campo DESDESCCALCPIS (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALRUPTURAESTOQUE (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMCREDPISCOFINSDEPR (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMIPICOMPRA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMIPIVENDA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CSTIPIENT (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Entrada c/Recuperação de Crédito |
| -1 | (-1)-Não sujeita ao IPI |
| 1 | 01-Entrada c/Alíquota zero |
| 2 | 02-Entrada Isenta |
| 3 | 03-Entrada Não Tributada |
| 4 | 04-Entrada Imune |
| 49 | 49-Outras Entradas |
| 5 | 05-Entrada c/Suspensão |

### Opções para campo CSTIPISAI (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| -1 | (-1)-Não sujeita ao IPI |
| 50 | 50-Saída Tributada |
| 51 | 51-Saída c/Alíquota zero |
| 52 | 52-Saída Isenta |
| 53 | 53-Saída Não Tributada |
| 54 | 54-Saída Imune |
| 55 | 55-Saída c/Suspensão |
| 99 | 99-Outras Saídas |

### Opções para campo PARTICIPAADRCST (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODALIADRCST (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODSUJFECOP (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCPRODDRCST (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSPRODCAT42 (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CAT1799SPRES (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENQREINTEGRA (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AP1RCTEGO (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OPEINTFETHAB (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| D | Destinatário |
| R | Remetente |

### Opções para campo OPEINTESTFETHAB (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| D | Destinatário |
| R | Remetente |

### Opções para campo OPEEXPFETHAB (Tabela: TGFPRO)
| Valor | Descrição |
|-------|-----------|
| D | Destinatário |
| R | Remetente |


## Tabela: TGFRAT
### Descrição: Rateio por Natureza de Receita e Despesa

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `PERCRATEIO` | % Rateio | F |  |
| `CODCENCUS` | Cód.Centro Resultado | I |  |
| `CODNAT` | Cód. Natureza | I |  |
| `CODPROJ` | Projeto | I |  |
| `CODCTACTB` | Conta Contábil | I |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `CODSITE` | Site | I |  |
| `DIGITADO` | Digitado | S | Veja opções na seção OPÇÕES |
| `NUFIN` | Num. Financeiro | I |  |
| `NUMCONTRATO` | Num. Contrato | I |  |
| `ORIGEM` | Origem | S | Veja opções na seção OPÇÕES |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | DTALTER | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo DIGITADO (Tabela: TGFRAT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ORIGEM (Tabela: TGFRAT)
| Valor | Descrição |
|-------|-----------|
| E | Estoque |
| F | Financeiro |
| P | Pessoal |


## Tabela: TGFREG
### Descrição: Regras

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODREGRA` | Regra | I |  |
| `DESCRREGRA` | Descrição | S |  |
| `INSTPRINC` | Instância Principal | S |  |
| `INSTSEC` | Instância Secundária | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Data da Alteração | H |  |
| `TIPO` | Permissão | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TGFREG)
| Valor | Descrição |
|-------|-----------|
| P | Permitido |
| R | Proibido |


## Tabela: TGFREJNFE
### Descrição: Rejeição NFe

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Nota | I |  |
| `CODREJEICAO` | Cód. Rejeição | I |  |
| `QTDREJEICOES` | Qtd. Rejeições | I |  |
| `HASHUTLREJEICAO` | Hash Ultima Rejeição | S |  |

## Tabela: TGFREN
### Descrição: GF Mapeamento das Renegociações

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Cód. Usuário | I |  |
| `NUFIN` | Número do financeiro | I |  |
| `NURENEGORIG` | Número da renegociação de origem | I |  |
| `DHALTER` | Data e hora da alteração | H |  |
| `NURENEG` | Número da renegociação | I |  |

## Tabela: TGFREP
### Descrição: Restrições da TOP

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DESCRICAO` | Descrição | S |  |
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `TIPREST` | Tipo Restrição | S | Veja opções na seção OPÇÕES |
| `CODCOLREST` | Coluna de Restrição | I |  |
| `SERIE` | Série | S |  |
| `RESTRICAO` | Restringe a TOP | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPREST (Tabela: TGFREP)
| Valor | Descrição |
|-------|-----------|
| A | Parceiro |
| B | Local |
| C | Centro de Resultado |
| D | TOP Destino |
| E | Empresa |
| G | Grupo de Produto |
| I | Top Baixa |
| L | Perfil |
| N | Natureza |
| O | Grupo de usuário |
| P | Produto |
| R | Região Vendedor |
| S | Série |
| T | Tipo de Negociação |
| U | Usuário |
| V | Vendedor |


## Tabela: TGFRGV
### Descrição: GF Relacionamento de grupos por vendedores

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODGRUPOPROD` | Grupo de Produto | I |  |
| `CODVEND` | Vendedor | I |  |

## Tabela: TGFRNG
### Descrição: RegraNegocio

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NURNG` | Num. Regra | I |  |
| `DESCRICAO` | Descrição | S |  |
| `ATIVO` | Ativa | S | Veja opções na seção OPÇÕES |
| `TIPOEXPRESSAO` | Tipo de expressão | S | Veja opções na seção OPÇÕES |
| `ONDE` | Onde | S | Veja opções na seção OPÇÕES |
| `QUANDO` | Quando | S | Veja opções na seção OPÇÕES |
| `EVENTO` | Evento de liberação | I |  |
| `CODUSULIB` | Cód. Usuário Liberador | I |  |
| `EXPRESSAO` | Expressão | S |  |
| `CONFIG` | Expressão | C |  |
| `INIBELIB` | Inibe alteração do liberador | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFRNG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOEXPRESSAO (Tabela: TGFRNG)
| Valor | Descrição |
|-------|-----------|
| JAVA | Rotina Java |
| SCRIPT | Script |
| STP | Stored Procedure |

### Opções para campo ONDE (Tabela: TGFRNG)
| Valor | Descrição |
|-------|-----------|
| FINANC | Financeiro |
| PORTAIS | Portais |
| VENDASSIS | Venda Assistida |

### Opções para campo QUANDO (Tabela: TGFRNG)
| Valor | Descrição |
|-------|-----------|
| CONFIRM | Confirmação |
| SAVECAB | Inclusão / Alteração Cabeçalho |
| SAVEITE | Inclusão / Alteração Itens |

### Opções para campo INIBELIB (Tabela: TGFRNG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFSBC
### Descrição: Saldos Bancários

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCTABCOINT` | Conta bancária | I |  |
| `SALDOREAL` | Saldo real | F |  |
| `SALDOBCO` | Saldo bancário | F |  |
| `REFERENCIA` | Referência | H |  |

## Tabela: TGFSTG
### Descrição: Tabelas do Sintegra

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Gênero | I |  |
| `DESCRICAO` | Descrição | S |  |
| `CHAVE` | Chave | I |  |

## Tabela: TGFTAB
### Descrição: TabelaPreco

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUTAB` | Nro. Único | I |  |
| `DTVIGOR` | Dt. Vigor | D |  |
| `PERCENTUAL` | Percentual % | F |  |
| `UTILIZADECCUSTO` | Utiliza decimais do custo para preço | S |  |
| `CODTABORIG` | Tabela de Origem | I |  |
| `DTALTER` | Dt. Alteração | D |  |
| `CODTAB` | Código Tabela | I |  |
| `JAPE_ID` | JAPE_ID | S |  |

## Tabela: TGFTAG
### Descrição: Tarefas Agendadas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUAGENDAMENTO` | Nro. agendamento | I |  |
| `TIPOAGE` | Tipo Agendamento | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `DESCRICAO` | Descrição agendamento | S |  |
| `CONFIG` | Configuração | C |  |
| `DHPROXEXEC` | Próxima execução em | H |  |
| `DHULTEXEC` | Data Final de Execução | H |  |
| `CODEMP` | Empresa | I |  |
| `GERALOTEPARA` | Gerar Lote para | S | Veja opções na seção OPÇÕES |
| `DIASEMANA` | Agendar os dias da Semana | S |  |
| `HORARIO` | Agendar os Horários | S |  |
| `DIAMES` | Agendar os Dias do Mês | S |  |
| `MES` | Agendar os Meses | S |  |
| `TIPOEXEC` | Tipo Execução | S | Veja opções na seção OPÇÕES |
| `DHEXECUCAO` | Data da ultima execução | H |  |
| `STATUSULTEXEC` | Status Última Execução | S | Veja opções na seção OPÇÕES |
| `INFO` | Informações | C |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo GERALOTEPARA (Tabela: TGFTAG)
| Valor | Descrição |
|-------|-----------|
| P | NF-e |
| S | NFS-e |

### Opções para campo TIPOEXEC (Tabela: TGFTAG)
| Valor | Descrição |
|-------|-----------|
| A | Automático |
| B | Ambos |
| M | Manual |

### Opções para campo STATUSULTEXEC (Tabela: TGFTAG)
| Valor | Descrição |
|-------|-----------|
| E | Erro |
| F | Finalizado |

### Opções para campo ATIVO (Tabela: TGFTAG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFTCA
### Descrição: Tabela de Totalizadores Adicionais

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nr Único da Nota | I |  |

## Tabela: TGFTIT
### Descrição: Tipos de Título

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `CODTIPTIT` | Tipo de Título | I |  |
| `DESCRTIPTIT` | Descrição | S |  |
| `SUBTIPOVENDA` | Subtipo | S | Veja opções na seção OPÇÕES |
| `ESPDOC` | Espécie | S |  |
| `CREDENCIADORACFE` | Instituição Credenciadora do Cartão | S | Veja opções na seção OPÇÕES |
| `CARENCIA` | Float(Carência) | I |  |
| `CONSDIASUTEIS` | Considerar dias úteis | S | Veja opções na seção OPÇÕES |
| `FISCAL` | Forma Pagamento TEF | S |  |
| `CARTAOTAXA` | % Taxa Administradora | F |  |
| `VALIDAQTDMAXTITVENCIDOS` | Validar Qtd. Máx. Títulos Vencidos | S | Veja opções na seção OPÇÕES |
| `EXIBBAIX` | Mensagem p/exibir na tela de baixa | S |  |
| `GRUPOLIMCRED` | Grupo p/Limite Crédito | S |  |
| `CODMOEDA` | Moeda | I |  |
| `PERCJUROS` | % Juros | F |  |
| `PERCMULTA` | % Multa | F |  |
| `EXPTES` | Exportação para TES | S | Veja opções na seção OPÇÕES |
| `EXPGRS` | Exportação para GRS | I | Veja opções na seção OPÇÕES |
| `EXIGBAIXAACERTO` | Valor Baixado deve ser igual ao Retornado? | S | Veja opções na seção OPÇÕES |
| `TRANSFDIF` | Transferir a diferença entre o valor Retornado e o Baixado? | S | Veja opções na seção OPÇÕES |
| `INDTIT` | Indicador do Tipo de Título | I | Veja opções na seção OPÇÕES |
| `TRANSFPEND` | Pode transferir título pendente? | S | Veja opções na seção OPÇÕES |
| `TRANSFBAIX` | Pode transferir depois de baixado? | S | Veja opções na seção OPÇÕES |
| `CODGRUPOTIPTIT` | Grupo | I |  |
| `CODCTACTB` | Conta Contábil 1 | I |  |
| `CODCTACTB2` | Conta Contábil 2 | I |  |
| `CODCTACTB3` | Conta Contábil 3 | I |  |
| `BAIXACERTO` | Pode Baixar? | S | Veja opções na seção OPÇÕES |
| `CARTAODESC` | Taxa Administradora | F |  |
| `PERCCUSVAR` | % Custo variável | F |  |
| `VLRCUSVAR` | Valor Custo Variável | F |  |
| `FASTUSA` | Utiliza no Fast Service? | S | Veja opções na seção OPÇÕES |
| `FASTBAIXA` | Baixa automática? | S | Veja opções na seção OPÇÕES |
| `CONFERENCIA` | Conferência | S | Veja opções na seção OPÇÕES |
| `IMPCOMPROVANTE` | Imprime comprovante? | S | Veja opções na seção OPÇÕES |
| `IMPBOLRENEG` | Imprimir Pix/Boleto/Duplicata p/os títulos renegociados? | S | Veja opções na seção OPÇÕES |
| `IMAGEM` | Imagem | B |  |
| `CODPARCTEF` | Parc.Administradora | I |  |
| `CODRECGNRE` | Código da Receita (GNRE) | I |  |
| `CODDETRECGNRE` | Código Detalhamento Receita (GNRE) | I |  |
| `CODPRODGNRE` | Código do Produto (GNRE) | I |  |
| `AJUSTAVP` | Ajusta Valor Presente | S | Veja opções na seção OPÇÕES |
| `TPAGNFCE` | Tipo de pgto para NFC-e / NF-e / CF-e | S | Veja opções na seção OPÇÕES |
| `PRAZO` | Prazo | I |  |
| `UTILIZAPOS` | Utiliza POS | S | Veja opções na seção OPÇÕES |
| `TIMUSADOLOCACAO` | Utilizado na Locação | S | Veja opções na seção OPÇÕES |
| `NROPARCELAS` | Nro. Parcelas | I |  |
| `NSUOPCIONALPOS` | Informar NSU opcional | S | Veja opções na seção OPÇÕES |
| `INTEGRAECONECT` | Integração EConect | S | Veja opções na seção OPÇÕES |
| `CODFINALIZADORA` | Cód. Finalizadora | I |  |
| `GRUPOFINALIZADORA` | Grupo Finalizadora | I |  |
| `CODBANDEIRAECONECT` | Bandeira Cartão | S |  |
| `CONVENIOECONECT` | Convênio | S | Veja opções na seção OPÇÕES |
| `OPERACAOCTF` | Operação CTF | S | Veja opções na seção OPÇÕES |
| `DIAVENC` | Vencimento | I |  |
| `TIPVENC` | Tipo vencimento | S | Veja opções na seção OPÇÕES |
| `QTDPARCELCTF` | Qtd. parcelas | I |  |
| `RECEBANTAPROV` | Receber antes de aprovar a nota | S | Veja opções na seção OPÇÕES |
| `ARREDPRIMEIRAPARC` | Ajusta arredondamento na 1ª parcela | S | Veja opções na seção OPÇÕES |
| `TRUNCPARCELA` | Truncar valores no parcelamento | S | Veja opções na seção OPÇÕES |
| `TIPDOCRURAL` | Tipo Documento Rural | S | Veja opções na seção OPÇÕES |
| `DESCRTPAGNFCE` | Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros) | S |  |
| `PROIBIMPBOL` | Proibir impressão boleto? | S | Veja opções na seção OPÇÕES |
| `ULTILIZAPDVWEB` | Tip. título cartão principal PDV Web | S | Veja opções na seção OPÇÕES |
| `ALTERASIMULTPV` | Permite alteração no tipo de negociação | S | Veja opções na seção OPÇÕES |
| `INDRECEFDCONT` | Indicador de Receita (registro F525 - EFD Cont.) | S | Veja opções na seção OPÇÕES |
| `INFCOMPLEFDCONT` | Informações complem. (registro F525 - EFD Cont.) | S |  |
| `NROPARCELASMAX` | Qtd de parcelas Máxima | I |  |
| `VLRPARCMINCART` | Valor de parcela minima para cartões | F |  |
| `INFCMC7` | Informar CMC7? | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SUBTIPOVENDA (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| 1 | A vista |
| 10 | PIX |
| 11 | PIX POS |
| 2 | A prazo |
| 3 | Parcelada |
| 4 | Cheque pré-datado |
| 5 | Crediário |
| 6 | Financeira |
| 7 | Cartão de crédito |
| 8 | Cartão de débito |
| 9 | Voucher |

### Opções para campo CREDENCIADORACFE (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| 001 | Administradora de Cartões Sicredi Ltda. |
| 002 | Administradora de Cartões Sicredi Ltda.(filial RS) |
| 003 | Banco American Express S/A - AMEX |
| 004 | BANCO GE - CAPITAL |
| 006 | BANCO TOPÁZIO S/A |
| 007 | BANCO TRIANGULO S/A |
| 008 | BIGCARD Adm. de Convenios e Serv. |
| 009 | BOURBON Adm. de Cartões de Crédito |
| 010 | CABAL Brasil Ltda. |
| 011 | CETELEM Brasil S/A - CFI |
| 012 | CIELO S/A |
| 013 | CREDI 21 Participações Ltda. |
| 014 | ECX CARD Adm. e Processadora de Cartões S/A |
| 015 | Empresa Bras. Tec. Adm. Conv. Hom. Ltda. - EMBRATEC |
| 016 | EMPÓRIO CARD LTDA |
| 017 | FREEDDOM e Tecnologia e Serviços S/A |
| 018 | FUNCIONAL CARD LTDA. |
| 019 | HIPERCARD Banco Multiplo S/A |
| 020 | MAPA Admin. Conv. e Cartões Ltda. |
| 021 | Novo Pag Adm. e Proc. de Meios Eletrônicos de Pagto. Ltda. |
| 022 | PERNAMBUCANAS Financiadora S/A Crédito, Fin. e Invest |
| 023 | POLICARD Systems e Serviços Ltda. |
| 024 | PROVAR Negócios de Varejo Ltda. |
| 025 | REDECARD S/A |
| 026 | RENNER Adm. Cartões de Crédito Ltda. |
| 027 | RP Administração de Convênios Ltda. |
| 028 | SANTINVEST S/A Crédito, Financiamento e Investimentos |
| 029 | SODEXHO Pass do Brasil Serviços e Comércio S/A |
| 030 | SOROCRED Meios de Pagamentos Ltda. |
| 031 | Tecnologia Bancária S/A - TECBAN |
| 032 | TICKET Serviços S/A |
| 033 | TRIVALE Administração Ltda |
| 034 | Unicard Banco Múltiplo S/A - TRICARD |
| 999 | Outros |

### Opções para campo CONSDIASUTEIS (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALIDAQTDMAXTITVENCIDOS (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXPTES (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| A | Arrecadação |
| N | Não exporta |
| R | Reclamação cobrança indevida - RI |

### Opções para campo EXPGRS (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Exporta |
| 1 | Inclusão |
| 2 | Cancelamento |

### Opções para campo EXIGBAIXAACERTO (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRANSFDIF (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDTIT (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Duplicata |
| 1 | 01-Cheque |
| 2 | 02-Promissória |
| 3 | 03-Recibo |
| 99 | 99-Outros |

### Opções para campo TRANSFPEND (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRANSFBAIX (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BAIXACERTO (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FASTUSA (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FASTBAIXA (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONFERENCIA (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMPCOMPROVANTE (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMPBOLRENEG (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AJUSTAVP (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TPAGNFCE (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Dinheiro |
| 02 | 02-Cheque |
| 03 | 03-Cartão de Crédito |
| 04 | 04-Cartão de Débito |
| 05 | 05 - Cartão da Loja (Private Label) |
| 10 | 10-Vale Alimentação |
| 11 | 11-Vale Refeição |
| 12 | 12-Vale Presente |
| 13 | 13-Vale Combustível |
| 14 | 14-Duplicata Mercantil (Desativado) |
| 15 | 15-Boleto Bancário |
| 16 | 16-Depósito Bancário |
| 17 | 17-Pagamento Instantâneo (PIX) - Dinâmico |
| 18 | 18-Transferência bancária, Carteira Digital |
| 19 | 19-Programa de fidelidade, Cashback, Crédito Virtual |
| 20 | 20-Pagamento Instantâneo (PIX) – Estático |
| 21 | 21-Crédito em Loja |
| 22 | 22-Pagamento Eletrônico não Informado - falha de hardware do sistema emissor |
| 90 | 90-Sem pagamento |
| 99 | 99-Outros |

### Opções para campo UTILIZAPOS (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMUSADOLOCACAO (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NSUOPCIONALPOS (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTEGRAECONECT (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONVENIOECONECT (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OPERACAOCTF (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| 101 | Débito |
| 103 | Débito Pré-datado |
| 104 | Débito Parcelado |
| 105 | Débito Parcelado com parcela à Vista |
| 106 | Voucher |
| 112 | Créd. a vista |
| 113 | Créd. Parcelado Lojista (sem juros) |
| 114 | Créd. Parcelado Administradora (com juros) |

### Opções para campo TIPVENC (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| F | Dia fixo |
| X | Hoje + Vencimento |

### Opções para campo RECEBANTAPROV (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ARREDPRIMEIRAPARC (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRUNCPARCELA (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPDOCRURAL (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| 1 | Nota Fiscal |
| 2 | Fatura |
| 3 | Recibo |
| 4 | Contrato |
| 5 | Folha de Pagamento |
| 6 | Outros |

### Opções para campo PROIBIMPBOL (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ULTILIZAPDVWEB (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALTERASIMULTPV (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDRECEFDCONT (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| 01 | 01- Clientes |
| 02 | 02- Administradora de cartão de débito/crédito |
| 03 | 03- Título de crédito - Duplicata, nota promissória, cheque, etc. |
| 04 | 04- Documento fiscal |
| 05 | 05- Item vendido (produtos e serviços) |
| 99 | 99-Outros |

### Opções para campo INFCMC7 (Tabela: TGFTIT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFTOKCAM
### Descrição: Campos Consulta Indexada

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCFG` | Código | I |  |
| `ENTIDADE` | Entidade | S |  |
| `TABELA` | Tabela | S |  |
| `CAMPO` | Campo | S |  |
| `RELEVANCIA` | Relevância | I |  |

## Tabela: TGFTOL
### Descrição: Liberacao Por Tipo Operacao

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `EVENTO` | Evento | I |  |
| `COPIARLIBER` | Copiar liberação quando faturando individualmente | S | Veja opções na seção OPÇÕES |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Dh. alteração | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo COPIARLIBER (Tabela: TGFTOL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFTOP
### Descrição: Tipos de Operação

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `NATEFDCONTM410M810` | Cód. Natureza (PIS/COFINS M410/M810) | I |  |
| `DESCROPER` | Descrição | S |  |
| `TIPMOV` | Tipo de movimento | S | Veja opções na seção OPÇÕES |
| `ORCAMENTO` | Orçamento | S | Veja opções na seção OPÇÕES |
| `DHALTER` | Data e hora alteração | H |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `GRUPO` | Grupo | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `ATUALFIN` | Financeiro | I | Veja opções na seção OPÇÕES |
| `TIPATUALFIN` | Atualização do financeiro | S | Veja opções na seção OPÇÕES |
| `ATUALEST` | Atualização do Estoque | S | Veja opções na seção OPÇÕES |
| `ATUALESTMP` | Atualiza estoque MP | I | Veja opções na seção OPÇÕES |
| `ATUALBEM` | Atualização do Bem | S | Veja opções na seção OPÇÕES |
| `ATUALCOM` | Comissão | S | Veja opções na seção OPÇÕES |
| `PRECIFICA` | Precifica | S | Veja opções na seção OPÇÕES |
| `ARMTIPAPU` | Tipo de Movimento Armazenagem | S | Veja opções na seção OPÇÕES |
| `MOVENDFLUTUANTE` | Movimentação de Endereços Flutuantes? | S | Veja opções na seção OPÇÕES |
| `IGNORAMPPVPA` | Ignora MP no preço de venda do PA | S | Veja opções na seção OPÇÕES |
| `PENDENTE` | A nota fica como pendente | S | Veja opções na seção OPÇÕES |
| `ALTNFCONF` | Permitir Alteração após confirmar | S | Veja opções na seção OPÇÕES |
| `SALVARCONFSEMPERG` | Salvar doc. confirmado sem perguntar | S | Veja opções na seção OPÇÕES |
| `ATUALPRECOFAT` | Recalcular preço prod. ao faturar | S | Veja opções na seção OPÇÕES |
| `CUPOMFISCAL` | TOP de Cupom Fiscal | S | Veja opções na seção OPÇÕES |
| `BONIFICACAO` | Bonificação | S | Veja opções na seção OPÇÕES |
| `ADIARATUALEST` | Atualizar Estoq.a partir da Confirmação | S | Veja opções na seção OPÇÕES |
| `OPERACAOAMOSTRA` | TOP de Amostra Grátis | S | Veja opções na seção OPÇÕES |
| `RATAUTPROD` | Ratear automaticamente por produto | S | Veja opções na seção OPÇÕES |
| `OBTERVLRMOEDAFAT` | Obter valor da moeda ao faturar | S | Veja opções na seção OPÇÕES |
| `CODTIPOPERDESTINO` | Cód.Tipo Operação Faturamento | I |  |
| `CODTIPOPERSEPARACAO` | Tipo Operação Separação | I |  |
| `USOPRODSEPARACAO` | Uso da Separação | S | Veja opções na seção OPÇÕES |
| `GOLDEV` | Identificador de Devolução | I | Veja opções na seção OPÇÕES |
| `GOLSINAL` | Tipo para análise | I | Veja opções na seção OPÇÕES |
| `GOLMPSINAL` | Tipo para análise de MP | I | Veja opções na seção OPÇÕES |
| `USARPRECOCUSTO` | Usar como Preço | S | Veja opções na seção OPÇÕES |
| `ATUALULTIMACOMP` | Atualizar Última Compra | S | Veja opções na seção OPÇÕES |
| `ATUALULTIMAVEND` | Atualizar Última Venda | S | Veja opções na seção OPÇÕES |
| `ANALISEGIRO` | Análise de Giro | I | Veja opções na seção OPÇÕES |
| `ATUALACDC` | Atualizar Acréscimos/Decréscimos | S | Veja opções na seção OPÇÕES |
| `FATENTPROD` | Na Entrada de Produtos | S | Veja opções na seção OPÇÕES |
| `INFCONTRATO` | Informar Contrato na Nota | S | Veja opções na seção OPÇÕES |
| `VALIDAATRASO` | Atraso | S | Veja opções na seção OPÇÕES |
| `PRODREP` | Aceitar Produto Repetido | S | Veja opções na seção OPÇÕES |
| `OC` | Tipo de Ordem de Carga | S | Veja opções na seção OPÇÕES |
| `ATUALTRANSG` | Saldo de Transgênico | I | Veja opções na seção OPÇÕES |
| `EXIGECOTACAO` | Exige Cotação | S | Veja opções na seção OPÇÕES |
| `PODEPESAGEM` | Tipo de Pesagem | S | Veja opções na seção OPÇÕES |
| `EXIGETRANSP` | Exige Transportadora | S | Veja opções na seção OPÇÕES |
| `VENDITE` | Exige vendedor nos itens | S | Veja opções na seção OPÇÕES |
| `EXECITE` | Exige executante nos itens | S | Veja opções na seção OPÇÕES |
| `EXIGECONF` | Exige conferência | S | Veja opções na seção OPÇÕES |
| `VALIDAAGRUPMIN` | Valida agrupamento mínimo | S | Veja opções na seção OPÇÕES |
| `EXIGELIB` | Exigir Liberação antes da Confirmação | S | Veja opções na seção OPÇÕES |
| `EXIGELAUDO` | Exige Laudo de análise | S | Veja opções na seção OPÇÕES |
| `LAUDOITEM` | Laudo por item | S | Veja opções na seção OPÇÕES |
| `VALIDAMEDIANEGOC` | Validar Média de Negociações Mensais | S | Veja opções na seção OPÇÕES |
| `VLRMINAP` | Valor mínimo p/Autorização de Pagamento | F |  |
| `FATESTCONF` | Fatura Produtos com Estoque na Confirmação | S | Veja opções na seção OPÇÕES |
| `SOLCOMPRA` | Gera Solicitação de Compra na Confirmação | S | Veja opções na seção OPÇÕES |
| `EDITANALISERENTAB` | Permite edição de análise de rentabilidade | S | Veja opções na seção OPÇÕES |
| `EXIGEGAR` | Exige garantia | S | Veja opções na seção OPÇÕES |
| `EXIGEDTVAL` | Exige data de validade | S | Veja opções na seção OPÇÕES |
| `USARCONFCEGA` | Usa conferência Cega | S | Veja opções na seção OPÇÕES |
| `EXIGEPEDFRET` | Exige Pedido de Frete p/Frete Extra Nota | S | Veja opções na seção OPÇÕES |
| `PEDFRETE` | Pedido de Frete | S | Veja opções na seção OPÇÕES |
| `GERAGNRE` | Gerar GNRE? | S | Veja opções na seção OPÇÕES |
| `PODETRANSFENT` | Pode Transformar Entradas | S | Veja opções na seção OPÇÕES |
| `PODEFIXAR` | Pode Fixar Preço | S | Veja opções na seção OPÇÕES |
| `REFNFE` | Buscar NF de origem p/ referenciar na NFe | S | Veja opções na seção OPÇÕES |
| `MPNUMAUTLOTE` | Numerar automaticamente MP por Lote | S | Veja opções na seção OPÇÕES |
| `EMPFUNCDIF` | Permitir Req. Func. de outra Empresa | S | Veja opções na seção OPÇÕES |
| `GERARTAGJNFE` | Gerar tag na NFe para Negociação de Veículos Novos | S | Veja opções na seção OPÇÕES |
| `EXIGANALITENS` | Exigir liberação com análise dos itens antes da confirmação | S | Veja opções na seção OPÇÕES |
| `ENVIARWMSCONF` | Enviar automaticamente para o WMS na Confirmação | S | Veja opções na seção OPÇÕES |
| `VALEST` | Validar Estoque p/ Reservar | S | Veja opções na seção OPÇÕES |
| `EXIGELIBSEMPRE` | Sempre exigir Liberação | S | Veja opções na seção OPÇÕES |
| `TEMFINORIGEM` | Atualiza Financeiro na TOP de Origem | S | Veja opções na seção OPÇÕES |
| `AUTDIGITAL` | Autorização por Digital | S | Veja opções na seção OPÇÕES |
| `DIGINFIMPORTA` | Digitar informações sobre Importação | S | Veja opções na seção OPÇÕES |
| `CODCONTARURAL` | Classificação da conta Produtor Rural | S | Veja opções na seção OPÇÕES |
| `NFESEMDTENTSAI` | Imprimir NF-e sem Data de Entrada/Saída | S | Veja opções na seção OPÇÕES |
| `CONTLAUDOSINT` | Participa da contagem de laudos internos | S | Veja opções na seção OPÇÕES |
| `AVISARCOMP` | Avisar sobre componentes | S | Veja opções na seção OPÇÕES |
| `CONFIMPOSTO` | Exige Conferência de Impostos | S | Veja opções na seção OPÇÕES |
| `CALCFUNTTELTOP` | Calcular FUNTTEL? | S | Veja opções na seção OPÇÕES |
| `CONFCFOP` | Exige Conferência de CFOP | S | Veja opções na seção OPÇÕES |
| `TOPPISCOFREDAQUIS` | Calcula PIS/COFINS red. pela aquisição | S | Veja opções na seção OPÇÕES |
| `CALCFUSTTOP` | Calcular FUST? | S | Veja opções na seção OPÇÕES |
| `NAOINCCONF` | Nunca incluir Confirmada | S | Veja opções na seção OPÇÕES |
| `PROVISENTREGA` | Exige previsão de entregas | S | Veja opções na seção OPÇÕES |
| `COPIARLIBER` | Copiar liberações quando faturando individualmente | S | Veja opções na seção OPÇÕES |
| `PESAITEM` | Pesagem por item | S | Veja opções na seção OPÇÕES |
| `DIGPUREZA` | Digitar % Pureza e % Germinação | S | Veja opções na seção OPÇÕES |
| `BLOQESTVENC` | Bloqueia saída de estoque vencido | S | Veja opções na seção OPÇÕES |
| `VALVCTLAUDOEST` | Valida laudo vencido na baixa de estoque | S | Veja opções na seção OPÇÕES |
| `GERABONPRE` | Gera Bonificação/Premiação | S | Veja opções na seção OPÇÕES |
| `FATCONTPORPESO` | Faturar contrato por peso | S | Veja opções na seção OPÇÕES |
| `TEMINDEX` | Utiliza Indexação | S | Veja opções na seção OPÇÕES |
| `CODTIPOPERREM` | Tipo Operação Remessa | I |  |
| `NUNOTAMODELO` | Nro único modelo | I |  |
| `GERARPARCDEST` | Gerar se parc.destinatário preenchido | S | Veja opções na seção OPÇÕES |
| `STATUSBAIXAEST` | Status para Baixa no estoque | S | Veja opções na seção OPÇÕES |
| `ATUALLIVFIS` | Atualização de Livro ICMS | S | Veja opções na seção OPÇÕES |
| `DENTROESTADO` | Top trabalha com CFOP para | S | Veja opções na seção OPÇÕES |
| `ATUALLIVISS` | Atualização livros de ISS | S | Veja opções na seção OPÇÕES |
| `TIPIPI` | Tipo de IPI | S | Veja opções na seção OPÇÕES |
| `TIPICMS` | Tipo de ICMS | S | Veja opções na seção OPÇÕES |
| `DESCONSIDNFEORIGEM` | Desconsidera Nfe de orig. referenciada? (Importação de XML) | S | Veja opções na seção OPÇÕES |
| `DATARETROFAT` | Permitir Data Retroativa no Faturamento | S | Veja opções na seção OPÇÕES |
| `PERMDESTVBATPREBCUS` | Permite destinação de Verba do tipo de Rebaixa de Custo | S | Veja opções na seção OPÇÕES |
| `CODCTACTBEFD` | Conta Contábil para EFD | I |  |
| `DESCQTDGRUDESCPRO` | Aplica Desc. Promocional por Qtd/Grupo de Desc. Prod? | S | Veja opções na seção OPÇÕES |
| `FORMRECISS` | Forma de Recolhimento ISS | S | Veja opções na seção OPÇÕES |
| `IGNORARAGRUPMINDEV` | Ignorar agrupamento mínimo de compra | S | Veja opções na seção OPÇÕES |
| `TIPMODALCTE` | Modal CT-e | S | Veja opções na seção OPÇÕES |
| `EXIGEANALISECRED` | Exige análise de crédito | S | Veja opções na seção OPÇÕES |
| `RESERVASEMLOTE` | Permitir reserva de estoque sem lote? | S | Veja opções na seção OPÇÕES |
| `CALCPESOCONFIRM` | Calcular Peso na Confirmação? | S | Veja opções na seção OPÇÕES |
| `SIMULACAUTOFRETE` | Simulação de frete automática | S | Veja opções na seção OPÇÕES |
| `CODMODDOCISS` | Modelo Documento ISS | S | Veja opções na seção OPÇÕES |
| `CODCFPS` | Código. CFPS | I |  |
| `VALVARIACVLRUNIT` | Validar variações do vlr. unit. orig./dest. | S | Veja opções na seção OPÇÕES |
| `CODMODDOC` | Modelo do Documento | I | Veja opções na seção OPÇÕES |
| `ACEITAFATACIMA` | Aceitar faturar quantidade maior que a da origem? | S | Veja opções na seção OPÇÕES |
| `CALCICMSREGTTS` | Calcular ICMS Regime TTS E-Commerce Vinculado? | S | Veja opções na seção OPÇÕES |
| `ENVGARANTIA` | Envio em Garantia? | S | Veja opções na seção OPÇÕES |
| `GERAR1400SPED` | Gerar Registro 1400 no SPED Fiscal ? | S | Veja opções na seção OPÇÕES |
| `USAALIQNATRATF100` | Usar Alíq.da Nat. do Rateio p/registro F100 do SPED PIS/COFINS ? | S | Veja opções na seção OPÇÕES |
| `VALTOTNOTAGERLIV` | Validar Totais da Nota na Geração do Livro? | S | Veja opções na seção OPÇÕES |
| `CALCDIFALPART` | Calcular DIFAL Partilhado | S | Veja opções na seção OPÇÕES |
| `EXIGECONFIRMACAOMDE` | Exigir confirmação do MD-e antes da confirmação | S | Veja opções na seção OPÇÕES |
| `PRODUETLOC` | Produção por Etapa e Local? | S | Veja opções na seção OPÇÕES |
| `USATABALTEMP` | Usar tabela de preço alternativa da empresa? | S | Veja opções na seção OPÇÕES |
| `INDPRESNFCE` | Indicador de Presença para NF-e/NFC-e/CF-e | S | Veja opções na seção OPÇÕES |
| `GERAENDENTRNFE` | Gerar endereço de entrega no XML da NF-e | S | Veja opções na seção OPÇÕES |
| `CONFVALEVENT68` | Validar diferença para | I | Veja opções na seção OPÇÕES |
| `PERMFINMENORVLRNOTA` | Permite financeiro menor que o valor total da nota | S | Veja opções na seção OPÇÕES |
| `FATFORAPLANENT` | Permitir faturamento fora do planejamento de entrega | S | Veja opções na seção OPÇÕES |
| `PERCTOLVARVLRUNIT` | % Tolerância na variação do Vlr. unitário | F |  |
| `VLRLIQITEMNFE` | Considera valor líquido do item na NF-e ou NFC-e ou CF-e(geração do XML e imp.Danfe) | S | Veja opções na seção OPÇÕES |
| `DESCONSIDPEDXML` | Desconsiderar pedido na geração do XML? | S | Veja opções na seção OPÇÕES |
| `CODCFO_SAIDA_FORA` | Saída | I |  |
| `CTE` | CT-e | S | Veja opções na seção OPÇÕES |
| `TIPSERVCTE` | Tipo de serviço CT-e | I | Veja opções na seção OPÇÕES |
| `CODTOPDENEGCTE` | Tipo Operação CT-e Denegado | I |  |
| `TIPOCTE` | Tipo de emissão CT-e | S | Veja opções na seção OPÇÕES |
| `CODMOEDAVP` | Cód. Moeda Ajusta Valor Presente | I |  |
| `AJUSTAVP` | Ajusta Valor Presente | S | Veja opções na seção OPÇÕES |
| `TIPALTDTVENC` | Tipo de Alteração da Data de Vencimento | S | Veja opções na seção OPÇÕES |
| `GERAAMOSTRALAUDO` | Gerar amostras para laudo | S | Veja opções na seção OPÇÕES |
| `TOPBACKORDER` | Top Back Order | I |  |
| `TOPATENDIMENTO` | Top de Atendimento | I |  |
| `VALSITCADSEFAZ` | Valida situação cadastro na SEFAZ ? | S | Veja opções na seção OPÇÕES |
| `CAT1799SPCCO` | Cód.Complem.Oper. (CAT-17/99) | I | Veja opções na seção OPÇÕES |
| `ENVWMSCONFIRMADA` | Permite confirmação antes do envio para o WMS? | S | Veja opções na seção OPÇÕES |
| `PERMCONFPARCIALWMS` | Permite conferência parcial no WMS? | S | Veja opções na seção OPÇÕES |
| `ARMAZENAGEM` | Armazenagem | S |  |
| `CALCICMS` | Cálculo de ICMS, IPI e ISS | S | Veja opções na seção OPÇÕES |
| `REDICMSBCPISCONFINS` | Deduzir valor do ICMS na BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `CODCFO_ENTRADA_FORA` | Entrada | I |  |
| `CODCFO_ENTRADA` | Entrada | I |  |
| `CODCFO_SAIDA` | Saída | I |  |
| `TEMCSL` | Tem CSLL | S | Veja opções na seção OPÇÕES |
| `ATUALESTTERC` | Estoque com/de Terceiros | S | Veja opções na seção OPÇÕES |
| `ESTOQUEMPTERCEIRO` | Estoque MP de Terceiros | S | Veja opções na seção OPÇÕES |
| `ATUALINDENIZ` | Saldo de Indenização | I | Veja opções na seção OPÇÕES |
| `CODMODRPS` | Mod. Imp. RPS | I |  |
| `CODMODNFSE` | Mod. Imp. NFS-e | I |  |
| `NFSEPORNAT` | NFS-e por natureza | S | Veja opções na seção OPÇÕES |
| `TEMII` | Tem II | S | Veja opções na seção OPÇÕES |
| `TEMVAVTCON` | Tem VA e/ou VT no contrato | S | Veja opções na seção OPÇÕES |
| `PODEAJUSTARORIGPRODWMS` | Permite Ajustar Nota Origem quando ligada a Produção | S | Veja opções na seção OPÇÕES |
| `TRANSFWMS` | Transferência no WMS | S | Veja opções na seção OPÇÕES |
| `VALTBCOMPCR` | Validar Tabela de compra por CR? | S | Veja opções na seção OPÇÕES |
| `STATUSLOTE` | Exige Status para o Lote na Compra | S | Veja opções na seção OPÇÕES |
| `TEMREAICMS` | Tem Convênio REA/ICMS | S | Veja opções na seção OPÇÕES |
| `NATOPERSPED` | Natureza da Operação (SPED) | S |  |
| `GERAPLANPROD` | Gerar plano de produção | S | Veja opções na seção OPÇÕES |
| `INTEGRAEVENTO` | Integra evento | S | Veja opções na seção OPÇÕES |
| `SEPBALCAO` | Separação em Balcão | S | Veja opções na seção OPÇÕES |
| `TRANSFCBGLOBAL` | Número de Série Global - Transferência | S | Veja opções na seção OPÇÕES |
| `AGRUPASERVFAT` | Agrupa serviços faturamento | S | Veja opções na seção OPÇÕES |
| `MARCARNAOPENDENTE` | Deixar pedido como NÃO pendente quando faturar com corte | S | Veja opções na seção OPÇÕES |
| `DESTOPADRCST1400` | Desconsiderar TOP na geração da ADRC-ST no R1400? | S | Veja opções na seção OPÇÕES |
| `NUCCO` | Configuração p/ conferência | I |  |
| `CODLOCALIMPXML` | Local padrão para importar XML | I |  |
| `SUGERELOCALPARC` | Sugerir local padrão do parceiro? | S | Veja opções na seção OPÇÕES |
| `USACUSMEDBASEST` | Usa Cus. Méd. Base ST? | S | Veja opções na seção OPÇÕES |
| `ALTITEMPARCFAT` | Permite alterar itens após faturar parcialmente | S | Veja opções na seção OPÇÕES |
| `GRAHISALTPED` | Gravar histórico de alterações do pedido | S | Veja opções na seção OPÇÕES |
| `AGRUPAPRODNFE` | Agrupar produtos semelhantes na NF-e? | S | Veja opções na seção OPÇÕES |
| `NFE` | NF-e | S | Veja opções na seção OPÇÕES |
| `NFCOM` | NFCom | S | Veja opções na seção OPÇÕES |
| `TPNFDEB` | Tipo de Nota Fiscal de Débito | S | Veja opções na seção OPÇÕES |
| `TPNFCRED` | Tipo de Nota Fiscal de Crédito | S | Veja opções na seção OPÇÕES |
| `TIPOIMPKIT` | Kit/Componentes - Impressão e Livro Fiscal | S | Veja opções na seção OPÇÕES |
| `CODNATOPERISS` | Cód. Natureza Oper. ISS (NFS-e) | S | Veja opções na seção OPÇÕES |
| `NUMPROCESSO` | Número do processo | S |  |
| `CODTIPOPERDENEG` | Tipo Operação NF-e Denegada | I |  |
| `CODREMEDI` | Modelo p/geração de EDI na confirmação | I |  |
| `COPIADTPREVORIG` | Copiar prev. entrega da origem | S | Veja opções na seção OPÇÕES |
| `TIPMOVBEMSPED` | Tipo de Mov. do  Bem (SPED) | S | Veja opções na seção OPÇÕES |
| `CODTIPOPERPENRET` | Tipo Operação NF-e Pendente de Retorno | I |  |
| `CODCFO_TERC` | CFOP p/Produtos de Terceiros | I |  |
| `CODCFO_COMBUST_LUBRIF` | CFOP p/Combustíveis e Lubrificantes | I |  |
| `TEMIPI` | Tem IPI | S | Veja opções na seção OPÇÕES |
| `IPIEMBUT` | IPI Embutido | S | Veja opções na seção OPÇÕES |
| `SOMARIPI` | Somar IPI ao total da nota | S | Veja opções na seção OPÇÕES |
| `IPIINCICMS` | IPI Incide na base de ICMS | S | Veja opções na seção OPÇÕES |
| `CSTIPIENT` | Código Sit.Trib.IPI Entrada | I | Veja opções na seção OPÇÕES |
| `CSTIPISAI` | Código Sit.Trib.IPI Saída | I | Veja opções na seção OPÇÕES |
| `CODENQIPIENT` | Código Enq. Legal IPI Entrada | I |  |
| `CODENQIPISAI` | Código Enq. Legal IPI Saída | I |  |
| `CALCDIFICMS` | Calcular diferença de ICMS | S | Veja opções na seção OPÇÕES |
| `SOMASUBST` | Soma ST no total da nota | S | Veja opções na seção OPÇÕES |
| `TEMICMS` | Tem ICMS | S | Veja opções na seção OPÇÕES |
| `TEMFUNRURAL` | Tem FUNRURAL/INSS | S | Veja opções na seção OPÇÕES |
| `TEMIRF` | Tem IRF | S | Veja opções na seção OPÇÕES |
| `TEMPIS` | Tem PIS | S | Veja opções na seção OPÇÕES |
| `TEMCOFINS` | Tem COFINS | S | Veja opções na seção OPÇÕES |
| `TEMISS` | Tem ISS | S | Veja opções na seção OPÇÕES |
| `CALCFETHAB` | Calcular FETHAB | S | Veja opções na seção OPÇÕES |
| `PERCMINBASEINSS` | % Mín. da Base de INSS sobre o Total da Nota | F |  |
| `CLASSIFICMS` | Classificação ICMS | S | Veja opções na seção OPÇÕES |
| `ATUSALDOCONT` | Atualização do saldo dos contratos | S | Veja opções na seção OPÇÕES |
| `COMPLEMENTO` | Tipo de Emissão | S | Veja opções na seção OPÇÕES |
| `TIPOEMISSAONFCOM` | Tipo de Emissão | S | Veja opções na seção OPÇÕES |
| `INDNATFRT` | Indicador da Natureza do Frete Contratado | S | Veja opções na seção OPÇÕES |
| `NATBCCRED` | Natureza da Base de Cálculo do Crédito de Pis/Cofins | S | Veja opções na seção OPÇÕES |
| `BASENUMERACAO` | Base numeração | S | Veja opções na seção OPÇÕES |
| `NUMSOMAUT` | Numeração somente automática | S | Veja opções na seção OPÇÕES |
| `TRAVAFIMIMP` | Travar até terminar a impressão | S | Veja opções na seção OPÇÕES |
| `TIPONUMERACAO` | Tipo de Numeração | S | Veja opções na seção OPÇÕES |
| `EMITENOTA` | Imprimir | S | Veja opções na seção OPÇÕES |
| `EMITEBOLETA` | Imprimir Pix/Boleto/Duplicata | S | Veja opções na seção OPÇÕES |
| `IMPNOTAADICIONAL` | Imprimir Nota Adicional | S | Veja opções na seção OPÇÕES |
| `VALESTMAXIMO` | Valida Estoque Máximo | S | Veja opções na seção OPÇÕES |
| `VALIDADATA` | Reiniciar numeração por data | S | Veja opções na seção OPÇÕES |
| `IMPNAOCONF` | Imprimir nota adicional antes de confirmada | S | Veja opções na seção OPÇÕES |
| `CODMODNF` | Modelo de impressão de nota fiscal | I |  |
| `CODMODDAD` | Modelo para Dados Adicionais de NF-e | I |  |
| `CODMODRO` | Modelo de impressão de romaneio | I |  |
| `VALNUM` | Valida Numeração por | S | Veja opções na seção OPÇÕES |
| `CODMODCFECANC` | Modelo de impressão de cancelamento CF-e | I |  |
| `NFSE` | NFS-e | S | Veja opções na seção OPÇÕES |
| `CAMGEREDICONF` | Caminho para geração de EDI na confirmação | S |  |
| `ICMSPROPFRETE` | ICMS proporcional para Frete | S | Veja opções na seção OPÇÕES |
| `ICMSPROPSEG` | ICMS proporcional para Seguro | S | Veja opções na seção OPÇÕES |
| `ICMSPROPDESTAQUE` | ICMS proporcional para Destaque | S | Veja opções na seção OPÇÕES |
| `ICMSPROPJURO` | ICMS proporcional para Juro | S | Veja opções na seção OPÇÕES |
| `ICMSPROPEMBALAGEM` | ICMS proporcional para Embalagem | S | Veja opções na seção OPÇÕES |
| `PISPROPFRETE` | PIS proporcional para Frete | S | Veja opções na seção OPÇÕES |
| `PISPROPSEG` | PIS proporcional para Seguro | S | Veja opções na seção OPÇÕES |
| `PISPROPDESTAQUE` | PIS proporcional para Destaque | S | Veja opções na seção OPÇÕES |
| `PISPROPEMBALAGEM` | PIS proporcional para Embalagem | S | Veja opções na seção OPÇÕES |
| `PISPROPJURO` | PIS proporcional para Juro | S | Veja opções na seção OPÇÕES |
| `IPIPROPFRETE` | IPI proporcional para Frete | S | Veja opções na seção OPÇÕES |
| `IPIPROPSEG` | IPI proporcional para Seguro | S | Veja opções na seção OPÇÕES |
| `IPIPROPDESTAQUE` | IPI proporcional para Destaque | S | Veja opções na seção OPÇÕES |
| `IPIPROPEMBALAGEM` | IPI proporcional para Embalagem | S | Veja opções na seção OPÇÕES |
| `IPIPROPJURO` | IPI proporcional para Juro | S | Veja opções na seção OPÇÕES |
| `COFINSPROPFRETE` | COFINS proporcional para Frete | S | Veja opções na seção OPÇÕES |
| `COFINSPROPSEG` | COFINS proporcional para Seguro | S | Veja opções na seção OPÇÕES |
| `COFINSPROPDESTAQUE` | COFINS proporcional para Destaque | S | Veja opções na seção OPÇÕES |
| `COFINSPROPEMBALAGEM` | COFINS proporcional para Embalagem | S | Veja opções na seção OPÇÕES |
| `COFINSPROPJURO` | COFINS proporcional para Juro | S | Veja opções na seção OPÇÕES |
| `STPROPFRETE` | S.T.proporcional para Frete | S | Veja opções na seção OPÇÕES |
| `STPROPFRETEEXT` | para Frete Extra | S | Veja opções na seção OPÇÕES |
| `STPROPSEG` | S.T.proporcional para Seguro | S | Veja opções na seção OPÇÕES |
| `STPROPDESTAQUE` | S.T.proporcional para Destaque | S | Veja opções na seção OPÇÕES |
| `STPROPEMBALAGEM` | S.T.proporcional para Embalagem | S | Veja opções na seção OPÇÕES |
| `STPROPJURO` | S.T.proporcional para Juro | S | Veja opções na seção OPÇÕES |
| `TIPIVASUBST` | Tipo de Calculo IVA ponderado | S | Veja opções na seção OPÇÕES |
| `CALCSTFRTXTNOTPROP` | Calc. ICMS/ST extra nota p/ frete extra nota proporcional aos itens | S | Veja opções na seção OPÇÕES |
| `BASEICMSFRETECALCST` | Usar base ICMS Frete Extra Nota p/calc.ST | S | Veja opções na seção OPÇÕES |
| `EXPGRS` | Exportação para GRS | I | Veja opções na seção OPÇÕES |
| `EXPTES` | Exportação para tesouraria | S | Veja opções na seção OPÇÕES |
| `ATUALCOMOS` | Calcular comissão para O.S. | S | Veja opções na seção OPÇÕES |
| `TIPFATSERV` | Faturamento relacionado a Ordem de Serviço | S | Veja opções na seção OPÇÕES |
| `BUSCMPTERC` | Apoio p/Devolução de Produtos de Terceiros | S | Veja opções na seção OPÇÕES |
| `ATUALFINTERC` | Soma itens com/de Terceiros ao Financeiro | S | Veja opções na seção OPÇÕES |
| `UTILIZAWMS` | Endereçamento no WMS | S | Veja opções na seção OPÇÕES |
| `TIPATUALWMS` | Atualização no WMS | S | Veja opções na seção OPÇÕES |
| `ATUALDATRECWMS` | Atualização Data Rec. no WMS | S | Veja opções na seção OPÇÕES |
| `EXIGEAGENDAWMS` | Exige agendamento p/Carga e Descarga no WMS | S | Veja opções na seção OPÇÕES |
| `EXPORTA` | Exporta Replicação | S | Veja opções na seção OPÇÕES |
| `CODTRIB` | Tributação | I |  |
| `ATUALIZARATEIO` | Atualiza Rateio | S | Veja opções na seção OPÇÕES |
| `CONSIGNACAO` | Consignação | S | Veja opções na seção OPÇÕES |
| `VLRBASEPGTO` | Valor Base Pagamento | F |  |
| `COFINSSTPROPFRETE` | COFINS ST Prop. Frete | S | Veja opções na seção OPÇÕES |
| `PISSTPROPEMBALAGEM` | PIS ST Prop. Embalagem | S | Veja opções na seção OPÇÕES |
| `SOMARCOFINSST` | Somar COFINS ST ao Total da Nota | S | Veja opções na seção OPÇÕES |
| `COFINSSTPROPSEG` | COFINS ST Prop. Seguro | S | Veja opções na seção OPÇÕES |
| `COFINSSTPROPEMBALAGEM` | COFINS ST Prop. Embalagem | S | Veja opções na seção OPÇÕES |
| `COFINSSTPROPDESTAQUE` | COFINS ST Prop. Destaque | S | Veja opções na seção OPÇÕES |
| `SOMARPISST` | Somar PIS ST ao Total da Nota | S | Veja opções na seção OPÇÕES |
| `PISSTPROPFRETE` | PIS ST Prop. Frete | S | Veja opções na seção OPÇÕES |
| `PISSTPROPJURO` | PIS ST Prop. Juro | S | Veja opções na seção OPÇÕES |
| `INTEGSERCON` | Integ. Série ao Contrato | S | Veja opções na seção OPÇÕES |
| `COFINSSTPROPJURO` | COFINS ST Prop. Juro | S | Veja opções na seção OPÇÕES |
| `PISSTPROPDESTAQUE` | PIS ST Prop. Destaque | S | Veja opções na seção OPÇÕES |
| `PISSTPROPSEG` | PIS ST Prop. Seguro | S | Veja opções na seção OPÇÕES |
| `AD_RELATORIO` | Relatorio | S | Veja opções na seção OPÇÕES |
| `NULAYOUT` | Nro. Layout | I |  |
| `NULAYOUTCVR` | Nro. Layout CVR | I |  |
| `ATUALCTB` | Atualiza Contabilidade | S | Veja opções na seção OPÇÕES |
| `OPERCOMMOEDA` | Operação em Moeda | S | Veja opções na seção OPÇÕES |
| `SEMMOEDAFIN` | Não preencher moeda para Financeiro | S | Veja opções na seção OPÇÕES |
| `NFEESTORNO` | NF-e de estorno | S | Veja opções na seção OPÇÕES |
| `DESCREMAIL` | Descrição do e-mail | S |  |
| `APLICLEITRANSP` | Aplicar a lei da transparência | S | Veja opções na seção OPÇÕES |
| `APLICTABIRFINSS` | Aplicar tabela de IRPF/INSS | S | Veja opções na seção OPÇÕES |
| `USASERVTABIRFINSS` | Usar serviço p/ cálculo com tabela de IRPF/INSS | S | Veja opções na seção OPÇÕES |
| `INDTERC` | Industrialização efetuada por terceiros | S | Veja opções na seção OPÇÕES |
| `DESCONNFSE` | Desconto Condicionado para NFS-e | S | Veja opções na seção OPÇÕES |
| `NUFOP` | Finalidade da Operação | I |  |
| `CONSAUXILIAR` | Consultas Auxiliares | S |  |
| `DISTSTVLRUNITFAT` | Distribuir valor do ST no preço unitário ao faturar | S | Veja opções na seção OPÇÕES |
| `CALCFCPINT` | Calcular FCP (ICMS/ST) Interno? | S | Veja opções na seção OPÇÕES |
| `ICMSORIGESTPED` | Calcular ICMS de Origem Estrangeira | S | Veja opções na seção OPÇÕES |
| `INDTIPREC` | Indicador do Tipo de Receita | S | Veja opções na seção OPÇÕES |
| `GERADEMANDAMPS` | Gerar demanda para MPS | S | Veja opções na seção OPÇÕES |
| `LIGORIGORIG` | Ligar com a Origem da Origem com quantidade negativa? | S | Veja opções na seção OPÇÕES |
| `IGNEXPAUTLOT` | Ignorar explosão automática de lotes nesta TOP | S | Veja opções na seção OPÇÕES |
| `ATUALESTWMSTERC` | Atualiza Estoque de Terceiros WMS? | S | Veja opções na seção OPÇÕES |
| `USARECPARCIAL` | Utiliza recebimento parcial? | S | Veja opções na seção OPÇÕES |
| `VALSITCADRF` | Valida situação cadastro na ReceitaWS ? | S | Veja opções na seção OPÇÕES |
| `GERCORAPON` | Gerar Correção de Apontamento (K280) | S | Veja opções na seção OPÇÕES |
| `CONSVLRREMRETIND` | Considerar o valor da remessa, no retorno de industrialização como | I | Veja opções na seção OPÇÕES |
| `INTERMED` | Indicador de Intermediador/Marketplace | S | Veja opções na seção OPÇÕES |
| `DEVSEMDESTAQUEST` | Devolver sem destacar ST | S | Veja opções na seção OPÇÕES |
| `CODINTERM` | Intermediador da Transação | I |  |
| `DEVSEMDESTAQUEIPI` | Devolver sem destacar IPI | S | Veja opções na seção OPÇÕES |
| `SEMCREDIPIST` | Operação sem direito a crédito IPI/ST | S | Veja opções na seção OPÇÕES |
| `IGNORACOMPLITEM` | Ignorar complemento dos itens nas informações adicionais dos produtos? | S | Veja opções na seção OPÇÕES |
| `PERMITECNAEDIFNOTA` | Possibilita emissão de NFS-e com múltiplos CNAEs | S | Veja opções na seção OPÇÕES |
| `OUTDESPSTEXTNOTA` | Frete/Seguro/Outras Despesas para ST extra nota | S | Veja opções na seção OPÇÕES |
| `IMPXMLMANTDESPACES` | Importar o XML mantendo as despesas acessórias com os valores do XML | S | Veja opções na seção OPÇÕES |
| `REDPISBCPISCOFINS` | Deduzir valor do PIS/COFINS da BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `CALCPISCFSFIN` | Calcula PIS/COFINS por percentual das notas | S | Veja opções na seção OPÇÕES |
| `VALDISPESTDEV` | Valida disponibilidade de estoque na devolução? | S | Veja opções na seção OPÇÕES |
| `CONSNFERELCANCEFD` | Considerar NFe relacionada como cancelada no EFD Contribuições | S | Veja opções na seção OPÇÕES |
| `DESCCSTBCPISCF` | Desconsiderar CST’s de ICMS da BC do PIS/COFINS? | S |  |
| `USAVENDAMAIS` | Utilizar no Sankhya Venda Mais | S | Veja opções na seção OPÇÕES |
| `PERMTRANSGALPAO` | Permite transferência entre galpões | S | Veja opções na seção OPÇÕES |
| `REDSTBCPISCOFINS` | Deduzir valor do ICMS/ST na BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `DESCONSLCDPR` | Desconsiderar Top na Geração do Livro Caixa Digital do Produtor Rural | S | Veja opções na seção OPÇÕES |
| `CONSTOPAPURSIMP` | Considerar na Apuração do Simples? | S | Veja opções na seção OPÇÕES |
| `IGNOBSORIGREM` | Ignorar Observação da Nota de Origem | S | Veja opções na seção OPÇÕES |
| `DEDFCPBCPISCOFINS` | Deduzir valor de FCP na BC do PIS e COFINS? | S | Veja opções na seção OPÇÕES |
| `CONFVLREVENT68` | Valor para validar o evento 68 | S | Veja opções na seção OPÇÕES |
| `GERINFOEFDPAG` | Gerar informações do EFD Reinf Grupo 4000? | S | Veja opções na seção OPÇÕES |
| `TIPCOMPLCUST` | Tipo complemento custo | I | Veja opções na seção OPÇÕES |
| `RECBRUTACIAP` | Receita Bruta p/ CIAP | S | Veja opções na seção OPÇÕES |
| `ARREDQTDUNALT` | Arredonda Qtd. unid. alternativa? | S | Veja opções na seção OPÇÕES |
| `AD_VALTECCOM` | Valida Técnico Comissão | S | Veja opções na seção OPÇÕES |
| `OPERESSACOMP` | Operação com Ressarcimento/Complemento de ST | S | Veja opções na seção OPÇÕES |
| `CONSDISBAIXEST` | Considerar estoque real na baixa de estoque | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPMOV (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| B | B-Movimento bancário |
| C | C-Compra |
| D | D-Devolução de venda |
| E | E-Devolução de compra |
| F | F-Produção |
| G | G-Pagamento |
| I | I-Financeiro |
| J | J-Pedido de Requisição |
| K | K-Pedido de Transferência |
| L | L-Devolução de Requisição |
| M | M-Devolução de Transf. |
| N | N-Entradas |
| O | O-Pedido de Compra |
| P | P-Pedido de Venda |
| Q | Q-Requisição |
| R | R-Recebimento |
| T | T-Transferência |
| V | V-Venda |
| 1 | 1-NF Depósito |
| 2 | 2-Pedido de Devolução |
| 3 | 3-Saídas |
| 4 | 4-Faturamento |
| 8 | 8-Pedido de Armazenagem |

### Opções para campo ORCAMENTO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATUALFIN (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não atualizar |
| -1 | Despesas |
| 1 | Receitas |

### Opções para campo TIPATUALFIN (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| I | Incluir |
| P | Provisionar |

### Opções para campo ATUALEST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| B | Baixar |
| E | Entrar |
| N | Nenhuma |
| R | Reservar |

### Opções para campo ATUALESTMP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Nenhuma |
| -1 | Baixar |
| 1 | Entrar |
| 2 | Reservar |

### Opções para campo ATUALBEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| B | Baixa/Venda |
| C | Compra |
| D | Transf.Entrada/Retorno |
| E | Dev. Venda de Bens |
| N | Não Atualizar |
| T | Transf.Saída/Remessa |
| 1 | Dev. Compra de Bens |

### Opções para campo ATUALCOM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| C | Calcular |
| L | Calc.Vend.da Nota na Confirmação |
| N | Não calcular |
| P | Calc.Vend.do Parc.na Confirmação |

### Opções para campo PRECIFICA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Atualiza custo pelo agendador |
| C | Atualiza somente custo |
| N | Não atualiza custo nem preço de venda |
| S | Atualiza custo e preço de venda |

### Opções para campo ARMTIPAPU (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| C | Compra |
| D | PD Devolução |
| F | Fixação |
| P | Procuração |
| T | Venda Futura |
| V | Venda |
| 1 | Romaneio |
| 2 | NF de Transporte |
| 3 | Impurezas |
| 4 | Devoluções de Armazenagem |
| 5 | Quebras |
| 6 | Expedição/Recepção |
| 7 | Armazenagem |
| 8 | Serviços Avulsos |
| 9 | Warrant |

### Opções para campo MOVENDFLUTUANTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IGNORAMPPVPA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PENDENTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALTNFCONF (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SALVARCONFSEMPERG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATUALPRECOFAT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CUPOMFISCAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BONIFICACAO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ADIARATUALEST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OPERACAOAMOSTRA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RATAUTPROD (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OBTERVLRMOEDAFAT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USOPRODSEPARACAO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| B | Brinde |
| C | Consumo |
| D | Revenda (Por Fórmula) |
| F | Brinde (NF) |
| I | Imobilizado |
| M | Matéria Prima |
| R | Revenda |
| S | Serviço |
| T | Terceiros |
| V | Venda (Fabricação Própria) |

### Opções para campo GOLDEV (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| -1 | Sim |
| 1 | Não |

### Opções para campo GOLSINAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Nada |
| -1 | Venda |
| 1 | Compra |

### Opções para campo GOLMPSINAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Nada |
| -1 | Venda |
| 1 | Compra |

### Opções para campo USARPRECOCUSTO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| D | Preço em Moeda |
| E | Último Custo de Entrada Com ICMS |
| G | Último Custo Médio Gerencial |
| L | Último Custo Gerencial |
| M | Último Custo Médio Com ICMS |
| N | Nenhum |
| O | Média das notas de origem |
| P | Preço de Venda |
| Q | Valor Líquido da origem |
| R | Último Custo de Reposição |
| S | Último Custo de Entrada Sem ICMS |
| V | Último Custo Variável |
| Z | Último Custo Médio Sem ICMS |

### Opções para campo ATUALULTIMACOMP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| E | Dt.Entrada |
| G | Dt.Negociação |
| M | Dt.Movimento |
| N | Não Atualizar |

### Opções para campo ATUALULTIMAVEND (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| F | Dt.Faturamento |
| G | Dt.Negociação |
| N | Não Atualizar |
| S | Dt.Saída |

### Opções para campo ANALISEGIRO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Desconsiderar |
| -1 | Venda (Saída) |
| 1 | Devolução de venda (Entrada) |

### Opções para campo ATUALACDC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não Atualizar |
| P | Provisão de Acréscimo |
| S | Saldo Disponível |

### Opções para campo FATENTPROD (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Faturar automaticamente |
| N | Não faturar |
| S | Abrir seleção de pedidos para faturar |

### Opções para campo INFCONTRATO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Proibido |
| O | Opcional |
| S | Obrigatório |

### Opções para campo VALIDAATRASO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Validar e avisar |
| N | Não validar |
| V | Validar e bloquear |

### Opções para campo PRODREP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| null | Usar o Parâmetro Global |
| S | Sim |

### Opções para campo OC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| E | Entrada |
| P | Proibido |
| S | Saída |

### Opções para campo ATUALTRANSG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não atualizar |
| -1 | Subtrair |
| 1 | Somar |

### Opções para campo EXIGECOTACAO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| C | Exigir completo |
| N | Não Exigir |
| S | Exigir algum item |

### Opções para campo PODEPESAGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não pesa |
| P | Permite |
| S | Exige |

### Opções para campo EXIGETRANSP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VENDITE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXECITE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGECONF (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALIDAAGRUPMIN (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| L | Valida e exige liberação |
| N | Não valida |
| S | Valida e bloqueia |

### Opções para campo EXIGELIB (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGELAUDO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo LAUDOITEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALIDAMEDIANEGOC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FATESTCONF (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SOLCOMPRA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EDITANALISERENTAB (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGEGAR (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGEDTVAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USARCONFCEGA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGEPEDFRET (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PEDFRETE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERAGNRE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PODETRANSFENT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PODEFIXAR (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REFNFE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MPNUMAUTLOTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| E | Embalagem |
| N | Não |
| S | Matéria Prima |

### Opções para campo EMPFUNCDIF (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERARTAGJNFE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGANALITENS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVIARWMSCONF (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALEST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGELIBSEMPRE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMFINORIGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AUTDIGITAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIGINFIMPORTA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODCONTARURAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 000 | 000 - Caixa |
| 999 | 999 - Em trânsito |

### Opções para campo NFESEMDTENTSAI (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONTLAUDOSINT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AVISARCOMP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONFIMPOSTO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCFUNTTELTOP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| P | Usar do Cadastro de Produto |
| S | Sim |

### Opções para campo CONFCFOP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TOPPISCOFREDAQUIS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não calcula |
| null | Usa do parâmetro |
| S | Usa da TOP |

### Opções para campo CALCFUSTTOP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| P | Usar do Cadastro de Produto |
| S | Sim |

### Opções para campo NAOINCCONF (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROVISENTREGA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COPIARLIBER (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PESAITEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIGPUREZA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BLOQESTVENC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALVCTLAUDOEST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERABONPRE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FATCONTPORPESO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMINDEX (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERARPARCDEST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSBAIXAEST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Aguardando Aprovação |
| N | Nenhum |
| P | Aprovado |
| Q | Quarentena |
| R | Reprovado |

### Opções para campo ATUALLIVFIS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| E | Livro de entrada |
| N | Não atualiza |
| S | Livro de saída |

### Opções para campo DENTROESTADO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| D | Dentro do Estado |
| F | Fora do Estado |

### Opções para campo ATUALLIVISS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| E | Aquisições |
| N | Não Atualiza |
| S | Prestações |

### Opções para campo TIPIPI (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 1 | Com créd/déb de imposto |
| 2 | Sem créd/déb - Isentas |
| 3 | Sem créd/déb - Outras |

### Opções para campo TIPICMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 1 | Com créd/déb de imposto |
| 2 | Sem créd/déb - Isentas |
| 3 | Sem créd/déb - Outras |
| 4 | Com créd/déb - Isentas |
| 5 | Com créd/déb - Outras |

### Opções para campo DESCONSIDNFEORIGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DATARETROFAT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMDESTVBATPREBCUS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCQTDGRUDESCPRO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FORMRECISS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 00 | Normal |
| 01 | Retido na Fonte |
| 03 | Simples Nacional |
| 04 | Fixo/Anual |
| 05 | Sem Recolhimento |
| 06 | Devido a Outro Município |
| 07 | Fixo Mensal |

### Opções para campo IGNORARAGRUPMINDEV (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPMODALCTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 1 | Rodoviário |
| 2 | Aéreo |
| 3 | Aquaviário |
| 6 | Multimodal |

### Opções para campo EXIGEANALISECRED (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RESERVASEMLOTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCPESOCONFIRM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SIMULACAUTOFRETE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODMODDOCISS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 03 | 03-Nota Fiscal de Serviços (modelo 3) |
| 2D | 2D-Cupom Fiscal emitido por ECF |
| 3A | 3A-Nota Fiscal de Serviços - Modelo Simplificado |
| 3B | 3B-Nota Fiscal de Serviços - Modelo Avulso |

### Opções para campo VALVARIACVLRUNIT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODMODDOC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Sem Modelo |
| 1 | 01-Nota Fiscal |
| 10 | 10-Conhecimento Aéreo |
| 11 | 11-Conhecimento de Transporte Ferroviário de Cargas |
| 13 | 13-Bilhete de Passagem Rodoviário |
| 14 | 14-Bilhete e Passagem Aquaviário |
| 15 | 15-Bilhete de Passagem e Nota de Bagagem |
| 16 | 16-Bilhete de Passagem Ferroviário |
| 17 | 17-Despacho de Transporte |
| 18 | 18-Resumo Movimento Diário |
| 2 | 02-Nota Fiscal de Venda a Consumidor |
| 20 | 20-Ordem de Coleta de Carga |
| 21 | 21-Nota Fiscal de Serviço de Comunicação |
| 22 | 22-Nota Fiscal de Serviço de Telecomunicações |
| 23 | 23-GNRE |
| 24 | 24-Autorização de Carregamento de Transporte |
| 25 | 25-Manifesto de Carga |
| 26 | 26-Conhecimento de Transporte Multimodal de Cargas |
| 27 | 27-Nota Fiscal De Transporte Ferroviário De Carga |
| 28 | 28-Nota Fiscal/Conta de Fornecimento de Gás Canalizado |
| 29 | 29-Nota Fiscal/Conta De Fornecimento D''água Canalizada |
| 3 | 03-Nota Fiscal de Entrada |
| 4 | 04-Nota Fiscal de Produtor |
| 55 | 55-Nota Fiscal Eletrônica |
| 57 | 57-Conhecimento Transporte Rodoviário Eletrônico |
| 59 | 59-Cupom Fiscal Eletrônico |
| 6 | 06-Nota Fiscal Conta de Energia Elétrica |
| 62 | 62-Nota Fiscal Eletrônica de Serviços de Comunicação |
| 63 | 63-Bilhete de Passagem Eletrônico |
| 65 | 65-Nota Fiscal Eletrônica de Venda a Consumidor |
| 66 | 66-Nota Fiscal de Energia Elétrica Eletrônica |
| 67 | 67-Conhecimento Transporte Eletrônico Outros Serviços |
| 7 | 07-Nota Fiscal de Serviço de Transporte |
| 8 | 08-Conhecimento de Transporte Rodoviário de Cargas |
| 9 | 09-Conhecimento de Transporte Aquaviário de Cargas |
| 901 | 1B-Nota Fiscal Avulsa |
| 902 | 8B-Conhecimento de Transporte de Cargas Avulso |

### Opções para campo ACEITAFATACIMA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCICMSREGTTS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVGARANTIA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERAR1400SPED (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USAALIQNATRATF100 (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALTOTNOTAGERLIV (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCDIFALPART (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGECONFIRMACAOMDE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODUETLOC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USATABALTEMP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDPRESNFCE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Não se aplica |
| 1 | 1-Operação presencial |
| 2 | 2-Não presencial, internet |
| 3 | 3-Não presencial, teleatendimento |
| 4 | 4-NFC-e com entrega em domicílio |
| 5 | 5-Presencial, fora do estabelecimento |
| 9 | 9-Não presencial, outros |

### Opções para campo GERAENDENTRNFE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| D | Parceiro destinatário |
| N | Nenhum |
| P | Parceiro principal |

### Opções para campo CONFVALEVENT68 (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Ambos |
| 1 | Maior |
| 2 | Menor |

### Opções para campo PERMFINMENORVLRNOTA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FATFORAPLANENT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VLRLIQITEMNFE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| E | Conforme empresa |
| N | Não |
| S | Sim |

### Opções para campo DESCONSIDPEDXML (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| E | Import. Doc. (Emissão Própria) |
| M | Convencional (Não usa CT-e) |
| N | Normal |
| T | Terceiros |

### Opções para campo TIPSERVCTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Normal |
| 1 | Subcontratação |
| 2 | Redespacho |
| 3 | Redespacho Intermediário |
| 4 | Serviço vinculado a multimodal |
| 6 | Transporte de Pessoas |
| 7 | Transporte de Valores |

### Opções para campo TIPOCTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | 4 - CTe de Anulação |
| C | 1 - CTe de Complemento de Valores |
| N | 0 - CTe Normal |
| P | 5 - CT-e Simplificado |
| S | 3 - CTe de Substituição |
| T | 6 - Substituição de CT-e Simplificado |

### Opções para campo AJUSTAVP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Anual |
| F | Fim do Período |
| M | Mensal |
| N | Não Ajusta |
| V | Vencimento |

### Opções para campo TIPALTDTVENC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| M | Manter |
| P | Perguntar |
| R | Recalcular |

### Opções para campo GERAAMOSTRALAUDO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALSITCADSEFAZ (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CAT1799SPCCO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | 00 - Operação Normal |
| -1 | -1 - Não Participa da Portaria CAT-17/99 |
| 1 | 01 - Complemento de devolução de venda para comercialização subsequente |
| 2 | 02 - Complemento de devolução de venda para consumidor final |
| 3 | 03 - Comp. de saída para comerc. subsequente ou transferência, amparada p. isenção ou não incidência |
| 4 | 04 - Complemento de saída para consumidor final, amparada por isenção ou não incidência |
| 5 | 05 - Comp. saída suj. a ST, p. com. subsequente ou transferência, amparada p. isenção/não incidência |
| 6 | 06 - Complemento de saída sujeita a ST, para comercialização subsequente |
| 7 | 07 - Complemento de saída por ECF, para contribuintes do imposto e a comercialização subsequente |
| 8 | 08 - Fato gerador não realizado |

### Opções para campo ENVWMSCONFIRMADA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| P | Parâmetro global |
| S | Sim |

### Opções para campo PERMCONFPARCIALWMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCICMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Não calcula e não digita |
| B | Não calcula e digita |
| C | Calcula e não digita |
| D | Calcula e digita |
| G | Calcula na confirmação |

### Opções para campo REDICMSBCPISCONFINS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMCSL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATUALESTTERC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| D | Subtrair do Estoque de terceiros em poder da empresa |
| N | Não controla |
| P | Somar ao estoque próprio em poder de terceiros |
| R | Subtrair do estoque próprio em poder de terceiros |
| T | Somar ao Estoque de terceiros em poder da empresa |

### Opções para campo ESTOQUEMPTERCEIRO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| D | Subtrair do estoque de terceiros em poder da empresa |
| N | Não controla |
| T | Somar ao estoque de terceiros em poder da empresa |

### Opções para campo ATUALINDENIZ (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Atualizar |
| -1 | Subtrair |
| 1 | Somar |

### Opções para campo NFSEPORNAT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMII (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMVAVTCON (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PODEAJUSTARORIGPRODWMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRANSFWMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| D | Considerar Destino |
| O | Considerar Origem |

### Opções para campo VALTBCOMPCR (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STATUSLOTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMREAICMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERAPLANPROD (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTEGRAEVENTO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SEPBALCAO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRANSFCBGLOBAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AGRUPASERVFAT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MARCARNAOPENDENTE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESTOPADRCST1400 (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SUGERELOCALPARC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USACUSMEDBASEST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALTITEMPARCFAT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GRAHISALTPED (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AGRUPAPRODNFE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NFE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Ajuste |
| B | Nota de Crédito |
| C | Complementar |
| D | Devolução |
| E | Import. Doc. (Emissão Própria) |
| F | Nota de Débito |
| M | Convencional (Não Usa NF-e) |
| N | Normal |
| T | Terceiros |

### Opções para campo NFCOM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| M | Convencional (Não Usa NFCom) |
| N | Normal |
| T | Terceiros |

### Opções para campo TPNFDEB (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 01 | Transferência de créditos para Cooperativas |
| 02 | Anulação de Crédito por Saídas Imunes/Isentas |
| 03 | Débitos de notas fiscais não processadas na apuração |
| 04 | Multa e juros |
| 05 | Transferência de crédito de sucessão |

### Opções para campo TPNFCRED (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 01 | Multa e juros |
| 02 | Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM (art. 450, § 1°, LC 214/25) |

### Opções para campo TIPOIMPKIT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| C | Componentes |
| K | Kit |
| T | Kit e Componentes |

### Opções para campo CODNATOPERISS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A1 | A1 - Tributado em São Paulo, porém Isento |
| B1 | B1 - Tributado Fora de São Paulo, porém Isento |
| E | E - Exigível |
| F | F - Tributado Fora de São Paulo |
| im | im - Imune |
| is | is - Isenta |
| M | M - Tributado em São Paulo, porém Imune |
| N | N - Tributado Fora de São Paulo, porém Imune |
| NB | NB - Tributação no Município |
| NI | NI - Não incidência |
| nt | nt – Não tributada |
| N1 | N - Tributação fora de Nova Santa Rita - RS |
| P | P - Exportação de Serviços |
| PB | PB - Emp. Simples Nacional |
| R | R - Retido/Isento/Imune |
| R1 | R - Tributado em São Paulo com Indicação de Imunidade Objetiva |
| S | S - Tributação em Nova Santa Rita - RS |
| T | T - Tributado em São Paulo |
| TB | TB - Tributação Fora do Município |
| tp | tp – Tributada no prestador |
| tt | tt – Tributada no tomador |
| V | V - Tributado Fora de São Paulo, porém Exigibilidade Suspensa |
| X | X - Tributado em São Paulo, porém Exigibilidade Suspensa |
| 01 | 1 - Exigível |
| 02 | 2 - Não incidência |
| 04 | 4 - Exportação |
| 05 | 5 - Imunidade |
| 06 | 6 - Exigibilidade suspensa por decisão judicial |
| 07 | 7 - Exigibilidade suspensa por procedimento administrativo |
| 08 | 8 - Fixo |
| 09 | 9 - Isento por lei específica |
| 1 | 1 - Tributação no Município |
| 2 | 2 - Tributação fora do Município |
| 3 | 3 - Isenção |
| 4 | 4 - Imune/Exportação |
| 5 | 5 - Exigibilidade suspensa por decisão judicial |
| 6 | 6 - Exigibilidade suspensa por procedimento administrativo |

### Opções para campo COPIADTPREVORIG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPMOVBEMSPED (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| AT | AT-Alienação ou Transferência |
| MC | MC-Imobilização oriunda de Ativo Circulante |
| OT | OT-Outras Saídas do Imobilizado |
| PE | PE-Perecimento, Extravio ou Deterioração |

### Opções para campo TEMIPI (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IPIEMBUT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SOMARIPI (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IPIINCICMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Usar do Parceiro |
| N | Não Incide |
| S | Incide |

### Opções para campo CSTIPIENT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Entrada c/Recuperação de Crédito |
| -1 | (-1) Não sujeita ao IPI |
| 1 | 01-Entrada c/Alíquota zero |
| 2 | 02-Entrada Isenta |
| 3 | 03-Entrada Não Tributada |
| 4 | 04-Entrada Imune |
| 49 | 49-Outras Entradas |
| 5 | 05-Entrada c/Suspensão |

### Opções para campo CSTIPISAI (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| -1 | (-1) Não sujeita ao IPI |
| 50 | 50-Saída Tributada |
| 51 | 51-Saída c/Alíquota zero |
| 52 | 52-Saída Isenta |
| 53 | 53-Saída Não Tributada |
| 54 | 54-Saída Imune |
| 55 | 55-Saída c/Suspensão |
| 99 | 99-Outras Saídas |

### Opções para campo CALCDIFICMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SOMASUBST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMICMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMFUNRURAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMIRF (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMPIS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMCOFINS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMISS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCFETHAB (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CLASSIFICMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Usar do Parceiro |
| C | Consumidor Final Não Contribuinte |
| I | Isento de ICMS |
| P | Produtor Rural |
| R | Revendedor |
| X | Consumidor Final Contribuinte |

### Opções para campo ATUSALDOCONT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| B | Baixar |
| E | Entrar |
| null | Não atualiza |

### Opções para campo COMPLEMENTO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | de Ajuste |
| N | Normal |
| S | Complementar |

### Opções para campo TIPOEMISSAONFCOM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | de Ajuste |
| N | Normal |
| S | Substituição |

### Opções para campo INDNATFRT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Operações de vendas, com ônus suportado pelo estabelecimento vendedor |
| 1 | 1 - Operações de vendas, com ônus suportado pelo adquirente |
| 2 | 2 - Operações de compras(bens para revenda, matérias-prima e outros produtos, geradores de crédito) |
| 3 | 3 - Operações de compras(bens p/ revenda, matéria-prima e outros produtos, não geradores de crédito) |
| 4 | 4 - Transferência de produtos acabados entre estabelecimentos da pessoa jurídica |
| 5 | 5 - Transferência de produtos em elaboração entre estabelecimentos da pessoa jurídica |
| 9 | 9 - Outras |

### Opções para campo NATBCCRED (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 01 | 01-Aquisição de bens para revenda |
| 02 | 02-Aquisição de bens utilizados como insumo |
| 03 | 03-Aquisição de serviços utilizados como insumo |
| 04 | 04-Energia elétrica e térmica, inclusive sob a forma de vapor |
| 05 | 05-Aluguéis de prédios |
| 06 | 06-Aluguéis de máquinas e equipamentos |
| 07 | 07-Armazenagem de mercadoria e frete na operação de venda |
| 08 | 08-Contraprestações de arrendamento mercantil |
| 09 | 09-Máq., equip. e outros bens incorporados ao ativo imobilizado(créd. sob. encargos de depreciação) |
| 10 | 10-Máq., equip. e outros bens incorporados ao ativo imobilizado(créd. c/ base no valor de aquisição) |
| 11 | 11-Amortização e Depreciação de edificações e benfeitorias em imóveis |
| 12 | 12-Devolução de Vendas Sujeitas à Incidência Não-Cumulativa |
| 13 | 13-Outras Operações com Direito a Crédito |
| 14 | 14-Atividade de Transporte de Cargas - Subcontratação |
| 15 | 15-Atividade Imobiliária - Custo Incorrido de Unidade Imobiliária |
| 16 | 16-Atividade Imobiliária - Custo Orçado de unidade não concluída |
| 17 | 17-Ativ. Prestação Serv. de Limp., Conservação e Manut. - V.T., V.R. ou V.A., fardamento ou uniforme |
| 18 | 18-Estoque de abertura de bens |

### Opções para campo BASENUMERACAO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | DAV cupom fiscal |
| D | Devolução de Venda |
| E | Devolução de Compra |
| I | Impressora |
| L | Lote de Produção |
| O | Pedido de Compra |
| P | Pedido de Venda |
| Q | Requisição |
| S | Manual (Informada pelo Usuário) |
| T | TOP |
| V | Venda |

### Opções para campo NUMSOMAUT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRAVAFIMIMP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPONUMERACAO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| F | Empresa |
| M | Matriz |
| S | Empresa / Série |
| U | Única |
| Z | Matriz / Série |

### Opções para campo EMITENOTA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Manual |
| O | Opcional |
| P | Proibido |
| S | Na Confirmação |

### Opções para campo EMITEBOLETA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Manual |
| P | Proibido |
| S | Na Confirmação |

### Opções para campo IMPNOTAADICIONAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALESTMAXIMO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALIDADATA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMPNAOCONF (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALNUM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| E | Parceiro / Número / Série |
| N | Não Validar |
| P | Parceiro / Número |
| S | Parceiro / Número / Tipo Movimento / Série |
| U | Parceiro / Número / Tipo Movimento |
| 1 | PROIBIR - Parceiro / Número / Tipo Mov. / Série |
| 2 | PROIBIR - Parceiro / Número / Tipo Mov. |
| 3 | PROIBIR - Parceiro / Número / Série |
| 4 | PROIBIR - Parceiro / Número |
| 5 | Número / Tipo Movimento |

### Opções para campo NFSE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| M | Convencional (Não usa NFS-e) |
| N | Normal |

### Opções para campo ICMSPROPFRETE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ICMSPROPSEG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ICMSPROPDESTAQUE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ICMSPROPJURO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ICMSPROPEMBALAGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISPROPFRETE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISPROPSEG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISPROPDESTAQUE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISPROPEMBALAGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISPROPJURO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IPIPROPFRETE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IPIPROPSEG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IPIPROPDESTAQUE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IPIPROPEMBALAGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IPIPROPJURO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COFINSPROPFRETE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COFINSPROPSEG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COFINSPROPDESTAQUE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COFINSPROPEMBALAGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COFINSPROPJURO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STPROPFRETE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STPROPFRETEEXT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STPROPSEG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STPROPDESTAQUE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STPROPEMBALAGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo STPROPJURO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPIVASUBST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| null | Soma Base S.T. / Soma Base ICMS Reduzida |
| 1 | Soma Base S.T. / Soma Base ICMS sem Redução |

### Opções para campo CALCSTFRTXTNOTPROP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BASEICMSFRETECALCST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXPGRS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não exportar |
| 1 | Inclusão |
| 2 | Cancelamento |

### Opções para campo EXPTES (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Arrecadação |
| N | Não exportar |
| R | Reclamação Cobrança Indevida - RI |

### Opções para campo ATUALCOMOS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPFATSERV (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Pelo Mód. Serviço por Horas de O.S. Executadas |
| C | Pela Central de Atendimento ao Cliente |
| F | Pelo Mód. Serviço para O.S. Fechadas |
| N | Não Faturar |
| P | Pelo Mód. Serviço pelas Parcelas do Financeiro |
| S | Pelo Mód. Serviço todas as Parcelas do Financeiro |
| U | Pelo Mód. Serviço ou pela Central (todas Parcelas) |

### Opções para campo BUSCMPTERC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| E | Busca com Local de Entrada |
| N | Não busca |
| P | Busca com Local de Produção |
| S | Busca com local da Nota |

### Opções para campo ATUALFINTERC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZAWMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Automática |
| M | Manual |
| N | Não Utiliza |

### Opções para campo TIPATUALWMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| B | Baixar |
| E | Entrar |

### Opções para campo ATUALDATRECWMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| D | Diário |
| M | Mensal |
| N | Não Utiliza |
| S | Semanal |

### Opções para campo EXIGEAGENDAWMS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXPORTA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATUALIZARATEIO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSIGNACAO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COFINSSTPROPFRETE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISSTPROPEMBALAGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SOMARCOFINSST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COFINSSTPROPSEG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COFINSSTPROPEMBALAGEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo COFINSSTPROPDESTAQUE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SOMARPISST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISSTPROPFRETE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISSTPROPJURO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTEGSERCON (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| B | Baixa |
| E | Entrada |
| N | Não atualizar |

### Opções para campo COFINSSTPROPJURO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISSTPROPDESTAQUE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PISSTPROPSEG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AD_RELATORIO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 1 | Não |

### Opções para campo ATUALCTB (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OPERCOMMOEDA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SEMMOEDAFIN (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NFEESTORNO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APLICLEITRANSP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Nunca aplicar |
| P | Usar do parceiro |
| S | Aplicar sempre |

### Opções para campo APLICTABIRFINSS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USASERVTABIRFINSS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDTERC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCONNFSE (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| C | Nota |
| N | Não usa |
| S | Financeiro |

### Opções para campo DISTSTVLRUNITFAT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCFCPINT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ICMSORIGESTPED (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDTIPREC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Receita própria - serviços prestados |
| 1 | 1 - Receita própria - cobrança de débitos |
| 2 | 2 - Receita própria - venda de serviço pré-pago - faturamento de períodos anteriores |
| 3 | 3 - Receita própria - venda de serviço pré-pago - faturamento no períodos |
| 4 | 4 - Outras receitas próprias de serviços de comunicação e telecomunicações |
| 5 | 5 - Receita própria - co-faturamento |
| 6 | 6 - Receita própria - serviços a faturar em período futuro |
| 7 | 7 - Outras receitas próprias de natureza não-cumulativa |
| 8 | 8 - Outras receitas de terceiros |
| 9 | 9 - Outras receitas |

### Opções para campo GERADEMANDAMPS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo LIGORIGORIG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IGNEXPAUTLOT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATUALESTWMSTERC (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USARECPARCIAL (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALSITCADRF (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERCORAPON (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSVLRREMRETIND (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| null | Considerar como Desconto e Sem Pagamento (tipo de pagamento = 90) |
| 1 | Considerar apenas como Desconto |

### Opções para campo INTERMED (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Operação sem intermediador (em site ou plataforma própria) |
| 1 | 1-Operação em site ou plataforma de terceiros (intermediadores/marketplace) |

### Opções para campo DEVSEMDESTAQUEST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DEVSEMDESTAQUEIPI (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SEMCREDIPIST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo IGNORACOMPLITEM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMITECNAEDIFNOTA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OUTDESPSTEXTNOTA (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMPXMLMANTDESPACES (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REDPISBCPISCOFINS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CALCPISCFSFIN (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALDISPESTDEV (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSNFERELCANCEFD (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USAVENDAMAIS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMTRANSGALPAO (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo REDSTBCPISCOFINS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCONSLCDPR (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSTOPAPURSIMP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IGNOBSORIGREM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DEDFCPBCPISCOFINS (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| F | FCP |
| N | Não Deduz |
| S | FCP-ST |

### Opções para campo CONFVLREVENT68 (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| L | Valor líquido do produto |
| null | Valor do produto |

### Opções para campo GERINFOEFDPAG (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCOMPLCUST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| null | Não se aplica |
| -1 | Negativo |
| 1 | Positivo |

### Opções para campo RECBRUTACIAP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não afeta |
| S | Soma |
| T | Subtrai |

### Opções para campo ARREDQTDUNALT (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AD_VALTECCOM (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OPERESSACOMP (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSDISBAIXEST (Tabela: TGFTOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFTPP
### Descrição: Tipos de Parceiros

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODTIPPARC` | Cód. Perfil | I |  |
| `CODUSUALTREG` | Cód. Usuário Alteração | I |  |
| `DHALTREG` | Dt. Alteração | H |  |
| `DESCRTIPPARC` | Descrição | S |  |
| `ANALITICO` | Analítico | S | Veja opções na seção OPÇÕES |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `CODTIPPARCPAI` | Cód. Perfil Pai | I |  |
| `GRAU` | Grau | I |  |
| `CODTAB` | Tabela de preço | I |  |
| `CODANT` | SGE | I |  |
| `TIPANT` | Tipo no SGE | S |  |
| `AD_VENDDESC` | Valor do pedido para 3% desconto | F |  |
| `AD_COMISSAO` | Comissao | F |  |
| `AD_MAXDESCONTO` | Max Desconto | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo ANALITICO (Tabela: TGFTPP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVO (Tabela: TGFTPP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFTPV
### Descrição: Tipos de Negociação

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODTIPVENDA` | Tipo de Negociação | I |  |
| `TIMQTDPARC` | Qtd. Parcelas Lançamento | I |  |
| `POSSUISIMSALVA` | Possui Simulação Salva | S |  |
| `DESCRTIPVENDA` | Descrição | S |  |
| `EXVENDAMAIS` | Exclusivo Venda Mais | S | Veja opções na seção OPÇÕES |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `SUBTIPOVENDA` | Subtipo | S | Veja opções na seção OPÇÕES |
| `BASEPRAZO` | Base do prazo | I | Veja opções na seção OPÇÕES |
| `VENDAMIN` | Valor mínimo p/ venda | F |  |
| `VENDAMAX` | Valor máximo p/ venda | F |  |
| `COMPRAMAX` | Valor máximo p/ compra | F |  |
| `COMISSAO` | Comissão | F |  |
| `GRUPOAUTOR` | Grupo de autorização | S |  |
| `SOMAPRAZOCLIENTE` | Soma prazo de cliente | S | Veja opções na seção OPÇÕES |
| `VALPRAZOCLIENTE` | Valida prazo de cliente | S | Veja opções na seção OPÇÕES |
| `FIXAVENC` | Fixa vencimento | S | Veja opções na seção OPÇÕES |
| `PODECONSUMIDOR` | Pode ser usado por consumidor | S | Veja opções na seção OPÇÕES |
| `CODTAB` | Tabela de preço | I |  |
| `NUNOTA` | Cabeçalho modelo | I |  |
| `EMITEBOLETA` | Imprimir Pix/Boleto/Duplicata? | S | Veja opções na seção OPÇÕES |
| `CODTCF` | Tabela financeira | I |  |
| `CODOBSPADRAO` | Observação Padrão | I |  |
| `PRAZOMEDMAX` | Prazo médio máximo | I |  |
| `PRAZOMAX` | Prazo máximo | I |  |
| `LUCROMIN` | % Lucro mínimo | F |  |
| `MARGEMMIN` | % MC Mínima | F |  |
| `CODFORMDESCMAX` | Fórmula desc. máximo | I |  |
| `CODFORMDESCMAXITENS` | Fórmula desc. máximo ítens | I |  |
| `DESCPROM` | Desconto Promocional | S | Veja opções na seção OPÇÕES |
| `DESCMAX` | % Desconto máximo | F |  |
| `TAXAJURO` | Taxa em % | F |  |
| `TIPTAXA` | Tipo da taxa | S | Veja opções na seção OPÇÕES |
| `TIPJURO` | Apresentação da taxa | S | Veja opções na seção OPÇÕES |
| `CODCTACTB_1` | Conta contábil 1 | I |  |
| `CODCTACTB_2` | Conta contábil 2 | I |  |
| `PERCMINENTRADA` | % Mín. entrada | F |  |
| `PRAZOMAXPRIPARC` | Prazo máx. 1ª parcela | I |  |
| `NROPARCELAS` | Número de parcelas | I |  |
| `DHALTER` | Data e hora alteração | H |  |
| `APRESTRANSP` | Apresenta transportadora | S | Veja opções na seção OPÇÕES |
| `FLEX` | Usar Créd. Flex | S | Veja opções na seção OPÇÕES |
| `EMITEDUPL` | Emite duplicata | S | Veja opções na seção OPÇÕES |
| `BAIXA` | Baixa | S | Veja opções na seção OPÇÕES |
| `CODUSU` | Cód. Usuário | I |  |
| `MODELOPGTO` | Disponível para simulação? | S | Veja opções na seção OPÇÕES |
| `TAXAJURSIM` | Taxa de juros em simulações | F |  |
| `TIPOJURSIM` | Tipo de juros em simulações | S | Veja opções na seção OPÇÕES |
| `PRAZOMIN` | Prazo mínimo | I |  |
| `EDITASIMULACAO` | Permite edição simulação pgto.? | S | Veja opções na seção OPÇÕES |
| `TXPARCADM` | Taxa mensal de Administradora | F |  |
| `INTEGRAECONECT` | Integrar com Econect | S | Veja opções na seção OPÇÕES |
| `FORMARECBTOSOCIN` | Forma Recebto. | I |  |
| `VENCPREFIXPED` | Vencimento pré-fixado no pedido | S | Veja opções na seção OPÇÕES |
| `AD_FRETEST` | Somente frete/st na 1º parcela | S | Veja opções na seção OPÇÕES |
| `FASTUSA` | Utiliza no Fast Service? | S | Veja opções na seção OPÇÕES |
| `ARREDPRIMEIRAPARC` | Ajusta arredondamento na 1ª parcela | S | Veja opções na seção OPÇÕES |
| `TRUNCPARCELA` | Truncar valores no parcelamento | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo EXVENDAMAIS (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVO (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SUBTIPOVENDA (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| 1 | A vista |
| 2 | A prazo |
| 3 | Parcelada |
| 4 | Cheque pré-datado |
| 5 | Crediário |
| 6 | Financeira |
| 7 | Cartão de Crédito |
| 8 | Cartão de Débito |

### Opções para campo BASEPRAZO (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| 0 | A partir do dia |
| 1 | Fora a semana |
| 2 | Fora a dezena |
| 3 | Fora a quinzena |
| 4 | Fora o mês |

### Opções para campo SOMAPRAZOCLIENTE (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALPRAZOCLIENTE (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FIXAVENC (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PODECONSUMIDOR (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EMITEBOLETA (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Manual |
| P | Proibido |
| S | Na confirmação |

### Opções para campo DESCPROM (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| D | Considerar por Qtde/Desconto |
| L | Limitante |
| M | Considerar Maior |
| N | Não considerar |
| O | Somar os dois |
| Q | Considerar por Qtde Somando |
| S | Considerar sempre |

### Opções para campo TIPTAXA (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| E | Desconto |
| U | Juro taxa Única |

### Opções para campo TIPJURO (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| I | Incluir no preço do produto |
| O | Destacar na nota fiscal (valor sugerido) |

### Opções para campo APRESTRANSP (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FLEX (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EMITEDUPL (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BAIXA (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MODELOPGTO (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOJURSIM (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| C | Composto |
| S | Simples |

### Opções para campo EDITASIMULACAO (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTEGRAECONECT (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VENCPREFIXPED (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo AD_FRETEST (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| 1 | Somente Frete e ST |

### Opções para campo FASTUSA (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ARREDPRIMEIRAPARC (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRUNCPARCELA (Tabela: TGFTPV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFTRN
### Descrição: TopRegraNegocio

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NURNG` | Regra | I |  |
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `SEQEXEC` | Seq. de execução | I |  |

## Tabela: TGFUFP
### Descrição: TGFUFP

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUVIAG` | Nro. Viagem | I |  |
| `SEQMDFE` | Sequência do manifesto | I |  |
| `CODUF` | UF | I |  |
| `ORDEM` | Ordem Percurso | I |  |
| `SEQVIAGEM` | SEQVIAGEM | I |  |

## Tabela: TGFUNM
### Descrição: Unidades de Medida

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Único da Nota | I |  |
| `SEQMED` | Sequência da Medida | I |  |
| `UNMED` | Unidade de Medida | S | Veja opções na seção OPÇÕES |
| `TIPMED` | Tipo da Medida | S |  |
| `QTDMED` | Quantidade na medida | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo UNMED (Tabela: TGFUNM)
| Valor | Descrição |
|-------|-----------|
| 00 | M3 |
| 01 | KG |
| 02 | TON |
| 03 | UNIDADE |
| 04 | LITROS |
| 05 | MMBTU |


## Tabela: TGFVALP
### Descrição: Vale Pedágio

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro. Único da Nota | I |  |
| `SEQUENCIA` | Sequência do Vale Pedágio | I |  |
| `CODPARCFORN` | Parceiro Fornecedor | I |  |
| `NUCOMPRA` | Nro. Compra | S |  |
| `TIPPAG` | Pagante do Pedágio | S | Veja opções na seção OPÇÕES |
| `CODPARCPAG` | Parceiro Pagante | I |  |
| `VLRPEDAGIO` | Valor do Pedágio | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPPAG (Tabela: TGFVALP)
| Valor | Descrição |
|-------|-----------|
| B | Recebedor |
| D | Destinatário |
| E | Emitente |
| O | Outro |
| R | Remetente |
| X | Expedidor |


## Tabela: TGFVAR
### Descrição: Compras e Vendas com vários Pedidos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `STATUSNOTA` | Status | S |  |
| `SEQUENCIA` | Seq. Item | I |  |
| `NUNOTA` | Nro. Único Nota | I |  |
| `NUNOTAORIG` | Nro. Único de Origem | I |  |
| `CUSATEND` | Custo atendimento | F |  |
| `ORDEMPROD` | Ordem do produto | I |  |
| `SEQUENCIAORIG` | Seq. Item de Origem | I |  |
| `QTDATENDIDA` | Quantidade atendida | F |  |
| `NROATOCONCDRAW` | Número do ato concessório de Drawback | S |  |
| `NROREGEXPORT` | Número do Registro de Exportação | S |  |
| `NROMEMORANDO` | Nro Memorando Exportação | I |  |
| `FIXACAO` | Fixação | S |  |

## Tabela: TGFVEI
### Descrição: Veículos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODVEICULO` | Código do Veículo | I |  |
| `TIPOVEICULO` | Tipo Veículo | S | Veja opções na seção OPÇÕES |
| `MARCAPLACA` | Marca [Placa] | S |  |
| `PLACA` | Placa | S |  |
| `CODCID` | Cidade Emplacamento | I |  |
| `MARCAMODELO` | Marca Modelo | S |  |
| `ESPECIETIPO` | Espécie e Tipo | S |  |
| `CAPPOTCIL` | Cap/Pot/Cil | S |  |
| `COR` | Cor | S |  |
| `CATEGORIA` | Categoria | S |  |
| `PESOMAX` | Peso Máximo | F |  |
| `M3MAX` | Metros Cúbicos Máximo | F |  |
| `ANOFABRIC` | Ano Fabricação | I |  |
| `ANOMOD` | Ano Modelo | I |  |
| `CHASSIS` | Chassis | S |  |
| `NUMMOTOR` | Número do Motor | S |  |
| `VLRDEPRECMENSAL` | Depreciação mensal do veículo | F |  |
| `CODFORMFRETE` | Fórmula p/cálculo de Frete | I |  |
| `RENAVAM` | RENAVAM | S |  |
| `CODMOTORISTA` | Motorista | I |  |
| `PROPRIO` | Veículo da empresa | S | Veja opções na seção OPÇÕES |
| `CODPARC` | Parceiro ou Empresa | I |  |
| `CODPARCPROPANTT` | Parceiro ANTT | I |  |
| `VIATRANSP` | Via de Transporte | S | Veja opções na seção OPÇÕES |
| `COMBUSTIVEL` | Combustível | S | Veja opções na seção OPÇÕES |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `CODFUNC` | Funcionário | I |  |
| `CODEMPFOLHA` | Empresa | I |  |
| `ANTT` | RNTRC | S |  |
| `EMITEEXPED` | Emite Expedição | S | Veja opções na seção OPÇÕES |
| `CODMARCAMOD` | Cód.Marca/Modelo | I |  |
| `CORFAB` | Cor Fabricante | S |  |
| `POTENCIA` | Potência | S |  |
| `DISTEIXOS` | Distância entre Eixos | S |  |
| `SERIAL` | Serial | S |  |
| `CMKG` | Cap. Máx. de Tração | S |  |
| `TIPINT` | Tipo Pintura | S |  |
| `ESPVEI` | Espécie de Veículo | I |  |
| `TIPVEI` | Tipo de Veículo | I |  |
| `EMPPARC` | Empresa ou Parceiro | S | Veja opções na seção OPÇÕES |
| `CONDVIN` | Condição do VIN | S | Veja opções na seção OPÇÕES |
| `CONDVEI` | Condição do Veículo | I | Veja opções na seção OPÇÕES |
| `DESCR_EMP_PARC` | Descrição do campo Parceiro ou Empresa | S |  |
| `VLRSEGMENSAL` | Valor do Seguro Mensal | F |  |
| `TIPFORMFRETE` | Tipo de Fórmula de Frete | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `VOLTAGEM` | Voltagem | S |  |
| `CODQUEST` | Questionário | I |  |
| `CODPROD` | Produto | I |  |
| `TIPOCOMBUST` | Tipo de Combustível (Tabela RENAVAM) | I |  |
| `CORDENATRAN` | Código da Cor (Tabela DENATRAN) | I |  |
| `MAXLOTACAO` | Capacidade Máxima de Lotação | I |  |
| `RESTRICAO` | Restrição | I | Veja opções na seção OPÇÕES |
| `TIPOROD` | Tipo de Rodado | S | Veja opções na seção OPÇÕES |
| `TIPOCAR` | Tipo de Carroceria | S | Veja opções na seção OPÇÕES |
| `TIPOPROP` | Tipo de Proprietário | S | Veja opções na seção OPÇÕES |
| `TARA` | Tara do veículo | F |  |
| `CODCENCUS` | Centro Resultado | I |  |
| `AFERICAO` | Aferição | S | Veja opções na seção OPÇÕES |
| `TIPOAFERICAO` | Tipo Aferição | S | Veja opções na seção OPÇÕES |
| `CODBEM` | Código do bem | S |  |
| `CODEMBARCACAO` | Cód. Embarcação | S |  |
| `TIPOEMBARCACAO` | Tipo Embarcação | I | Veja opções na seção OPÇÕES |
| `NOMEEMBARCACAO` | Nome Embarcação | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOVEICULO (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| 1 | Rodoviário |
| 3 | Aquaviário |

### Opções para campo PROPRIO (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VIATRANSP (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| A | Aéreo |
| F | Ferroviário |
| M | Marítimo |
| R | Rodoviário |

### Opções para campo COMBUSTIVEL (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| A | Álcool |
| B | Gasogênio |
| C | Gás Metano |
| D | Diesel |
| E | Elétrico/Fonte Interna |
| F | Álcool/Gasolina |
| G | Gasolina |
| H | Elétrico/Fonte Externa |
| I | Gasolina/Gás Natural Combustível |
| J | Álcool/Gás Natural Combustível |
| K | Diesel/Gás Natural Combustível |
| L | Álcool/Gás Natural Veicular |
| M | Gasolina/Gás Natural Veicular |
| N | Gás Natural Veicular |
| O | Vide/Campo/Observação |
| P | Diesel/Gás Natural Veicular |
| Q | Gasolina/Álcool/Gás Natural Veicular |
| R | Gasolina/Elétrico |

### Opções para campo TIPO (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| B | Bi-Trem |
| C | Caminhão |
| E | 4º EIXO |
| R | Carreta |
| Z | Bitruck |

### Opções para campo EMITEEXPED (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EMPPARC (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| E | Empresa |
| P | Parceiro |

### Opções para campo CONDVIN (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| N | Normal |
| R | Remarcado |

### Opções para campo CONDVEI (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - Acabado |
| 2 | 2 - Inacabado |
| 3 | 3 - Semi-Acabado |

### Opções para campo ATIVO (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RESTRICAO (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-Não há |
| 1 | 1-Alienação Fiduciária |
| 2 | 2-Arrendamento Mercantil |
| 3 | 3-Reserva de Domínio |
| 4 | 4-Penhor de Veículos |
| 9 | 9-Outras |

### Opções para campo TIPOROD (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| 00 | 00-Não Aplicável |
| 01 | 01-Truck |
| 02 | 02-Toco |
| 03 | 03-Cavalo Mecânico |
| 04 | 04-Van |
| 05 | 05-Utilitário |
| 06 | 06-Outros |

### Opções para campo TIPOCAR (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| 00 | 00-Não Aplicável |
| 01 | 01-Aberta |
| 02 | 02-Fechada/Baú |
| 03 | 03-Graneleira |
| 04 | 04-Porta Container |
| 05 | 05-Sider |

### Opções para campo TIPOPROP (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| 0 | 0-TAC-Agregado |
| 1 | 1-TAC-Independente |
| 2 | 2-Outros |

### Opções para campo AFERICAO (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| N | Não Usa |
| O | Obrigatória |
| P | Permitida |

### Opções para campo TIPOAFERICAO (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| H | Horímetro |
| K | Hodômetro |
| N | Não Usa |

### Opções para campo TIPOEMBARCACAO (Tabela: TGFVEI)
| Valor | Descrição |
|-------|-----------|
| 11 | 11-Empurrador |
| 39 | 39-Balsa |


## Tabela: TGFVEN
### Descrição: Vendedores Representantes

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `SALDODISPCAC` | Saldo Diponivel do Carrinho | F |  |
| `PROVACRESCCAC` | Provisão do carrinho | F |  |
| `CODVEND` | Código | I |  |
| `APELIDO` | Apelido | S |  |
| `TIPOCERTIF` | Tipo p/ certificação | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `CODREG` | Região | I |  |
| `COMVENDA` | Comissão venda | F |  |
| `COMGER` | Comissão gerência | F |  |
| `VLRHORA` | Valor hora p/ comissão de O.S. | F |  |
| `CODFORM` | Fórmula Comissão | I |  |
| `CODCARGAHOR` | Carga Horária | I |  |
| `DIACOM` | Dia inicial p/período de comissão | I |  |
| `CODEMP` | Empresa | I |  |
| `CODGER` | Gerente | I |  |
| `CODPARC` | Parceiro | I |  |
| `CODFUNC` | Funcionário | I |  |
| `CODCENCUSPAD` | Centro Resultado Padrão | I |  |
| `PERCCUSVAR` | % Custo Variável | F |  |
| `EMAIL` | Email | S |  |
| `SALDODISP` | Saldo Disponível | F |  |
| `PROVACRESC` | Provisão acréscimo | F |  |
| `DESCMAX` | Desconto máximo | F |  |
| `TIPVALOR` | Usar valor p/ comissão de OS | S | Veja opções na seção OPÇÕES |
| `ACRESCMAX` | Acréscimo máximo | F |  |
| `TIPVEND` | Tipo | S | Veja opções na seção OPÇÕES |
| `GRUPORETENCAO` | Grupo de retenção | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Data de alteração | H |  |
| `PARTICMETA` | Participação na meta | F |  |
| `SENHA` | Senha | I |  |
| `ATUACOMPRADOR` | Atua também como comprador | S | Veja opções na seção OPÇÕES |
| `TIPCALC` | Pagamento de Comissão por data de | S | Veja opções na seção OPÇÕES |
| `GRUPODESCVEND` | Grupo Desc. Vendedor | S |  |
| `COMCM` | Recebe comissão em CM | S | Veja opções na seção OPÇÕES |
| `RECHREXTRA` | Recebe Hora Dobrada | S | Veja opções na seção OPÇÕES |
| `TIPFECHCOM` | Tipo de fechamento de comissão | S | Veja opções na seção OPÇÕES |
| `AD_METAQTD` | Meta de peças | F |  |
| `AD_METAVLR` | Meta Preço Médio | F |  |
| `AD_METAPARC` | Meta de parc. novos | I |  |
| `AD_TRCOM` | Trava Comissão | F |  |
| `AD_VENDDESC` | Valor do pedido para 3% desconto | F |  |
| `AD_GRUPOAUTOR` | Grupo de autorização | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TGFVEN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPVALOR (Tabela: TGFVEN)
| Valor | Descrição |
|-------|-----------|
| N | da Negociação |
| U | do Vendedor |

### Opções para campo TIPVEND (Tabela: TGFVEN)
| Valor | Descrição |
|-------|-----------|
| C | Comprador |
| E | Executante |
| G | Gerente |
| R | Representante |
| S | Supervisor |
| T | Técnico |
| V | Vendedor |

### Opções para campo ATUACOMPRADOR (Tabela: TGFVEN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCALC (Tabela: TGFVEN)
| Valor | Descrição |
|-------|-----------|
| B | Baixa |
| N | Negociação |

### Opções para campo COMCM (Tabela: TGFVEN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECHREXTRA (Tabela: TGFVEN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPFECHCOM (Tabela: TGFVEN)
| Valor | Descrição |
|-------|-----------|
| F | Financeiro |
| N | Nenhuma |
| P | Folha |


## Tabela: TGFVIAG
### Descrição: Viagem

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUVIAG` | Nro. Viagem | I |  |
| `CODEMP` | Empresa | I |  |
| `SERIE` | Série | S |  |
| `STATUSDOC` | Status Doc. | S | Veja opções na seção OPÇÕES |
| `CODVEIPRIN` | Veículo de tração | I |  |
| `CODVEIREB1` | Reboque 1 | I |  |
| `CODVEIREB2` | Reboque 2 | I |  |
| `CODVEIREB3` | Reboque 3 | I |  |
| `TIPAMB` | Tip. Amb. MDF-e | S | Veja opções na seção OPÇÕES |
| `DHALTER` | Data de Alteração | H |  |
| `CODUSU` | CODUSU | I |  |
| `USACIOTCTEVINC` | Usar CIOTs dos CT-e vinculados ao MDF-e? | S | Veja opções na seção OPÇÕES |
| `USATOMSERVCONTR` | Usar tomadores de serv. como contratantes? | S | Veja opções na seção OPÇÕES |
| `CONTEMDOCTERC` | Contém documentos de terceiros? | S | Veja opções na seção OPÇÕES |
| `TIPMODALMDFE` | Tipo Modal MDFe | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo STATUSDOC (Tabela: TGFVIAG)
| Valor | Descrição |
|-------|-----------|
| C | Confirmado |
| E | Em edição |

### Opções para campo TIPAMB (Tabela: TGFVIAG)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Usa |
| 1 | Produção |
| 2 | Homologação |

### Opções para campo USACIOTCTEVINC (Tabela: TGFVIAG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USATOMSERVCONTR (Tabela: TGFVIAG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONTEMDOCTERC (Tabela: TGFVIAG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPMODALMDFE (Tabela: TGFVIAG)
| Valor | Descrição |
|-------|-----------|
| 1 | Rodoviário |
| 3 | Aquaviário |


## Tabela: TGFVOA
### Descrição: Volume Alternativo

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPROD` | Produto | I |  |
| `CODVOL` | Unidade | S |  |
| `DIVIDEMULTIPLICA` | Operação | S | Veja opções na seção OPÇÕES |
| `QUANTIDADE` | Quantidade | F |  |
| `M3` | Metros Cúbicos | F |  |
| `SELECIONADO` | Seleção | S |  |
| `MULTIPVLR` | Multiplicador do valor | F |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `CODBARRA` | Código de Barras | S |  |
| `TIPCODBARRA` | Tipo do código de barras | S | Veja opções na seção OPÇÕES |
| `CONTROLE` | Controle | S |  |
| `UNIDTRIB` | Unid. Tributação | S | Veja opções na seção OPÇÕES |
| `UNIDSELO` | Unid. Selo | S | Veja opções na seção OPÇÕES |
| `TIPGTINNFE` | EAN/GTIN Unid.Tributação | I | Veja opções na seção OPÇÕES |
| `LASTRO` | Lastro | I |  |
| `CAMADAS` | Camadas | I |  |
| `OPCAOSEP` | Apresentar nas tarefas do WMS | S | Veja opções na seção OPÇÕES |
| `DESCRDANFE` | Descrição de unidade/qtd. para o DANFE | S |  |
| `UNTRIBEXPORTACAO` | Un. Tributação Exportação em Toneladas | S | Veja opções na seção OPÇÕES |
| `QTDDECIMAISUPF` | Qtd Casas Decimais UPF | I |  |
| `DESCRUNTRIBEXPORT` | Descrição Un. Tributação Exportação | S |  |
| `OPCOESGERAR0220` | Opções para gerar Registros 0220 | S | Veja opções na seção OPÇÕES |
| `UNDTRIBRECOB` | Unidade de Tributação para RECOB | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo DIVIDEMULTIPLICA (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| D | Divide |
| M | Multiplica |

### Opções para campo ATIVO (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCODBARRA (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| A | EAN13 |
| B | EAN14 |

### Opções para campo UNIDTRIB (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UNIDSELO (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPGTINNFE (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| 0 | Não Informar |
| 1 | Código do Produto |
| 2 | Referência |
| 3 | Código de Barras |

### Opções para campo OPCAOSEP (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UNTRIBEXPORTACAO (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OPCOESGERAR0220 (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| null | Utiliza Unidade Alternativa |
| 2 | Utiliza UND do Produto Equivalente |
| 3 | A partir da função |

### Opções para campo UNDTRIBRECOB (Tabela: TGFVOA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFVOL
### Descrição: Volumes

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODVOL` | Sigla da Unidade | S |  |
| `DESCRVOL` | Descrição | S |  |
| `UTILIREGVOLWMS` | Utiliza no Registro de Volumes WMS | S | Veja opções na seção OPÇÕES |
| `DECQTD` | Decimais para quantidade | I |  |
| `CODVOLFCI` | Unidade para FCI | S |  |
| `UTILICONFPESO` | Utiliza Conferência por peso | S | Veja opções na seção OPÇÕES |
| `NUVERSAO` | Versão | I |  |
| `ATUNUVERSAO` | Atualizar versão | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo UTILIREGVOLWMS (Tabela: TGFVOL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILICONFPESO (Tabela: TGFVOL)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIACE
### Descrição: Sugestao Acesso Cartao EVO

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `RESOURCEID` | ResourceID | S |  |
| `CODUSU` | Cod. Usuário | I |  |
| `LIBERADO` | Liberado | S | Veja opções na seção OPÇÕES |
| `DTALTER` | Dt. Alteração | H |  |
| `ALTERADOPELOUSUARIO` | Acesso alterador pelo usuário | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo LIBERADO (Tabela: TSIACE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALTERADOPELOUSUARIO (Tabela: TSIACE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIACI
### Descrição: Controle de Acesso dos Relatórios

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Cód. Usuário | I |  |
| `CODGRUPO` | Cód.Grupo de Usuário | I |  |
| `CODREL` | Cód.Relatório | I |  |
| `CONS` | Permite Consulta ? | S |  |
| `ALTERA` | Permite Alteração? | S |  |
| `FILTRO` | Permite Alterar Filtros? | S |  |
| `RESUMO` | Permite Alterar Resumo? | S |  |
| `SEGURANCA` | Permite Outros Usuários a Alterar | S |  |

## Tabela: TSIACM
### Descrição: Acesso Menu

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Cód. Usuário | I |  |
| `SEQACESSO` | Seq. Acesso | I |  |
| `DHACESSO` | Dh. Acesso | H |  |
| `RESOURCEID` | Id da Tela | S |  |
| `CAMINHO` | Caminho do Menu | S |  |
| `DESCRMENU` | Menu | S |  |

## Tabela: TSIAGE
### Descrição: Agências Bancárias

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODAGE` | Agência | S |  |
| `CODBCO` | Banco | I |  |
| `NOMEAGE` | Nome da Agência | S |  |
| `NOMEGER` | Nome do Gerente | S |  |
| `TELEFONE` | Telefone | S |  |
| `FAX` | Fax | S |  |
| `EMAIL` | Email | S |  |
| `CODEND` | Endereço | I |  |
| `NUMEND` | Número | S |  |
| `COMPLEMENTO` | Complemento | S |  |
| `CEP` | CEP | S |  |
| `CODBAI` | Bairro | I |  |
| `CODCID` | Cód. Cidade | I |  |

## Tabela: TSIALT
### Descrição: Log Alterações

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NOMETAB` | Nome tabela | S |  |
| `DHACAO` | Data e hora ação | H |  |
| `CHAVE` | Chave | S |  |
| `CAMPO` | Campo | S |  |
| `CONTEUDO` | Conteúdo | S |  |
| `ALTDESCNMOVMES` | Alteração do produto já foi gerada no EFD Fiscal? | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ALTDESCNMOVMES (Tabela: TSIALT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIANX
### Descrição: Anexo Sistema

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUATTACH` | Código | I |  |
| `NOMEINSTANCIA` | Instância | S |  |
| `CHAVEARQUIVO` | Chave arquivo | S |  |
| `NOMEARQUIVO` | Arquivo | S |  |
| `DESCRICAO` | Descrição | S |  |
| `LINK` | Link | S |  |
| `CODUSU` | Usuário Inclusão | I |  |
| `DHCAD` | Criado em | H |  |
| `CODUSUALT` | Usuário Alteração | I |  |
| `DHALTER` | Modificado em | H |  |
| `TIPOAPRES` | Visível | S | Veja opções na seção OPÇÕES |
| `TIPOACESSO` | Acesso | S | Veja opções na seção OPÇÕES |
| `RESOURCEID` | ID tela | S |  |
| `PKREGISTRO` | Pk Registro | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOAPRES (Tabela: TSIANX)
| Valor | Descrição |
|-------|-----------|
| GLO | Qualquer tela |
| LOC | Nesta tela |

### Opções para campo TIPOACESSO (Tabela: TSIANX)
| Valor | Descrição |
|-------|-----------|
| ALL | Qualquer usuário |
| GRU | Meu grupo |
| USU | Privado |


## Tabela: TSIARF
### Descrição: TABLE TSIARF

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `EMAILMANUAL` | EMAILMANUAL | C |  |
| `NURFE` | NURFE | I |  |
| `SEQUENCIA` | SEQUENCIA | I |  |
| `DHINI` | DHINI | H |  |
| `DHFIM` | DHFIM | H |  |
| `AGENDAMENTO` | AGENDAMENTO | S |  |
| `PROXEXEC` | PROXEXEC | H |  |
| `EXECUNICA` | EXECUNICA | S | Veja opções na seção OPÇÕES |
| `DESCRICAO` | DESCRICAO | S |  |
| `ARQMODEMAIL` | ARQMODEMAIL | S |  |
| `CODUSURESP` | Usuário responsável | I |  |
| `CODSMTP` | CODSMTP | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo EXECUNICA (Tabela: TSIARF)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIATA
### Descrição: Anexo

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODATA` | Cód. Anexo | I |  |
| `TIPO` | Tipo do Anexo | S |  |
| `ENDARQUI` | Fim do Arquivo | S |  |
| `DESCRICAO` | Descrição do Arquivo | S |  |
| `ARQUIVO` | Arquivo anexado | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Data de Alteração | H |  |
| `TIPOCONTEUDO` | Tipo de Conteúdo | S | Veja opções na seção OPÇÕES |
| `CONTEUDO` | Conteúdo | B |  |
| `DTEXPIRA` | Data da expiração | H |  |
| `EDITA` | Edita | S |  |
| `CODEMP` | Cód. Empresa | I |  |
| `SEQUENCIA` | SEQUENCIA | I |  |
| `SEQUENCIAPR` | SEQUENCIAPR | I |  |
| `PUBLICO` | PUBLICO | S |  |
| `DTVIGOR` | Dt. Vigor | D |  |
| `IDENTIFICACAOARQUIVO` | Identificação Arquivo Físico | S |  |
| `LINK` | LINK | S |  |
| `DTINCLUSAO` | Data inclusão | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOCONTEUDO (Tabela: TSIATA)
| Valor | Descrição |
|-------|-----------|
| D | application/msword |
| I | image/jpeg |
| N | Nenhum |
| O | Outro |
| P | application/pdf |
| X | application/vnd.ms-excel |


## Tabela: TSIAVI
### Descrição: Avisos do sistema

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DTEXPIRACAO` | Dt. Expiração | D |  |
| `DTNOTIFICACAO` | Dt. Notificação | D |  |
| `ORDEM` | Ordem | I |  |
| `NUAVISO` | Aviso | I |  |
| `TITULO` | Título | S |  |
| `DESCRICAO` | Descrição | S |  |
| `SOLUCAO` | Solução | S |  |
| `IMPORTANCIA` | Importância | I |  |
| `CODUSU` | Usuário | I |  |
| `CODGRUPO` | Grupo | I |  |
| `DHCRIACAO` | Dh. Criação | H |  |
| `IDENTIFICADOR` | Identificador | S |  |
| `TIPO` | Tipo | S |  |
| `CODUSUREMETENTE` | Remetente | I |  |
| `NUAVISOPAI` | Aviso Pai | I |  |

## Tabela: TSIBAI
### Descrição: Bairros

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODBAI` | Código do Bairro | I |  |
| `NOMEBAI` | Nome | S |  |
| `CODREG` | Região | I |  |
| `DESCRICAOCORREIO` | Nome do Correio | S |  |
| `DTALTER` | Data de alteração | H |  |
| `ATUNUVERSAO` | Atualizar versão | S |  |

## Tabela: TSIBCO
### Descrição: Bancos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODBCO` | Cód. Banco | I |  |
| `ABREVIATURA` | Abreviatura | S |  |
| `NOMEBCO` | Descrição | S |  |
| `CTACMC7INI` | Pos. Inicial (Conta CMC7) | I |  |
| `CTACMC7FIM` | Pos. Final (Conta CMC7) | I |  |

## Tabela: TSIBTA
### Descrição: Botão de Ação

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDBTNACAO` | Código | I |  |
| `DESCRICAO` | Descrição | S |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `NOMEINSTANCIA` | Instância | S |  |
| `RESOURCEID` | Filtro de telas | S |  |
| `CONFIG` | Configuração | C |  |
| `CODMODULO` | Módulo Java | I |  |
| `ORDEM` | Ordem | I |  |
| `CONTROLAACESSO` | Controla Acesso | S | Veja opções na seção OPÇÕES |
| `TECLAATALHO` | Tecla de Atalho | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TSIBTA)
| Valor | Descrição |
|-------|-----------|
| LC | Lançador |
| RJ | Rotina Java |
| SC | Script (JavaScript) |
| SP | Rotina no Banco de Dados |

### Opções para campo CONTROLAACESSO (Tabela: TSIBTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIBTEF
### Descrição: BandeirasTEF

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Código | S |  |
| `BANDEIRA` | Bandeira | S |  |
| `TIPO` | Tipo | S |  |

## Tabela: TSICAN
### Descrição: Cancelamento de NFSe

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `CODCAN` | Código | S |  |
| `CODCID` | Cód. Cidade | I |  |
| `MOTIVO` | Motivo/Descrição | S |  |
| `ENVIARPREFEITURA` | Enviar a prefeitura | S | Veja opções na seção OPÇÕES |
| `TIPO` | Tipo | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TSICAN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVIARPREFEITURA (Tabela: TSICAN)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| C | Somente o código |
| D | Somente o motivo/descrição |


## Tabela: TSICEP
### Descrição: CEP

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCID` | Cód. Cidade | I |  |
| `CODBAI` | Cód.Bairro | I |  |
| `CODEND` | Cód.Endereço | I |  |
| `CEP` | CEP | S |  |
| `INTERVALO` | Intervalo de Números | S |  |

## Tabela: TSICFG
### Descrição: Configuração de recurso

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CHAVE` | CHAVE | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `CONFIG` | CONFIG | C |  |
| `TIPO` | TIPO | S | Veja opções na seção OPÇÕES |
| `CHAVEPAI` | CHAVEPAI | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TSICFG)
| Valor | Descrição |
|-------|-----------|
| Filtro | F |
| Tela | T |


## Tabela: TSICFGBK
### Descrição: Backup Configuração de recurso

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNICO` | NUNICO | I |  |
| `CONFIG` | CONFIG | C |  |
| `CODUSU` | Cód. Usuário | I |  |
| `SEQUENCIA` | SEQUENCIA | I |  |
| `CHAVE` | CHAVE | S |  |
| `TIPO` | TIPO | S |  |
| `CHAVEPAI` | CHAVEPAI | S |  |

## Tabela: TSICID
### Descrição: Cidades

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `UFNOMECID` | Cidade - UF | S |  |
| `CODCID` | Cód. Cidade | I |  |
| `NOMECID` | Nome | S |  |
| `UF` | Cód. UF | I |  |
| `DDD` | DDD | S |  |
| `CODREG` | Região | I |  |
| `DISTANCIA` | Distância | I |  |
| `SEQENTREGA` | Sequência de entrega | I |  |
| `POPULACAO` | População | I |  |
| `CODMUNFIS` | Mun. domicílio fiscal | I |  |
| `CODMUNSIAFI` | Cód. município SIAFI | I |  |
| `CODMUNDMS` | Cód. município DMS | I |  |
| `DESCRICAOCORREIO` | Nome do correio | S |  |
| `DTALTER` | Data de alteração | H |  |
| `VLRFRETEMIN` | Valor de frete mínimo | F |  |
| `VLRFRETETON` | Valor de frete por tonelada | F |  |
| `TIPOFRETE` | Tipo de frete | S | Veja opções na seção OPÇÕES |
| `METARREDVLRISS` | Método de arredondamento do valor ISS | S | Veja opções na seção OPÇÕES |
| `VLRFRETEKM` | Valor de frete por KM | F |  |
| `VLRTAXAENT` | Valor taxa de entrada | F |  |
| `TEMSUBSTITNFSE` | Tem substituição NFS-e | S | Veja opções na seção OPÇÕES |
| `LINKAGUA` | Link conta água | S |  |
| `AD_FRETE` | FRETE | F |  |
| `LINKENERGIA` | Link conta energia | S |  |
| `QTDSUB` | Quantidade de substituições permitidas | I |  |
| `QTDDIASSUB` | Prazo para substituição de NFS-e | I |  |
| `LINKIPTU` | Link conta IPTU | S |  |
| `LATITUDE` | Latitude | S |  |
| `LONGITUDE` | Longitude | S |  |
| `VENDAMIN` | Venda Mínima | F |  |
| `TIPCANCNFSE` | Tipo de cancelamento para NFS-e | S | Veja opções na seção OPÇÕES |
| `VLRLIMCANCNFSE` | Valor limite para cancelamento NFS-e | F |  |
| `MAXNOTALOTENFSE` | Qtd. máxima de notas em um lote NFS-e | I |  |
| `ACTCANEXNT` | Permite cancelamento extemporâneo? | S | Veja opções na seção OPÇÕES |
| `MOTCANCSUBNFSE` | Motivo de cancelamento para substituição de NFS-e | S |  |
| `TIMPARCPREFEITURA` | Parceiro Prefeitura | I |  |
| `TIPOCNAE` | Tipo de envio do CNAE | I | Veja opções na seção OPÇÕES |
| `NOINSCMUNPAR` | Não enviar insc. mun. quando ISS não incidir no município do parceiro | S | Veja opções na seção OPÇÕES |
| `CNAEFULLNFSE` | Usar CNAE completo | S | Veja opções na seção OPÇÕES |
| `NOFORMATLC116` | Não formatar LC116 | S | Veja opções na seção OPÇÕES |
| `GERCODNATISSJSON` | Gerar Código Natureza Operação ISS no Json | S | Veja opções na seção OPÇÕES |
| `ENVITENSSEPJSON` | Enviar itens de NFS-e separados no Json | S | Veja opções na seção OPÇÕES |
| `ENVFPJSON` | Enviar forma de pagamento no Json | S | Veja opções na seção OPÇÕES |
| `GERNUNFSEINFCPM` | Gerar o nº da NFSe nas Inf. Complementares da Substituição | S | Veja opções na seção OPÇÕES |
| `VMINRETENCAOISS` | Valor mínimo para retenção | F |  |
| `QTDMAXENVITENSJSON` | Quantidade Máxima p/ enviar itens NFS-e no Json | I |  |
| `INFQTDVLRUNIJSON` | Enviar quantidade e valor unitário no Json | S | Veja opções na seção OPÇÕES |
| `JSONSEMALIDENMUN` | Envia alíquota no Json apenas quando o ISS for devido a outro município | S | Veja opções na seção OPÇÕES |
| `ENVMULEMAILJSON` | Envia múltiplos e-mails no Json | S | Veja opções na seção OPÇÕES |
| `ENVTAGDESCONJSON` | Enviar tag descontoCondicionado no metadados do Json? | S | Veja opções na seção OPÇÕES |
| `ENVCODIGONBSJSON` | Enviar o Código NBS no JSON | S | Veja opções na seção OPÇÕES |
| `REMZEROESQUERDLC116` | Remover zero a esquerda LC116 | S | Veja opções na seção OPÇÕES |
| `MASCARANBS` | Máscara NBS | S |  |
| `NFSETEMPLATESUBST` | Utiliza processo específico para substituição? | S | Veja opções na seção OPÇÕES |
| `OBSJSONENOTAS` | Observação do Json | S | Veja opções na seção OPÇÕES |
| `PERMCANCNFSESUBSTIT` | Permite cancelamento de NFS-e substituta? | S | Veja opções na seção OPÇÕES |
| `CODPARCNFSE` | Parceiro Padrão NFSe | I |  |
| `ATUNUVERSAO` | Atualizar versão | S |  |
| `MASCARALC116` | Máscara LC116 | S |  |
| `GERCNAEMULTJSON` | Gerar CNAE para Múltiplos Itens no JSON | S | Veja opções na seção OPÇÕES |
| `REGESPTRIB` | Enviar o Regime Especial de Tributação no json? | S | Veja opções na seção OPÇÕES |
| `ENVTPSERVJSON` | Enviar Tipo de Serviço no Json? | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOFRETE (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| C | CTRC |
| N | Nota Série A |

### Opções para campo METARREDVLRISS (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| A | ABNT NBR 5891 |
| B | Truncar em duas casas decimais |
| C | Convencional |

### Opções para campo TEMSUBSTITNFSE (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPCANCNFSE (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| 1 | Via web service |
| 2 | Via web service com valor limite de cancelamento |
| 3 | Via prefeitura com número de protocolo |
| 4 | Via prefeitura sem número de protocolo |

### Opções para campo ACTCANEXNT (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOCNAE (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| null | Normal |
| 1 | 9 dígitos com zeros a direita |
| 2 | 9 dígitos com zeros a esquerda |
| 3 | 7 dígitos com zeros a direita |
| 4 | 7 dígitos com zeros a esquerda |

### Opções para campo NOINSCMUNPAR (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CNAEFULLNFSE (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NOFORMATLC116 (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERCODNATISSJSON (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVITENSSEPJSON (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVFPJSON (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERNUNFSEINFCPM (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INFQTDVLRUNIJSON (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo JSONSEMALIDENMUN (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVMULEMAILJSON (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVTAGDESCONJSON (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVCODIGONBSJSON (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REMZEROESQUERDLC116 (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NFSETEMPLATESUBST (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OBSJSONENOTAS (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| A | Observação da nota |
| B | Observação padrão da nota |
| C | Obs. da nota + Obs. padrão da nota |
| D | Observação dos itens de serviços |
| E | Observação da nota + Obs. dos itens de serviços |
| F | Obs. padrão da nota + Obs. dos itens de serviços |
| G | Obs. da nota + Obs. padrão da nota + Obs. dos itens de serv. |
| null | Padrão |

### Opções para campo PERMCANCNFSESUBSTIT (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERCNAEMULTJSON (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGESPTRIB (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVTPSERVJSON (Tabela: TSICID)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSICLA
### Descrição: Classificação de campos proteção de dados

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCLA` | Código da Classificação | I |  |
| `DESCCLA` | Descrição da Classificação | S |  |
| `CODUSUCRIAC` | Código usuário criação | I |  |
| `DTCRIAC` | Data criação | H |  |
| `CODUSUALTER` | Código usuário alteração | I |  |
| `DTALTER` | Data alteração | H |  |

## Tabela: TSICONF
### Descrição: Configurações do Usuário

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `FORM` | Form | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `CONF` | Configurações | S |  |

## Tabela: TSICTA
### Descrição: Contas Bancárias

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TIPOBOLETO` | Tipo Boleto | S | Veja opções na seção OPÇÕES |
| `LOGOURL` | Guarda logomarca | S |  |
| `PJBCRED` | Credencial | S |  |
| `PJBCONBAIXCRED` | Conciliar a baixa do titulo ao receber o crédito | S |  |
| `PJBCHAVE` | Chave | S |  |
| `BJBBAIBOLPAG` | Baixar o tílulo quando o boleto for pago | S |  |
| `CODCTABCOINT` | Código da conta bancária | I |  |
| `CODCTABCO` | Conta | S |  |
| `DESCRICAO` | Descrição | S |  |
| `CODBCO` | Banco | I |  |
| `CODAGE` | Agência bancária | S |  |
| `CODEMP` | Empresa | I |  |
| `CODCTACTB` | Conta contábil | I |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `DTIMPLANT` | Referência p/ aceitar lançamentos | D |  |
| `SALDOBCO` | Saldo do banco na referência | F |  |
| `SALDOREAL` | Saldo real na referência | F |  |
| `EXCLUSIVA` | Exclusiva da empresa | S | Veja opções na seção OPÇÕES |
| `ATIVA` | Ativa | S | Veja opções na seção OPÇÕES |
| `CLASSE` | Tipo de conta | S | Veja opções na seção OPÇÕES |
| `NUMCHEQ` | Último nro. cheque | I |  |
| `CODOPEREXCL` | Operador exclusivo | I |  |
| `CODMOEDA` | Moeda | I |  |
| `CODCORRBCO` | Correspondente bancário | I |  |
| `CARTEIRA` | Carteira | I |  |
| `CONVENIO` | Convênio | I |  |
| `INSTRUCAOI` | Instrução I | I |  |
| `INSTRUCAOII` | Instrução II | I |  |
| `DIASPROT` | Dias para protesto | I |  |
| `CODCTABCOINTREM` | Conta p/controlar a seq.de remessa | I |  |
| `SEQREM` | Sequência remessa | I |  |
| `REMFINAL` | Nro máx.p/seq.remessa | I |  |
| `SEQREM2` | Sequência remessa alternativa | I |  |
| `REMFINAL2` | Nro máx.p/seq.remessa alternativa | I |  |
| `CODTIPOPERBAIXABOLRAP` | TOP Baixa boleto | I |  |
| `REMBCO` | Último boleto | I |  |
| `CODLANCBAIXABOLRAP` | Lançamento baixa boleto | I |  |
| `REMBCOMAX` | Número máximo | I |  |
| `ZERARAUT` | Zerar automaticamente | S | Veja opções na seção OPÇÕES |
| `EMITEBOLETA` | Emite | S | Veja opções na seção OPÇÕES |
| `CTADEFEMIBOL` | Conta padrão para emissão | S | Veja opções na seção OPÇÕES |
| `IMPBOLETA` | Impressora | S |  |
| `TIPOIMPRESSORA` | Tipo impressora | S | Veja opções na seção OPÇÕES |
| `MODBOLETA` | Modelo | I |  |
| `VLRMINBOLETA` | Valor mínimo | F |  |
| `CTAMINBOLETA` | Alterar p/outra conta | I |  |
| `TAXA` | Ou cobrar taxa | F |  |
| `NURFEMODCHEQG` | Modelo de cheque | I |  |
| `DTALTER` | Data alteração | D |  |
| `CODUSU` | Cód. Usuário | I |  |
| `NUCONTRATO` | Nro. Contrato | I |  |
| `CATEGLANCHQ` | Categoria p/ lançamento de cheque | I |  |
| `MODALIDADE` | Modalidade | I |  |
| `NUMCLIENTE` | Número do cliente | I |  |
| `CAMPOLIVRE` | Campo Livre | S |  |
| `NUMBENEFICIARIO` | Número Beneficiário | S |  |
| `NOSSONUMERO` | Configuração do Nosso Número | S |  |
| `MULTIPNOSSONUM` | Multiplicadores | S |  |
| `TIPMULTIPSOMA` | Ao somar as multiplicações | S | Veja opções na seção OPÇÕES |
| `TIPMODNOSSNUM` | Tipo do Módulo | S | Veja opções na seção OPÇÕES |
| `SUBRESTMODULO` | Substitui resto: | S |  |
| `RESTOSUBST1` | Se resto igual: | I |  |
| `RESTOSUBST2` | Se resto igual: | I |  |
| `RESTOSUBST3` | Se resto igual: | I |  |
| `DIGITOSUBST1` | substitui por: | S |  |
| `DIGITOSUBST2` | substitui por: | S |  |
| `DIGITOSUBST3` | substitui por: | S |  |
| `NOSSONUMATIVO` | Usar geração de Nosso Número | S |  |
| `LINHADIGATIVO` | Usar geração da Linha Digitável | S |  |
| `IDCLIENTE` | ID do cliente | S |  |
| `CODAGEBENEF` | Agência Beneficiário | I |  |
| `CODCTABENEF` | Conta Beneficiário | I |  |
| `CODCTABAIXA` | Conta p/ baixa (Processamento de Retorno) | I |  |
| `CODCONTARURAL` | Classificação da conta Produtor Rural | S | Veja opções na seção OPÇÕES |
| `NUMCONTARURAL` | Número da conta Produtor Rural | S |  |
| `TITINFADICPIX` | Titulo Inf. Adicional Pix API | S |  |
| `MENADICPIX` | Mensagem Inf. Adicional Pix API | S |  |
| `CHAVEAPIPIX` | Chave da API Pix | S |  |
| `NURFEMODBOLETO` | Modelo de Boleto | I |  |
| `SENCLIPIX` | Client Secret Pix | S |  |
| `IDCLIPIX` | Client ID Pix | S |  |
| `CHAVEPIX` | Chave pix | S |  |
| `URLPIX` | URL pix | S |  |
| `IDAPIBANCO` | Sequência remessa alternativa | I |  |
| `QTDDIASVALPIX` | Qtd. Dias Val. Pix após Venc | I |  |
| `CONCAUTRECEBPIX` | Conciliar automaticamente os recebimentos via API | S | Veja opções na seção OPÇÕES |
| `VARIACAO` | Variação | I |  |
| `TIPOAPIBOLETO` | Selecione o serviço | S | Veja opções na seção OPÇÕES |
| `ACEITATITULOVENCIDO` | Aceita Titulo Vencido | S |  |
| `UTILIZAPIXPDV` | Utiliza PIX PDV | S | Veja opções na seção OPÇÕES |
| `RECEBIMENTODIAS` | Dias de recebimento | I |  |
| `RECEBIMENTOPARCIAL` | Recebimento parcial | S |  |
| `STATUSAPI` | Status Api | S |  |
| `INDICADORPIX` | Indicador pix | S |  |
| `DTREGCONTA` | Data de registro da conta | D |  |
| `APIBAIXAAUTOMATICA` | Selecione o tipo | S | Veja opções na seção OPÇÕES |
| `APICONCILIACAOAUTOMATICA` | Selecione o tipo | S | Veja opções na seção OPÇÕES |
| `TIPOJUROS` | Selecione o tipo | S | Veja opções na seção OPÇÕES |
| `TIPOMULTA` | Selecione o tipo | S | Veja opções na seção OPÇÕES |
| `DATAMULTA` | Selecione o tipo | S | Veja opções na seção OPÇÕES |
| `VALORJUROS` | Valor juros | F |  |
| `VALORMULTA` | Valor multa | F |  |
| `DIASMULTA` | Dias Multa | I |  |
| `DIASPARANEGATIVACAO` | Dias para Negativação | I |  |
| `ORGAONEGATIVADOR` | Orgão Negativador | I |  |
| `DIASPROTESTO` | Dias para protesto | I |  |
| `INSTRUCAOPROTESTO` | Instrução de protesto | I |  |
| `INSTRUCAONEGATIVACAO` | Instrução de negativação | I |  |
| `CONTABILIZARDIAS` | Contabilizar dia útil ou dias corridos | S |  |
| `DTENVIOAPIBANCO` | Data da integração com a API de boletos | D |  |
| `IDSEQBOL` | Id Sequencial do boleto Liquidado | I |  |
| `DATAJURO` | Data dos juros | S | Veja opções na seção OPÇÕES |
| `DIASJURO` | Dias Juros | I |  |
| `DTDESCREDCONTA` | Data de descredenciamento da conta | D |  |
| `DESCONSLCDPR` | Desconsiderar Conta na Geração do Livro Caixa Digital do Produtor Rural | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOBOLETO (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| A | AVANCADO |
| I | PIX |
| P | CNAB |
| R | RAPIDO |

### Opções para campo EXCLUSIVA (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVA (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CLASSE (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| A | Aplicação |
| C | Corrente |
| D | Adiantamento |
| E | Empréstimo |
| G | Garantida |
| M | Comissões |
| O | Outros |
| S | Sócios |
| X | Caixa-Tesouraria |
| Z | Caixa (PDV) |

### Opções para campo ZERARAUT (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EMITEBOLETA (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CTADEFEMIBOL (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOIMPRESSORA (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| 1 | ELEBRA RIMA |
| 2 | EPSON |
| 3 | RIMA ITAUTEC |
| 4 | ELGIN |
| 5 | OUTRAS |
| 6 | DESKJET |
| 7 | XEROX LAZER |

### Opções para campo TIPMULTIPSOMA (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| D | Somar dígito a dígito dos totais |
| T | Somar os totais da multiplicação |

### Opções para campo TIPMODNOSSNUM (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| D | Módulo 10 |
| O | Módulo 11 |

### Opções para campo CODCONTARURAL (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| 000 | 000 - Caixa |
| 999 | 999 - Em trânsito |

### Opções para campo CONCAUTRECEBPIX (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOAPIBOLETO (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| B | API do Banco |
| R | PJ Bank |

### Opções para campo UTILIZAPIXPDV (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APIBAIXAAUTOMATICA (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| C | Realizar na data do crédito em conta |
| N | Não realizar |
| R | Realizar na data de pagamento |

### Opções para campo APICONCILIACAOAUTOMATICA (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| C | Realizar na data do crédito em conta |
| N | Não realizar |
| R | Realizar na data de pagamento |

### Opções para campo TIPOJUROS (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| A | Percentual anual |
| D | Dispensar |
| I | Isento |
| P | Percentual diário |
| T | Taxa mensal |
| V | Valor fixo por dia de atraso |

### Opções para campo TIPOMULTA (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| D | Dispensar |
| P | Percentual |
| V | Valor fixo |

### Opções para campo DATAMULTA (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| C | Configurar quantidade de dias |
| =U | Usar data de vencimento |

### Opções para campo DATAJURO (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| C | Configurar quantidade de dias |
| U | Usar data de vencimento |

### Opções para campo DESCONSLCDPR (Tabela: TSICTA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSICUS
### Descrição: Centros de Resultado

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCENCUS` | Código | I |  |
| `DESCRCENCUS` | Descrição | S |  |
| `CALCELALURPARTEA` | CR para calculo e-LALUR (Parte A) | S | Veja opções na seção OPÇÕES |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `ANALITICO` | Analítico | S | Veja opções na seção OPÇÕES |
| `VEICULO` | Veículo Obrigatório | S | Veja opções na seção OPÇÕES |
| `CODUSURESP` | Usuário Responsável | I |  |
| `CODPARCRESP` | Parceiro Responsável | I |  |
| `AREA` | Área | F |  |
| `CODUNN` | Unidade de negócio | I |  |
| `AREAREAL` | Área Real | F |  |
| `DTINCLUSAO` | Dt. Inclusão | H |  |
| `AREACONT` | Área Contábil | F |  |
| `CODTAB` | Tabela de Preço | I |  |
| `AREAPERM` | Área Permutada | F |  |
| `FRACGEREN` | Fração Real | F |  |
| `FRACCONT` | Fração Contábil | F |  |
| `GRAU` | Grau | I |  |
| `CODUNG` | Unidade Gerencial | I |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `CODCENCUSPAI` | Cód.Centro Resultado Pai | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo CALCELALURPARTEA (Tabela: TSICUS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVO (Tabela: TSICUS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANALITICO (Tabela: TSICUS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VEICULO (Tabela: TSICUS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSICVT
### Descrição: Consultas Variáveis por tabela

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `COLCON` | Coluna para Consulta | S |  |
| `CONSULTA` | Consulta | S |  |
| `COLRET` | Coluna de retorno | S |  |
| `COLEXIBE` | Exibição no lookup | S |  |

## Tabela: TSIDRF
### Descrição: Destinatários Relatórios Formatados

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NURFE` | NURFE | I |  |
| `SEQUENCIA` | SEQUENCIA | I |  |
| `CODCON` | CODCON | I |  |

## Tabela: TSIDSB
### Descrição: Tabela de Dashboards

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUDSB` | Dashboard | I |  |
| `TITULO` | Título | S |  |
| `DESCRICAO` | Descrição | S |  |
| `LAYOUT` | Layout | C | Veja opções na seção OPÇÕES |
| `GRUPO` | Grupo | S |  |
| `CODUSUINC` | Cód. Usuário Inclusão | I |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DHALTER` | Data/Hora Modificação | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo LAYOUT (Tabela: TSIDSB)
| Valor | Descrição |
|-------|-----------|
| true | encodedtransport |


## Tabela: TSIDSG
### Descrição: Gadgets por Dashboard

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUDSB` | NUDSB | I |  |
| `NUGDG` | NUGDG | I |  |

## Tabela: TSIEJO
### Descrição: Estatisticas Job

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `ID` | Cod. Job | S |  |
| `DESCRICAO` | Descrição | S |  |
| `STATUSEXEC` | Status | S | Veja opções na seção OPÇÕES |
| `DHEXEC` | Dt. Última Execução | H |  |
| `DHPROXEXEC` | Dt. Próxima Execução | H |  |
| `TEMPOMINEXEC` | Menor Tempo de Execução | I |  |
| `TEMPOULIMAEXEC` | Tempo Última Execução | I |  |
| `MEDIAEXEC` | Tempo Médio | I |  |
| `TEMPOMAXEXEC` | Maior Tempo de Execução | I |  |
| `TEMPOEXEC` | Tempo Exec | I |  |
| `QTDEXECS` | Qtd. Execuções | I |  |
| `MSGERRO` | Mensagem de Erro | S |  |
| `QTDFALHAS` | Qtd. Falhas | I |  |
| `TIPJOB` | Tipo de Job | S | Veja opções na seção OPÇÕES |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `ERROTRACE` | Detalhe do erro | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo STATUSEXEC (Tabela: TSIEJO)
| Valor | Descrição |
|-------|-----------|
| E | Erro |
| P | Pausado |
| R | Executando |
| S | Parado |
| W | Aguardando |

### Opções para campo TIPJOB (Tabela: TSIEJO)
| Valor | Descrição |
|-------|-----------|
| I | Interno |
| U | Usuário |

### Opções para campo ATIVO (Tabela: TSIEJO)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIEMP
### Descrição: Empresas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód. Empresa | I |  |
| `COOPERATIVA` | Cooperativa | S | Veja opções na seção OPÇÕES |
| `TIPOREGRA` | Tipo p/ Certificação de Regra | S |  |
| `NOMEFANTASIA` | Nome Fantasia | S |  |
| `RAZAOSOCIAL` | Razão Social | S |  |
| `RAZAOABREV` | Razão Abreviada | S |  |
| `RAZAOSOCIALCOMPLETA` | Razão Social Completa | S |  |
| `CODEMPMATRIZ` | Empresa Matriz | I |  |
| `NUMPROPR` | Número de Proprietários | I |  |
| `USARAZAOSOCIAL` | Usar como Razão Social o campo | S | Veja opções na seção OPÇÕES |
| `PRINCTITULAR` | Principal Titular | S |  |
| `CGC` | CNPJ/CPF | S |  |
| `INSCESTAD` | Inscrição Estadual | S |  |
| `INSCMUN` | Inscrição Municipal | S |  |
| `CODCNL` | Código Nacional Localidade | S |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `EMPAGRUPARGOL` | Empresa p/ Agrupar no GOL | I |  |
| `LIMCURVA_B` | Limite Curva B | F |  |
| `LIVROSFISCAIS` | Livros Fiscais | S | Veja opções na seção OPÇÕES |
| `CODEND` | Endereço | I |  |
| `NUMEND` | Número | S |  |
| `COMPLEMENTO` | Complemento | S |  |
| `CODBAI` | Bairro | I |  |
| `CODCID` | Cód. Cidade | I |  |
| `CEP` | CEP | S |  |
| `TELEFONE` | Telefone | S |  |
| `FAX` | Fax | S |  |
| `TELEX` | Telex | S |  |
| `EMAIL` | Email | S |  |
| `HOMEPAGE` | Home Page | S |  |
| `CODMUN` | Cód. Município | I |  |
| `NATESTAB` | Natureza Estabelecimento | I |  |
| `NATJUR` | Natureza Jurídica | I |  |
| `RAMOATIV` | Ramo de Atividade | S |  |
| `ATIVECON` | Atividade Econômica | I |  |
| `CNAEPREPON` | CNAE Preponderante | I |  |
| `REGJUNTACOM` | Reg. Junta Comercial (NIRE) | S |  |
| `DTREGJUNTA` | Data Registro na Junta (NIRE) | D |  |
| `DTCONVSOC` | Data Conversão (Sociedade Simples p/ Empresária) | D |  |
| `SIMPLES` | Optante pelo SIMPLES | S | Veja opções na seção OPÇÕES |
| `SIMPLESNACNAUF` | Tem convênio Simples Nacional no Estado | S | Veja opções na seção OPÇÕES |
| `CODREGTRIB` | Cód. Regime Tribut. | I | Veja opções na seção OPÇÕES |
| `INDCOOP` | Cooperativa | I | Veja opções na seção OPÇÕES |
| `TIPOSN` | Tipo de Partilha/Anexo SN | I | Veja opções na seção OPÇÕES |
| `SERIENFDES` | Série NF DES-BH | S |  |
| `INDCONSTR` | Construtora | I | Veja opções na seção OPÇÕES |
| `INFOOBRA` | Contribuição Patronal | I | Veja opções na seção OPÇÕES |
| `MODELONFDES` | Modelo Nota Fiscal | S |  |
| `ESTOQUE` | Estoque | S | Veja opções na seção OPÇÕES |
| `ACDINTISENMULTA` | Acordo internacional Isenção | I | Veja opções na seção OPÇÕES |
| `COMISSOES` | Comissões | S | Veja opções na seção OPÇÕES |
| `CLASSTRIB` | Classificação Tributária | I | Veja opções na seção OPÇÕES |
| `INDOPCCP` | Tributação da Contribuição Previdenciária | I | Veja opções na seção OPÇÕES |
| `FINANCEIRO` | Financeiro | S | Veja opções na seção OPÇÕES |
| `INDSITESP` | Situação Especial | I | Veja opções na seção OPÇÕES |
| `CONTABILIDADE` | Contabilidade | H |  |
| `PRODUCAO` | Produção | S | Veja opções na seção OPÇÕES |
| `DHCONSITIMEND` | Última Consulta IMENDES | H |  |
| `SUPDECISAO` | Suporte a Decisão | S | Veja opções na seção OPÇÕES |
| `CARGAS` | Cargas | S | Veja opções na seção OPÇÕES |
| `CNPJPREFEITURA` | CNPJ Unidade Gestora | S |  |
| `LIMCURVA_C` | Limite Curva C | F |  |
| `FOLHAPAGTO` | Folha de Pagamento | S |  |
| `CPFRESP` | CPF do responsável | S |  |
| `DUPLIV` | Gera duplicata do Livro para a Empresa do Parceiro | S | Veja opções na seção OPÇÕES |
| `LATITUDE` | Latitude | S |  |
| `LONGITUDE` | Longitude | S |  |
| `RNTRC` | RNTRC | S |  |
| `EMPIDENOTAS` | ID NFS-e | S |  |
| `COTM` | COTM - CERTIFICADO DO OPERADOR DE TRANSPORTE MULTIMODAL | S |  |
| `NUREST` | Número do Registro Estadual | S |  |
| `NUMTAF` | Termo de Autorização de Fretamento – TAF | S |  |
| `COREMPRESA` | Cor da empresa | I |  |
| `QTDACESSOS` | Quantidade de usuários logados simultaneamente | I |  |
| `AD_DESC0A3` | % Com. p/ desconto de 0 a 2,99 | F |  |
| `AD_DESC3A590` | % Com. p/ desconto de 3 a 5,89 | F |  |
| `AD_DESC590A874` | % Com. p/ desconto de 5,90 a 8,73 | F |  |
| `AD_DESC874A1147` | % Com. p/ desconto de 8,74 a 11,46 | F |  |
| `AD_DESC1147` | % Com. p/ desconto acima de 11,47 | F |  |
| `PRODUTORRURAL` | Produtor Rural | S | Veja opções na seção OPÇÕES |
| `LOGOMARCA` | Logomarca | B |  |

## OPÇÕES DE CAMPOS

### Opções para campo COOPERATIVA (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USARAZAOSOCIAL (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| C | Razão Social Completa |
| null | Não se aplica |
| R | Razão Social |

### Opções para campo LIVROSFISCAIS (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SIMPLES (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SIMPLESNACNAUF (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODREGTRIB (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Simples Nacional |
| 2 | Simples Nacional - Sublimite |
| 3 | Regime Normal |

### Opções para campo INDCOOP (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não é cooperativa |
| 1 | Cooperativa de Trabalho |
| 2 | Cooperativa de Produção |
| 3 | Outras Cooperativas |

### Opções para campo TIPOSN (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Anexo I - Comércio |
| 2 | Anexo II - Indústria |
| 3 | Anexo III - Rec. de locação de bens/móveis e prest. de serv. não relac. no § 5o-C do art. 18 da Lei |
| 4 | Anexo IV - Rec. decorrentes da prest. de serv. relacionados no § 5o-C do art. 18 da Lei |
| 7 | Anexo V - Rec. decorrentes da prest. de serv. relacionados no § 5o-I do art. 18 da Lei |

### Opções para campo INDCONSTR (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não é construtora |
| 1 | Empresa Construtora |

### Opções para campo INFOOBRA (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | Substituída |
| 2 | Não substituída |

### Opções para campo ESTOQUE (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ACDINTISENMULTA (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| null | Não se Aplica |
| 0 | Sem acordo |
| 1 | Com acordo |

### Opções para campo COMISSOES (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CLASSTRIB (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| 1 | 01. Enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída |
| 10 | 10. Entidade sindical a que se refere a Lei 12.023/2009 |
| 11 | 11. Associação desportiva que mantém clube de futebol profissional |
| 13 | 13. Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas... |
| 14 | 14. Sindicatos em geral, exceto aquele classificado no código [10] |
| 2 | 02. Enquadrada no regime de trib. Simples Nacional com tributação previdenciária não substituída |
| 21 | 21. Pessoa Física, exceto segurado especial |
| 22 | 22. Segurado especial, inclusive quando for empregador doméstico |
| 3 | 03. Enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída |
| 4 | 04. Microempreendedor Individual - MEI |
| 6 | 06. Agroindústria |
| 60 | 60. Missão diplomática ou repartição consular de carreira estrangeira |
| 7 | 07. Produtor rural Pessoa Jurídica |
| 70 | 70. Empresa de que trata o Decreto 5.436/2005 |
| 80 | 80. Entidade beneficente de assistência social isenta de contribuições sociais |
| 85 | 85. Administração direta da União, Estados, Distrito Federal e Municípios; autarquias e fundaçõe... |
| 9 | 09. Órgão Gestor de Mão de Obra - OGMO |
| 99 | 99. Pessoas Jurídicas em geral |

### Opções para campo INDOPCCP (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Não se aplica |
| 1 | Sobre a comercialização da sua produção |
| 2 | Sobre a folha de pagamento |

### Opções para campo FINANCEIRO (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDSITESP (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| 0 | Situação Normal |
| 1 | Extinção |
| 2 | Fusão |
| 3 | Cisão |
| 4 | Incorporação |

### Opções para campo PRODUCAO (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SUPDECISAO (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CARGAS (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DUPLIV (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODUTORRURAL (Tabela: TSIEMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIEND
### Descrição: Endereços

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEND` | Cód.Endereço | I |  |
| `NOMEEND` | Nome | S |  |
| `TIPOENDERECO` | Endereço | S |  |
| `TIPO` | Tipo | S |  |
| `DESCRICAOCORREIO` | Nome do correio | S |  |
| `DTALTER` | Data de Alteração | H |  |
| `CODLOGRADOURO` | Cód. Logradouro p/ E-social | S |  |
| `ATUNUVERSAO` | Atualizar versão | S |  |

## Tabela: TSIERF
### Descrição: Entidades Recentes e Favoritas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Usuário | I |  |
| `PKREGISTRO` | Chave do registro | S |  |
| `DHULTIMOACESSO` | Último acesso | H |  |
| `FAVORITO` | Favorito | S | Veja opções na seção OPÇÕES |
| `NOMEINSTANCIA` | Nome da Instância | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo FAVORITO (Tabela: TSIERF)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIESTATSERVICO
### Descrição: Estatísticas de chamada de serviço

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Usuário | I |  |
| `HASH` | Hash | S |  |
| `QTD` | Qtd. acesso | I |  |
| `TMENOR` | Menor tempo | I |  |
| `SERVICO` | Nome serviço | S |  |
| `TEMPOTOTAL` | Qtd. acesso | I |  |
| `TMAIOR` | Maior tempo | I |  |
| `TMEDIO` | Tempo médio | I |  |
| `DTACESSO` | Dt. Acesso | D |  |
| `RESOURCEID` | ResourceID | S |  |

## Tabela: TSIFER
### Descrição: Feriado

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NACIONAL` | Tipo | S | Veja opções na seção OPÇÕES |
| `CODPAIS` | País | I |  |
| `CODUF` | Estado | I |  |
| `CODCID` | Cód. Cidade | I |  |
| `DESCRFERIADO` | Descrição | S |  |
| `DTFERIADO` | Data do feriado | D |  |
| `OBRIGATORIO` | Obrigatório | S | Veja opções na seção OPÇÕES |
| `RECORRENTE` | Recorrente | S | Veja opções na seção OPÇÕES |
| `USANOPONTO` | Usar no Ponto/Pessoal | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo NACIONAL (Tabela: TSIFER)
| Valor | Descrição |
|-------|-----------|
| E | Estadual |
| I | Internacional |
| M | Municipal |
| N | Nacional |

### Opções para campo OBRIGATORIO (Tabela: TSIFER)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RECORRENTE (Tabela: TSIFER)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USANOPONTO (Tabela: TSIFER)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIFTD
### Descrição: SI Formatador de Detalhes

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Código | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `TIPREG` | Tipo do Registro | I |  |
| `MODULO` | Módulo | S |  |
| `CAMPO` | Campo | S |  |
| `TAMANHO` | Tamanho | I |  |
| `TIPO` | Tipo | S |  |
| `QTDDEC` | Quantidade Decimal | I |  |

## Tabela: TSIFTM
### Descrição: Formatador de Master

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Código | I |  |
| `MODULO` | Módulo | S |  |
| `TITULO` | Título | S |  |
| `TAMREGISTRO` | Tamanho do Registro | I |  |
| `PROGRAMA` | Programa | S |  |
| `CODBCO` | Código do banco | I |  |
| `GRAU` | Grau | I |  |

## Tabela: TSIGDG
### Descrição: Tabela de Gadgets

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUGDG` | Código | I |  |
| `TEMHTML5` | Possui HTML5 | S | Veja opções na seção OPÇÕES |
| `TITULO` | Título | S |  |
| `DESCRICAO` | Descrição | S |  |
| `CONFIG` | Configuração (XML) | C |  |
| `THUMBNAIL` | Thumbnail | B |  |
| `CATEGORIA` | Categoria | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `CODUSUINC` | Cód. Usuário Inclusão | I |  |
| `CODUSU` | Cód. Usuário Modificação | I |  |
| `DHALTER` | Dt./Hora Modificação | H |  |
| `URLCOMPONENTE` | URL do Componente | S |  |
| `QTDANALISESUTILIZADAS` | Quantidade de Análises | I |  |
| `HTML5` | HTML5 | B |  |
| `EVOCARD` | Cartão Inteligente | S |  |
| `LAYOUT` | Layout | S |  |
| `GDGASSINADO` | Assinado? | S | Veja opções na seção OPÇÕES |
| `APVNC` | Atualiza Preço pela Nota de compra | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TEMHTML5 (Tabela: TSIGDG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVO (Tabela: TSIGDG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GDGASSINADO (Tabela: TSIGDG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APVNC (Tabela: TSIGDG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIGRE
### Descrição: Grupo de Relatórios

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODGRUPOREL` | Cód.Grupo Relatório | I |  |
| `DESCRGRUPOREL` | Descrição | S |  |
| `CODGRUPORELPAI` | Cód.Grupo Relatório Pai | I |  |
| `GRAU` | Grau | I |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `ANALITICO` | Analítico | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TSIGRE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANALITICO (Tabela: TSIGRE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIGRU
### Descrição: Grupos de usuários

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODGRUPO` | Código | I |  |
| `NOMEGRUPO` | Nome | S |  |
| `EMAIL` | Email | S |  |
| `CODUNN` | Unidade de negócio | I |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `USER_NAME` | Nome do Usuário | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TSIGRU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIHCF
### Descrição: Histórico de Cópia de Configuração

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNICO` | Núm. Único | I |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DHALTER` | Data Criação | H |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `ABASEG` | Conf. Segurança | S | Veja opções na seção OPÇÕES |
| `REMOVEANT` | Remover Conf. Atuais | S | Veja opções na seção OPÇÕES |
| `CHAVE` | Chave | S |  |
| `SELECAOTELAS` | Seleção de telas | S |  |
| `CONFTOP` | Configurações de Top | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TSIHCF)
| Valor | Descrição |
|-------|-----------|
| A | Acessos |
| C | Tela/Filtros |
| F | Filtros |
| O | Exceções/Restrições da Top |
| P | Personalizações |
| T | Tela |
| X | Personalizações/Acessos |

### Opções para campo ABASEG (Tabela: TSIHCF)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REMOVEANT (Tabela: TSIHCF)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONFTOP (Tabela: TSIHCF)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIHCU
### Descrição: Histórico de Cópia de Configuração Usu

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNICO` | NUNICO | I |  |
| `CODUSU` | Cód. Usuário | I |  |

## Tabela: TSIIMP
### Descrição: Formatador de Relatórios

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `ACESSOCUBO` | Acessos do cubo | S |  |
| `TEMLAYOUTSW` | Usa modelo IReport | S |  |
| `TIPO` | Tipo | S |  |
| `CODREL` | Cód.Relatório | I |  |
| `NOME` | Nome | S |  |
| `CODGRUPOREL` | Grupo Relatório | I |  |
| `ESCOLHIDOS` | Escolhidos | S |  |
| `ORDEM` | Ordem | S |  |
| `RESUMO` | Resumo | S |  |
| `FILTROS` | Filtros | S |  |
| `CONTASBCO` | Contas Bancárias | S |  |
| `FILTROS2` | Filtros2 | S |  |
| `PARAMSGEN` | ParamsGen | S |  |
| `LISTA1` | Lista1 | S |  |
| `LISTA2` | Lista2 | S |  |
| `LISTA3` | Lista3 | S |  |
| `LISTA4` | Lista4 | S |  |
| `ORIENTACAO` | Orientação do relatório | S |  |
| `TIPOFONTE` | Tipo da Fonte | S |  |
| `TAMFONTE` | Tamanho da fonte | I |  |
| `PERSONALIZADO` | Personalizado | S |  |
| `LAYOUT` | Layout | B |  |
| `GRAFIC` | Gráfico | B |  |
| `DTINICIAL` | Data inicial | H |  |
| `DTFINAL` | Data final | H |  |
| `CODEMP` | Cód.Empresa | I |  |
| `ORIGEM` | Origem | I |  |
| `NIVEL` | Nivel | I |  |
| `SANKHYA` | Modelo | S | Veja opções na seção OPÇÕES |
| `OBSERVACAO` | Observação | S |  |
| `LAYOUTSW` | Arquivo IReport | B |  |
| `FASTSERVICE` | Fast Service | S | Veja opções na seção OPÇÕES |
| `QTDVISUALIZACOES` | Qtd. visualizações | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo SANKHYA (Tabela: TSIIMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FASTSERVICE (Tabela: TSIIMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIIMS
### Descrição: Informação Modulos Sistema

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `MODULO` | Módulo | S |  |
| `CHAVE` | Chave | S |  |
| `VALOR` | Valor | C |  |

## Tabela: TSIIRE
### Descrição: Formatador Bancos Ítens

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `SEQUENCIA` | Sequência | I |  |
| `TIPO` | Tipo do Campo | S | Veja opções na seção OPÇÕES |
| `CAMPO` | Conteúdo | S |  |
| `TAMANHO` | Tamanho | I |  |
| `MODULO` | Módulo | S |  |
| `QTDDEC` | Quantidade Decimal | I |  |
| `POSINI` | Posição Inicial | I |  |
| `POSFIM` | Posição Final | I |  |
| `CODIGO` | Código | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TSIIRE)
| Valor | Descrição |
|-------|-----------|
| A | Decimal com zeros à esquerda |
| B | Decimal com brancos à esquerda |
| C | Inteiro com zeros à esquerda |
| D | Inteiro com brancos à esquerda |
| E | Alfanumérico |
| F | Alfanumérico com zeros à esquerda |
| G | Inicialização |
| null | Filtro |


## Tabela: TSIIRT
### Descrição: SI Detalhes do Retorno Movimento Bancário com Hierarquia

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Código | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `NOME` | Nome do Campo | S |  |
| `QTDDEC` | Decimais | I |  |
| `POSINI` | Início | I |  |
| `POSFIM` | Fim | I |  |
| `IDLINHA` | Identificador | S | Veja opções na seção OPÇÕES |
| `IDVALOR` | Conteúdo p/Identificação | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo IDLINHA (Tabela: TSIIRT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIJPR
### Descrição: Trabalho de impressão

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUJPR` | Código | I |  |
| `JOBSTATUS` | Status | S |  |
| `DESCRIPTION` | Descrição | S |  |
| `COPIES` | Cópias | I |  |
| `TIPODOC` | Tipo de documento | S |  |
| `IDDOC` | Número Documento | S |  |
| `MIMETYPE` | Tipo de arquivo | S |  |
| `ORIGINALPRINTER` | Nome da impressora | S |  |
| `DHINC` | Dt. Inclusão | H |  |
| `MSGERRO` | Mensagem de erro | S |  |
| `DHULTENV` | Dt. Último envio | H |  |
| `NUMTENTATIVAS` | Número de tentativas | I |  |
| `PRINTERURI` | Endereço da impressora | S |  |
| `PRINTSERVERURI` | Endereço do servidor de impressão | S |  |
| `FILENAME` | Arquivo | S |  |
| `CODUSU` | Usuário | I |  |
| `JOBID` | Código no Servidor de impressão | S |  |
| `IDGRUPOJOB` | Transação | S |  |

## Tabela: TSIJPS
### Descrição: Status de trabalho de impressão

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `JOBSTATUS` | Código | S |  |
| `DESCRIPTION` | Status | S |  |

## Tabela: TSILAC
### Descrição: Log de Acessos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DHACESSO` | Data e Hora | H |  |
| `USUARIO` | Usuário | S |  |
| `HOSTNAME` | Hostname | S |  |
| `SID` | Sid | I |  |
| `IP` | IP | S |  |
| `TERMINAL` | Terminal | S |  |
| `MODULO` | Módulo | S |  |
| `CODPROD` | Cód.Produto | I |  |
| `SUCESSO` | SUCESSO | S |  |

## Tabela: TSILBA
### Descrição: Liberação de acesso por PC

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUSOLIC` | Núm. Solicitação | I |  |
| `PCSOLIC` | Local Solicitação | S |  |
| `DTSOLIC` | Data Solicitação | H |  |
| `CODUSUSOLIC` | Cód. Usuário Solicitante | I |  |
| `CODUSULIBER` | Cód. Usuário Liberador | I |  |
| `DTLIBER` | Data Liberação | D |  |
| `OBSERVACAO` | Observação | S |  |
| `STATUS` | Status Solicitação | S | Veja opções na seção OPÇÕES |
| `DTVALIDADE` | Validade Liberação | D |  |
| `IPLOCAL` | IP Local | S |  |
| `IPREQUISICAO` | IP Requisição | S |  |
| `MACREQUISICAO` | MAC | S |  |
| `NOMEPCSOLIC` | Hostname Solicitação | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo STATUS (Tabela: TSILBA)
| Valor | Descrição |
|-------|-----------|
| D | Denegado |
| L | Liberado |
| P | Pendente |


## Tabela: TSILIB
### Descrição: Liberacao de Limites

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `EVENTO` | Evento | I |  |
| `VLRLIMITE` | Valor limite | F |  |
| `VLRTOTAL` | Valor Total | F |  |
| `VLRATUAL` | Valor atual | F |  |
| `CODUSULIB` | Usuário Liberador | I |  |
| `CODUSUSOLICIT` | Usuário Solicitante | I |  |
| `OBSERVACAO` | Observação solicitante | S |  |
| `NUCHAVE` | Número chave | I |  |
| `TABELA` | Tabela | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `DHLIB` | Data e hora da liberação | H |  |
| `PERCANTERIOR` | Percentual Anterior | F |  |
| `VLRANTERIOR` | Valor Anterior | F |  |
| `NULBO` | Número do limite de bonificação | I |  |
| `DHSOLICIT` | Data e hora da solicitação | H |  |
| `VLRLIBERADO` | Valor liberado | F |  |
| `OBSLIB` | Observação liberador | S |  |
| `PERCLIMITE` | Percentual limite | F |  |
| `OBSCOMPL` | Observação Complementar | S |  |
| `CODMETA` | Meta | I |  |
| `REPROVADO` | Reprovado | S | Veja opções na seção OPÇÕES |
| `SUPLEMENTO` | Suplemento | S |  |
| `ANTECIPACAO` | Antecipação | S |  |
| `TRANSF` | Transferência | S |  |
| `SEQCASCATA` | Seq. Cascata | I |  |
| `VLRDESDOB` | Valor Desdobramento | F |  |
| `CODCENCUS` | Centro Resultado | I |  |
| `CODTIPOPER` | Tipo Operação | I |  |
| `ORDEM` | Ordem | I |  |
| `NURNG` | Regra de negócio | I |  |
| `NUCLL` | Número Laudo Classificação Produto | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo REPROVADO (Tabela: TSILIB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSILIM
### Descrição: Limites

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Cód. Usuário | I |  |
| `CODGRU` | Cód.Grupo | I |  |
| `EVENTO` | Evento | I |  |
| `TIPOEVENTO` | Tipo evento | S | Veja opções na seção OPÇÕES |
| `LIMITE` | Limite | F |  |
| `TIPOLIMITE` | Tipo limite | S | Veja opções na seção OPÇÕES |
| `ENVIAREMAIL` | Enviar E-Mail | S | Veja opções na seção OPÇÕES |
| `ENVIARSMS` | Enviar SMS | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOEVENTO (Tabela: TSILIM)
| Valor | Descrição |
|-------|-----------|
| P | Percentual |
| V | Valor |

### Opções para campo TIPOLIMITE (Tabela: TSILIM)
| Valor | Descrição |
|-------|-----------|
| E | Evento |
| M | Mensal |

### Opções para campo ENVIAREMAIL (Tabela: TSILIM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENVIARSMS (Tabela: TSILIM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSILPD
### Descrição: Log de Proteção de Dados.

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `ID` | Codigo Registro | I |  |
| `TIPOLOG` | Tipo do Log | I |  |
| `CODUSU` | Usuário | I |  |
| `DESCRICAO` | Descrição do Evento | S |  |
| `DHREGISTRO` | DataHora Registro | D |  |

## Tabela: TSILRE
### Descrição: Log de Relatórios

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUREL` | Número do Relatório | I |  |
| `CLASSNAME` | Classe do Formulário | S |  |
| `DTALTER` | Data da alteração | H |  |
| `CODUSU` | Cód. Usuário | I |  |
| `TIPO` | Tipo | S |  |
| `CONSULTA` | Consulta | S |  |
| `IMPRESSORA` | Impressora | S |  |

## Tabela: TSIMASANO
### Descrição: Máscara de anonimização

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODMASANO` | Código máscara e anonimização | I |  |
| `DESCMASC` | Descrição da máscara de aninimização | S |  |
| `TIPOCAMPO` | Tipo do campo | S |  |
| `CODUSUCRIAC` | Código usuário criação | I |  |
| `DTCRIAC` | Data criação | H |  |
| `CODUSUALTER` | Código usuário alteração | I |  |
| `DTALTER` | Data alteração | H |  |

## Tabela: TSIOBC
### Descrição: Ocorrências Bancárias

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Codigo | I |  |
| `NURFE` | Número | I |  |
| `CODMODELO` | Código Modelo | I |  |
| `ENVPIXEMAIL` | Enviar E-mail PIX | S | Veja opções na seção OPÇÕES |
| `SEQUENCIA` | Sequência | I |  |
| `CODOCORRENCIA` | Cód.Ocorrência | S |  |
| `DESCRICAO` | Descrição | S |  |
| `REPORTAR` | Reportar | S | Veja opções na seção OPÇÕES |
| `INTERROMPER` | Interromper | S | Veja opções na seção OPÇÕES |
| `BAIXAR` | Baixar | S | Veja opções na seção OPÇÕES |
| `CONCILIAR` | Conciliar | S | Veja opções na seção OPÇÕES |
| `REGISTRARNOSSONUM` | Registrar Nosso Número | S | Veja opções na seção OPÇÕES |
| `REGISTRARLOG` | Registrar Log | S | Veja opções na seção OPÇÕES |
| `BAIXAPARCIAL` | Baixa Parcial | S | Veja opções na seção OPÇÕES |
| `CODEMP` | Cód.Empresa | I |  |
| `CODPARC` | Cód.Parceiro | I |  |
| `CODCENCUS` | Cód.Centro Resultado | I |  |
| `CODTIPTIT` | Tipo de título | I |  |
| `CODNAT` | Cód. Natureza | I |  |
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `INSERIR` | Inserir | S | Veja opções na seção OPÇÕES |
| `ALTERAR` | Alterar | S | Veja opções na seção OPÇÕES |
| `TRATAROCORRENCIA` | Tratar Ocorrência | S | Veja opções na seção OPÇÕES |
| `CODOCOREMESSA` | Cód.Ocorrência Remessa | S |  |
| `ATUALIZACAOREMESSA` | Atualização Ocorrência Remessa | S | Veja opções na seção OPÇÕES |
| `CODCTABCOINT` | Conta Bancária | I |  |
| `CODBCO` | Banco | I |  |
| `REMOVERMONCOB` | Remover título do monitoramento de cobrança | S | Veja opções na seção OPÇÕES |
| `CAMPOSAJUSTAR` | Campos a serem ajustados | C |  |
| `REGISTRARQRCODE` | Gravar QR Code Pix | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ENVPIXEMAIL (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REPORTAR (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTERROMPER (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BAIXAR (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONCILIAR (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGISTRARNOSSONUM (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGISTRARLOG (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BAIXAPARCIAL (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INSERIR (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALTERAR (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TRATAROCORRENCIA (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATUALIZACAOREMESSA (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| P | Processada |
| R | Rejeitada |

### Opções para campo REMOVERMONCOB (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo REGISTRARQRCODE (Tabela: TSIOBC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIOBCLOG
### Descrição: Log de ocorrências bancárias

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `NROLINHA` | Nro Linha | I |  |
| `NUFIN` | Nro Único | I |  |
| `NOSSONUM` | Nosso Nro | S |  |
| `CARTEIRA` | Carteira | I |  |
| `CODCTABCO` | Cta. Bancária | S |  |
| `CODAGE` | Agência | S |  |
| `CODBCO` | Banco | I |  |
| `CODMSGERRO` | Status da Mensagem | I | Veja opções na seção OPÇÕES |
| `DTCREDITO` | Dt. Crédito | H |  |
| `DTBAIXA` | Dt. Baixa | H |  |
| `DTVENCIMENTO` | Dt. Vencimento | H |  |
| `VLRBAIXA` | Vlr. Baixa | F |  |
| `VLRTITULO` | Vlr. Título | F |  |
| `VLRDESC` | Vlr. Desc. | F |  |
| `VLRMULTA` | Vlr. Multa | F |  |
| `VLRJURO` | Vlr. Juro | F |  |
| `VLRTXADM` | Vlr. Adm. | F |  |
| `VLRVENDOR` | Vlr. Vendor | F |  |
| `CODUSU` | Usuário | I |  |
| `DATOCORRENCIA` | Dt. Ocorrência | H |  |
| `NOMEARQ` | Nome do Arquivo | S |  |
| `ALTERADO` | Alterado | S |  |
| `INTERROMPIDO` | Interrompido | S |  |
| `CONCILIADO` | Conciliado | S |  |
| `DESCRICAO` | Desc. Ocorrência | S |  |
| `CODOCORRENCIA` | Ocorrência | S |  |
| `TRATAROCORRENCIA` | Tratar Ocorrência | S |  |
| `REGISTRADONOSSONUM` | Registra Nosso Num | S |  |
| `REPORTADO` | Reportado | S |  |
| `BAIXADO` | Baixado | S |  |
| `OBSERVACAO` | Detalhe da Mensagem | S |  |
| `NUOBCLOG` | Nro Único Proc/Prev. | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TSIOBCLOG)
| Valor | Descrição |
|-------|-----------|
| E | Prévia |
| O | Processado |

### Opções para campo CODMSGERRO (Tabela: TSIOBCLOG)
| Valor | Descrição |
|-------|-----------|
| 1 | I001 - AGRUPAMENTO NOSSO NÚMERO COMEÇA COM PG |
| 10 | E010 - LANÇAMENTO DE EXCESSÃO |
| 11 | I011 - AGRUPAMENTO DE BOLETOS |
| 12 | I012 - BAIXA CONCILIADA |
| 13 | I013 - OCORRÊNCIA CONFIGURADA PARA REGISTRAR NOSSO NÚMERO |
| 14 | E014 - TÍTULO NÃO ENCONTRADO |
| 15 | I015 - REGISTRO DE COBRANÇA REGISTRADA |
| 16 | I016 - BAIXA COM SUCESSO |
| 17 | I017 - NENHUM TÍTULO BAIXADO |
| 18 | I018 - ERRO AO GERAR FINANCEIRO COM DIFERENÇA  (Correspondente Bancário) |
| 19 | I019 - FINANCEIRO DA DIFERENÇA GERADA COM SUCESSO (Correspondente Bancário) |
| 2 | I002 - VALIDAÇÕES DO NOSSO NÚMERO |
| 20 | I020 - VALIDAR A EXISTÊNCIA TOP DA BAIXA |
| 21 | I021 - LANÇAMENTO BANCÁRIO NÃO CONFIGURADO |
| 22 | I022 - CONTA BANC. NÃO ENCONTRADA NO ARQUIVO (NUMCLIENTE/CONTADIGITO/CONVENIO) |
| 23 | I023 - CONTA BANC. NÃO ENCONTRADA NA TABELA (TSICTA) |
| 24 | I024 - TÍTULO GERADO |
| 25 | I025 - OCORRÊNCIA INVÁLIDA NO ARQUIVO |
| 26 | I026 - CAMPO INEXISTENTE |
| 27 | I027 - CAMPO COM ERRO DE CONVERSÃO |
| 28 | I028 - FALTA PARÂMETRO PARA EXECUTAR A STORED PROCEDURE |
| 29 | I029 - OS PARÂMETROS DA PROCEDURE SÃO INCOMPATÍVEIS COM AS VARIÁVEIS DISPONÍVEIS |
| 3 | I003 - FINANCEIRO NÃO ENCONTRADO |
| 30 | E030 - PROBLEMAS NA BAIXA |
| 31 | E031 - NENHUM TÍTULO BAIXADO (Correspondente Bancário) |
| 32 | E032 - ERRO AO PROCESSAR OCORRÊNCIAS |
| 33 | E033 - ERRO AO REGISTRAR O NOSSO NÚMERO |
| 34 | E034 - ERRO AO CONCILIAR TÍTULO |
| 35 | E035 - ERRO NA BAIXA |
| 36 | E036 - ERRO NA STORED PROCEDURE |
| 37 | E037 - ERRO NO CORRESPONDENTE BANCÁRIO |
| 38 | E038 - PROBLEMA NO ARQUIVO FÍSICO |
| 39 | E039 - ERRO AO REGISTRAR O QRCODE PIX |
| 4 | I004 - OCORRÊNCIA CONFIGURADA PARA INTERROMPER |
| 40 | I040 - PROCESSADO PELA PROCEDURE |
| 41 | I041 - REGISTRAR LOG |
| 42 | I042 - OCORRÊNCIA CONFIGURADA PARA GRAVAR QRCODE PIX |
| 43 | I043 - OCORRÊNCIA CONFIGURADA PARA ENVIAR EMAIL |
| 44 | E044 - PROBLEMA NO ENVIO DE EMAIL |
| 5 | I005 - OCORRÊNCIA CONFIGURADA PARA REPORTAR |
| 6 | I006 - OCORRÊNCIA CONFIGURADA PARA TRATAR OCORRÊNCIA REJEITADA |
| 7 | E007 - ENTRADA REJEITADA |
| 9 | I009 - OCORRÊNCIA NÃO CONFIGURADA - LINHA NÃO PROCESSADA |


## Tabela: TSIPAI
### Descrição: Países

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPAIS` | Código do país | I |  |
| `DESCRICAO` | Descrição | S |  |
| `ABREVIATURA` | Abreviatura | S |  |
| `CODPAISFIS` | País Domicílio Fiscal | I |  |
| `TIMNACIONALIDAD` | Nacionalidade | S |  |

## Tabela: TSIPAR
### Descrição: Parâmetros

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CHAVE` | Chave | S |  |
| `DESCRICAO` | Descrição | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `TIPO` | Tipo | S |  |
| `MODULO` | Módulo do Sistema | S |  |
| `CLASSE` | Classe | S |  |
| `ABA` | Aba | S |  |
| `LOGICO` | Lógico | S |  |
| `INTEIRO` | Inteiro | I |  |
| `NUMDEC` | Número decimal | F |  |
| `DATA` | Data | H |  |
| `TEXTO` | Texto | S |  |

## Tabela: TSIPER
### Descrição: Permissão de acesso

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODGRUPO` | Cód.Grupo | I |  |
| `PERMISSAO` | Permissão | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `TIPOACESSO` | Tipo de acesso | I |  |

## Tabela: TSIPNZ
### Descrição: TABLE TSIPNZ

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODSEQ` | CODSEQ | I |  |
| `CODUSU` | CODUSU | I |  |
| `CODSANKHYAID` | CODSANKHYAID | I |  |
| `DEVID` | DEVID | S |  |
| `DTCRIACAO` | DTCRIACAO | H |  |
| `DTALTERACAO` | DTALTERACAO | H |  |
| `TIPPERSONALIZACAO` | TIPPERSONALIZACAO | S | Veja opções na seção OPÇÕES |
| `IDPERSONALIZACAO` | IDPERSONALIZACAO | S |  |
| `NOMEPERSONALIZACAO` | NOMEPERSONALIZACAO | S |  |
| `COMPANYID` | COMPANYID | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPPERSONALIZACAO (Tabela: TSIPNZ)
| Valor | Descrição |
|-------|-----------|
| AR | Arquivo Relatório |
| CA | Campos Adicionais |
| CD | Consolidador de Dados |
| CT | Construtor de Telas |
| DB | Construtor_De_Dashboard |
| EV | Evento Programável |
| FR | Formatador de Remessa |
| GD | Construtor de Componentes de BI |
| GO | Gerenciador de Objetos |
| IT | Item Remessa |
| MG | Metas Gerenciais |
| MJ | Módulo Java |
| PC | Processamento Cartão |
| PN | Processo de Negócio |
| RC | Layout Processamento Arquivo |
| RE | Relatórios Formatados |


## Tabela: TSIPUE
### Descrição: Pefil Usuario EVO

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Cód. Usuário | I |  |
| `PERFIL` | Tipo de Perfil | S |  |
| `DTALTER` | Dt. Alteração | H |  |

## Tabela: TSIRAV
### Descrição: Respostas de Avisos de Sistema

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NURESPAVISO` | NURESPAVISO | I |  |
| `CODUSU` | CODUSU | I |  |
| `NUAVISO` | NUAVISO | I |  |

## Tabela: TSIREG
### Descrição: Regiões

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODREG` | Cód.Região | I |  |
| `NOMEREG` | Nome | S |  |
| `ATIVA` | Ativa | S | Veja opções na seção OPÇÕES |
| `ANALITICA` | Analítica | S | Veja opções na seção OPÇÕES |
| `CODTAB` | Tabela Preço | I |  |
| `CODTABMIN` | Tabela Preço Mínimo | I |  |
| `FRETEMIN` | Frete mínimo | F |  |
| `PERCCUSVAR` | % Custo Variável | F |  |
| `PERCDESCFOB` | % Desc. FOB | F |  |
| `CODVEND` | Vendedor | I |  |
| `PERCADICIONAL` | Perc. Adicional | F |  |
| `PERCPREMIO` | Perc. Prêmio | F |  |
| `GERARRECEITA` | Tipo | S | Veja opções na seção OPÇÕES |
| `VLRANTECIPACAO` | Valor | F |  |
| `GRAU` | Grau | I |  |
| `CODREGPAI` | Cód.Região Pai | I |  |
| `SEMANA1_DOM` | % Domingo | F |  |
| `SEMANA1_SEG` | % Segunda | F |  |
| `SEMANA1_TER` | % Terça | F |  |
| `SEMANA1_QUA` | % Quarta | F |  |
| `SEMANA1_QUI` | % Quinta | F |  |
| `SEMANA1_SEX` | % Sexta | F |  |
| `SEMANA1_SAB` | % Sábado | F |  |
| `SEMANA2_DOM` | % Domingo | F |  |
| `SEMANA2_SEG` | % Segunda | F |  |
| `SEMANA2_TER` | % Terça | F |  |
| `SEMANA2_QUA` | % Quarta | F |  |
| `SEMANA2_QUI` | % Quinta | F |  |
| `SEMANA2_SEX` | % Sexta | F |  |
| `SEMANA2_SAB` | % Sábado | F |  |
| `VENDAMIN` | Venda Mínima | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVA (Tabela: TSIREG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANALITICA (Tabela: TSIREG)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERARRECEITA (Tabela: TSIREG)
| Valor | Descrição |
|-------|-----------|
| N | Ajuda de Custo |
| S | Adiantamento |


## Tabela: TSIREGMOD
### Descrição: Registro de Modificações

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NOMECAT` | Nome da Instância | S |  |
| `INSTANCIA` | Instância | S |  |
| `TABELA` | Tabela | S |  |
| `DHALTER` | Data/hora | H |  |
| `CHAVE` | Chave | S |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `USERNAME` | Nome Usuário | S |  |
| `CODUSU` | Código Usuário | I |  |
| `CONTEUDO` | Conteúdo | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TSIREGMOD)
| Valor | Descrição |
|-------|-----------|
| D | Remoção |
| I | Inserção |
| U | Edição |


## Tabela: TSIREM
### Descrição: Formatador de Remessa

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Código | I |  |
| `MODULO` | Módulo | S |  |
| `TITULO` | Título | S |  |
| `TAMREGISTRO` | Tamanho do Registro | I |  |
| `CODPAI` | Cód.Formatador pai | I |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `ANALITICO` | Detalhe | S | Veja opções na seção OPÇÕES |
| `GRAU` | Grau | I |  |
| `FILTRO` | Filtro | S |  |
| `COMGROUPBY` | Com Group By | S |  |
| `COMHAVING` | Com Having | S |  |
| `NOMEARQ` | Nome do arquivo | S |  |
| `COMSELECT` | Com Select | S |  |
| `COMORDERBY` | Com Order By | S |  |
| `UTILIZASEQALT` | Utiliza Sequência Alternativa | S | Veja opções na seção OPÇÕES |
| `UTILIZASEQINFO` | Utiliza Sequência Informada | S | Veja opções na seção OPÇÕES |
| `SEQINFO` | Sequência Informada | I |  |
| `ORDENAR` | Ordenar | S | Veja opções na seção OPÇÕES |
| `FICHA` | Primeira coluna somente p/ ordenação | S | Veja opções na seção OPÇÕES |
| `ARQPORLINHA` | Gerar um arquivo p/cada linha | S | Veja opções na seção OPÇÕES |
| `ARQPORLAYOUTDETALHE` | Gerar um arquivo p/cada detalhe do layout | S | Veja opções na seção OPÇÕES |
| `INICARQREM` | Iniciais do arquivo p/ nome automático | S |  |
| `CONF` | Configuração | S |  |
| `CONSULTASQLLOTE` | Consulta SQL | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TSIREM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANALITICO (Tabela: TSIREM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZASEQALT (Tabela: TSIREM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILIZASEQINFO (Tabela: TSIREM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ORDENAR (Tabela: TSIREM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FICHA (Tabela: TSIREM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ARQPORLINHA (Tabela: TSIREM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ARQPORLAYOUTDETALHE (Tabela: TSIREM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIRET
### Descrição: Retorno Movimento Bancário com Hierarquia

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Cód.Layout | I |  |
| `TITULO` | Título do Layout | S |  |
| `SP_CHAMADA` | Stored Chamada | S |  |
| `CODPAI` | Cód.Pai | I |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `ANALITICO` | Analítico | S | Veja opções na seção OPÇÕES |
| `GRAU` | Grau | I |  |
| `USASQLNUFIN` | Usa SQL Para Número Único | S | Veja opções na seção OPÇÕES |
| `CONCEXTBANC` | Conciliação Extrato Bancário | S | Veja opções na seção OPÇÕES |
| `CONFIGTAXAADMIN` | Taxa Administrativa | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TSIRET)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANALITICO (Tabela: TSIRET)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USASQLNUFIN (Tabela: TSIRET)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONCEXTBANC (Tabela: TSIRET)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONFIGTAXAADMIN (Tabela: TSIRET)
| Valor | Descrição |
|-------|-----------|
| + | Somar ao valor recebido |
| - | Subtrair do valor recebido |
| D | Destacar |
| G | Considerar configuração global |
| N | Nada a fazer |


## Tabela: TSIRFA
### Descrição: Arquivos de Relatórios

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NURFE` | NURFE | I |  |
| `ARQUIVO` | ARQUIVO | C |  |
| `ARQUIVOBIN` | Arquivo em bytes | B |  |
| `SEQUENCIA` | SEQUENCIA | I |  |
| `NOME` | NOME | S |  |

## Tabela: TSIRFE
### Descrição: Relatórios

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CONFIG` | Configuração | C |  |
| `DESCRICAO` | Descrição | S |  |
| `CATEGORIA` | Categoria | S |  |
| `DHALTER` | Data/Hora alteração | H |  |
| `CODUSU` | Cód. Usuário | I |  |
| `NUINSTANCIA` | Instância | I |  |
| `IDTELA` | IDTELA | S |  |
| `NURFEDEPENDENTE` | Nro relatório dependente | I |  |
| `FORMATO` | Formato de arquivo | S | Veja opções na seção OPÇÕES |
| `DSNAME` | Fonte de Dados | S |  |
| `PREFIXOANEXO` | Nome do anexo para e-mail | S |  |
| `TIPO` | Tipo | S |  |
| `NURFE` | Número | I |  |
| `NOMEIMPRESSORA` | Impressora | S |  |
| `EXPFILTROINSTANCIA` | Mostrar na Tela/Instância quando | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo FORMATO (Tabela: TSIRFE)
| Valor | Descrição |
|-------|-----------|
| E | Excel (.xlsx) |
| P | PDF |
| W | Word (.docx) |
| X | Excel (.xls) |


## Tabela: TSIRHI
### Descrição: Relatórios Hierárquicos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUNI` | Cód.Único | I |  |
| `PROGRAMA` | Programa | S |  |
| `CODCAMPO` | Cód.Campo | I |  |
| `CODCAMPOPAI` | Cód.Campo Pai | I |  |
| `SOHIERARQUIA` | Só Hierarquia | S | Veja opções na seção OPÇÕES |
| `DESCRICAO` | Descrição | S |  |
| `TAMANHO` | Tamanho | I |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `ALINHAMENTO` | Alinhamento | I | Veja opções na seção OPÇÕES |
| `TOTALIZA` | Totaliza/Filtro | S | Veja opções na seção OPÇÕES |
| `MASCARA` | Máscara | S |  |
| `EXPRESSAO` | Expressão | S |  |
| `TABELAS` | Tabelas | S |  |
| `LIGACAO` | Ligação | S |  |
| `SANKHYA` | Modelo Sankhya | S | Veja opções na seção OPÇÕES |
| `ZERARNAQUEBRA` | Zerar na quebra | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo SOHIERARQUIA (Tabela: TSIRHI)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPO (Tabela: TSIRHI)
| Valor | Descrição |
|-------|-----------|
| $ | Dinheiro |
| B | Imagem |
| D | Data |
| F | Número |
| I | Inteiro |
| L | Lista |
| M | Memo |
| R | Rich Text |
| S | Letras |
| T | Data/Hora |

### Opções para campo ALINHAMENTO (Tabela: TSIRHI)
| Valor | Descrição |
|-------|-----------|
| 0 | Esquerda |
| 1 | Direita |
| 2 | Centro |

### Opções para campo TOTALIZA (Tabela: TSIRHI)
| Valor | Descrição |
|-------|-----------|
| N | Não Totaliza |
| S | Totaliza |
| X | Não filtra |

### Opções para campo SANKHYA (Tabela: TSIRHI)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ZERARNAQUEBRA (Tabela: TSIRHI)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIRLG
### Descrição: log acessos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Cód. Usuário | I |  |
| `SEQACESSO` | Sessão | I |  |
| `LOGIN` | Dh. Entrada | H |  |
| `LOGOUT` | Dh. Saída | H |  |
| `IP` | Endereço IP | S |  |
| `AGENTE` | Navegador | S |  |
| `EVENTO` | Evento | S | Veja opções na seção OPÇÕES |
| `SESSIONID` | SESSIONID | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo EVENTO (Tabela: TSIRLG)
| Valor | Descrição |
|-------|-----------|
| B | Bloqueado |
| D | Desbloqueado |
| F | Falha de login |
| L | Login |


## Tabela: TSIRMU
### Descrição: Tabela criada para quantificar o número de vezes que um registro é utilizado.

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CHAVE` | CHAVE | S |  |
| `DTINIPERIODO` | DTINIPERIODO | D |  |
| `ENTIDADE` | ENTIDADE | S |  |
| `RESOURCEID` | RESOURCEID | S |  |
| `CODUSU` | CODUSU | I |  |
| `QTD` | QTD | I |  |

## Tabela: TSIRTD
### Descrição: Detalhe de Retorno

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Cód.Layout | I |  |
| `TIPREG` | Tipo do Registro | S |  |
| `SEQUENCIA` | Sequência da Coluna | I |  |
| `NOME` | Nome Coluna | S |  |
| `TIPO` | Tipo Coluna | S |  |
| `QTDDEC` | Quantidade Decimais | I |  |
| `POSINI` | Posição inicial da variável | I |  |
| `POSFIM` | Posição final da variável | I |  |

## Tabela: TSIRTEF
### Descrição: RedesTEF

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `REDE` | Rede | S |  |
| `DESCRICAO` | Descrição | S |  |

## Tabela: TSIRTM
### Descrição: Mestre de Retorno

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODIGO` | Cód.Layout | I |  |
| `TIPREG` | Tipo de Registro | S |  |
| `TITULO` | Título do Layout | S |  |
| `TAMREG` | Tamanho Registro | I |  |
| `POSINITIPREG` | Pos Ini Tipo Registo | I |  |
| `SP_CHAMADA` | Stored Chamada | S |  |

## Tabela: TSISBP
### Descrição: Impressora substituta

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Usuário | I |  |
| `TIPODOC` | Tipo de documento | S |  |
| `ORIGINALPRINTERNAME` | Nome da impressora | S |  |
| `PRINTERURI` | Caminho da impressora | S |  |

## Tabela: TSISCI
### Descrição: TSISCI

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NOME` | Nome do Script | S |  |
| `EXECUCAO` | EXECUCAO | S |  |
| `DTEXECUCAO` | DTEXECUCAO | H |  |

## Tabela: TSISESSAOITERACAO
### Descrição: Sessão de iteração

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Usuário | I |  |
| `RESOURCEID` | ResourceID | S |  |
| `QTDITERACOES` | Qtd. acesso | I |  |
| `DHINICIO` | Dh. Início | H |  |
| `DHULTIMAATIVIDADE` | Última atividade | H |  |

## Tabela: TSISMTP
### Descrição: tabela servidor smtp

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODSMTP` | Cód. Conta | I |  |
| `SERVIDOR` | Servidor SMTP | S |  |
| `PORTA` | Porta | I |  |
| `TIPO` | Tipo de Conexão | S | Veja opções na seção OPÇÕES |
| `IGNORACERTIFICADO` | Ignorar validação do certificado do servidor ? | S | Veja opções na seção OPÇÕES |
| `REMETENTE` | Remetente | S |  |
| `USUARIO` | Usuário | S |  |
| `SENHA` | Senha | S |  |
| `UTILDOWNXML` | Utilizar para download de XML de DF-e? | S | Veja opções na seção OPÇÕES |
| `SERVIDORPOP` | Servidor | S |  |
| `PORTAPOP` | Porta | I |  |
| `PADRAO` | Conta padrão | S | Veja opções na seção OPÇÕES |
| `USEOAUTH` | Autenticar com OAuth | S | Veja opções na seção OPÇÕES |
| `REFRESHTOKENV2` | Refresh Token V2 | C |  |
| `CODATH` | Configurações OAuth | I |  |
| `REFRESHTOKEN` | Refresh Token | S |  |
| `ACCESSTOKEN` | Refresh Token | S |  |
| `ACCESSTOKENV2` | Refresh Token V2 | C |  |
| `EXPIRESIN` | Expira em | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TSISMTP)
| Valor | Descrição |
|-------|-----------|
| P | Comum |
| S | Segura com SSL |
| T | Segura com TLS |

### Opções para campo IGNORACERTIFICADO (Tabela: TSISMTP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo UTILDOWNXML (Tabela: TSISMTP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PADRAO (Tabela: TSISMTP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USEOAUTH (Tabela: TSISMTP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSITAB
### Descrição: Tabelas do Sistema

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUTABSIS` | Número único da Tabela | I |  |
| `CODTABELA` | Cód.Tabela | S |  |
| `NOMETAB` | Nome da Tabela | S |  |
| `DESCRTAB` | Descrição da Tabela | S |  |
| `CODCHAVE` | Cód.Chave | S |  |

## Tabela: TSITCM
### Descrição: Telemetria de Customizações

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `DESCRICAO` | Descrição | S |  |
| `PROCESSO` | Processo | S |  |
| `QTDCOLETA` | Qtd. Execuções | I |  |
| `TEMPOTOTAL` | Total Exec. (ms) | I |  |
| `TEMPOMEDIO` | Tempo Médio (ms) | I |  |
| `DHEXECUCAO` | Dt. Execução | D |  |
| `QTDERROS` | Qtd. Erros | I |  |
| `IDTIPO` | ID | S |  |
| `SERVERID` | Hash Info. Server | S |  |
| `IPSERVER` | IP | S |  |
| `PORTASERVER` | Porta | S |  |
| `PATHSERVER` | Caminho Absoluto | S |  |
| `ENTIDADE` | Entidade | S |  |
| `DETALHES` | Detalhes | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TSITCM)
| Valor | Descrição |
|-------|-----------|
| ACAO_AGEN | Ações Agendadas |
| BTN_BD | Botão de Ação de Banco de Dados |
| BTN_JAVA | Botão de Ação Java |
| BTN_JAVASCRIPT | Botão de Ação Javascript |
| CAMP_CALC | Campos Calculados SQL |
| CONECT_PREP | Preparação da conexão |
| EVT_BD | Evento de Banco de Dados |
| EVT_JAVA | Evento Java |
| FORMULA | Fórmulas |
| GADGET | Gadget |
| KEY_GEN | KEY-GEN |
| LONG_TRANSAC | Transações Longas |
| MOD_BOLETO | Modelo de Boleto |
| MOD_IMP | DANFE Personalizado ou Modelo de Impressão |
| REGRA_NEG | Regras de Negócio |
| REPORT | Relatórios |
| REQ_HTTP | Requisições HTTP |


## Tabela: TSITEND
### Descrição: Tipo de Endereço

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TIPO` | Tipo | S |  |
| `DESCRICAO` | Descrição | S |  |

## Tabela: TSITMF
### Descrição: TopsMaisFiltradas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODTIPOPER` | CODTIPOPER | I |  |
| `CODUSU` | CODUSU | I |  |
| `QTDFILT` | QTDFILT | I |  |

## Tabela: TSITPA
### Descrição: Tipo de arquivo

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DOCTASTE` | Código | S |  |
| `DESCRIPTION` | Tipo de arquivo | S |  |

## Tabela: TSITPD
### Descrição: Tipo de documento

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `DOCTYPE` | Código | S |  |
| `DESCRIPTION` | Tipo de documento | S |  |

## Tabela: TSIUFS
### Descrição: Unidade Federativa

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUF` | Cód. Unidade Federativa | I |  |
| `UF` | Sigla | S |  |
| `DESCRICAO` | Descrição | S |  |
| `CODPAIS` | País | I |  |
| `CODPARCSECRECEST` | Cód. Parceiro Secretaria da Receita Estadual | I |  |
| `CODIBGE` | Código IBGE | I |  |
| `CODSTGNRE` | Código da Receita (GNRE) | S |  |
| `CODRECDIME` | Código da Receita (DIME) | I |  |
| `CODCLSVENCDIME` | Código Classe Vencimento (DIME) | I |  |
| `CODDETGNRE` | Código Detalhamento Receita (GNRE) | I |  |
| `CODPRODGNRE` | Código do Produto (GNRE) | I |  |
| `PROTOCOLOCONVENIO` | Protocolo/Convênio (GNRE) | S |  |
| `VLRPERSGNRE` | Valor personalizado GNRE | S |  |
| `CODCAMPOEXTRAGNRE` | Código (Campos Extras GNRE) | I |  |
| `CODCAMPOEXTRAGNRE2` | Código (Campos Extras GNRE 2) | I |  |
| `ESTORNONFE` | Permite Estorno de NF-e | S | Veja opções na seção OPÇÕES |
| `GERINFCAMPADICGNRE` | Gera Informação dos Campos Adicionais na GNRE | S | Veja opções na seção OPÇÕES |
| `VALORCAMPOEXTRA` | Valor para Campo Extra GNRE | S | Veja opções na seção OPÇÕES |
| `VERSAOGNRE` | Versão GNRE | S | Veja opções na seção OPÇÕES |
| `TIPODOC` | Tipo de documento | I |  |
| `CODFCPSTGNRE` | Código da Receita (GNRE) p/ FCP ST | I |  |
| `CODRECDIMEFCPST` | Código da Receita (DIME) para FCP ST | I |  |
| `CODCLSVENCDIMEFCPST` | Código Classe Vencimento (DIME) p/ FCP ST | I |  |
| `TIPOINFO` | Tipo da Informação | S | Veja opções na seção OPÇÕES |
| `TIPTITGNREFCPST` | Tipo de Título p/ indicar GNRE p/ FCP S.T. | I |  |
| `USAWEBSERVICEGNRE` | Utiliza webservice para GNRE | S | Veja opções na seção OPÇÕES |
| `AD_SUPERVISOR` | Supervisor | I |  |
| `TABPRECPMC` | Tabela de Preço PMC | I |  |
| `TABPRECOPF` | Tabela de Preço PF | I |  |
| `DHALTREG` | Dt. Alteração | H |  |
| `CODUSUALTREG` | Cód. Usuário Alteração | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo ESTORNONFE (Tabela: TSIUFS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERINFCAMPADICGNRE (Tabela: TSIUFS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALORCAMPOEXTRA (Tabela: TSIUFS)
| Valor | Descrição |
|-------|-----------|
| C | Chave NF-e/CT-e |
| null | Chave NF-e/CT-e e Observação |
| O | Observação |

### Opções para campo VERSAOGNRE (Tabela: TSIUFS)
| Valor | Descrição |
|-------|-----------|
| 100 | 1.0 |
| 200 | 2.0 |

### Opções para campo TIPOINFO (Tabela: TSIUFS)
| Valor | Descrição |
|-------|-----------|
| C | Chave do documento |
| N | Nota Fiscal (Número da nota) |

### Opções para campo USAWEBSERVICEGNRE (Tabela: TSIUFS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TSIUSU
### Descrição: Usuários

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODUSU` | Cód. Usuário | I |  |
| `CODEQUIP` | Equipamento Fiscal | I |  |
| `TIMBAIXTITRECABE` | Baixar tít. reg. lote c/tít. entrada/comissão em aberto | S | Veja opções na seção OPÇÕES |
| `GRUPOREDE` | Grupo de Rede | S |  |
| `IGNORALDAP` | Ignorar login via LDAP | S | Veja opções na seção OPÇÕES |
| `USUREDE` | Usuário de Rede | S |  |
| `INSTALAPACOTESS` | Permite instalar pacote Sankhya Store? | S | Veja opções na seção OPÇÕES |
| `NOMEUSU` | Nome | S |  |
| `ACCOUNTEMAIL` | Sankhya ID | S |  |
| `ACESSOPDVCANCITENS` | Cancelamento de itens | S | Veja opções na seção OPÇÕES |
| `DTLIMACESSO` | Data limite de acesso | D |  |
| `ACESSOPDVSANG` | Sangria | S | Veja opções na seção OPÇÕES |
| `INTERNO` | Senha | S |  |
| `ACESSOPDVSUPR` | Suprimento | S | Veja opções na seção OPÇÕES |
| `ACESSOPDVSANGPDESP` | Sangria para despesas | S | Veja opções na seção OPÇÕES |
| `CODGRUPO` | Grupo | I |  |
| `DESCTOTALNOTAPDV` | Desconto no Total | S | Veja opções na seção OPÇÕES |
| `EMAIL` | Email | S |  |
| `CODEMP` | Empresa | I |  |
| `CODFUNC` | Funcionário | I |  |
| `CODCENCUSPAD` | Cód.Centro Resultado Padrão | I |  |
| `CODPARC` | Cód. Parceiro | I |  |
| `NOMEFILA` | Nome Fila p/ num. boleto | S |  |
| `NUVERSAO` | NUVERSAO | I |  |
| `TOPBAIXARECEITA` | Tipo Operação Baixa Receita | I |  |
| `TOPBAIXADESPESA` | Tipo Operação Baixa Despesa | I |  |
| `RENDIASVALJUR` | Dias tol. juros reneg | I |  |
| `TIPENVNOTSOL` | Notificar solicitante de liberações | S | Veja opções na seção OPÇÕES |
| `EMAILSOLLIB` | Email p/ solicitação liberação | S |  |
| `ATUNUVERSAO` | ATUNUVERSAO | S |  |
| `NOMEUSUCPLT` | Nome Completo | S |  |
| `DTNASC` | Data Nascimento | D |  |
| `CPF` | CPF | S |  |
| `RG` | RG | S |  |
| `CODVEND` | Vendedor | I |  |
| `CAIXA` | Caixa | S | Veja opções na seção OPÇÕES |
| `TEMECF` | Tem ECF | S | Veja opções na seção OPÇÕES |
| `BAIXAREC` | Baixa Receita | S | Veja opções na seção OPÇÕES |
| `SENHANOVA` | Senha Nova | S |  |
| `SENHASMTP` | Senha SMTP | S |  |
| `SENHAREPETE` | Senha Repetir | S |  |
| `USUARIOSMTP` | Usuário SMTP | S |  |
| `SERVIDORSMTP` | Servidor de SMTP | S |  |
| `VLRMAXAUT` | Valor Máximo de autorização | F |  |
| `SENHAANTIGA` | Senha Antiga | S |  |
| `CONTACESSO` | Controle | S |  |
| `DTULTIMASENHA` | Data da Última senha | H |  |
| `DTALTER` | Data de Alteração | H |  |
| `NIVEL` | Nível | I |  |
| `BAIXADESP` | Baixa Despesa | S | Veja opções na seção OPÇÕES |
| `ALTCTAFAT` | Altera conta bancária no faturamento? | S | Veja opções na seção OPÇÕES |
| `ALTCTAIMPBOL` | Altera conta bancária na impressão de boleto? | S | Veja opções na seção OPÇÕES |
| `ABREGAVETA` | Abre Gaveta | S | Veja opções na seção OPÇÕES |
| `IMP2SANSUPCAI` | Imprime segunda via sangria suprimento e fechamento de caixa | S | Veja opções na seção OPÇÕES |
| `TIPOSMTP` | Tipo de SMTP | S | Veja opções na seção OPÇÕES |
| `CODCTABCOINT` | Conta | I |  |
| `SENHANUNCAEXPIRA` | Senha expira | S |  |
| `CODCTABCOINT2` | Conta 2 | I |  |
| `VERCABPROPRIA` | Ver as Próprias Notas | S | Veja opções na seção OPÇÕES |
| `PORTASMTP` | Porta SMTP | I |  |
| `APROVCOT` | Aprovar cotação | S | Veja opções na seção OPÇÕES |
| `SEGURANCASMTP` | Conexão segura? | S | Veja opções na seção OPÇÕES |
| `ALTORDCFECH` | Altera Ordem de Carga fechada? | S | Veja opções na seção OPÇÕES |
| `CODETAPA` | Etapa | I |  |
| `EXIBIRVALANALRENT` | Exibir valores na Análise de Rentabilidade? | S | Veja opções na seção OPÇÕES |
| `DTULTACESSO` | Data Último Acesso | H |  |
| `CONTAGOL` | Controle GOL | S |  |
| `NOTSLAFILA` | Notifica Fila SLA | S | Veja opções na seção OPÇÕES |
| `ACESSOVISUALCAB` | Ver Pedidos/Notas (WEB) | S | Veja opções na seção OPÇÕES |
| `IMPNFCENTRAL` | Imprimir/Reimprimir Nota nas Centrais | S | Veja opções na seção OPÇÕES |
| `MINUTOSFIN` | Finaliza se Inativo em (minutos) | I |  |
| `RESTRINGECART` | Restringir carteira? | S | Veja opções na seção OPÇÕES |
| `CODPARCPERFIL` | Cód. Parceiro Perfil | I |  |
| `CODCONTATOPERFIL` | Contato Perfil | I |  |
| `EXCLIBORC` | Pode excluir liberações/negações de orçamento | S | Veja opções na seção OPÇÕES |
| `LOCALE` | Idioma | S | Veja opções na seção OPÇÕES |
| `FOTO` | Foto | B |  |
| `PERMEXPREL` | Permite exportar relatórios ? | S | Veja opções na seção OPÇÕES |
| `CODCARGAACESSO` | Carga horária para acesso | I |  |
| `TOLERANCIAACESSO` | Tolerância acesso fora horário | I |  |
| `VISACESOUTUSU` | Visualiza acesso de outros Usuários | S | Veja opções na seção OPÇÕES |
| `APENASCOMPLIB` | Acessar apenas por computadores liberados? | S | Veja opções na seção OPÇÕES |
| `INFRECSEN` | Informação de Recuperação de Senha | S |  |
| `ACESSAFORMULAREL` | Acessa fórmulas relacionadas | S | Veja opções na seção OPÇÕES |
| `INTEGRAECONECT` | Integrar com EConect | S | Veja opções na seção OPÇÕES |
| `NIVELACESSO` | Nível de Acesso | S | Veja opções na seção OPÇÕES |
| `AVISAVARPRECO` | Acompanha alteração de custo(WMS) | S | Veja opções na seção OPÇÕES |
| `PERMALTMOEDA` | Permite alterar valor de moeda na baixa? | S | Veja opções na seção OPÇÕES |
| `PERMIMPRIMEREL` | Permite imprimir relatórios? | S | Veja opções na seção OPÇÕES |
| `IGNORAHORASCRUZ` | Ignora Horas Cruzadas | S | Veja opções na seção OPÇÕES |
| `SELECTWCAPO` | Seleciona Centro de Trabalho em Apontamento de Produção | S | Veja opções na seção OPÇÕES |
| `CORCODIGO` | Corretor | I |  |
| `TIMVERTODASFACS` | Visualizar todas as FACs? | S | Veja opções na seção OPÇÕES |
| `SENHAECONECT` | Senha | I |  |
| `CODPERFIL` | Cód. Perfil | I |  |
| `CODIDECONECT` | Cód. Ident. | S |  |
| `IDPERFILECONECT` | Cód. Perfil | S |  |
| `PERMREPERRO` | Permite reportar erros ? | S | Veja opções na seção OPÇÕES |
| `TIMPATHSCANNER` | Path Scanner | S |  |
| `PROPRIETARIO` | Proprietário | S | Veja opções na seção OPÇÕES |
| `ACCOUNTID` | Account ID | S |  |
| `IMPLANTADOR` | Implantador | S | Veja opções na seção OPÇÕES |
| `GESTOR` | Gestor | S | Veja opções na seção OPÇÕES |
| `TIMBAIXAWORD` | Permitir Baixar Word | S | Veja opções na seção OPÇÕES |
| `OPERACIONAL` | Operacional | S | Veja opções na seção OPÇÕES |
| `ACCOUNTTOKEN` | Account TOKEN | C |  |
| `ACCOUNTDHEXPIRA` | Data de expiração do Account TOKEN | H |  |
| `ACCOUNTNOMEFOTO` | Nome da foto do Account | S |  |
| `TOKENCHECKOUT` | Token de Identificação do Checkout | S |  |
| `ACCOUNTPARTNER` | Cód. Parceiro | I |  |
| `TIPOUSU` | Tipo do Usuário | I | Veja opções na seção OPÇÕES |
| `AD_EDITORC` | Edita Orçamento | I | Veja opções na seção OPÇÕES |
| `AD_SENAPEX` | Senha Apex | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIMBAIXTITRECABE (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IGNORALDAP (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INSTALAPACOTESS (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ACESSOPDVCANCITENS (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ACESSOPDVSANG (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ACESSOPDVSUPR (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ACESSOPDVSANGPDESP (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DESCTOTALNOTAPDV (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPENVNOTSOL (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| E | Por e-mail |
| S | Por Notificação no SankhyaOm |

### Opções para campo CAIXA (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TEMECF (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BAIXAREC (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BAIXADESP (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALTCTAFAT (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ALTCTAIMPBOL (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ABREGAVETA (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMP2SANSUPCAI (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOSMTP (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| C | Autorização Digest MD5 |
| L | Meu Servidor Requer Autorização |
| N | Não Requer Autorização |
| P | Autorização Simples |

### Opções para campo VERCABPROPRIA (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APROVCOT (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| M | Melhor Resultado |
| N | Não aprova |
| Q | Qualquer Resultado |

### Opções para campo SEGURANCASMTP (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| D | TLS, se disponível |
| N | Não |
| S | SSL |
| T | TLS |

### Opções para campo ALTORDCFECH (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIBIRVALANALRENT (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NOTSLAFILA (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| R | Responsável |
| T | Todos |

### Opções para campo ACESSOVISUALCAB (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| C | Do mesmo C.R. do vendedor |
| S | Desse vendedor e subordinados |
| T | De todos |
| V | Desse vendedor |

### Opções para campo IMPNFCENTRAL (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RESTRINGECART (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXCLIBORC (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo LOCALE (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| en_US | Inglês (Estados Unidos) |
| es_ES | Espanhol |
| fr_FR | Francês |
| pt_BR | Português (Brasil) |

### Opções para campo PERMEXPREL (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VISACESOUTUSU (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APENASCOMPLIB (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ACESSAFORMULAREL (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INTEGRAECONECT (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo NIVELACESSO (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| D | Diretor Comercial |
| G | Diretor |

### Opções para campo AVISAVARPRECO (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMALTMOEDA (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMIMPRIMEREL (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IGNORAHORASCRUZ (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SELECTWCAPO (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMVERTODASFACS (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMREPERRO (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROPRIETARIO (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo IMPLANTADOR (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GESTOR (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIMBAIXAWORD (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo OPERACIONAL (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOUSU (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| 0 | Interface |
| 1 | Integração |

### Opções para campo AD_EDITORC (Tabela: TSIUSU)
| Valor | Descrição |
|-------|-----------|
| 0 | Não |
| 1 | Sim |


## Tabela: TCBBFC
### Descrição: Bloqueio Fechamento Contábil

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUBLOQUEIO` | Nro. Config. Bloqueio | I |  |
| `CODEMP` | Código Empresa | I |  |
| `SEQUENCIA` | Sequência Bloqueio | I |  |
| `TIPOFECHAESTENT` | Tipo de Fechamento Estoque - Entrada | S | Veja opções na seção OPÇÕES |
| `DTFECHAMENTOENT` | Dt Fechamento Estoque - Entrada | D |  |
| `TIPOFECHAESTSAI` | Tipo de Fechamento Estoque - Saída | S | Veja opções na seção OPÇÕES |
| `DTFECHAMENTOSAI` | Dt Fechamento Estoque Saída | D |  |
| `TIPOFECHACALCUST` | Tipo de Fechamento Calculo Custo | S | Veja opções na seção OPÇÕES |
| `DTFECHAMENTOCUS` | Dt Fechamento Calculo Custo | D |  |
| `TIPOFECHAFINREC` | Tipo de Fechamento Financeiro - Receita | S | Veja opções na seção OPÇÕES |
| `DTFECHAMENTOREC` | Dt Fechamento Financeiro - Receita | D |  |
| `TIPOFECHAFINDESP` | Tipo de Fechamento Financeiro - Despesa | S | Veja opções na seção OPÇÕES |
| `DTFECHAMENTODESP` | Dt Fechamento Financeiro - Despesa | D |  |
| `TIPOFECHAMOVBCO` | Tipo de Fechamento Movimento Bancário | S | Veja opções na seção OPÇÕES |
| `DTFECHAMENTOBCO` | Dt Fechamento Movimento Bancário | D |  |
| `TIPOFECHAMOVCTB` | Tipo de Fechamento Contábil | S | Veja opções na seção OPÇÕES |
| `DTFECHAMENTOCTB` | Dt Fechamento Contábil | D |  |
| `TIPOFECHAMOVFIS` | Tipo de Fechamento Fiscal | S | Veja opções na seção OPÇÕES |
| `DTFECHAMENTOFIS` | Dt Fechamento Fiscal | D |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DHINCLUSAO` | Dh. Inclusão | H |  |
| `REFERENCIA` | Referência | D |  |
| `REFFIXA` | Referência fixa | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOFECHAESTENT (Tabela: TCBBFC)
| Valor | Descrição |
|-------|-----------|
| D | 48 Horas |
| null | Data |
| Q | Quinzenal |

### Opções para campo TIPOFECHAESTSAI (Tabela: TCBBFC)
| Valor | Descrição |
|-------|-----------|
| D | 48 Horas |
| null | Data |
| Q | Quinzenal |

### Opções para campo TIPOFECHACALCUST (Tabela: TCBBFC)
| Valor | Descrição |
|-------|-----------|
| D | 48 Horas |
| null | Data |
| Q | Quinzenal |

### Opções para campo TIPOFECHAFINREC (Tabela: TCBBFC)
| Valor | Descrição |
|-------|-----------|
| D | 48 Horas |
| null | Data |
| Q | Quinzenal |

### Opções para campo TIPOFECHAFINDESP (Tabela: TCBBFC)
| Valor | Descrição |
|-------|-----------|
| D | 48 Horas |
| null | Data |
| Q | Quinzenal |

### Opções para campo TIPOFECHAMOVBCO (Tabela: TCBBFC)
| Valor | Descrição |
|-------|-----------|
| D | 48 Horas |
| null | Data |
| Q | Quinzenal |

### Opções para campo TIPOFECHAMOVCTB (Tabela: TCBBFC)
| Valor | Descrição |
|-------|-----------|
| D | 48 Horas |
| null | Data |
| Q | Quinzenal |

### Opções para campo TIPOFECHAMOVFIS (Tabela: TCBBFC)
| Valor | Descrição |
|-------|-----------|
| D | 48 Horas |
| null | Data |
| Q | Quinzenal |

### Opções para campo REFFIXA (Tabela: TCBBFC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TCBCTR
### Descrição: Conta Contábil Referencial

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCTACTB` | Conta reduzida | I |  |
| `TIPO` | Tipo | I | Veja opções na seção OPÇÕES |
| `CODCTAREF` | Cód. Conta Ref. | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TCBCTR)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - PJ em Geral |
| 10 | 10 - Financeiras - Lucro Presumido |
| 2 | 2 - PJ em Geral - Lucro Presumido |
| 3 | 3 - Financeiras |
| 4 | 4 - Seguradoras ou Entidades Abertas de Previdência Complementar |
| 5 | 5 - Imunes e Isentas em Geral |
| 6 | 6 - Imunes e Isentas - Financeiras |
| 7 | 7 - Imunes e Isentas - Seguradoras |
| 8 | 8 - Entidades Fechadas de Previdência Complementar |
| 9 | 9 - Partidos Políticos |


## Tabela: TCBDIN
### Descrição: Tabelas Dinâmicas Importadas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TABELA` | Tabela | S |  |
| `CODIGO` | Código | S |  |
| `TIPOLANC` | Tipo de Lançamento | S |  |
| `DESCRICAO` | Descrição | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Dt. Alteração | H |  |

## Tabela: TCBDPLR
### Descrição: Tabelas Dinâmicas do Plano de Conta Referencial

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TABELA` | Tabela | S |  |
| `TIPO` | Tipo | I |  |
| `ANO` | Ano | I |  |
| `VERSAO` | Versão | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Dt. Alteração | H |  |

## Tabela: TCBECB
### Descrição: Definição dos blocos a serem gerados EBC

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód.Emp | I |  |
| `BLOCO` | Bloco | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `DESCRICAO` | Descrição | S |  |
| `GERARBLOCO` | Gerar Bloco | S | Veja opções na seção OPÇÕES |
| `CODUSU` | CODUSU | I |  |
| `DTALTER` | DTALTER | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo GERARBLOCO (Tabela: TCBECB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TCBECR
### Descrição: Definição Registro Bloco ECB

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód.Emp | I |  |
| `BLOCO` | Bloco | S |  |
| `REGISTRO` | Registro | S |  |
| `DESCRICAO` | Descrição | S |  |
| `FORMAESCRIT_G` | G | S | Veja opções na seção OPÇÕES |
| `FORMAESCRIT_R` | R | S | Veja opções na seção OPÇÕES |
| `FORMAESCRIT_A` | A | S | Veja opções na seção OPÇÕES |
| `FORMAESCRIT_B` | B | S | Veja opções na seção OPÇÕES |
| `FORMAESCRIT_Z` | Z | S | Veja opções na seção OPÇÕES |
| `CODUSU` | CODUSU | I |  |
| `DTALTER` | DTALTER | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo FORMAESCRIT_G (Tabela: TCBECR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FORMAESCRIT_R (Tabela: TCBECR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FORMAESCRIT_A (Tabela: TCBECR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FORMAESCRIT_B (Tabela: TCBECR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo FORMAESCRIT_Z (Tabela: TCBECR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TCBEFB
### Descrição: Definição dos blocos a serem gerados EFB

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód. Empresa | I |  |
| `BLOCO` | Bloco | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `DESCRICAO` | Descrição | S |  |
| `GERARBLOCO` | Gerar Bloco | S | Veja opções na seção OPÇÕES |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Dt. Alteração | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo GERARBLOCO (Tabela: TCBEFB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TCBEFR
### Descrição: Definição Registro Bloco EFB

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód. Empresa | I |  |
| `BLOCO` | Bloco | S |  |
| `REGISTRO` | Registro | S |  |
| `DESCRICAO` | Descrição | S |  |
| `GERARREGISTRO` | Gerar Registro | S | Veja opções na seção OPÇÕES |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Dt. Alteração | H |  |

## OPÇÕES DE CAMPOS

### Opções para campo GERARREGISTRO (Tabela: TCBEFR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TCBERR
### Descrição: TABLE TCBERR

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUAGENDCTZ` | Número Único Agend. | I |  |
| `NUSEQERR` | Sequência Erro | I |  |
| `TIPO` | Tipo Agendamento | S |  |
| `DHCTZ` | Data da Contabilização | H |  |
| `ORIGEM` | Origem Mov. | S |  |
| `NUNICO` | Número Único Mov. | I |  |
| `TIPLANC` | Tipo Lançamento | S |  |
| `CODTIPOPER` | Cód.Tipo Operação Ctbz | I |  |
| `SEQCTB` | Sequência Ctbz | I |  |
| `DESCRICAO` | Descrição do Erro | S |  |
| `CONTABILIZADO` | Contabilizado | S |  |

## Tabela: TCBHCT
### Descrição: TABLE TCBHCT

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUAGENDCTZ` | Número Único Agend. | I |  |
| `TIPO` | Tipo do Agendamento | S |  |
| `DHCTZ` | Data da Contabilização | H |  |
| `QTDLANCTOT` | Qtde de Lançamentos | I |  |
| `QTDLANCCTZ` | Qtde Contabilizados | I |  |
| `QTDLANCNCTZ` | Qtde  Não Contabilizados | I |  |
| `MINUTOSCTZ` | Tempo Gasto | I |  |
| `TIPOEXEC` | Tipo de Execução | S | Veja opções na seção OPÇÕES |
| `ERROEXEC` | Mensagem | C |  |
| `LIBERADA` | Status | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOEXEC (Tabela: TCBHCT)
| Valor | Descrição |
|-------|-----------|
| A | Automático |
| M | Manual |

### Opções para campo LIBERADA (Tabela: TCBHCT)
| Valor | Descrição |
|-------|-----------|
| L | Liberado Com Int. |
| null | Liberado |
| P | Pendente |
| S | Liberado Sem Int. |


## Tabela: TCBHIS
### Descrição: Histórico

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODHISTCTB` | Código | I |  |
| `HISTORICO` | Descrição | S |  |

## Tabela: TCBHLT
### Descrição: Histórico de lotes

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUAGENDCTZ` | Número Único Agend. | I |  |
| `TIPO` | Tipo | S |  |
| `DHCTZ` | Data da Contabilização | H |  |
| `NUMLOTE` | Número do Lote | I |  |
| `REFERENCIA` | Referência | H |  |
| `CODEMP` | Empresa | I |  |

## Tabela: TCBINT
### Descrição: Integração da Contabilidade com o Financeiro

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód.Empresa | I |  |
| `REFERENCIA` | Referência | H |  |
| `NUMLANC` | Número do lançamento | I |  |
| `TIPLANC` | Tipo de lançamento | S |  |
| `ORIGEM` | Origem | S | Veja opções na seção OPÇÕES |
| `NUNICO` | Número único | I |  |
| `NUMLOTE` | Número do lote | I |  |
| `VLRLANC` | Valor do Lançamento | F |  |
| `SEQNOTA` | SEQNOTA | I |  |
| `SEQUENCIA` | SEQUENCIA | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo ORIGEM (Tabela: TCBINT)
| Valor | Descrição |
|-------|-----------|
| B | Baixa |
| E | Estoque |
| F | Financeiro |
| M | Banco |
| R | Renegociado |


## Tabela: TCBITELP
### Descrição: Itens para Apuração do LP

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODNATLP` | Código Natureza | I |  |
| `DESCRICAO` | Descrição | S |  |
| `CODIGO` | Código | S |  |
| `TABELA` | Tabela | S |  |
| `ALIQUOTA` | Alíquota | F |  |
| `TIPIMP` | Tipo Imposto | S | Veja opções na seção OPÇÕES |
| `DTINI` | Data Início | D |  |
| `DTFIM` | Data Fim | D |  |
| `GRUPO` | Grupo | S | Veja opções na seção OPÇÕES |
| `DTALTER` | Data de alteração | D |  |
| `DTATT` | Data da Atualização da Tabela | D |  |
| `ITEMDESC` | Descrição | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPIMP (Tabela: TCBITELP)
| Valor | Descrição |
|-------|-----------|
| C | CSLL |
| I | IRPJ |

### Opções para campo GRUPO (Tabela: TCBITELP)
| Valor | Descrição |
|-------|-----------|
| 1 | Discriminação da Receita Bruta |
| 2 | Receitas com Tributação Integral |
| 3 | Cálculo para IRPJ/CSLL |
| 4 | Deduções |


## Tabela: TCBLAN
### Descrição: Lançamentos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCTACTB` | Conta Contábil (Red.) | I |  |
| `NUMDOC` | Núm. Documento | I |  |
| `VENCIMENTO` | Vencimento | D |  |
| `VLRLANC` | Valor Lançamento | F |  |
| `TIPLANC` | Tip. Lançamento | S | Veja opções na seção OPÇÕES |
| `LIBERADO` | Liberado | S | Veja opções na seção OPÇÕES |
| `CODHISTCTB` | Histórico | I |  |
| `REFERENCIA` | Referência | D |  |
| `CODEMP` | Empresa | I |  |
| `CODUSU` | Usuário | I |  |
| `DTMOV` | Data Movimento | D |  |
| `NUMLOTE` | Núm. Lote | I |  |
| `NUMLANC` | Núm. Lançamento | I |  |
| `CODCONPAR` | Conta Contrapartida | I |  |
| `COMPLHIST` | Complemento | S |  |
| `CODCENCUS` | Centro Resultado | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `CODPROJ` | Projeto | I |  |
| `PARTLALUR_A` | Parte A do e-LALUR | S | Veja opções na seção OPÇÕES |
| `VLRCRED` | Valor Crédito | F |  |
| `VLRDEB` | Valor Débito | F |  |
| `EXTEMPORANEO` | Extemporâneo? | S | Veja opções na seção OPÇÕES |
| `DTEXTEMPORANEO` | Dt. Ocorrência Extem. | D |  |
| `CODEMPORIG` | Empresa de Origem | I |  |
| `CHAVE` | Chave | S |  |
| `CONCILIADO` | Conciliado | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPLANC (Tabela: TCBLAN)
| Valor | Descrição |
|-------|-----------|
| D | Débito |
| R | Crédito |

### Opções para campo LIBERADO (Tabela: TCBLAN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PARTLALUR_A (Tabela: TCBLAN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXTEMPORANEO (Tabela: TCBLAN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONCILIADO (Tabela: TCBLAN)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TCBLOT
### Descrição: Mestres de Lotes

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód.Empresa | I |  |
| `CODUSU` | Cód. Usuário | I |  |
| `NUMLOTE` | Nro. Lote | I |  |
| `REFERENCIA` | Referência | D |  |
| `DTMOV` | Dt. Movimento | D |  |
| `TOTLOTE` | Total do lote | F |  |
| `SITUACAO` | Situação | S | Veja opções na seção OPÇÕES |
| `ULTLANC` | Últ. Lançamento | I |  |
| `VLRDEBITO` | Débito | F |  |
| `VLRCREDITO` | Crédito | F |  |
| `VLRDIFERENCA` | Diferença | F |  |
| `QTDLANC` | Qtd. Lançamentos | I |  |
| `CODEMPCONSOLID` | Empresa Origem (Consolidação)] | I |  |
| `COMENTARIOS` | Observação | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo SITUACAO (Tabela: TCBLOT)
| Valor | Descrição |
|-------|-----------|
| A | Aberto |
| F | Fechado |


## Tabela: TCBPCT
### Descrição: Período Contábil

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUPERIODOCTB` | Nro período contábil | I |  |
| `CODEMP` | Código Empresa | I |  |
| `INICIOPERIODO` | Inicio período contábil | D |  |
| `FIMPERIODO` | Fim período contábil | D |  |
| `DHALTER` | Dh. alteração | H |  |
| `CODUSU` | Codigo Usuário | I |  |
| `DESCRICAO` | Descrição | S |  |

## Tabela: TCBPLA
### Descrição: Plano de contas

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCTACTB` | Conta reduzida | I |  |
| `CODLALURB` | Código Parte B do e-LALUR | S |  |
| `DESCRCTA` | Descrição | S |  |
| `CTACTB` | Conta contábil | S |  |
| `CODCONTA` | Código da Conta | I |  |
| `PODELANCTOMANUAL` | Aceita lançamento manual | S | Veja opções na seção OPÇÕES |
| `DESCRCONTA` | Descrição | S |  |
| `ANALITICA` | Analítica | S | Veja opções na seção OPÇÕES |
| `TABELALALURB` | Tabela lalurb | S |  |
| `PROJOBRIG` | Projeto obrigatório | S | Veja opções na seção OPÇÕES |
| `CENCUSOBRIG` | Centro de Resultado obrigatório | S | Veja opções na seção OPÇÕES |
| `BEMORIGINAL` | Bem Original | S | Veja opções na seção OPÇÕES |
| `BEMRESREAV` | Reserva de Reavaliação | S | Veja opções na seção OPÇÕES |
| `BEMOUTROS` | Outros acréscimos | S | Veja opções na seção OPÇÕES |
| `ATIVA` | Ativa | S | Veja opções na seção OPÇÕES |
| `CODGRUPOCTA` | Grupo de Conta | S | Veja opções na seção OPÇÕES |
| `RECDESP` | Tipo | S | Veja opções na seção OPÇÕES |
| `CODCTACTBSUBST` | Conta Substituta | I |  |
| `DTINCLUSAO` | Referência de ativação | H |  |
| `DTINATIV` | Referência de inativação | H |  |
| `DTALTER` | Dt. Alteração | H |  |
| `CODUSU` | Usuário | I |  |
| `CODEMP` | Código da empresa | I |  |
| `GRAU` | Grau | I |  |
| `OBSERVACOES` | Observação | S |  |
| `PROCESSO` | Processo | I |  |
| `PRODUTO` | Produto | I |  |
| `PLANTA` | Planta | I |  |
| `CODCTACTBPAI` | Cód. conta reduzida pai | I |  |
| `CONVSALDOMOEDA` | Conversão do saldo para moeda | S |  |
| `DTBASECONVMOEDA` | Data base conversão de moedas | S |  |
| `LALUR_A` | Parte A do e-LALUR | S |  |
| `LALUR_A_CRED` | Part A of e-LALUR (Saldo Credor) | S |  |
| `INDTRIBLALURB` | Indicador Tributos Parte B do e-LALUR | S | Veja opções na seção OPÇÕES |
| `TIPSALALUR` | Tipo de Saldo e-LALUR | I | Veja opções na seção OPÇÕES |
| `CODRAZAUX` | Cód. Razão Auxiliar | I |  |
| `TABELA` | Tabela | S |  |
| `TABELACRED` | Tabela | S |  |
| `NATUREZAEFD` | Natureza para EFD | I | Veja opções na seção OPÇÕES |
| `CLASSIFIRPJ` | Classificação IRPJ | S | Veja opções na seção OPÇÕES |
| `CLASSIFCSLL` | Classificação CSLL | S | Veja opções na seção OPÇÕES |
| `ADICOESIRPJ` | ( + ) Adições | S | Veja opções na seção OPÇÕES |
| `EXCLUSOESIRPJ` | ( - ) Exclusões | S | Veja opções na seção OPÇÕES |
| `PAT4IRPJ` | PAT 4% | S | Veja opções na seção OPÇÕES |
| `CONRESULTIRPJ` | Conta de Resultado | S | Veja opções na seção OPÇÕES |
| `ZERACRIRPJ` | Zeramento de Contas de Resultado | S | Veja opções na seção OPÇÕES |
| `ADICOESCSLL` | ( + ) Adições | S | Veja opções na seção OPÇÕES |
| `EXCLUSOESCSLL` | ( - ) Exclusões | S | Veja opções na seção OPÇÕES |
| `CONRESULTCSLL` | Conta de Resultado | S | Veja opções na seção OPÇÕES |
| `ZERACRCSLL` | Zeramento de Contas de Resultado | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo PODELANCTOMANUAL (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANALITICA (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROJOBRIG (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CENCUSOBRIG (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BEMORIGINAL (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BEMRESREAV (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BEMOUTROS (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVA (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODGRUPOCTA (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| 01 | 01 - Contas de ativo |
| 02 | 02 - Contas de passivo |
| 03 | 03 - Patrimônio líquido |
| 04 | 04 - Contas de resultado |
| 05 | 05 - Contas de compensação |
| 09 | 09 - Outras |

### Opções para campo RECDESP (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Despesa |
| S | Receita |

### Opções para campo INDTRIBLALURB (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| A | A - Ambos (IRPJ e CSLL) |
| C | C - Contribuição Social sobre o Lucro Líquido |
| null | I - Imposto de Renda Pessoa Jurídica |

### Opções para campo TIPSALALUR (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| 0 | 0 - Buscar Lançamentos (Parcial) |
| 1 | 1 - Saldo Total |

### Opções para campo NATUREZAEFD (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| 1 | 01 - Receita de vendas, Receitas prestação serviços, Receitas financeiras, Receitas não operacionais |
| 10 | 10 - Encargos de depreciação do período, encargos de amortização do período, etc |
| 11 | 11 - Máquinas e Equipamentos do Ativo Imobilizado, ativo fixo, etc |
| 12 | 12 - Despesas de Aplicações Financeiras; Despesas Financeiras (Juros/Multas) |
| 13 | 13 - Receitas de Aplicações Financeiras; Receitas Financeiras (Juros/Multas) |
| 2 | 02 - Receitas de vendas não tributadas |
| 3 | 03 - Receita de Fretes, Receita de transportes rodoviário de cargas |
| 4 | 04 - Custos de Produtos/Serviços prestados por pessoa jurídica |
| 5 | 05 - Custos com transportes |
| 6 | 06 - Despesas Diversas |
| 7 | 07 - Despesas de fretes contratados e despesas de comercialização |
| 8 | 08 - Estoques, Matéria prima e material de embalagem |
| 9 | 09 - Aquisições de bens para revenda, aquisições de insumos para industrialização |

### Opções para campo CLASSIFIRPJ (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| A | ( + ) Adições |
| C | Conta de Resultado |
| E | ( - ) Exclusões |
| P | PAT 4% |
| Z | Zeramento de Contas de Resultado |

### Opções para campo CLASSIFCSLL (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| A | ( + ) Adições |
| C | Conta de Resultado |
| E | ( - ) Exclusões |
| Z | Zeramento de Contas de Resultado |

### Opções para campo ADICOESIRPJ (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXCLUSOESIRPJ (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PAT4IRPJ (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONRESULTIRPJ (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ZERACRIRPJ (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ADICOESCSLL (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXCLUSOESCSLL (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONRESULTCSLL (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ZERACRCSLL (Tabela: TCBPLA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TCBPLA_IMP
### Descrição: Plano de Contas com base na ECD

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCTACTB` | Conta reduzida | I |  |
| `CODEMP` | Cód. da Empresa | I |  |
| `CTACTB` | Cód. da Conta Contábil Externa | S |  |
| `CODCTACTBPAI` | Cód. da Conta Pai Externa | S |  |
| `GRAU` | Grau da Conta | I |  |
| `DESCRCTA` | Descrição | S |  |
| `ANALITICA` | Analítica | S | Veja opções na seção OPÇÕES |
| `CODGRUPOCTA` | Grupo de Conta | S | Veja opções na seção OPÇÕES |
| `DTINCLUSAO` | Dt. Inclusão | H |  |
| `CODUSU` | Usuário | I |  |
| `DTPRIMIMP` | Data e hora primeira importação | H |  |
| `DTALTER` | Data e hora alteração | H |  |
| `CODCTACTBINTPAI` | Cód. conta reduzida pai | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo ANALITICA (Tabela: TCBPLA_IMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CODGRUPOCTA (Tabela: TCBPLA_IMP)
| Valor | Descrição |
|-------|-----------|
| 01 | 01 - Contas de ativo |
| 02 | 02 - Contas de passivo |
| 03 | 03 - Patrimônio líquido |
| 04 | 04 - Contas de resultado |
| 05 | 05 - Contas de compensação |
| 09 | 09 - Outras |


## Tabela: TCBPLR
### Descrição: Plano de Contas Referencial

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `TIPO` | Tipo | I | Veja opções na seção OPÇÕES |
| `CODCTAREF` | Cód. Conta Ref. | S |  |
| `DESCRCTAREF` | Descrição | S |  |
| `GRAU` | Grau | I |  |
| `ANALITICA` | Analítica | S | Veja opções na seção OPÇÕES |
| `NATUREZA` | Natureza | S |  |
| `CTCCTBPAI` | Cód. Conta Pai | S |  |
| `DTALTER` | Dt. Alteração | H |  |
| `CODUSU` | Cód. Usuário | I |  |
| `TABELA` | Tabela | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TCBPLR)
| Valor | Descrição |
|-------|-----------|
| 1 | 1 - PJ em Geral ( L100_A + L300_A + L300_R) |
| 10 | 10 - Financeiras - Lucro Presumido ( P100B + P150B ) |
| 2 | 2 - PJ em Geral - Lucro Presumido ( P100 + P150 ) |
| 3 | 3 - Financeiras ( L100_B + L300_B ) |
| 4 | 4 - Seguradoras ou Entidades Abertas de Previdência Complementar ( L100_C + L300_C ) |
| 5 | 5 - Imunes e Isentas em Geral ( U100_A + U150_A ) |
| 6 | 6 - Financeiras - Imunes e Isentas ( U100_B + U150_B ) |
| 7 | 7 - Seguradoras - Imunes e Isentas ( U100_C + U150_C ) |
| 8 | 8 - Entidades Fechadas de Previdência Complementar ( U100_D + U150_D ) |
| 9 | 9 - Partidos Políticos ( U100_E + U150_E ) |

### Opções para campo ANALITICA (Tabela: TCBPLR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TCBSAL
### Descrição: Saldo

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCTACTB` | Cód.Conta | I |  |
| `REFERENCIA` | Referência | D |  |
| `CODEMP` | Código Empresa | I |  |
| `CODCENCUS` | Cód.Centro Resultado | I |  |
| `CODPROJ` | Projeto | I |  |
| `SALDOINICMES` | Saldo no início do mês | F |  |
| `DEBMES` | Débito no mês | F |  |
| `CREDMES` | Crédito no mês | F |  |

## Tabela: TCBSAL_IMP
### Descrição: Saldo com base na ECD

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód. da Empresa | I |  |
| `CTACTB` | Cód. da Conta Contábil | S |  |
| `REFERENCIA` | Referência | H |  |
| `CODCENCUS` | Cód. Centro Resultado | S |  |
| `SALDOINICMES` | Saldo Inicial | F |  |
| `INDSTINI` | Ind. da Situação do Saldo Inicial | S | Veja opções na seção OPÇÕES |
| `DEBMES` | Débito | F |  |
| `CREDMES` | Crédito | F |  |
| `SALDOFINMES` | Saldo Final | F |  |
| `INDSTFIN` | Ind. da Situação do Saldo Final | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo INDSTINI (Tabela: TCBSAL_IMP)
| Valor | Descrição |
|-------|-----------|
| C | Credor |
| D | Devedor |

### Opções para campo INDSTFIN (Tabela: TCBSAL_IMP)
| Valor | Descrição |
|-------|-----------|
| C | Credor |
| D | Devedor |


## Tabela: TCBVCED
### Descrição: Vinculação de Contas Contábeis Externas Detalhes

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód. Empresa da Importação | I |  |
| `CODCTACTB` | Conta reduzida | I |  |
| `CRIMPORTADO` | Centro Resultado | S |  |
| `SEQUENCIA` | Sequência | I |  |
| `CTACTBEXT` | Conta contábil externa manual | S |  |
| `CTACTBEXTIMP` | Conta contábil externa importada | S |  |
| `CTACTB` | Conta contábil | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DTALTER` | Dt. Alteração | H |  |
| `CRVINCULADO` | Centro Resultado | S |  |
| `SALCTACTBVINC` | Saldo da conta vinculada | F |  |
| `INDSITINI` | Indicador da situação do saldo inicial | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo INDSITINI (Tabela: TCBVCED)
| Valor | Descrição |
|-------|-----------|
| C | C-Credor |
| D | D-Devedor |


## Tabela: TGFCTB
### Descrição: Parâmetros Contabilização

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODTIPOPER` | Cód.Tipo Operação | I |  |
| `DC` | Tipo de Lançamento | S | Veja opções na seção OPÇÕES |
| `CODHISTCTB` | Cód. Histórico | I |  |
| `CENCUSCONST` | Tipo de Centro de Resultado | S | Veja opções na seção OPÇÕES |
| `CODCENCUS` | Cód.Centro de Resultado | S | Veja opções na seção OPÇÕES |
| `CTACTBCONST` | Tipo de Conta Contábil | S | Veja opções na seção OPÇÕES |
| `CODCTACTB` | Conta contábil | S | Veja opções na seção OPÇÕES |
| `PROJCONST` | Tipo de Projeto | S | Veja opções na seção OPÇÕES |
| `CODPROJ` | Cód. Projeto | S | Veja opções na seção OPÇÕES |
| `LANCAMENTO` | Lançamento | I |  |
| `FORMULA` | Fórmula | S |  |
| `TIPDT` | Tipo de data | S | Veja opções na seção OPÇÕES |
| `CODEMP` | Empresa | I |  |
| `SINTETIZA` | Sintetiza | S | Veja opções na seção OPÇÕES |
| `HISTORICO` | Desc. Histórico | S |  |
| `TIPOEMPORIG` | Regra p/ Empresa de Origem | S | Veja opções na seção OPÇÕES |
| `SEQUENCIA` | Sequência | I |  |
| `TIPCTBZCOMPANY` | Contabilização entre Partes Relacionadas | S | Veja opções na seção OPÇÕES |
| `TIPEMPCOMPANY` | Representante Company | S | Veja opções na seção OPÇÕES |
| `CTACTBCONSTTRANS` | Tipo de Conta Contábil Transitória | S | Veja opções na seção OPÇÕES |
| `CODCTACTBTRANS` | Conta Contábil Transitória | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo DC (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| C | Crédito |
| D | Débito |

### Opções para campo CENCUSCONST (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| N | Variável |
| S | Constante |

### Opções para campo CODCENCUS (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| C | C - Cabeçalho da Nota |
| E | E - Empresa origem (CR 2) |
| F | F - Financeiro |
| N | N - Rateio ou Financeiro |
| O | O - Empresa origem (CR 1) |
| P | P - Produto |
| R | R - Rateio |
| 1 | 1 - Empresa destino (CR 1) |
| 2 | 2 - Empresa destino (CR 2) |

### Opções para campo CTACTBCONST (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| N | Variável |
| S | Constante |

### Opções para campo CODCTACTB (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| CFO | CFO dos itens |
| CTABCO | Conta da conta bancária |
| EMP1 | Conta 1 da empresa |
| EMP2 | Conta 2 da empresa |
| EMP3 | Conta 3 da empresa |
| NAT | Conta 1 da natureza |
| NAT2 | Conta 2 da natureza |
| PARCTR1 | Conta 1 da Transportadora |
| PARCTR2 | Conta 2 da Transportadora |
| PARCTR3 | Conta 3 da Transportadora |
| PARCTR4 | Conta 4 da Transportadora |
| PARC1 | Conta 1 do parceiro |
| PARC2 | Conta 2 do parceiro |
| PARC3 | Conta 3 do parceiro |
| PARC4 | Conta 4 do parceiro |
| PROD | Conta 1 do produto |
| PROJ | Conta 1 do projeto |
| PROJ2 | Conta 2 do projeto |
| PRO2 | Conta 2 do produto |
| PRO3 | Conta 3 do produto |
| PRO4 | Conta 4 do produto |
| RAT | Conta do rateio |
| TITCTA | Conta 1 do Tip.Título |
| TIT2CTA | Conta 2 do Tip.Título |
| TIT3CTA | Conta 3 do Tip.Título |
| TPV1 | Conta 1 do tipo de negociação |
| TPV2 | Conta 2 do tipo de negociação |

### Opções para campo PROJCONST (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| N | Variável |
| S | Constante |

### Opções para campo CODPROJ (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| C | C - Cabeçalho da Nota |
| F | F - Financeiro |
| N | N - Rateio ou Financeiro |
| P | P - Produto |
| R | R - Rateio |

### Opções para campo TIPDT (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| A | Validade |
| B | Baixa |
| C | Conciliação |
| E | Ent./Saída |
| F | Faturamento |
| J | Juro/Multa Mês |
| M | Movimento |
| N | Negociação |
| P | Ajusta Valor Presente |
| V | Vencimento |

### Opções para campo SINTETIZA (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOEMPORIG (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| C | Empresa da Conta Bancária |
| null | Regra Padrão |
| T | Empresa do Título |

### Opções para campo TIPCTBZCOMPANY (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| E | Inter-company |
| I | Intra-company |
| N | Normal |
| null | Não há |

### Opções para campo TIPEMPCOMPANY (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| F | Filial |
| M | Matriz |

### Opções para campo CTACTBCONSTTRANS (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| N | Variável |
| S | Constante |

### Opções para campo CODCTACTBTRANS (Tabela: TGFCTB)
| Valor | Descrição |
|-------|-----------|
| CFO | CFO dos itens |
| CTABCO | Conta da conta bancária |
| EMP1 | Conta 1 da empresa |
| EMP2 | Conta 2 da empresa |
| NAT | Conta 1 da natureza |
| NAT2 | Conta 2 da natureza |
| PARCTR1 | Conta 1 da Transportadora |
| PARCTR2 | Conta 2 da Transportadora |
| PARCTR3 | Conta 3 da Transportadora |
| PARCTR4 | Conta 4 da Transportadora |
| PARC1 | Conta 1 do parceiro |
| PARC2 | Conta 2 do parceiro |
| PARC3 | Conta 3 do parceiro |
| PARC4 | Conta 4 do parceiro |
| PROD | Conta 1 do produto |
| PROJ | Conta 1 do projeto |
| PROJ2 | Conta 2 do projeto |
| PRO2 | Conta 2 do produto |
| PRO3 | Conta 3 do produto |
| PRO4 | Conta 4 do produto |
| RAT | Conta do rateio |
| TITCTA | Conta 1 do Tip.Título |
| TIT2CTA | Conta 2 do Tip.Título |
| TIT3CTA | Conta 3 do Tip.Título |
| TPV1 | Conta 1 do tipo de negociação |
| TPV2 | Conta 2 do tipo de negociação |


## Tabela: TGFENA
### Descrição: Relação de empresa natureza e conta contábil

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODNAT` | Cód. Natureza | I |  |
| `CODEMP` | Empresa | I |  |
| `CODCTACTB` | Conta contábil | I |  |

## Tabela: TGFAJA
### Descrição: Ajuste Apuração

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUAJA` | Nro. único ajuste | I |  |
| `CODEMP` | Empresa | I |  |
| `DTREF` | Referência | D |  |
| `TIPAJUSTE` | Tipo ajuste | I |  |
| `TIPIMPOSTO` | Tipo imposto | S | Veja opções na seção OPÇÕES |
| `TIPAPURACAO` | Tipo apuração | I | Veja opções na seção OPÇÕES |
| `SEQUENCIA` | Sequência | I |  |
| `NUMDA` | Nro doc. arrecadação | S |  |
| `CODUF` | UF | I |  |
| `NUMPROCESSO` | Número processo | S |  |
| `ORIGPROCESSO` | Origem processo | I | Veja opções na seção OPÇÕES |
| `DESCRPROCESSO` | Descrição processo | S |  |
| `APURACAOUF` | Apuração por UF | S | Veja opções na seção OPÇÕES |
| `CODOBSPADRAO` | Observação padrão | I |  |
| `VLRAJUSTE` | Valor ajuste | F |  |
| `OBSERVACAO` | Observação | S |  |
| `CODUSU` | Usuário | I |  |
| `DTALTER` | Data alteração | H |  |
| `CODAJUSTE` | Código ajuste | S |  |
| `DEBESP` | Débitos especiais | S | Veja opções na seção OPÇÕES |
| `SUBAPURACAO` | Sub-Apuração | S | Veja opções na seção OPÇÕES |
| `INDSUBAPURACAO` | Indicador de Sub-Apuração | S | Veja opções na seção OPÇÕES |
| `CODCFG` | Código Configuração Ajuste Apuração | F |  |
| `REGAJDIME` | Registro do Ajuste na DIME SC | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPIMPOSTO (Tabela: TGFAJA)
| Valor | Descrição |
|-------|-----------|
| A | ICMS FCP Interno |
| B | ST FCP Interno |
| C | ICMS |
| D | ICMS DIFAL |
| F | ICMS FCP DIFAL |
| I | Imobilizado |
| S | ICMS ST |
| Z | Produzir |

### Opções para campo TIPAPURACAO (Tabela: TGFAJA)
| Valor | Descrição |
|-------|-----------|
| 100 | Débito especial |
| 101 | Controle do ICMS extra-apuração |
| 12 | Deduções do imposto apurado |
| 2 | Outros débitos |
| 3 | Estorno de créditos |
| 6 | Outros créditos |
| 7 | Estorno de débitos |

### Opções para campo ORIGPROCESSO (Tabela: TGFAJA)
| Valor | Descrição |
|-------|-----------|
| 0 | Sefaz |
| 1 | Justiça Federal |
| 2 | Justiça Estadual |
| 9 | Outros |

### Opções para campo APURACAOUF (Tabela: TGFAJA)
| Valor | Descrição |
|-------|-----------|
| null | Não |
| S | Sim |

### Opções para campo DEBESP (Tabela: TGFAJA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SUBAPURACAO (Tabela: TGFAJA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INDSUBAPURACAO (Tabela: TGFAJA)
| Valor | Descrição |
|-------|-----------|
| 3 | Apuração 1 |
| 4 | Apuração 2 |
| 5 | Apuração 3 |
| 6 | Apuração 4 |
| 7 | Apuração 5 |
| 8 | Apuração 6 |

### Opções para campo REGAJDIME (Tabela: TGFAJA)
| Valor | Descrição |
|-------|-----------|
| 60 | Item 60 - Outros Estornos de Crédito |
| 65 | Item 65 - Estorno de Crédito da Entrada em Decorrência da Utilização de Crédito Presumido |


## Tabela: TGFEFDVMRSTDIA
### Descrição: Consultar a Média Diária dos Impostos ICMS/ST

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Empresa | I |  |
| `DTREF` | Data Referência | D |  |
| `CODPROD` | Produto | I |  |
| `TIPIMPOSTO` | Tipo do Imposto | S | Veja opções na seção OPÇÕES |
| `TIPMEDIA` | Tipo da Média | S | Veja opções na seção OPÇÕES |
| `DTMOV` | Data do Movimento | D |  |
| `DTCALCULO` | Data do Cálculo | D |  |
| `QTDTOT` | Qtd. Inicial do Estoque | F |  |
| `VLRTOT` | Vlr. Total do Imposto | F |  |
| `VLRUNITMED` | Vlr. Unit. do Item | F |  |
| `QTDFIM` | Qtd. Final do Estoque | F |  |
| `VLRFIM` | Vlr. Final do Imposto | F |  |
| `QTDTOTENT` | Total das entradas | F |  |
| `QTDTOTSAI` | Total das saídas | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPIMPOSTO (Tabela: TGFEFDVMRSTDIA)
| Valor | Descrição |
|-------|-----------|
| B | BASE ST |
| F | FCP |
| I | ICMS |
| S | ST |

### Opções para campo TIPMEDIA (Tabela: TGFEFDVMRSTDIA)
| Valor | Descrição |
|-------|-----------|
| D | Diária |
| I | Inventário |


## Tabela: TGFEPS
### Descrição: Tabela Eventos Periódicos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODEMP` | Cód. Empresa | I |  |
| `EVENTO` | Evento | S |  |
| `DESCRICAO` | Descrição | S |  |
| `GERAREVENTO` | Gerar Evento | S | Veja opções na seção OPÇÕES |
| `DTALTER` | DTALTER | H |  |
| `CODUSU` | CODUSU | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo GERAREVENTO (Tabela: TGFEPS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TGFINU
### Descrição: Numeração Inutilizada

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUMNOTA` | Nro. Nota | I |  |
| `CODEMP` | Empresa | I |  |
| `SERIENOTA` | Série da nota | S |  |
| `CODMODDOC` | Modelo do Documento | I |  |
| `DTMOV` | Dt. do Movimento | H |  |
| `MOTIVO` | Motivo | S |  |
| `NUMPROTOC` | Nro. Protocolo NF-e | S |  |
| `DHPROTOC` | Dt. Protocolo | H |  |
| `CODUSU` | Cód. Usuário | I |  |
| `TPAMBNFE` | Tipo Ambiente NFe | S | Veja opções na seção OPÇÕES |
| `ENTSAI` | Tipo Livro | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TPAMBNFE (Tabela: TGFINU)
| Valor | Descrição |
|-------|-----------|
| 1 | Produção |
| 2 | Homologação |

### Opções para campo ENTSAI (Tabela: TGFINU)
| Valor | Descrição |
|-------|-----------|
| E | Entrada |
| S | Saída |


## Tabela: TGFLIS
### Descrição: Registro ISS

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Número único Nota | I |  |
| `SEQUENCIA` | Sequência | I |  |
| `CODEMP` | Empresa | I |  |
| `ORIGEM` | Origem | S | Veja opções na seção OPÇÕES |
| `NUMNOTA` | Número da nota | I |  |
| `NUMNOTA2` | Número da Nota para Redução Z | I |  |
| `SERIENOTA` | Série da nota | S |  |
| `DTMOV` | Data do movimento | D |  |
| `DTDOC` | Data do documento | D |  |
| `RETIDO` | ISS Retido | S | Veja opções na seção OPÇÕES |
| `VLRCTB` | Valor Contábil | F |  |
| `BASEISS` | Base do ISS | F |  |
| `ALIQISS` | Alíquota ISS | F |  |
| `VLRISS` | Valor do ISS | F |  |
| `ISENTASISS` | Valor Isento | F |  |
| `NAOTRIBISS` | Valor Não Tributado | F |  |
| `VLRREDBASEISS` | Valor da Redução de Base | F |  |
| `VLRMAT` | Valor do Material Aplicado | F |  |
| `VLRSUB` | Valor Sub-empreito | F |  |
| `DIGITADO` | Digitado | S | Veja opções na seção OPÇÕES |
| `OBSERVACAO` | Observação | S |  |
| `CODEMPORIG` | Empresa de Origem | I |  |
| `ENTSAI` | Tipo do Livro | S | Veja opções na seção OPÇÕES |
| `CODPARC` | Parceiro | I |  |
| `UFORIGEM` | UF origem | S |  |
| `UFDESTINO` | UF destino | S |  |
| `CODCIDORIGEM` | Cidade origem | I |  |
| `CODCIDDESTINO` | Cidade destino | I |  |
| `CODCIDEXECSERV` | Cidade exec. serv. | I |  |
| `CODCFPS` | CFPS | I |  |
| `CODTRIBISS` | Trib. ISS | I |  |
| `CODMODDOCISS` | CODMODDOCISS | S |  |
| `VLRMATTERC` | Valor mat. terc. | F |  |
| `DTFILT` | Data filtro | H |  |
| `CODLST` | Tipo de Serviço | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo ORIGEM (Tabela: TGFLIS)
| Valor | Descrição |
|-------|-----------|
| C | Cancelamento |
| E | Estoque |
| F | Financeiro |
| Z | Redução Z |

### Opções para campo RETIDO (Tabela: TGFLIS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DIGITADO (Tabela: TGFLIS)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENTSAI (Tabela: TGFLIS)
| Valor | Descrição |
|-------|-----------|
| E | Serviços Adquiridos |
| S | Serviços Prestados |


## Tabela: TGFLIV
### Descrição: Movimento Livros Fiscais

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUNOTA` | Nro único Nota | I |  |
| `ORIGEM` | Origem | S | Veja opções na seção OPÇÕES |
| `SEQUENCIA` | Sequência | I |  |
| `CODEMP` | Empresa | I |  |
| `NUMNOTA` | Nro. da nota | I |  |
| `NUMNOTA2` | Nro. da nota 2 | I |  |
| `SERIENOTA` | Série da nota | S |  |
| `DTDOC` | Dt. do documento | D |  |
| `DHMOV` | Dt. do movimento | D |  |
| `EMPPARC` | Destino | S | Veja opções na seção OPÇÕES |
| `CODPARC` | Empresa/Parceiro | I |  |
| `CODCFO` | CFOP | I |  |
| `NUMLANC` | Nro. do lançamento | I |  |
| `ESPDOC` | Espécie do documento | S |  |
| `CODTRIB` | Cód. de tributação | I | Veja opções na seção OPÇÕES |
| `TIPICMS` | Tipo de ICMS | S | Veja opções na seção OPÇÕES |
| `BASEICMS` | Base do ICMS | F |  |
| `ALIQICMS` | Alíquota ICMS | F |  |
| `VLRICMS` | Vlr. do ICMS | F |  |
| `ISENTASICMS` | Isentas de ICMS | F |  |
| `OUTRASICMS` | Outras ICMS | F |  |
| `BASERETENCAO` | Base retenção | F |  |
| `ICMSRETENCAO` | ICMS retenção | F |  |
| `TIPIPI` | Tipo de IPI | S | Veja opções na seção OPÇÕES |
| `BASEIPI` | Base do IPI | F |  |
| `ALIQIPI` | Alíquota de IPI | F |  |
| `VLRIPI` | Vlr. do IPI | F |  |
| `ISENTASIPI` | Isentas de IPI | F |  |
| `OUTRASIPI` | Outras IPI | F |  |
| `VLRCTB` | Vlr. contábil | F |  |
| `CODCTACTB` | Conta contábil | I |  |
| `OBSERVACAO` | Observação | S |  |
| `DIGITADO` | Digitado | S | Veja opções na seção OPÇÕES |
| `ENTSAI` | Entrada/Saída | S | Veja opções na seção OPÇÕES |
| `DIFICMS` | Diferença ICMS | F |  |
| `UFORIGEM` | UF de Origem | S |  |
| `UFDESTINO` | UF de Destino | S |  |
| `GTOTECF` | Grande total | F |  |
| `DTFILT` | Dt. p/ filtro do tipo de movimento | H |  |
| `CODEMPORIG` | Empresa de Origem | I |  |
| `CODMODDOC` | Modelo do Documento | I | Veja opções na seção OPÇÕES |
| `DESCR_EMP_PARC` | Descrição Parceiro/Empresa | S |  |
| `VLRTARE` | Apurar valor credito ICMS | F |  |
| `VLRCTBTARE` | Apuração do valor contábil TARE | F |  |
| `BASEICMSTARE` | Apuração da base ICMS TARE1 | F |  |
| `VLRICMSTARE` | Apuração do valor ICMS TARE | F |  |
| `BASERETENCAOSEMRED` | Base de Retenção sem redução | F |  |
| `CODANTECIPST` | Cód. Antecipação ST | S | Veja opções na seção OPÇÕES |
| `CHAVENFE` | Chave NF-e | S |  |
| `CHAVECTE` | Chave CT-e | S |  |
| `CHAVECTEREF` | Chave CT-e de Referência | S |  |
| `DTENTSAIINFO` | Dt. Extemporânea | D |  |
| `VLRICMSDIFALREM` | Vlr. DIFAL UF Remet. | F |  |
| `VLRICMSDIFALDEST` | Vlr. DIFAL UF Destino | F |  |
| `VLRICMSFCP` | Vlr. para Fundo Comb. Pobreza | F |  |
| `CODCONTATOENTREGA` | Contato de Entrega | I |  |
| `UFENTREGA` | UF de Entrega | S |  |
| `VLRICMSFCPINT` | Vlr. ICMS FCP Interno | F |  |
| `VLRSTFCPINT` | Vlr. ST FCP Interno | F |  |
| `CODPROD` | Produto | I |  |
| `CODCIDINICTE` | Cód. Cid. Inicio CT-e | I |  |
| `CODCIDFIMCTE` | Cód. Cid. Fim CT-e | I |  |
| `VLRICMSCOMPL` | Vlr. ICMS Complemento | F |  |
| `DTCANC` | Dt. Cancelamento | D |  |
| `CODUSU` | Cód. Usuário | I |  |
| `TIPMOV` | Tipo de movimento | S |  |
| `CODTIPOPER` | Tipo Operação | I |  |
| `DHALTER` | Data Inclusão/Alteração | D |  |

## OPÇÕES DE CAMPOS

### Opções para campo ORIGEM (Tabela: TGFLIV)
| Valor | Descrição |
|-------|-----------|
| A | Complemento |
| C | Cancelada |
| D | Devolução |
| E | Estoque |
| F | Financeiro |
| Z | Redução Z |

### Opções para campo EMPPARC (Tabela: TGFLIV)
| Valor | Descrição |
|-------|-----------|
| E | Empresa |
| P | Parceiro |

### Opções para campo CODTRIB (Tabela: TGFLIV)
| Valor | Descrição |
|-------|-----------|
| 0 | 00-Tributada integralmente |
| 02 | 02-Tributação monofásica própria sobre combustíveis |
| 10 | 10-Tributada e c/cobrança por substituição |
| 15 | 15-Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis |
| 20 | 20-Com redução de base de cálculo |
| 30 | 30-Isenta e não tribut. e c/cobrança por subst. |
| 40 | 40-Isenta |
| 41 | 41-Não tributada |
| 50 | 50-Suspensão |
| 51 | 51-Diferimento |
| 53 | 53-Tributação monofásica sobre combustíveis com recolhimento diferido |
| 60 | 60-ICMS cobrado anteriormente por substituição |
| 61 | 61-Tributação monofásica sobre combustíveis cobrada anteriormente |
| 70 | 70-Com redução de base e c/cobrança por subst. |
| 90 | 90-Outras |

### Opções para campo TIPICMS (Tabela: TGFLIV)
| Valor | Descrição |
|-------|-----------|
| 1 | Com créd/déb de imposto |
| 2 | Sem créd/déb- Isentas |
| 3 | Sem créd/déb- Outras |
| 4 | Com créd/déb- Isentas |
| 5 | Com créd/déb- Outras |

### Opções para campo TIPIPI (Tabela: TGFLIV)
| Valor | Descrição |
|-------|-----------|
| 1 | Com créd/déb de imposto |
| 2 | Sem créd/déb- Isentas |
| 3 | Sem créd/déb - Outras |

### Opções para campo DIGITADO (Tabela: TGFLIV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ENTSAI (Tabela: TGFLIV)
| Valor | Descrição |
|-------|-----------|
| E | Entrada |
| S | Saída |

### Opções para campo CODMODDOC (Tabela: TGFLIV)
| Valor | Descrição |
|-------|-----------|
| 0 | Sem Modelo |
| 1 | 01-Nota Fiscal |
| 10 | 10-Conhecimento Aéreo |
| 11 | 11-Conhecimento de Transporte Ferroviário de Cargas |
| 13 | 13-Bilhete de Passagem Rodoviário |
| 14 | 14-Bilhete e Passagem Aquaviário |
| 15 | 15-Bilhete de Passagem e Nota de Bagagem |
| 16 | 16-Bilhete de Passagem Ferroviário |
| 17 | 17-Despacho de Transporte |
| 18 | 18-Resumo Movimento Diário |
| 2 | 02-Nota Fiscal de Venda a Consumidor |
| 20 | 20-Ordem de Coleta de Carga |
| 21 | 21-Nota Fiscal de Serviço de Comunicação |
| 22 | 22-Nota Fiscal de Serviço de Telecomunicações |
| 23 | 23-GNRE |
| 24 | 24-Autorização de Carregamento de Transporte |
| 25 | 25-Manifesto de Carga |
| 26 | 26-Conhecimento de Transporte Multimodal de Cargas |
| 27 | 27-Nota Fiscal De Transporte Ferroviário De Carga |
| 28 | 28-Nota Fiscal/Conta de Fornecimento de Gás Canalizado |
| 29 | 29-Nota Fiscal/Conta De Fornecimento D'água Canalizada |
| 3 | 03-Nota Fiscal de Entrada |
| 4 | 04-Nota Fiscal de Produtor |
| 55 | 55-Nota Fiscal Eletrônica |
| 57 | 57-Conhecimento Transporte Rodoviário Eletrônico |
| 59 | 59-Cupom Fiscal Eletrônico |
| 6 | 06-Nota Fiscal Conta de Energia Elétrica |
| 62 | 62-Nota Fiscal Eletrônica de Serviços de Comunicação |
| 63 | 63-Bilhete de Passagem Eletrônico |
| 65 | 65-Nota Fiscal Eletrônica de Venda a Consumidor |
| 66 | 66 - Nota Fiscal de Energia Elétrica Eletrônica |
| 67 | 67-Conhecimento Transporte Eletrônico Outros Serviços |
| 7 | 07-Nota Fiscal de Serviço de Transporte |
| 8 | 08-Conhecimento de Transporte Rodoviário de Cargas |
| 9 | 09-Conhecimento de Transporte Aquaviário de Cargas |
| 901 | 901-Nota Fiscal Avulsa |
| 902 | 902-Conhecimento de Transporte de Cargas Avulso |

### Opções para campo CODANTECIPST (Tabela: TGFLIV)
| Valor | Descrição |
|-------|-----------|
| A | A-ST informada pelo substituto/substituído que não incorra em nenhuma das situações anteriores |
| N | N-(Não Usa) Operação não envolve ST |
| 1 | 1-Pgto de ST efetuado pelo destinatário quando não efetuado ou efetuado a menor pelo substituto |
| 2 | 2-Antecip. tribut. efetuada pelo destinatário apenas como complemento do diferencial de alíquota |
| 3 | 3-Antecip. tribut. com MVA efetuada pelo destinatário sem encerrar a fase de tributação |
| 4 | 4-Antecip. tribut. com MVA efetuada pelo destinatário encerrando a fase de tributação |
| 5 | 5-Substituição tributária interna motivada por regime especial de tributação |
| 6 | 6-ICMS pago na importação |


## Tabela: TGFNRR
### Descrição: Cadastro da Natureza de Rendimentos

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODNATREND` | Código Natureza Rendimento | I |  |
| `DESCNATREND` | Descrição Natureza Rendimento | S |  |
| `FCI` | Fundo ou Clube de Investimento | S | Veja opções na seção OPÇÕES |
| `DECIMOTERCEIRO` | Décimo Terceiro | S | Veja opções na seção OPÇÕES |
| `RRA` | Rendimento Recebido Acumuladamente | S | Veja opções na seção OPÇÕES |
| `DEDUCAO` | Tipo de Dedução | S |  |
| `RENDISENTO` | Tipo Rendimento Isento | S |  |
| `TRIBUTO` | Tipo Tributo | S |  |
| `BLOCOAPLIC` | Bloco de aplicação | S |  |
| `APLICACAO` | Local de Aplicação | S | Veja opções na seção OPÇÕES |
| `DTINICIOVAL` | Data Início Validade | D |  |
| `DTFIMVAL` | Data Fim Validade | D |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `GERSEMTRIB` | Gerar sem tributação? | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo FCI (Tabela: TGFNRR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DECIMOTERCEIRO (Tabela: TGFNRR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo RRA (Tabela: TGFNRR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APLICACAO (Tabela: TGFNRR)
| Valor | Descrição |
|-------|-----------|
| A | Ambos |
| F | Financeiro |
| S | Serviço |

### Opções para campo ATIVO (Tabela: TGFNRR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERSEMTRIB (Tabela: TGFNRR)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRAMP
### Descrição: Apontamento de Materiais

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUAPO` | Nro. único | I |  |
| `SEQAPA` | Sequência | I |  |
| `CODPRODMP` | Cód. Produto (MP) | I |  |
| `REFERENCIA` | Referência do Produto | S |  |
| `CONTROLEMP` | Controle (MP) | S |  |
| `QTD` | Qtd. apontada | F |  |
| `CODVOL` | UN. | S |  |
| `TIPOUSO` | Tipo de Uso | S | Veja opções na seção OPÇÕES |
| `SEQMP` | Sequência MP | I |  |
| `VINCULOSERIEPA` | VINCULOSERIEPA | S |  |
| `QTDPERDA` | Qtd. Total de Perda | F |  |
| `CODMPE` | Motivo de perda | I |  |
| `QTDMPE` | Qtd. de Motivos de Perda | I |  |
| `CODLOCALBAIXA` | Local de Baixa | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOUSO (Tabela: TPRAMP)
| Valor | Descrição |
|-------|-----------|
| C | Material Consumido |
| R | Material Reaproveitado |


## Tabela: TPRAPA
### Descrição: Apontamento de PA

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUAPO` | Nro. único | I |  |
| `SEQAPA` | Sequência | I |  |
| `CODPRODPA` | Cód. Produto (PA) | I |  |
| `REFERENCIA` | Referência do Produto | S |  |
| `CONTROLEPA` | Controle (PA) | S |  |
| `QTDAPONTADA` | Qtd. apontada | F |  |
| `QTDPERDA` | Qtd. Total de Perda | F |  |
| `QTDFAT` | Qtd. Baixada (PA) | F |  |
| `QTDFATSP` | Qtd. Baixada (SP) | F |  |
| `QTDMPE` | Qtd. de Motivos de Perda | I |  |
| `CODMPE` | Motivo de perda | I |  |

## Tabela: TPRAPF
### Descrição: Faturamento de Apontamento

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUAPO` | Apontamento | I |  |
| `SEQAPA` | SEQAPA | I |  |
| `NUNOTA` | Nro. Único | I |  |
| `SEQITE` | SEQITE | I |  |
| `QTD` | Quantidade | F |  |

## Tabela: TPRAPO
### Descrição: Cabeçalho de Apontamento

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NUAPO` | Nro. único | I |  |
| `IDIATV` | Atividade | I |  |
| `CODUSU` | Usuário responsável | I |  |
| `DHAPO` | Dh. Apontamento | H |  |
| `SITUACAO` | Situação | S | Veja opções na seção OPÇÕES |
| `OBSERVACAO` | Observação | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo SITUACAO (Tabela: TPRAPO)
| Valor | Descrição |
|-------|-----------|
| C | Confirmado |
| P | Pendente |


## Tabela: TPRATV
### Descrição: Atividade do processo produtivo

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDEFX` | Código | I |  |
| `OPERCQ` | Operação a ser realizada | S | Veja opções na seção OPÇÕES |
| `SUBAPOPORCONF` | Tipo de Apontamento | S | Veja opções na seção OPÇÕES |
| `DATAHORAAPONTAMENTO` | Data/Hora de Apontamento | S | Veja opções na seção OPÇÕES |
| `IDRPADEST` | Repositório de destino | I |  |
| `IDRPAOPER` | Repositório da operação | I |  |
| `IDAWC` | Alocação de C. Trabalho | I |  |
| `PERMITEPARCIAL` | Permite fluxo parcial | S | Veja opções na seção OPÇÕES |
| `TIPOTEMPO` | Tipo de tempo | S | Veja opções na seção OPÇÕES |
| `TEMPOATIVIDADE` | Tempo da atividade | F |  |
| `UNTEMPO` | Unidade de tempo | S | Veja opções na seção OPÇÕES |
| `QTDBASEAPON` | Quantidade base para apontamento | S | Veja opções na seção OPÇÕES |
| `APONTAMP` | Aponta matéria-prima | S | Veja opções na seção OPÇÕES |
| `APONTAPA` | Exige apontamento de PA | S | Veja opções na seção OPÇÕES |
| `APONTACOMP` | Aponta componente de manufatura | S | Veja opções na seção OPÇÕES |
| `APONTASP` | Aponta subproduto | S | Veja opções na seção OPÇÕES |
| `PERMITENOVOPA` | Apontar PA diferente em relação ao inicio do processo | S | Veja opções na seção OPÇÕES |
| `PROIBEAPONT` | Proibir apontamento à maior | S | Veja opções na seção OPÇÕES |
| `TIPOREPROCESSO` | Tipo de reprocesso | S | Veja opções na seção OPÇÕES |
| `ALTSTATUSPROC` | Status do processo | S | Veja opções na seção OPÇÕES |
| `CODUSULOGON` | Usuário para logon | I |  |
| `LISTAMPPADRAO` | Lista de matéria-prima padrão | S | Veja opções na seção OPÇÕES |
| `LIBERARWCFINAL` | Libera centro de trabalho no final da atividade | S | Veja opções na seção OPÇÕES |
| `LIBERARWCMANUAL` | Libera centro de trabalho manualmente | S | Veja opções na seção OPÇÕES |
| `INICIALIZARPA` | Inicializa repositório de produtos acabados | S | Veja opções na seção OPÇÕES |
| `CODPRCSUB` | Subprocesso | I |  |
| `IDCCQ` | Ciclo controle de qualidade | I |  |
| `VALIDACQ` | Validar ciclo de controle de qualidade | S | Veja opções na seção OPÇÕES |
| `IDPROC` | IDPROC | I |  |
| `EXECTERCEIRO` | Execução Terceirizada | S | Veja opções na seção OPÇÕES |
| `CONCLUICQ` | Conclui Ciclo de Controle de Qualidade | S | Veja opções na seção OPÇÕES |
| `CONTCUMULATIVA` | Contagem Cumulativa | S | Veja opções na seção OPÇÕES |
| `TIPOCONFERENCIA` | Tipo de Conferência | S | Veja opções na seção OPÇÕES |
| `QTDCONFIGUAIS` | Qtd. de conferências iguais | I |  |
| `QTDRECONTAGENS` | Qtd. de recontagens | I |  |
| `USASEQCODBAR` | Usar seq. lote no cód. barras | S | Veja opções na seção OPÇÕES |
| `SEPSEQCODBAR` | Separador | S |  |
| `APONTARECWC` | Aponta Recursos do Centro de Trabalho | S | Veja opções na seção OPÇÕES |
| `MULTITURNO` | Multi-turno | S | Veja opções na seção OPÇÕES |
| `CODMTPFINTURNO` | Motivo de parada (fim de turno) | I |  |
| `PERMITEALTLOCMP` | Permite alterar local de baixa da MP | S | Veja opções na seção OPÇÕES |
| `PERMITEPERDATOTAL` | Permitir apontamento de 100% de perda | S | Veja opções na seção OPÇÕES |
| `DESCRICAO` | Descrição | S |  |
| `SETUP` | Considerar atividades de Setup no OEE | S | Veja opções na seção OPÇÕES |
| `SEQEXECUCAO` | Sequencia de Execução | S |  |
| `APROVARSTATUSLOTE` | Aprova/Reprova 'Status do Lote' no Final do Ciclo | S | Veja opções na seção OPÇÕES |
| `GERAMLAUDO` | Gerar registro de Amostra e Laudo. | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo OPERCQ (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| A | Amostragem |
| L | Laudo |
| N | Nenhuma |
| T | Amostragem + Laudo |

### Opções para campo SUBAPOPORCONF (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Apontamento de PA/MP |
| P | Pesagem de Volumes |
| S | Conferência |

### Opções para campo DATAHORAAPONTAMENTO (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Automático Sem edição |
| P | Automático Com edição |
| S | Manual Com edição (Vazio) |

### Opções para campo PERMITEPARCIAL (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOTEMPO (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| F | Fixo |
| L | Por Lote |
| Q | Por Quantidade |

### Opções para campo UNTEMPO (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| D | Dias |
| H | Horas |
| M | Minutos |

### Opções para campo QTDBASEAPON (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| A | Qtd. apontada de PA |
| L | Qtd. do lote a produzir |
| N | Não sugere |
| R | Qtd. atual de PA no repositório de trabalho |

### Opções para campo APONTAMP (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| A | Aponta as MPs da Atividade |
| N | Não aponta MP |
| O | Aponta as MPs da OP |

### Opções para campo APONTAPA (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APONTACOMP (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APONTASP (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| A | Aponta os Subprodutos da Atividade |
| N | Não aponta Subprodutos |
| O | Aponta os Subprodutos da OP |

### Opções para campo PERMITENOVOPA (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROIBEAPONT (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOREPROCESSO (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não inicia reprocesso |
| P | Reprocesso c/ quantidade parcial |
| T | Reprocesso c/ quantidade total |

### Opções para campo ALTSTATUSPROC (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| A | Em andamento |
| C | Cancelado |
| M | Mantém o status atual |
| S | Suspenso |

### Opções para campo LISTAMPPADRAO (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo LIBERARWCFINAL (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo LIBERARWCMANUAL (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo INICIALIZARPA (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VALIDACQ (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXECTERCEIRO (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Nunca |
| O | Opcional |
| S | Sempre |

### Opções para campo CONCLUICQ (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONTCUMULATIVA (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOCONFERENCIA (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| CI | Exige Conferências Iguais |
| RE | Exige Recontagem |

### Opções para campo USASEQCODBAR (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APONTARECWC (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| A | Aponta os Recursos de CT da Atividade |
| N | Não aponta |
| O | Aponta os Recursos de CT da OP |

### Opções para campo MULTITURNO (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMITEALTLOCMP (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PERMITEPERDATOTAL (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo SETUP (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo APROVARSTATUSLOTE (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERAMLAUDO (Tabela: TPRATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRAUD
### Descrição: Auditoria

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODAUT` | Codigo Auditoria | I |  |
| `IDORIG` | Codigo do cadastro responsavel | I |  |
| `IDORIGAUX` | Codigo do cadastro responsavel 2 | I |  |
| `IDORIGAUXSUP` | Codigo do cadastro responsavel 3 | I |  |
| `TABACAO` | Tipo de acao na tabela | S |  |
| `COLREG` | Coluna alterada | S |  |
| `DHACAO` | Data e Hora ação | H |  |
| `CODUSU` | Usuário manipulador do registro | I |  |
| `TABREG` | Tabela alterada | S |  |

## Tabela: TPRCAP
### Descrição: TPRCAP

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCAP` | Cód. Capacidade | I |  |
| `DESCRICAO` | Descrição | S |  |
| `UNIDADE` | Unidade | S |  |
| `UNTMP` | Tempo | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo UNTMP (Tabela: TPRCAP)
| Valor | Descrição |
|-------|-----------|
| D | Dia |
| E | Mês |
| H | Hora |
| M | Minutos |
| S | Semana |


## Tabela: TPRCPM
### Descrição: TPRCPM

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODCPM` | Cód. Componente | I |  |
| `DESCRICAO` | Descrição | S |  |
| `CODCPMPAI` | Cód. Componente Pai | I |  |
| `QTDCOMP` | Quantidade | I |  |
| `ANALITICO` | Analítico | S | Veja opções na seção OPÇÕES |
| `GRAU` | Grau | I |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo ANALITICO (Tabela: TPRCPM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ATIVO (Tabela: TPRCPM)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPREFX
### Descrição: Elemento Básico de fluxo

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDEFX` | Código | I |  |
| `IDPROC` | Processo | I |  |
| `TIPO` | Tipo | I | Veja opções na seção OPÇÕES |
| `DESCRICAO` | Descrição | S |  |
| `X1POS` | X1POS | F |  |
| `Y1POS` | Y1POS | F |  |
| `X2POS` | X2POS | F |  |
| `Y2POS` | Y2POS | F |  |
| `CORPREENCHIMENTO` | CORPREENCHIMENTO | S |  |
| `TAMFONTE` | TAMFONTE | I |  |
| `CORFONTE` | CORFONTE | S |  |
| `IDEFXLANE` | IDEFXLANE | I |  |
| `WAYPOINTS` | WAYPOINTS | C |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TPREFX)
| Valor | Descrição |
|-------|-----------|
| 1101 | Tarefa de usuário |
| 1102 | Tarefa manual |
| 1103 | Serviço |
| 1104 | Envio de email |
| 1105 | Tarefa de recebimento |
| 1106 | Tarefa de script |
| 1107 | Tarefa de relatório |
| 1108 | Tarefa especial |
| 1109 | Config. de C. Trabalho |
| 1110 | Limpeza de C. Trabalho |
| 1201 | Sub-processo |
| 1202 | Processo de chamada |
| 2101 | Gateway exclusivo |
| 2201 | Gateway inclusivo |
| 2301 | Gateway paralelo |
| 2401 | Gateway complexo |
| 3101 | Evento de início |
| 3102 | Evento de mensagem inicial |
| 3103 | Evento temporizador inicial |
| 3104 | Evento de sinal inicial |
| 3201 | Evento final |
| 3202 | Evento final de mensagem |
| 3203 | Evento final de sinal |
| 3204 | Evento de término |
| 3301 | Evento intermed. mensagem(Catch) |
| 3302 | Evento intermed. mensagem(Throw) |
| 3303 | Evento temporizador intermediário |
| 3304 | Evento intermed. sinal(Catch) |
| 3305 | Evento intermed. sinal(Throw) |
| 4101 | Pool |
| 4102 | Lane |
| 5101 | Ligação de sequência |
| 5102 | Ligação de mensagem |
| 6101 | Anotação de texto |
| 6102 | Associação |
| 6103 | Grupos |


## Tabela: TPREIATV
### Descrição: Execução de Atividade

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDEIATV` | Código | I |  |
| `IDIATV` | Cód. Inst. Atividade | I |  |
| `CODEXEC` | Cód. Executante | I |  |
| `CODUSU` | Cód. Responsável | I |  |
| `DHINICIO` | Dh. Início | H |  |
| `DHFINAL` | Dh. Final | H |  |
| `TIPO` | Tipo | S | Veja opções na seção OPÇÕES |
| `CODMTP` | Motivo Parada | I |  |
| `OBSERVACAO` | Observação | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPO (Tabela: TPREIATV)
| Valor | Descrição |
|-------|-----------|
| N | Normal |
| P | Parada |
| S | Suspenso |
| T | Fim de turno |


## Tabela: TPRESR
### Descrição: Estoque por repositório de PA

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `REFERENCIA` | Referência do Produto | S |  |
| `IDRPA` | Cód. Repositório | I |  |
| `IDIPROC` | Nro. OP | I |  |
| `CODPRODPA` | Cód. Produto | I |  |
| `CONTROLEPA` | Controle | S |  |
| `CODCPM` | Cód. Componente | I |  |
| `STATUSEXEC` | Status | S | Veja opções na seção OPÇÕES |
| `ESTOQUE` | Estoque | F |  |
| `ESTOQUEPERDA` | Qtd. Perdida | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo STATUSEXEC (Tabela: TPRESR)
| Valor | Descrição |
|-------|-----------|
| N | Normal |
| R | Reprocesso |


## Tabela: TPREVT
### Descrição: Evento de Fluxo

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDEFX` | Código | I |  |
| `IDEFXANEXADO` | Atividade Anexada | I |  |
| `IDENTIFICADOR` | Identificador | S |  |
| `IDRPAINICIALIZA` | Repositório de Inicialização | I |  |
| `INTERROMPE` | Interrompe Atividade | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo INTERROMPE (Tabela: TPREVT)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRIATV
### Descrição: Mantem dados sobre uma instância de atividade de usuário.

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDIPROC` | Nro. OP | I |  |
| `SITUACAO` | Situação | S | Veja opções na seção OPÇÕES |
| `STATUSINSTCICLOCONTQUAL` | Status Instância Ciclo Controle de Qualidade | S | Veja opções na seção OPÇÕES |
| `DESCRGRUPOPRODPA` | Descr. Grupo do Produto | S |  |
| `DESCRPRODPA` | Descrição do Produto | S |  |
| `REFERENCIA` | Referência do Produto | S |  |
| `IDIATV` | Código | I |  |
| `PRIORIDADE` | Prioridade | I |  |
| `NROLOTE` | Nro. Lote | S |  |
| `CODPRODPA` | Cód. Produto | I |  |
| `CONTROLEPA` | Controle | S |  |
| `CODGRUPOPRODPA` | Grupo do Produto | I |  |
| `COMPLDESCPA` | Complemento do Produto | S |  |
| `CODVOLPA` | Un. Lote | S |  |
| `QTDPRODUZIR` | Tam. Lote | F |  |
| `MULTIPRODUTO` | Multi-produto | S | Veja opções na seção OPÇÕES |
| `DHINCLUSAO` | Dh. Entrada Atividade | H |  |
| `DHACEITE` | Dh. Aceite Atividade | H |  |
| `CODPARCTERC` | Cód. Parceiro Terceiro | I |  |
| `DHINICIO` | Dh. Inicio Atividade | H |  |
| `CODUSU` | Cód. Usuário Inicial | I |  |
| `DHFINAL` | Dh. Fim Atividade | H |  |
| `DHINIPREV` | Dt./Hr. Início Prev. | H |  |
| `DHFINPREV` | Dt./Hr. Final Prev. | H |  |
| `IDEFX` | Atividade | I |  |
| `CODWCP` | Centro de Trabalho | I |  |
| `IDEXECWFLOW` | Token | S |  |
| `CODEXEC` | Executante | I |  |
| `TEMPOGASTOMIN` | Tempo Gasto em Minutos | I |  |
| `CODUSUFIN` | Cód. Usuário Final | I |  |
| `CODULTEXEC` | Último Executante | I |  |
| `CODMTP` | Motivo Parada | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo SITUACAO (Tabela: TPRIATV)
| Valor | Descrição |
|-------|-----------|
| A | Aceita |
| F | Finalizada |
| G | Aguardando aceite |
| I | Iniciada |
| P | Parada |

### Opções para campo STATUSINSTCICLOCONTQUAL (Tabela: TPRIATV)
| Valor | Descrição |
|-------|-----------|
| A | Aprovado |
| E | Aprovado com Ressalvas |
| I | Não Iniciado |
| P | Em Andamento |
| R | Reprovado |

### Opções para campo MULTIPRODUTO (Tabela: TPRIATV)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRIPA
### Descrição: PAs a serem produzidos na instância

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDIPROC` | Código do Cabeçalho | I |  |
| `CODPRODPA` | Produto (PA) | I |  |
| `REFERENCIA` | Referência do Produto | S |  |
| `CONTROLEPA` | Controle (PA) | S |  |
| `QTDPRODUZIR` | Qtd. | F |  |
| `SALDOOP` | Saldo a Produzir | F |  |
| `NROLOTE` | Nro.Lote | S |  |
| `CONCLUIDO` | Concluído | S | Veja opções na seção OPÇÕES |
| `DTVAL` | Data de Validade | D |  |
| `DTFAB` | Data de Fabricação | D |  |
| `QTDPRODUZIR_ORIGINAL` | Qtd. Sem Ajuste | F |  |

## OPÇÕES DE CAMPOS

### Opções para campo CONCLUIDO (Tabela: TPRIPA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRIPROC
### Descrição: Manter dados de tempo de execução de uma ordem

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `PERIODOMPS` | Periodo MPS | S |  |
| `IDIPROC` | Nro. OP | I |  |
| `DECQTD` | Qtd. Casas Decimais | I |  |
| `NROLOTE` | Nro. Lote | S |  |
| `QTDPRODUZIR` | Tam. Lote | F |  |
| `SALDOOP` | Saldo a Produzir | F |  |
| `STATUSPROC` | Status | S | Veja opções na seção OPÇÕES |
| `CODPRODPA` | Cód. Produto | I |  |
| `REFERENCIA` | Referência do Produto | S |  |
| `DESCRPRODPA` | Descr. Produto | S |  |
| `CONTROLEPA` | Controle | S |  |
| `COMPLDESCPA` | Compl. Produto | S |  |
| `DHINC` | Dh. Inclusão | H |  |
| `DHINST` | Dh. Inicialização | H |  |
| `DHTERMINO` | Dh. Finalização | H |  |
| `DESCRICAO` | Operação Atual | S |  |
| `CODPARCTERC` | Parceiro Terceiro | I |  |
| `DTPREVENT` | Previsão de Entrega | H |  |
| `TEMPOATRAVESS` | Tempo de Atravessamento (min) | F |  |
| `DTINICIOMAX` | Dh. Inicialização (máx) | H |  |
| `NUNOTA` | Nro. Pedido | I |  |
| `CODUSUFINAL` | Usuário Finalizante | I |  |
| `CODEXEC` | Executante Atual | I |  |
| `NUMPS` | NUMPS | I |  |
| `SEQNOTA` | Sequência do Item Nota/Pedido | I |  |
| `NOMEEXEC` | Nome do Exec. | S |  |
| `NOMERPA` | Fase do processo | S |  |
| `IDICOP` | Nro. OP Conjunta | I |  |
| `QTDRPA` | Qtd. na Fase | F |  |
| `PRIORIDADE` | Prioridade | I |  |
| `IDPROC` | Processo | I |  |
| `MULTIPRODUTO` | Multi-produtos | S | Veja opções na seção OPÇÕES |
| `CODPLP` | Planta | I |  |
| `CODPARC` | Parceiro | I |  |
| `IDWFLOW` | Código do Workflow | S |  |
| `CODUSUINC` | Usuário | I |  |
| `IDIPROCPAI` | Nro. OP Principal | I |  |
| `CODGRUPOPRODPA` | Grupo do Produto (PA) | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo STATUSPROC (Tabela: TPRIPROC)
| Valor | Descrição |
|-------|-----------|
| A | Em andamento |
| AP | Aguardando programação |
| C | Cancelado |
| C2 | Cancelando |
| F | Finalizado |
| P | Em programação |
| P2 | Programado |
| R | Criado |
| S | Suspenso |
| S2 | Suspendendo |

### Opções para campo MULTIPRODUTO (Tabela: TPRIPROC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRLMP
### Descrição: ListaMateriaisAtividade

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `SEQMP` | Sequência | I |  |
| `CODPRODPA` | Produto (PA) | I |  |
| `CONTROLEPA` | Controle (PA) | S |  |
| `IDEFX` | Elemento | I |  |
| `CODPRODMP` | Matéria-prima | I |  |
| `TIPOCONTROLEMP` | Tipo de Controle (MP) | S | Veja opções na seção OPÇÕES |
| `CONTROLEMP` | Controle (MP) | S |  |
| `REFERENCIA` | Referência do Produto | S |  |
| `FIXAQTDAPO` | Fixar qtd. apontada da MP ao editar qtd. apontada do PA | S | Veja opções na seção OPÇÕES |
| `TIPOUSOMP` | Tipo de Uso do Material | S | Veja opções na seção OPÇÕES |
| `TIPOQTD` | Tipo de Quantidade | S | Veja opções na seção OPÇÕES |
| `QTDMISTURA` | Quantidade | F |  |
| `CODVOL` | Unidade | S |  |
| `VERIFICAEST` | Verifica Estoque | S | Veja opções na seção OPÇÕES |
| `GERAREQUISICAO` | Gera Requisição | S | Veja opções na seção OPÇÕES |
| `CODLOCALORIG` | Local de Origem | I |  |
| `CODLOCALBAIXA` | Local de Baixa | I |  |
| `PERCDESVIOINF` | % Desvio inferior | F |  |
| `PERCDESVIOSUP` | % Desvio superior | F |  |
| `CONSUREFUGO` | Material consumido por refugo | S | Veja opções na seção OPÇÕES |
| `VINCULOSERIEPA` | Vínculo direto com série do PA | S | Veja opções na seção OPÇÕES |
| `CODUSUALT` | Usuário Última Alteração | I |  |
| `CODUSUCAD` | Usuário Resp. Cadastro | I |  |
| `LIBERADESVIO` | Solicitar liberação ao exceder desvio | S | Veja opções na seção OPÇÕES |
| `ESTOQUETERCEIRO` | Estoque de terceiro | S | Veja opções na seção OPÇÕES |
| `DHALTER` | Data e Hora Alteração | H |  |
| `DHCAD` | Data e Hora Inclusão | H |  |
| `PROPMPFIXA` | Proporcionalizar matéria-prima do tipo Fixa | S | Veja opções na seção OPÇÕES |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOCONTROLEMP (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| H | Herdar do PA |
| I | Automático |
| L | Literal |

### Opções para campo FIXAQTDAPO (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOUSOMP (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| A | Usada em Ajustes |
| N | Usada na Operação Normal |
| R | Reaproveitamento em Desmonte |

### Opções para campo TIPOQTD (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| F | Fixa |
| V | Variável |

### Opções para campo VERIFICAEST (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo GERAREQUISICAO (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONSUREFUGO (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo VINCULOSERIEPA (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo LIBERADESVIO (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ESTOQUETERCEIRO (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROPMPFIXA (Tabela: TPRLMP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRLND
### Descrição: Lane de Diagrama

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDEFX` | IDEFX | I |  |
| `IDRPAPADRAO` | IDRPAPADRAO | I |  |
| `IDEFXPOOL` | IDEFXPOOL | I |  |

## Tabela: TPRLOP
### Descrição: Lançamento de OP

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `NULOP` | NULOP | I |  |
| `DESCRICAO` | DESCRICAO | S |  |
| `DHINC` | DHINC | H |  |
| `CODUSU` | CODUSU | I |  |
| `REUTILIZAR` | REUTILIZAR | S | Veja opções na seção OPÇÕES |
| `NUMPS` | NUMPS | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo REUTILIZAR (Tabela: TPRLOP)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRLPA
### Descrição: Produto Acabado

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDPROC` | Cód. Composição | I |  |
| `VALIDAVERSAO` | VALIDAVERSAO | S | Veja opções na seção OPÇÕES |
| `CODPRODPA` | Produto | I |  |
| `REFERENCIA` | Referência do Produto | S |  |
| `TAMLOTEPAD` | Tamanho de Lote Padrão | F |  |
| `CONTROLEPA` | Controle | S |  |
| `MULTIDEAL` | Múltiplo Ideal | F |  |
| `QTDPRODMIN` | Qtd. Mínima | F |  |
| `TIPOTEMPO` | Tipo de Tempo | S | Veja opções na seção OPÇÕES |
| `TEMPOATRAVESS` | Tempo de Atravessamento | F |  |
| `TEMPOFIXO` | Tempo de Atravessamento (parte fixa) | F |  |
| `UNTEMPOATRAVESS` | Un. Tempo | S | Veja opções na seção OPÇÕES |
| `BASCALCDTVAL` | Base para cálculo da Dt.Validade | S | Veja opções na seção OPÇÕES |
| `TIPOGERASERIE` | Tipo de geração do Nro. de Série | S | Veja opções na seção OPÇÕES |
| `MASCSERIE` | Máscara do Nro. Série | S |  |
| `CODLOCDEST` | Local de Destino | I |  |
| `IDFORMULA` | Fórmula p/ Ajuste Tamanho de Lote | I |  |
| `DHALTER` | Data e Hora Alteração | H |  |
| `DHCAD` | Data e Hora Inclusão | H |  |
| `CODUSUALT` | Usuário Última Alteração | I |  |
| `CODUSUCAD` | Usuário Resp. Cadastro | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo VALIDAVERSAO (Tabela: TPRLPA)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOTEMPO (Tabela: TPRLPA)
| Valor | Descrição |
|-------|-----------|
| L | Por Lote |
| Q | Por Quantidade |

### Opções para campo UNTEMPOATRAVESS (Tabela: TPRLPA)
| Valor | Descrição |
|-------|-----------|
| D | Dias |
| H | Horas |
| M | Minutos |

### Opções para campo BASCALCDTVAL (Tabela: TPRLPA)
| Valor | Descrição |
|-------|-----------|
| F | Data da primeira nota de produção do lote |
| I | Data de inicialização da OP |
| M | Menor Dt.Validade das MPs |
| N | Não calcula |

### Opções para campo TIPOGERASERIE (Tabela: TPRLPA)
| Valor | Descrição |
|-------|-----------|
| A | Automática |
| G | Automático (Série Global) |
| L | Manual (lançamento) |
| P | Manual (apontamento) |


## Tabela: TPRMER
### Descrição: Registro das movientações entre repositórios de PA

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDMER` | Código | I |  |
| `SEQMER` | Sequência | I |  |
| `IDRPA` | Repositório | I |  |
| `IDIPROC` | Instância de Processo | I |  |
| `IDIATV` | Instância de Atividade | I |  |
| `CODPRODPA` | Produto (PA) | I |  |
| `CONTROLEPA` | Controle (PA) | S |  |
| `QTD` | Qtd. movimentada | F |  |
| `QTDPERDA` | Qtd. Perdida | F |  |
| `SINAL` | Sinal da Operação | I | Veja opções na seção OPÇÕES |
| `DHMOV` | Dh. Movimentação | H |  |
| `STATUSEXEC` | Status | S |  |
| `CODCPM` | Componente de Manufatura | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo SINAL (Tabela: TPRMER)
| Valor | Descrição |
|-------|-----------|
| -1 | Saída |
| 1 | Entrada |


## Tabela: TPRMPE
### Descrição: TABLE TPRMPE

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODMPE` | Código | I |  |
| `DESCRICAO` | Descrição | S |  |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `MOTIVOPERDA` | Motivo de perda | S | Veja opções na seção OPÇÕES |
| `AD_CODEST` | Cód. Estoque | I |  |
| `AD_CODNCF` | Cód Ncf | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo ATIVO (Tabela: TPRMPE)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MOTIVOPERDA (Tabela: TPRMPE)
| Valor | Descrição |
|-------|-----------|
| R | Descarte |
| S | Subprodutos/Refugos |


## Tabela: TPRMPEAPA
### Descrição: Motivo de Perda de Apontamento de PA

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODMPEAPA` | Cód. Detalhamento Perda | I |  |
| `NUAPO` | Nro. Único | I |  |
| `SEQAPA` | Sequência | I |  |
| `CODMPE` | Motivo de Perda | I |  |
| `QTDPERDA` | Qtd. Perda | F |  |

## Tabela: TPROEST
### Descrição: Operações com Estoque

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDEFX` | Código | I |  |
| `SEQOPER` | Código | I |  |
| `ORDEM` | Ordem | I |  |
| `DESCRICAO` | Descrição da Operação | S |  |
| `TIPOOPER` | Tipo de Execução da Operação | S | Veja opções na seção OPÇÕES |
| `TIPOPRODUCAO` | Tipo de Produção | S | Veja opções na seção OPÇÕES |
| `OBRIGATORIO` | Obrigatória | S | Veja opções na seção OPÇÕES |
| `QUANDO` | Quando | S | Veja opções na seção OPÇÕES |
| `NUNOTAMODELO` | Modelo de Nota | I |  |
| `IDEFXBASE` | Atividade Base | I |  |
| `CODPARC` | Parceiro | I |  |
| `CODCENCUS` | Centro de Resultado | I |  |
| `CODPROJ` | Projeto | I |  |
| `CODNAT` | Natureza | I |  |
| `CODTIPVENDA` | Tipo de Negociação | I |  |
| `CODTIPOPER` | Tipo de Operação | I |  |
| `CODTIPOPERPERDA` | Tipo de Operação para Perda | I |  |
| `UTILIZALOCALORIG` | Sempre utilizar Local de Origem da Operação | S | Veja opções na seção OPÇÕES |
| `CODLOCALORIG` | Local de Origem | I |  |
| `CODLOCALDEST` | Local de Destino | I |  |
| `CODLOCALDESTPERDA` | Local de Destino para Perda | I |  |
| `CODLOCALBAIXAMP` | Local para baixa de MPs | I |  |
| `CODEMPORIG` | Empresa de Origem | I |  |
| `TIPOITENS` | Tipo dos Itens | S | Veja opções na seção OPÇÕES |
| `CODEMPDEST` | Empresa de Destino | I |  |
| `TIPOMATERIAL` | Tipo Material | S | Veja opções na seção OPÇÕES |
| `SELIMPRESSORA` | Selecionar Impressora | S | Veja opções na seção OPÇÕES |
| `CONSUMIRESTOQUE` | Quantidade de PI | S | Veja opções na seção OPÇÕES |
| `NOMEIMPRESSORA` | Impressora | S |  |
| `STATUSEXEC` | Status da Execução | S | Veja opções na seção OPÇÕES |
| `IDFORM` | Formulário | I |  |
| `CONFIRMAR` | Confirmar Operação | S | Veja opções na seção OPÇÕES |
| `BAIXARESERVAEST` | Baixar reserva na nota de produção | S | Veja opções na seção OPÇÕES |
| `TIPOEXEC` | Execução da Atividade | S | Veja opções na seção OPÇÕES |
| `USARPARCTERC` | Usar o Parceiro Terceiro da OP | S | Veja opções na seção OPÇÕES |
| `USARPARCTERCENCAD` | Usar o Parceiro Terceiro da OP (Encad) | S | Veja opções na seção OPÇÕES |
| `ANULAOPEREST` | Anular operação ao cancelar OP | S | Veja opções na seção OPÇÕES |
| `TIPOOPERENCAD` | Tipo de Execução | S | Veja opções na seção OPÇÕES |
| `OBRIGENCAD` | Obrigatória | S | Veja opções na seção OPÇÕES |
| `CONFIRMENCAD` | Confirmar Operação | S | Veja opções na seção OPÇÕES |
| `NUMODELOENCAD` | Modelo de Nota | I |  |
| `CODTIPOPERENCAD` | Tipo de Operação | I |  |
| `CODPARCENCAD` | Parceiro | I |  |
| `CODEMPDESTENCAD` | Empresa de Destino | I |  |
| `CODLOCALDESTENCAD` | Local de Destino | I |  |
| `KANBAN` | Utilizar Kanban | S | Veja opções na seção OPÇÕES |
| `NUNOTAMODELOKANBAN` | Modelo de Nota (Pedido de Requisição) | I |  |
| `CODTIPOPERKANBAN` | Tipo de Operação (Pedido de Requisição) | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOOPER (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| A | Automática |
| M | Manual |
| T | Ambas |

### Opções para campo TIPOPRODUCAO (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| A | Ambas |
| E | Para estoque próprio |
| T | Para terceiros |

### Opções para campo OBRIGATORIO (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo QUANDO (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| AC | Aceite da atividade |
| AJ | Ao apontar materiais de ajustes |
| EN | Entrada |
| IN | Quando o usuário iniciar a atividade |
| PA | Ao apontar PA |
| PF | Ao preencher um formulário |
| SA | Saída |

### Opções para campo UTILIZALOCALORIG (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOITENS (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| MA | Materiais de ajuste |
| MB | Lista de materiais da atividade base |
| MT | Lista de materiais de todas as atividades |
| PA | Produto acabado apontado na atividade |
| SP | Subproduto da Atividade |

### Opções para campo TIPOMATERIAL (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| AB | Ambos |
| MP | Somente MPs |
| PI | Somente PIs |

### Opções para campo SELIMPRESSORA (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| E | Específica |
| T | Conforme a TOP |
| W | Usar impressora padrão do Centro de Trabalho |

### Opções para campo CONSUMIRESTOQUE (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| CE | Consumida do estoque |
| FS | Fabricada em sub-ordem |
| T | Total |

### Opções para campo STATUSEXEC (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Normal |
| R | Reprocesso |
| T | Todos |

### Opções para campo CONFIRMAR (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo BAIXARESERVAEST (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOEXEC (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| E | Terceiros |
| P | Própria |
| T | Todos |

### Opções para campo USARPARCTERC (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USARPARCTERCENCAD (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ANULAOPEREST (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOOPERENCAD (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| A | Automática |
| M | Manual |

### Opções para campo OBRIGENCAD (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo CONFIRMENCAD (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo KANBAN (Tabela: TPROEST)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRPLP
### Descrição: Planta de manufatura

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `CODPLP` | Cód. Planta | I |  |
| `NOME` | Nome | S |  |
| `CODEMP` | Empresa | I |  |
| `CODCARGAHOR` | Carga Horária Padrão | I |  |
| `CODCENCUS` | Centro de Resultado | I |  |

## Tabela: TPRPRC
### Descrição: Metainformações sobre um processo produtivo.

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDPROC` | Número Único | I |  |
| `VALIDAVERSAO` | VALIDAVERSAO | S | Veja opções na seção OPÇÕES |
| `CODPRC` | Código | I |  |
| `TIPOPROC` | Tipo de Processo | S | Veja opções na seção OPÇÕES |
| `DESCRLONGA` | Descrição Completa | S |  |
| `DESCRABREV` | Descrição | S |  |
| `IDRPAINICIAL` | Repositório Inicial | I |  |
| `VERSAOANT` | Versão Anterior | I |  |
| `VERSAO` | Versão | I |  |
| `CODPLP` | Planta de Manufatura | I |  |
| `CODLOCALALMOXARIFE` | Local de Almoxarifado | I |  |
| `CODLOCALMANUFATURA` | Local de Manufatura | I |  |
| `MULTIPA` | Aceita Múltiplos PAs | S | Veja opções na seção OPÇÕES |
| `MULTICONTROLE` | Aceita Múltiplos Controles de PA | S | Veja opções na seção OPÇÕES |
| `TIPOINICIA` | Tipo de inicialização | S | Veja opções na seção OPÇÕES |
| `DHCAD` | Data e Hora Inclusão | H |  |
| `DHALTER` | Data e Hora Alteração | H |  |
| `CODUSUCAD` | Usuário Resp. Cadastro | I |  |
| `CODUSUALT` | Usuário Última Alteração | I |  |
| `XMLBPMN` | XMLBPMN | C |  |
| `XMLBPMNUI` | XMLBPMNUI | C |  |
| `IDWFLOW` | IDWFLOW | S |  |
| `TIPONROLOTE` | Tipo do Nro. Lote | S | Veja opções na seção OPÇÕES |
| `ATIVO` | Ativo | S | Veja opções na seção OPÇÕES |
| `MASCNROLOTE` | Máscara Nro. Lote | S |  |
| `PRODPARATERCEIRO` | Produção para Terceiro | S | Veja opções na seção OPÇÕES |
| `PROCDESMONTE` | Desmonte | S | Veja opções na seção OPÇÕES |
| `PROCREPARO` | Reprocessamento/reparo | S | Veja opções na seção OPÇÕES |
| `CODPRCPRODUCAO` | Processo de Produção Relacionado | I |  |
| `TIPOFRAGNROLOTE` | Reiniciar numeração | S | Veja opções na seção OPÇÕES |
| `USATERCEIRO` | Produção terceirizada | S | Veja opções na seção OPÇÕES |
| `DEFTERCEIRO` | Definição de Terceiro | S | Veja opções na seção OPÇÕES |
| `PADRAO` | Padrão | S | Veja opções na seção OPÇÕES |
| `EXIGEPEDIDO` | Exige pedido de venda | S | Veja opções na seção OPÇÕES |
| `LOTECURINGA` | Lote Curinga | S |  |
| `PERCDESVIOINF` | % Desvio Inferior | F |  |
| `LIBERADESVIO` | Solicitar liberação ao exceder desvio | S | Veja opções na seção OPÇÕES |
| `PERCDESVIOSUP` | % Desvio Superior | F |  |
| `USALOTECURINGA` | Usa Lote Curinga | S | Veja opções na seção OPÇÕES |
| `IDFORMULA` | Fórmula p/ Ajuste Tamanho de Lote | I |  |
| `USACONFNROLOTESP` | Utilizar essa configuração para Subproduto | S | Veja opções na seção OPÇÕES |
| `ROTEIROHTML5` | Editado em HTML5 | S | Veja opções na seção OPÇÕES |
| `TIPONROLOTESP` | Tipo do Nro. Lote | S | Veja opções na seção OPÇÕES |
| `MASCNROLOTESP` | Máscara Nro. Lote | S |  |
| `TIPOFRAGNROLOTESP` | Reiniciar numeração | S | Veja opções na seção OPÇÕES |
| `TIPEXECATV` | Tipo de Execução das Atividades | S | Veja opções na seção OPÇÕES |
| `PEREDICAO` | Período permitido para realizar a edição | S | Veja opções na seção OPÇÕES |
| `PADRAOPRODUTO` | Padrão por Produto | S | Veja opções na seção OPÇÕES |
| `QTDDIAS` | Qtd. Dias | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo VALIDAVERSAO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOPROC (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| M | Processo mestre |
| S | Sub-Processo |

### Opções para campo MULTIPA (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo MULTICONTROLE (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOINICIA (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| C | Após confirmação |
| I | Imediato |

### Opções para campo TIPONROLOTE (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| AE | Automático (por Empresa) |
| AG | Automático (Global) |
| AP | Automático (por Produto) |
| AX | Automático (por Empresa + Produto) |
| MN | Manual |

### Opções para campo ATIVO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PRODPARATERCEIRO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Nunca |
| O | Opcional |
| S | Sempre |

### Opções para campo PROCDESMONTE (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PROCREPARO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPOFRAGNROLOTE (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| A | Anualmente |
| D | Diariamente |
| M | Mensalmente |
| N | Não reiniciar |

### Opções para campo USATERCEIRO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Nunca |
| O | Opcional |
| S | Sempre |

### Opções para campo DEFTERCEIRO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| A | Por Operação |
| O | Por OP |

### Opções para campo PADRAO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo EXIGEPEDIDO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Nunca |
| O | Opcional |
| S | Sempre |

### Opções para campo LIBERADESVIO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USALOTECURINGA (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo USACONFNROLOTESP (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo ROTEIROHTML5 (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo TIPONROLOTESP (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| AE | Automático (por Empresa) |
| AG | Automático (Global) |
| AP | Automático (por Produto) |
| AX | Automático (por Empresa + Produto) |
| MN | Manual |

### Opções para campo TIPOFRAGNROLOTESP (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| A | Anualmente |
| M | Mensalmente |
| N | Não reiniciar |

### Opções para campo TIPEXECATV (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| A | Automático sem edição |
| E | Automático com edição |
| M | Manual |

### Opções para campo PEREDICAO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| L | Livre |
| M | Mês |
| Q | Quinzena |
| S | Semana |

### Opções para campo PADRAOPRODUTO (Tabela: TPRPRC)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |


## Tabela: TPRROPE
### Descrição: Registro de operações com estoque

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDIATV` | Instância da Atividade | I |  |
| `SEQROPE` | Sequência | I |  |
| `IDEFX` | Elemento | I |  |
| `SEQOPER` | Seq. Conf. Operação | I |  |
| `CODPRODPA` | Cód. Produto | I |  |
| `CONTROLEPA` | Controle | S |  |
| `QTDBASE` | Qtd. base | F |  |
| `STATUSEXEC` | Status | S |  |
| `NUNOTA` | Nro. Nota | I |  |
| `NUAPO` | Nro. Apontamento | I |  |
| `TIPOOPER` | Tipo de Execução da Operação | S | Veja opções na seção OPÇÕES |
| `CODUSU` | Usuário | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo TIPOOPER (Tabela: TPRROPE)
| Valor | Descrição |
|-------|-----------|
| A | Automática |
| M | Manual |
| T | Ambas |


## Tabela: TPRRPA
### Descrição: Repositorio de PA

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDRPA` | Cód. Repositório | I |  |
| `DESCRICAO` | Descrição | S |  |

## Tabela: TPRTFX
### Descrição: Transição do fluxo

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `IDEFX` | Código | I |  |
| `IDEFXORIG` | Elemento de Origem | I |  |
| `IDEFXDEST` | Elemento de Destino | I |  |
| `PRIORITARIO` | Prioritário | S | Veja opções na seção OPÇÕES |
| `EXPCONDICAO` | Expressão | S |  |
| `PADRAO` | Padrão | S | Veja opções na seção OPÇÕES |
| `DEFSTATUSEXEC` | Status da Execução | S | Veja opções na seção OPÇÕES |
| `ORDEMAVAL` | Ordem | I |  |

## OPÇÕES DE CAMPOS

### Opções para campo PRIORITARIO (Tabela: TPRTFX)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo PADRAO (Tabela: TPRTFX)
| Valor | Descrição |
|-------|-----------|
| N | Não |
| S | Sim |

### Opções para campo DEFSTATUSEXEC (Tabela: TPRTFX)
| Valor | Descrição |
|-------|-----------|
| A | Mantém o status atual |
| N | Normal |
| R | Reprocesso |


## Tabela: TSIMAP
### Descrição: Api Monitor

| Campo | Descrição | Tipo | Observações |
|-------|-----------|------|-------------|
| `HASH` | Hash | S |  |
| `CODUSU` | Cód. Usuário | I |  |
| `DATA` | Data | D |  |
| `PRIMEIROLOGIN` | Primeiro Login | H |  |
| `ULTIMOLOGIN` | Ultimo Login | H |  |
| `QTDLOGIN` | Qtd. Login | I |  |
| `IP` | Endereço IP | S |  |
| `ORIGEM` | Origem | S | Veja opções na seção OPÇÕES |
| `IDENTIFICADOR` | Identificador | S |  |
| `USERAGENT` | UserAgent | S |  |

## OPÇÕES DE CAMPOS

### Opções para campo ORIGEM (Tabela: TSIMAP)
| Valor | Descrição |
|-------|-----------|
| A | App |
| D | API Direta |
| G | API Gateway |
| S | App Sankhya |



## Relacionamentos entre campos

| Tabela Origem | Campo Origem | Tabela Destino | Campo Destino |
|---|---|---|---|
| `TCBCTR` | `CODCTAREF` | `TCBPLR` | `CODCTAREF` |
| `TCBCTR` | `TIPO` | `TCBPLR` | `TIPO` |
| `TCBECB` | `BLOCO` | `TCBECR` | `BLOCO` |
| `TCBECB` | `CODEMP` | `TCBECR` | `CODEMP` |
| `TCBEFB` | `CODEMP` | `TCBEFR` | `CODEMP` |
| `TCBEFB` | `BLOCO` | `TCBEFR` | `BLOCO` |
| `TCBHLT` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TCBINT` | `REFERENCIA` | `TCBLAN` | `REFERENCIA` |
| `TCBINT` | `NUMLANC` | `TCBLAN` | `NUMLANC` |
| `TCBINT` | `TIPLANC` | `TCBLAN` | `TIPLANC` |
| `TCBINT` | `NUMLOTE` | `TCBLAN` | `NUMLOTE` |
| `TCBINT` | `CODEMP` | `TCBLAN` | `CODEMP` |
| `TCBLAN` | `CODHISTCTB` | `TCBHIS` | `CODHISTCTB` |
| `TCBLAN` | `NUMLOTE` | `TCBINT` | `NUMLOTE` |
| `TCBLAN` | `REFERENCIA` | `TCBINT` | `REFERENCIA` |
| `TCBLAN` | `TIPLANC` | `TCBINT` | `TIPLANC` |
| `TCBLAN` | `CODEMP` | `TCBINT` | `CODEMP` |
| `TCBLAN` | `NUMLANC` | `TCBINT` | `NUMLANC` |
| `TCBLAN` | `REFERENCIA` | `TCBLOT` | `REFERENCIA` |
| `TCBLAN` | `CODEMP` | `TCBLOT` | `CODEMP` |
| `TCBLAN` | `NUMLOTE` | `TCBLOT` | `NUMLOTE` |
| `TCBLAN` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TCBLAN` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TCBLAN` | `CODEMPORIG` | `TSIEMP` | `CODEMP` |
| `TCBLAN` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TCBLOT` | `NUMLOTE` | `TCBLAN` | `NUMLOTE` |
| `TCBLOT` | `CODEMP` | `TCBLAN` | `CODEMP` |
| `TCBLOT` | `REFERENCIA` | `TCBLAN` | `REFERENCIA` |
| `TCBLOT` | `CODEMPCONSOLID` | `TSIEMP` | `CODEMP` |
| `TCBLOT` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TCBPCT` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TCBPLA` | `CODCTACTB` | `TCBCTR` | `CODCTACTB` |
| `TCBPLA` | `LALUR_A` | `TCBDIN` | `CODIGO` |
| `TCBPLA` | `TABELALALURB` | `TCBDIN` | `TABELA` |
| `TCBPLA` | `TABELACRED` | `TCBDIN` | `TABELA` |
| `TCBPLA` | `LALUR_A_CRED` | `TCBDIN` | `CODIGO` |
| `TCBPLA` | `CODLALURB` | `TCBDIN` | `CODIGO` |
| `TCBPLA` | `TABELA` | `TCBDIN` | `TABELA` |
| `TCBPLA` | `CODCTACTBSUBST` | `TCBPLA` | `CODCTACTB` |
| `TCBPLA` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TCBPLA_IMP` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TCBPLA_IMP` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TCBPLR` | `TABELA` | `TCBDPLR` | `TABELA` |
| `TCBPLR` | `TIPO` | `TCBDPLR` | `TIPO` |
| `TCBSAL` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TCBVCED` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TCBVCED` | `CTACTBEXTIMP` | `TCBPLA_IMP` | `CTACTB` |
| `TCBVCED` | `CODEMP` | `TCBPLA_IMP` | `CODEMP` |
| `TGFACF` | `NUFIN` | `TGFFIN` | `NUFIN` |
| `TGFACT` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFACT` | `NUNOTA` | `TGFITE` | `NUNOTA` |
| `TGFACT` | `SEQUENCIA` | `TGFITE` | `SEQUENCIA` |
| `TGFACT` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFAID` | `CODUF` | `TSIUFS` | `CODUF` |
| `TGFAJA` | `CODOBSPADRAO` | `TGFOBS` | `CODOBSPADRAO` |
| `TGFAJA` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFAJA` | `CODUF` | `TSIUFS` | `CODUF` |
| `TGFAJA` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFASN` | `NUANEXO` | `TGFFSN` | `NUANEXO` |
| `TGFBAR` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TGFCAB` | `NUNOTA` | `TGFACT` | `NUNOTA` |
| `TGFCAB` | `NUNOTASUB` | `TGFCAB` | `NUNOTA` |
| `TGFCAB` | `NUNOTA` | `TGFCCM` | `NUNOTA` |
| `TGFCAB` | `NUNOTA` | `TGFCOM` | `NUNOTAORIG` |
| `TGFCAB` | `CODCONTATOENTREGA` | `TGFCTT` | `CODCONTATO` |
| `TGFCAB` | `CODPARC` | `TGFCTT` | `CODPARC` |
| `TGFCAB` | `CODCONTATO` | `TGFCTT` | `CODCONTATO` |
| `TGFCAB` | `NUNOTA` | `TGFFIN` | `NUNOTA` |
| `TGFCAB` | `NUNOTA` | `TGFITE` | `NUNOTA` |
| `TGFCAB` | `NULOTENFE` | `TGFLNF` | `NULOTE` |
| `TGFCAB` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TGFCAB` | `NUNOTA` | `TGFNCE` | `NUNOTA` |
| `TGFCAB` | `NUNOTA` | `TGFNCT` | `NUNOTA` |
| `TGFCAB` | `NUNOTA` | `TGFNCTE` | `NUNOTA` |
| `TGFCAB` | `NUNOTA` | `TGFNFE` | `NUNOTA` |
| `TGFCAB` | `CODOBSPADRAO` | `TGFOBS` | `CODOBSPADRAO` |
| `TGFCAB` | `ORDEMCARGA` | `TGFORD` | `ORDEMCARGA` |
| `TGFCAB` | `CODEMP` | `TGFORD` | `CODEMP` |
| `TGFCAB` | `CODPARCRETIRADA` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODPARCCONSIGNATARIO` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODMOTORISTA` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODPARCREMETENTE` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODPARCDEST` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODPARCREDESPACHO` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODINTERM` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODPARCTRANSP` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODPARCTRANSPFINAL` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `CODPARCDESCARGAMDFE` | `TGFPAR` | `CODPARC` |
| `TGFCAB` | `DHTIPOPER` | `TGFTOP` | `DHALTER` |
| `TGFCAB` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFCAB` | `DHTIPVENDA` | `TGFTPV` | `DHALTER` |
| `TGFCAB` | `CODTIPVENDA` | `TGFTPV` | `CODTIPVENDA` |
| `TGFCAB` | `NUNOTA` | `TGFUNM` | `NUNOTA` |
| `TGFCAB` | `NUNOTA` | `TGFVALP` | `NUNOTA` |
| `TGFCAB` | `REBOQUE1` | `TGFVEI` | `CODVEICULO` |
| `TGFCAB` | `REBOQUE3` | `TGFVEI` | `CODVEICULO` |
| `TGFCAB` | `REBOQUE2` | `TGFVEI` | `CODVEICULO` |
| `TGFCAB` | `CODVEICULO` | `TGFVEI` | `CODVEICULO` |
| `TGFCAB` | `CODVENDTEC` | `TGFVEN` | `CODVEND` |
| `TGFCAB` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TGFCAB` | `CODCIDPREST` | `TSICID` | `CODCID` |
| `TGFCAB` | `CODCIDFIMCTE` | `TSICID` | `CODCID` |
| `TGFCAB` | `CODCIDINICTE` | `TSICID` | `CODCID` |
| `TGFCAB` | `CODCID` | `TSICID` | `CODCID` |
| `TGFCAB` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFCAB` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFCAB` | `CODEMPFUNC` | `TSIEMP` | `CODEMP` |
| `TGFCAB` | `CODEMPNEGOC` | `TSIEMP` | `CODEMP` |
| `TGFCAB` | `UFEMISS` | `TSIUFS` | `CODUF` |
| `TGFCAB` | `UFVEICULO` | `TSIUFS` | `CODUF` |
| `TGFCAB` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFCAB` | `AD_VENDSEC` | `TSIUSU` | `CODUSU` |
| `TGFCAB` | `CODUSUINC` | `TSIUSU` | `CODUSU` |
| `TGFCAB_EXC` | `DHEXCLUSAO` | `TGFITE_EXC` | `DHEXCLUSAO` |
| `TGFCAB_EXC` | `NUNOTA` | `TGFITE_EXC` | `NUNOTA` |
| `TGFCAB_EXC` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFCAB_EXC` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFCAB_EXC` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFCAN` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFCAN` | `NUNOTA` | `TGFCAB_EXC` | `NUNOTA` |
| `TGFCAN` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFCAN` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFCCM` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TGFCER` | `CODREGRA` | `TGFREG` | `CODREGRA` |
| `TGFCFO` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TGFCNF` | `NUCONTING` | `TGFICNF` | `NUCONTING` |
| `TGFCNF` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFCOM` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TGFCONTR` | `CODPARCCONTR` | `TGFPAR` | `CODPARC` |
| `TGFCPL` | `CODTABCOT` | `TGFNTA` | `CODTAB` |
| `TGFCPL` | `CODPARCTRANSP` | `TGFPAR` | `CODPARC` |
| `TGFCPL` | `SUGTIPNEGENTR` | `TGFTPV` | `CODTIPVENDA` |
| `TGFCPL` | `SUGTIPNEGSAID` | `TGFTPV` | `CODTIPVENDA` |
| `TGFCPL` | `CODBAIENTREGA` | `TSIBAI` | `CODBAI` |
| `TGFCPL` | `CODBAITRAB` | `TSIBAI` | `CODBAI` |
| `TGFCPL` | `CODBAIRECEB` | `TSIBAI` | `CODBAI` |
| `TGFCPL` | `CODCIDRECEB` | `TSICID` | `CODCID` |
| `TGFCPL` | `NATURALIDADE` | `TSICID` | `CODCID` |
| `TGFCPL` | `CODCIDTRAB` | `TSICID` | `CODCID` |
| `TGFCPL` | `CODCIDENTREGA` | `TSICID` | `CODCID` |
| `TGFCPL` | `CODENDENTREGA` | `TSIEND` | `CODEND` |
| `TGFCPL` | `CODENDTRAB` | `TSIEND` | `CODEND` |
| `TGFCPL` | `CODENDRECEB` | `TSIEND` | `CODEND` |
| `TGFCPL` | `NACIONALIDADE` | `TSIPAI` | `CODPAIS` |
| `TGFCTB` | `CODHISTCTB` | `TCBHIS` | `CODHISTCTB` |
| `TGFCTB` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFCTB` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFCTE` | `CODLOCAL` | `TGFLOC` | `CODLOCAL` |
| `TGFCTE` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFCTE` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFCTE` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TGFCTE` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFCTENT` | `CODEMP` | `TGFEMP` | `CODEMP` |
| `TGFCTT` | `TIMPROCURADOR` | `TGFPAR` | `CODPARC` |
| `TGFCTT` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFCTT` | `CODCONTATO` | `TGFPPA` | `CODCONTATO` |
| `TGFCTT` | `CODPARC` | `TGFPPA` | `CODPARC` |
| `TGFCTT` | `CODBAI` | `TSIBAI` | `CODBAI` |
| `TGFCTT` | `TIMBANCO` | `TSIBCO` | `CODBCO` |
| `TGFCTT` | `CODCID` | `TSICID` | `CODCID` |
| `TGFCTT` | `CODEND` | `TSIEND` | `CODEND` |
| `TGFCTT` | `TIMNACIONALIDAD` | `TSIPAI` | `CODPAIS` |
| `TGFCTT` | `CODREG` | `TSIREG` | `CODREG` |
| `TGFCTT` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFCUS` | `CODLOCAL` | `TGFLOC` | `CODLOCAL` |
| `TGFCUS` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFCUS` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFCUSITE` | `SEQUENCIA` | `TGFITE` | `SEQUENCIA` |
| `TGFCUSITE` | `NUNOTA` | `TGFITE` | `NUNOTA` |
| `TGFCUSITE` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFDES` | `NUPROMOCAO` | `TGFDPQ` | `NUPROMOCAO` |
| `TGFDES` | `CODLOCAL` | `TGFLOC` | `CODLOCAL` |
| `TGFDES` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFDES` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFDES` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFDES` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TGFDES` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TGFDES` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFDIN` | `CODNATREND` | `TGFNRR` | `CODNATREND` |
| `TGFDIN` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFEBOL` | `NUFIN` | `TGFFIN` | `NUFIN` |
| `TGFEFB` | `BLOCO` | `TGFEFR` | `BLOCO` |
| `TGFEFB` | `CODEMP` | `TGFEFR` | `CODEMP` |
| `TGFEFDVMRSTDIA` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFEFDVMRSTDIA` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFEMDF` | `NUVIAG` | `TGFMDFE` | `NUVIAG` |
| `TGFEMDF` | `SEQMDFE` | `TGFMDFE` | `SEQMDFE` |
| `TGFEMDF` | `CODMOTORISTA` | `TGFPAR` | `CODPARC` |
| `TGFEMDF` | `CODCIDEVE` | `TSICID` | `CODCID` |
| `TGFEMDF` | `UFEVE` | `TSIUFS` | `CODUF` |
| `TGFEMDF` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFEMP` | `CODCTACTB_2` | `TCBPLA` | `CODCTACTB` |
| `TGFEMP` | `CODCTACTBMULT` | `TCBPLA` | `CODCTACTB` |
| `TGFEMP` | `CODCTACTB_1` | `TCBPLA` | `CODCTACTB` |
| `TGFEMP` | `CODCTACTBBONIF` | `TCBPLA` | `CODCTACTB` |
| `TGFEMP` | `CODCTACTBDESC` | `TCBPLA` | `CODCTACTB` |
| `TGFEMP` | `CODCTACTBJUROS` | `TCBPLA` | `CODCTACTB` |
| `TGFEMP` | `CODCTACTB_3` | `TCBPLA` | `CODCTACTB` |
| `TGFEMP` | `NOTAENTAJUSTESTCTER` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTAENTAJUSTEST` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTASAIAJUSTEST` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTAMODELODAGENDA` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTAENTAJUSTESTDTER` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTASAIPERDAWMS` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTASAIAJUSTESTCONS` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTASAIAJUSTESTCTER` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTASAIAJUSTBEM` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTAENTAJUSTERECLAS` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTASAIAJUSTERECLAS` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTASAIAJUSTESTDTER` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTAENTSOBRAWMS` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `MODESTCPAWMS` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `CODMODRETESTWMS` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `NOTAENTAJUSTESTCONS` | `TGFCAB` | `NUNOTA` |
| `TGFEMP` | `CODEMP` | `TGFCTENT` | `CODEMP` |
| `TGFEMP` | `CODEMP` | `TGFEFB` | `CODEMP` |
| `TGFEMP` | `CODEMP` | `TGFEFR` | `CODEMP` |
| `TGFEMP` | `CODEMP` | `TGFEPS` | `CODEMP` |
| `TGFEMP` | `CODLANCBCOREC` | `TGFHBC` | `CODLANC` |
| `TGFEMP` | `CODLANCBCOPAG` | `TGFHBC` | `CODLANC` |
| `TGFEMP` | `LOCALPAD` | `TGFLOC` | `CODLOCAL` |
| `TGFEMP` | `CODLOCALTERC` | `TGFLOC` | `CODLOCAL` |
| `TGFEMP` | `LOCALPADECONECT` | `TGFLOC` | `CODLOCAL` |
| `TGFEMP` | `WMSLOCALAJEST` | `TGFLOC` | `CODLOCAL` |
| `TGFEMP` | `CODEMP` | `TGFMIX` | `CODEMP` |
| `TGFEMP` | `MODEXPED` | `TGFMON` | `CODMODNF` |
| `TGFEMP` | `MODDUPL` | `TGFMON` | `CODMODNF` |
| `TGFEMP` | `CODMODNFCECOMPL` | `TGFMON` | `CODMODNF` |
| `TGFEMP` | `CODMODDANFECONTINGENCIA` | `TGFMON` | `CODMODNF` |
| `TGFEMP` | `CODMODNFCESIMPL` | `TGFMON` | `CODMODNF` |
| `TGFEMP` | `CODMODDANFE` | `TGFMON` | `CODMODNF` |
| `TGFEMP` | `CODMODDACTE` | `TGFMON` | `CODMODNF` |
| `TGFEMP` | `CODNATIPI` | `TGFNAT` | `CODNAT` |
| `TGFEMP` | `EFDCODNATDESPRECICMS` | `TGFNAT` | `CODNAT` |
| `TGFEMP` | `NATCANPIX` | `TGFNAT` | `CODNAT` |
| `TGFEMP` | `CODEMP` | `TGFNFENT` | `CODEMP` |
| `TGFEMP` | `CODTABCKC` | `TGFNTA` | `CODTAB` |
| `TGFEMP` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFEMP` | `CODTABALT` | `TGFNTA` | `CODTAB` |
| `TGFEMP` | `CODTABCALC` | `TGFNTA` | `CODTAB` |
| `TGFEMP` | `CODEMP` | `TGFNUM` | `CODEMP` |
| `TGFEMP` | `CODPARCCTB` | `TGFPAR` | `CODPARC` |
| `TGFEMP` | `CODPARCIPI` | `TGFPAR` | `CODPARC` |
| `TGFEMP` | `RESPENTREINF` | `TGFPAR` | `CODPARC` |
| `TGFEMP` | `CODPARCNFCE` | `TGFPAR` | `CODPARC` |
| `TGFEMP` | `CODTAB` | `TGFTAB` | `CODTAB` |
| `TGFEMP` | `CODTIPTITIPI` | `TGFTIT` | `CODTIPTIT` |
| `TGFEMP` | `EFDCODTIPTIT` | `TGFTIT` | `CODTIPTIT` |
| `TGFEMP` | `TOPDEVOLUCAOWMS` | `TGFTOP` | `CODTIPOPER` |
| `TGFEMP` | `TOPSAIDADIFPESOWMS` | `TGFTOP` | `CODTIPOPER` |
| `TGFEMP` | `TOPENTRADAWMS` | `TGFTOP` | `CODTIPOPER` |
| `TGFEMP` | `TOPENTDIFPESOWMS` | `TGFTOP` | `CODTIPOPER` |
| `TGFEMP` | `CODTIPOPERIPI` | `TGFTOP` | `CODTIPOPER` |
| `TGFEMP` | `TOPENVWMSAGRUP` | `TGFTOP` | `CODTIPOPER` |
| `TGFEMP` | `EFDCODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFEMP` | `TOPCANPIXREC` | `TGFTOP` | `CODTIPOPER` |
| `TGFEMP` | `CODTIPPARC` | `TGFTPP` | `CODTIPPARC` |
| `TGFEMP` | `EFDCODBCO` | `TSIBCO` | `CODBCO` |
| `TGFEMP` | `CODBCOIPI` | `TSIBCO` | `CODBCO` |
| `TGFEMP` | `CODCTABCOIPI` | `TSICTA` | `CODCTABCOINT` |
| `TGFEMP` | `CODCTAPIXTEF` | `TSICTA` | `CODCTABCOINT` |
| `TGFEMP` | `CODCENCUSIPI` | `TSICUS` | `CODCENCUS` |
| `TGFEMP` | `EFDCODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFEMP` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFEMP` | `CODCENCUSDESP` | `TSICUS` | `CODCENCUS` |
| `TGFEMP` | `CODEMPMATRIZGNRE` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `CODEMPIMPOSTO` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `CODEMPORIGMOVFIN` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `CODEMPMATRIZNFSE` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `CODEMPOC` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `CODEMPMATRIZEFD` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `EMPDESTINOWMS` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `CODEMPGRUPFRETE` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `EMPSOMA` | `TSIEMP` | `CODEMP` |
| `TGFEMP` | `NURFECARTACORR` | `TSIRFE` | `NURFE` |
| `TGFEMP` | `CODMODDANFESIMPLIFNFE` | `TSIRFE` | `NURFE` |
| `TGFEMP` | `NURFEPRODUCAO` | `TSIRFE` | `NURFE` |
| `TGFEMP` | `NURFECARTACORRCTE` | `TSIRFE` | `NURFE` |
| `TGFEMP` | `NURFE` | `TSIRFE` | `NURFE` |
| `TGFEMP` | `MODETQVOL` | `TSIRFE` | `NURFE` |
| `TGFEMP` | `CODRELMINUTAODP` | `TSIRFE` | `NURFE` |
| `TGFEMP` | `CODSMTP` | `TSISMTP` | `CODSMTP` |
| `TGFENA` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TGFENA` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TGFENA` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFENFE` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFESE` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFEST` | `CODEMP` | `TGFEMP` | `CODEMP` |
| `TGFEST` | `CODLOCAL` | `TGFLOC` | `CODLOCAL` |
| `TGFEST` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFEST` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFEST` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFEXB` | `NROCTA` | `TSICTA` | `CODCTABCO` |
| `TGFEXC` | `CODLOCAL` | `TGFLOC` | `CODLOCAL` |
| `TGFEXC` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFEXC` | `NUTAB` | `TGFTAB` | `NUTAB` |
| `TGFFAM` | `CODPRODFILHO` | `TGFPRO` | `CODPROD` |
| `TGFFCP` | `CODLOCAL` | `TGFLOC` | `CODLOCAL` |
| `TGFFCP` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFFIN` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFFIN` | `CODCFO` | `TGFCFO` | `CODCFO` |
| `TGFFIN` | `CODPARC` | `TGFCTT` | `CODPARC` |
| `TGFFIN` | `CODCONTATO` | `TGFCTT` | `CODCONTATO` |
| `TGFFIN` | `NUFIN` | `TGFFIN` | `TIMNUFINORIG` |
| `TGFFIN` | `TIMNUFINORIG` | `TGFFIN` | `NUFIN` |
| `TGFFIN` | `NUBCO` | `TGFMBC` | `NUBCO` |
| `TGFFIN` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TGFFIN` | `CODOBSPADRAO` | `TGFOBS` | `CODOBSPADRAO` |
| `TGFFIN` | `ORDEMCARGA` | `TGFORD` | `ORDEMCARGA` |
| `TGFFIN` | `CODEMP` | `TGFORD` | `CODEMP` |
| `TGFFIN` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFFIN` | `NUFIN` | `TGFRAT` | `NUFIN` |
| `TGFFIN` | `NUFIN` | `TGFREN` | `NUFIN` |
| `TGFFIN` | `CODTIPTIT` | `TGFTIT` | `CODTIPTIT` |
| `TGFFIN` | `CODTIPOPERBAIXA` | `TGFTOP` | `CODTIPOPER` |
| `TGFFIN` | `DHTIPOPERBAIXA` | `TGFTOP` | `DHALTER` |
| `TGFFIN` | `DHTIPOPER` | `TGFTOP` | `DHALTER` |
| `TGFFIN` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFFIN` | `CODVEICULO` | `TGFVEI` | `CODVEICULO` |
| `TGFFIN` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TGFFIN` | `CODBCO` | `TSIBCO` | `CODBCO` |
| `TGFFIN` | `CODCIDINICTE` | `TSICID` | `CODCID` |
| `TGFFIN` | `CODCIDFIMCTE` | `TSICID` | `CODCID` |
| `TGFFIN` | `CODCTABCOINT` | `TSICTA` | `CODCTABCOINT` |
| `TGFFIN` | `TIMCONTALANC` | `TSICTA` | `CODCTABCOINT` |
| `TGFFIN` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFFIN` | `CODEMPBAIXA` | `TSIEMP` | `CODEMP` |
| `TGFFIN` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFFIN` | `CODIMOVELRURAL` | `TSIEMP` | `CODEMP` |
| `TGFFIN` | `NUFIN` | `TSILIB` | `NUCHAVE` |
| `TGFFIN` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFFIN` | `CODUSUBAIXA` | `TSIUSU` | `CODUSU` |
| `TGFFIN` | `TIMREPINTELIGENTE` | `TSIUSU` | `CODUSU` |
| `TGFFNF` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFFNF` | `NUFIN` | `TGFFIN` | `NUFIN` |
| `TGFFRE` | `NUFIN` | `TGFFIN` | `NUFIN` |
| `TGFGRU` | `CODCTACTBEFD` | `TCBPLA` | `CODCTACTB` |
| `TGFGRU` | `TIPOIMPOSTO` | `TGFIMA` | `TIPO` |
| `TGFGRU` | `CODGRUPOPROD` | `TGFIMA` | `CODIGO` |
| `TGFGRU` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TGFGRU` | `CODGRUPOPROD` | `TGFPRO` | `CODGRUPOPROD` |
| `TGFGRU` | `CODGRUPOPROD` | `TGFRGV` | `CODGRUPOPROD` |
| `TGFGRU` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFICM` | `CODTABICMS` | `TGFNTA` | `CODTAB` |
| `TGFICM` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFICM` | `CODOBSPADRAO` | `TGFOBS` | `CODOBSPADRAO` |
| `TGFICM` | `UFORIG` | `TSIUFS` | `CODUF` |
| `TGFICM` | `UFDEST` | `TSIUFS` | `CODUF` |
| `TGFICNF` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFICNF` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFIFE` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFIFE` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFIFE` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFIFE` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFIIF` | `NUFIN` | `TGFFIN` | `NUFIN` |
| `TGFIMA` | `CODIGO` | `TGFGRU` | `CODGRUPOPROD` |
| `TGFIMA` | `CODIMP` | `TGFIMC` | `CODIMP` |
| `TGFIMA` | `CODIGO` | `TGFPAR` | `CODPARC` |
| `TGFIMA` | `CODIGO` | `TGFPRO` | `CODPROD` |
| `TGFIMA` | `CODIGO` | `TGFTOP` | `CODTIPOPER` |
| `TGFIMA` | `CODIGO` | `TSIEMP` | `CODEMP` |
| `TGFIMC` | `CODCTACTB1` | `TCBPLA` | `CODCTACTB` |
| `TGFIMC` | `CODCTACTB2` | `TCBPLA` | `CODCTACTB` |
| `TGFIMC` | `CODIMP` | `TGFIMA` | `CODIMP` |
| `TGFIMN` | `CODIMP` | `TGFIMC` | `CODIMP` |
| `TGFIMN` | `CODNATREND` | `TGFNRR` | `CODNATREND` |
| `TGFIMN` | `CODCID` | `TSICID` | `CODCID` |
| `TGFINCT` | `NUNOTA` | `TGFNCT` | `NUNOTA` |
| `TGFINCT` | `SEQNOTA` | `TGFNCT` | `SEQUENCIA` |
| `TGFINU` | `NUMNOTA` | `TGFCAB` | `NUMNOTA` |
| `TGFIPI` | `CODIPI` | `TGFPRO` | `CODIPI` |
| `TGFISS` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFISS` | `CODCID` | `TSICID` | `CODCID` |
| `TGFISS` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFITC` | `CODCONTATO` | `TGFCTT` | `CODCONTATO` |
| `TGFITC` | `CODPARC` | `TGFCTT` | `CODPARC` |
| `TGFITC` | `CODPROD` | `TGFITC` | `CODPROD` |
| `TGFITC` | `NUMCOTACAO` | `TGFITC` | `NUMCOTACAO` |
| `TGFITC` | `CONTROLE` | `TGFITC` | `CONTROLE` |
| `TGFITC` | `CODLOCAL` | `TGFITC` | `CODLOCAL` |
| `TGFITC` | `DIFERENCIADOR` | `TGFITC` | `DIFERENCIADOR` |
| `TGFITC` | `CODLOCAL` | `TGFLOC` | `CODLOCAL` |
| `TGFITC` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TGFITC` | `MELHORFORNEC` | `TGFPAR` | `CODPARC` |
| `TGFITC` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFITC` | `FORNECAPROVADO` | `TGFPAR` | `CODPARC` |
| `TGFITC` | `CODPRODESP` | `TGFPRO` | `CODPROD` |
| `TGFITC` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFITC` | `CODTIPVENDA` | `TGFTPV` | `CODTIPVENDA` |
| `TGFITC` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TGFITC` | `CENTRESULT` | `TSICUS` | `CODCENCUS` |
| `TGFITC` | `EMPRESA` | `TSIEMP` | `CODEMP` |
| `TGFITC` | `USUSOL` | `TSIUSU` | `CODUSU` |
| `TGFITC` | `USURESP` | `TSIUSU` | `CODUSU` |
| `TGFITE` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFITE` | `CODPROD` | `TGFCUSITE` | `CODPROD` |
| `TGFITE` | `SEQUENCIA` | `TGFCUSITE` | `SEQUENCIA` |
| `TGFITE` | `NUNOTA` | `TGFCUSITE` | `NUNOTA` |
| `TGFITE` | `SEQUENCIA` | `TGFDIN` | `SEQUENCIA` |
| `TGFITE` | `NUNOTA` | `TGFDIN` | `NUNOTA` |
| `TGFITE` | `IDALIQICMS` | `TGFICM` | `IDALIQ` |
| `TGFITE` | `CODLOCALDEST` | `TGFLOC` | `CODLOCAL` |
| `TGFITE` | `CODLOCALORIG` | `TGFLOC` | `CODLOCAL` |
| `TGFITE` | `CODNATREND` | `TGFNRR` | `CODNATREND` |
| `TGFITE` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFITE` | `CODEXEC` | `TGFVEN` | `CODVEND` |
| `TGFITE` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TGFITE` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TGFITE` | `AD_CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFITE` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFITE_EXC` | `CODLOCALORIG` | `TGFLOC` | `CODLOCAL` |
| `TGFITE_EXC` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFITE_EXC` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TGFITR` | `CODINSTSECFIN` | `TGFGRU` | `CODGRUPOPROD` |
| `TGFITR` | `CODINSTPRINC` | `TGFGRU` | `CODGRUPOPROD` |
| `TGFITR` | `CODINSTSECINI` | `TGFGRU` | `CODGRUPOPROD` |
| `TGFITR` | `CODINSTPRINC` | `TGFLOC` | `CODLOCAL` |
| `TGFITR` | `CODINSTSECFIN` | `TGFLOC` | `CODLOCAL` |
| `TGFITR` | `CODINSTSECINI` | `TGFLOC` | `CODLOCAL` |
| `TGFITR` | `CODINSTPRINC` | `TGFNAT` | `CODNAT` |
| `TGFITR` | `CODINSTSECINI` | `TGFNAT` | `CODNAT` |
| `TGFITR` | `CODINSTSECFIN` | `TGFNAT` | `CODNAT` |
| `TGFITR` | `CODINSTSECINI` | `TGFPAR` | `CODPARC` |
| `TGFITR` | `CODINSTPRINC` | `TGFPAR` | `CODPARC` |
| `TGFITR` | `CODINSTSECFIN` | `TGFPAR` | `CODPARC` |
| `TGFITR` | `CODINSTSECINI` | `TGFPRO` | `CODPROD` |
| `TGFITR` | `CODINSTPRINC` | `TGFPRO` | `CODPROD` |
| `TGFITR` | `CODINSTSECFIN` | `TGFPRO` | `CODPROD` |
| `TGFITR` | `CODREGRA` | `TGFREG` | `CODREGRA` |
| `TGFITR` | `CODINSTSECINI` | `TGFTOP` | `CODTIPOPER` |
| `TGFITR` | `CODINSTSECFIN` | `TGFTOP` | `CODTIPOPER` |
| `TGFITR` | `CODINSTPRINC` | `TGFTOP` | `CODTIPOPER` |
| `TGFITR` | `CODINSTSECINI` | `TGFTPV` | `CODTIPVENDA` |
| `TGFITR` | `CODINSTPRINC` | `TGFTPV` | `CODTIPVENDA` |
| `TGFITR` | `CODINSTSECFIN` | `TGFTPV` | `CODTIPVENDA` |
| `TGFITR` | `CODINSTSECINI` | `TSICTA` | `CODCTABCOINT` |
| `TGFITR` | `CODINSTPRINC` | `TSICTA` | `CODCTABCOINT` |
| `TGFITR` | `CODINSTSECFIN` | `TSICTA` | `CODCTABCOINT` |
| `TGFITR` | `CODINSTSECFIN` | `TSICUS` | `CODCENCUS` |
| `TGFITR` | `CODINSTPRINC` | `TSICUS` | `CODCENCUS` |
| `TGFITR` | `CODINSTSECINI` | `TSICUS` | `CODCENCUS` |
| `TGFITR` | `CODINSTSECINI` | `TSIEMP` | `CODEMP` |
| `TGFITR` | `CODINSTPRINC` | `TSIEMP` | `CODEMP` |
| `TGFITR` | `CODINSTSECFIN` | `TSIEMP` | `CODEMP` |
| `TGFIXN` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TGFIXN` | `CODPARCREMET` | `TGFPAR` | `CODPARC` |
| `TGFIXN` | `CODPARCEXPED` | `TGFPAR` | `CODPARC` |
| `TGFIXN` | `CODPARCRECEB` | `TGFPAR` | `CODPARC` |
| `TGFIXN` | `CODPARCDEST` | `TGFPAR` | `CODPARC` |
| `TGFIXN` | `CODPARCTRANSP` | `TGFPAR` | `CODPARC` |
| `TGFIXN` | `CODPARCENTREGACTE` | `TGFPAR` | `CODPARC` |
| `TGFIXN` | `CODPARCCOLETACTE` | `TGFPAR` | `CODPARC` |
| `TGFIXN` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFIXN` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFIXN` | `CODTIPVENDA` | `TGFTPV` | `CODTIPVENDA` |
| `TGFIXN` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TGFIXN` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFIXN` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFIXN` | `CODUSUPROC` | `TSIUSU` | `CODUSU` |
| `TGFIXN` | `CODUSUIMP` | `TSIUSU` | `CODUSU` |
| `TGFLIC` | `CODUSULIB` | `TSIUSU` | `CODUSU` |
| `TGFLIS` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFLIS` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFLIV` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TGFLIV` | `CODCFO` | `TGFCFO` | `CODCFO` |
| `TGFLIV` | `CODPARC` | `TGFCTT` | `CODPARC` |
| `TGFLIV` | `CODCONTATOENTREGA` | `TGFCTT` | `CODCONTATO` |
| `TGFLIV` | `NUNOTA` | `TGFITE` | `NUNOTA` |
| `TGFLIV` | `SEQUENCIA` | `TGFITE` | `SEQUENCIA` |
| `TGFLIV` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFLIV` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFLIV` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFLIV` | `CODCIDFIMCTE` | `TSICID` | `CODCID` |
| `TGFLIV` | `CODCIDINICTE` | `TSICID` | `CODCID` |
| `TGFLIV` | `CODEMPORIG` | `TSIEMP` | `CODEMP` |
| `TGFLIV` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFLNF` | `NULOTE` | `TGFCAB` | `NULOTENFE` |
| `TGFLOC` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFLOC` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFLOC` | `CODTAB` | `TGFTAB` | `CODTAB` |
| `TGFMBC` | `CODLANC` | `TGFHBC` | `CODLANC` |
| `TGFMBC` | `CODLANCDEST` | `TGFHBC` | `CODLANC` |
| `TGFMBC` | `NUBCO` | `TGFMBC` | `NUBCO` |
| `TGFMBC` | `CODCTABCOINT` | `TGFSBC` | `CODCTABCOINT` |
| `TGFMBC` | `DHTIPOPER` | `TGFTOP` | `DHALTER` |
| `TGFMBC` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFMBC` | `CODCTABCOINTDEST` | `TSICTA` | `CODCTABCOINT` |
| `TGFMBC` | `CODCTABCOINT` | `TSICTA` | `CODCTABCOINT` |
| `TGFMBC` | `CODCTABCOCONTRA` | `TSICTA` | `CODCTABCOINT` |
| `TGFMBC` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFMDFE` | `NUVIAG` | `TGFCONTR` | `NUVIAG` |
| `TGFMDFE` | `SEQMDFE` | `TGFCONTR` | `SEQMDFE` |
| `TGFMDFE` | `SEQMDFE` | `TGFEMDF` | `SEQMDFE` |
| `TGFMDFE` | `NUVIAG` | `TGFEMDF` | `NUVIAG` |
| `TGFMDFE` | `NUVIAG` | `TGFMDFESEG` | `NUVIAG` |
| `TGFMDFE` | `SEQMDFE` | `TGFMDFESEG` | `SEQMDFE` |
| `TGFMDFE` | `NUVIAG` | `TGFNMDFE` | `NUVIAG` |
| `TGFMDFE` | `SEQMDFE` | `TGFNMDFE` | `SEQMDFE` |
| `TGFMDFE` | `NUVIAG` | `TGFUFP` | `NUVIAG` |
| `TGFMDFE` | `SEQMDFE` | `TGFUFP` | `SEQMDFE` |
| `TGFMDFE` | `NUVIAG` | `TGFVIAG` | `NUVIAG` |
| `TGFMDFE` | `MUNINICIAL` | `TSICID` | `CODCID` |
| `TGFMDFE` | `MUNFINAL` | `TSICID` | `CODCID` |
| `TGFMDFE` | `CODCIDENCERRAMENTO` | `TSICID` | `CODCID` |
| `TGFMDFE` | `UFINICIAL` | `TSIUFS` | `CODUF` |
| `TGFMDFE` | `UFFINAL` | `TSIUFS` | `CODUF` |
| `TGFMDFE` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFMDFESEG` | `SEQMDFE` | `TGFAVE` | `SEQMDFE` |
| `TGFMDFESEG` | `NUVIAG` | `TGFAVE` | `NUVIAG` |
| `TGFMDFESEG` | `NUMAPOLICE` | `TGFAVE` | `NUMAPOLICE` |
| `TGFMDFESEG` | `CODPARCRESPSEG` | `TGFPAR` | `CODPARC` |
| `TGFMDFESEG` | `CODPARCSEG` | `TGFPAR` | `CODPARC` |
| `TGFMIX` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFMME` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFMME` | `NUVIAG` | `TGFVIAG` | `NUVIAG` |
| `TGFMMS` | `CODGRUPOPROD` | `TGFGRU` | `CODGRUPOPROD` |
| `TGFMMS` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFMON` | `NURFE` | `TSIRFE` | `NURFE` |
| `TGFNAT` | `CODHISTCTB` | `TCBHIS` | `CODHISTCTB` |
| `TGFNAT` | `CODHISTCTB2` | `TCBHIS` | `CODHISTCTB` |
| `TGFNAT` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TGFNAT` | `CODCTACTB2` | `TCBPLA` | `CODCTACTB` |
| `TGFNAT` | `CODCTACTBEFD` | `TCBPLA` | `CODCTACTB` |
| `TGFNAT` | `CODNAT` | `TGFENA` | `CODNAT` |
| `TGFNAT` | `CODSERVUNICO` | `TGFPRO` | `CODPROD` |
| `TGFNCE` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFNCE` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFNCT` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFNFE` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFNFENT` | `CODEMP` | `TGFEMP` | `CODEMP` |
| `TGFNMDFE` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFNMDFE` | `NUVIAG` | `TGFMDFE` | `NUVIAG` |
| `TGFNMDFE` | `SEQMDFE` | `TGFMDFE` | `SEQMDFE` |
| `TGFNTA` | `CODTABFLEX` | `TGFNTA` | `CODTAB` |
| `TGFNTA` | `CODTAB` | `TGFTAB` | `CODTAB` |
| `TGFNTA` | `CODTIPPARC` | `TGFTPP` | `CODTIPPARC` |
| `TGFNTA` | `CODREG` | `TSIREG` | `CODREG` |
| `TGFNUM` | `MODNOTAFIS` | `TGFMON` | `CODMODNF` |
| `TGFNUM` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFOMDF` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFORD` | `ORDEMCARGA` | `TGFCAB` | `ORDEMCARGA` |
| `TGFORD` | `CODLOCAL` | `TGFLOC` | `CODLOCAL` |
| `TGFORD` | `CODPARCMOTORISTA` | `TGFPAR` | `CODPARC` |
| `TGFORD` | `CODPARCDEST` | `TGFPAR` | `CODPARC` |
| `TGFORD` | `CODPARCTRANSP` | `TGFPAR` | `CODPARC` |
| `TGFORD` | `CODPARCORIG` | `TGFPAR` | `CODPARC` |
| `TGFORD` | `CODTIPOPERTRANSB` | `TGFTOP` | `CODTIPOPER` |
| `TGFORD` | `CODVEICULO` | `TGFVEI` | `CODVEICULO` |
| `TGFORD` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFORD` | `CODREG` | `TSIREG` | `CODREG` |
| `TGFPAEM` | `CODEMP` | `TGFEMP` | `CODEMP` |
| `TGFPAEM` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFPAEM` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFPAEM` | `CODTAB` | `TGFTAB` | `CODTAB` |
| `TGFPAEM` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFPAP` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFPAP` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFPAP` | `CODPROD` | `TGFVOA` | `CODPROD` |
| `TGFPAP` | `UNIDADELOTE` | `TGFVOA` | `CODVOL` |
| `TGFPAP` | `CONTROLE` | `TGFVOA` | `CONTROLE` |
| `TGFPAP` | `UNIDADEPARC` | `TGFVOL` | `CODVOL` |
| `TGFPAP` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFPAR` | `CODCTACTB2` | `TCBPLA` | `CODCTACTB` |
| `TGFPAR` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TGFPAR` | `CODCTACTB3` | `TCBPLA` | `CODCTACTB` |
| `TGFPAR` | `CODCTACTB4` | `TCBPLA` | `CODCTACTB` |
| `TGFPAR` | `MODELONOTACOMPRA` | `TGFCAB` | `NUNOTA` |
| `TGFPAR` | `CODPARC` | `TGFCPL` | `CODPARC` |
| `TGFPAR` | `CODPARC` | `TGFCTT` | `CODPARC` |
| `TGFPAR` | `CODCONTATOPADCOT` | `TGFCTT` | `CODCONTATO` |
| `TGFPAR` | `CODPARC` | `TGFIMA` | `CODIGO` |
| `TGFPAR` | `CODLOCALPADRAO` | `TGFLOC` | `CODLOCAL` |
| `TGFPAR` | `AD_CODNAT` | `TGFNAT` | `CODNAT` |
| `TGFPAR` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFPAR` | `CODTABST` | `TGFNTA` | `CODTAB` |
| `TGFPAR` | `CODPARC` | `TGFPAEM` | `CODPARC` |
| `TGFPAR` | `CODPARC` | `TGFPAP` | `CODPARC` |
| `TGFPAR` | `CODPARCGRUECONOMICO` | `TGFPAR` | `CODPARC` |
| `TGFPAR` | `CODPARCMATRIZ` | `TGFPAR` | `CODPARC` |
| `TGFPAR` | `CODPARC` | `TGFPPA` | `CODPARC` |
| `TGFPAR` | `CODPARC` | `TGFPRO` | `CODPARCFORN` |
| `TGFPAR` | `CODTAB` | `TGFTAB` | `CODTAB` |
| `TGFPAR` | `CODTIPPARC` | `TGFTPP` | `CODTIPPARC` |
| `TGFPAR` | `CODASSESSOR` | `TGFVEN` | `CODVEND` |
| `TGFPAR` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TGFPAR` | `TIMBAIRROCOMPRA` | `TSIBAI` | `CODBAI` |
| `TGFPAR` | `CODBAI` | `TSIBAI` | `CODBAI` |
| `TGFPAR` | `CODBCO` | `TSIBCO` | `CODBCO` |
| `TGFPAR` | `CODCID` | `TSICID` | `CODCID` |
| `TGFPAR` | `CODCTABCOINT` | `TSICTA` | `CODCTABCOINT` |
| `TGFPAR` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFPAR` | `CODEMPPREF` | `TSIEMP` | `CODEMP` |
| `TGFPAR` | `CODEND` | `TSIEND` | `CODEND` |
| `TGFPAR` | `TIMNACIONALIDAD` | `TSIPAI` | `CODPAIS` |
| `TGFPAR` | `CODREG` | `TSIREG` | `CODREG` |
| `TGFPAR` | `REDE` | `TSIRTEF` | `REDE` |
| `TGFPAR` | `CODUSUCOBR` | `TSIUSU` | `CODUSU` |
| `TGFPAR` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFPEM` | `CODCTACTBEFD` | `TCBPLA` | `CODCTACTB` |
| `TGFPEM` | `CODEMP` | `TGFEMP` | `CODEMP` |
| `TGFPEM` | `CODLOCALPAD` | `TGFLOC` | `CODLOCAL` |
| `TGFPEM` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFPEM` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFPPA` | `CODCONTATO` | `TGFCTT` | `CODCONTATO` |
| `TGFPPA` | `CODPARC` | `TGFCTT` | `CODPARC` |
| `TGFPPA` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFPPA` | `CODTIPPARC` | `TGFTPP` | `CODTIPPARC` |
| `TGFPPG` | `CODNATPAD` | `TGFNAT` | `CODNAT` |
| `TGFPPG` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFPPG` | `CODTIPTITPAD` | `TGFTIT` | `CODTIPTIT` |
| `TGFPPG` | `CODTIPVENDA` | `TGFTPV` | `CODTIPVENDA` |
| `TGFPPG` | `CODBCOPAD` | `TSIBCO` | `CODBCO` |
| `TGFPPG` | `CODCTABCOINT` | `TSICTA` | `CODCTABCOINT` |
| `TGFPPG` | `CODCENCUSPAD` | `TSICUS` | `CODCENCUS` |
| `TGFPPG` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFPRC` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFPRO` | `CODCTACTB4` | `TCBPLA` | `CODCTACTB` |
| `TGFPRO` | `CODCTACTBEFD` | `TCBPLA` | `CODCTACTB` |
| `TGFPRO` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TGFPRO` | `CODCTACTB3` | `TCBPLA` | `CODCTACTB` |
| `TGFPRO` | `CODCTACTB2` | `TCBPLA` | `CODCTACTB` |
| `TGFPRO` | `CODPROD` | `TGFAID` | `CODPROD` |
| `TGFPRO` | `CODPROD` | `TGFBAR` | `CODPROD` |
| `TGFPRO` | `CODIGONFCOM` | `TGFCINFCOM` | `CODIGO` |
| `TGFPRO` | `CODPROD` | `TGFEST` | `CODPROD` |
| `TGFPRO` | `CODPROD` | `TGFFAM` | `CODPRODPAI` |
| `TGFPRO` | `CODGRUPOPROD` | `TGFGRU` | `CODGRUPOPROD` |
| `TGFPRO` | `GRUPOPIS` | `TGFIFE` | `GRUPOIMP` |
| `TGFPRO` | `GRUPOCSSL` | `TGFIFE` | `GRUPOIMP` |
| `TGFPRO` | `GRUPOCOFINS` | `TGFIFE` | `GRUPOIMP` |
| `TGFPRO` | `CODPROD` | `TGFIMA` | `CODIGO` |
| `TGFPRO` | `CODIPI` | `TGFIPI` | `CODIPI` |
| `TGFPRO` | `CODPROD` | `TGFISS` | `CODPROD` |
| `TGFPRO` | `CODLOCALPADRAO` | `TGFLOC` | `CODLOCAL` |
| `TGFPRO` | `CODMARCA` | `TGFMAR` | `CODIGO` |
| `TGFPRO` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TGFPRO` | `NCM` | `TGFNCM` | `CODNCM` |
| `TGFPRO` | `CODNATREND` | `TGFNRR` | `CODNATREND` |
| `TGFPRO` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFPRO` | `CODPROD` | `TGFPAP` | `CODPROD` |
| `TGFPRO` | `CODPARCCONSIG` | `TGFPAR` | `CODPARC` |
| `TGFPRO` | `CODFAB` | `TGFPAR` | `CODPARC` |
| `TGFPRO` | `CODPARCFORN` | `TGFPAR` | `CODPARC` |
| `TGFPRO` | `CODPROD` | `TGFPEM` | `CODPROD` |
| `TGFPRO` | `CODGAR` | `TGFPRO` | `CODPROD` |
| `TGFPRO` | `CODPRODSUBST` | `TGFPRO` | `CODPROD` |
| `TGFPRO` | `CODPRODAGRUPAPTENC` | `TGFPRO` | `CODPROD` |
| `TGFPRO` | `CODPRODSUBKIT` | `TGFPRO` | `CODPROD` |
| `TGFPRO` | `CODPRODAGRUPAPT` | `TGFPRO` | `CODPROD` |
| `TGFPRO` | `CODGENERO` | `TGFSTG` | `CODIGO` |
| `TGFPRO` | `TOPFATURCON` | `TGFTOP` | `CODTIPOPER` |
| `TGFPRO` | `CODPROD` | `TGFVOA` | `CODPROD` |
| `TGFPRO` | `CODVOLFETHAB` | `TGFVOL` | `CODVOL` |
| `TGFPRO` | `CODVOLKANBAN` | `TGFVOL` | `CODVOL` |
| `TGFPRO` | `UNIDMINARMAZ` | `TGFVOL` | `CODVOL` |
| `TGFPRO` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TGFPRO` | `CODVOLCOMPRA` | `TGFVOL` | `CODVOL` |
| `TGFPRO` | `CODVOLRES` | `TGFVOL` | `CODVOL` |
| `TGFPRO` | `CODVOLPESOVAR` | `TGFVOL` | `CODVOL` |
| `TGFPRO` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFPRO` | `AD_EMPRESA` | `TSIEMP` | `CODEMP` |
| `TGFPRO` | `MODETIQSEPWMS` | `TSIRFE` | `NURFE` |
| `TGFPRO` | `NURFE` | `TSIRFE` | `NURFE` |
| `TGFRAT` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TGFRAT` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TGFRAT` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFRAT` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFREG` | `CODREGRA` | `TGFITR` | `CODREGRA` |
| `TGFREJNFE` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFREN` | `NUFIN` | `TGFFIN` | `NUFIN` |
| `TGFREN` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFRGV` | `CODGRUPOPROD` | `TGFGRU` | `CODGRUPOPROD` |
| `TGFRNG` | `NURNG` | `TGFTRN` | `NURNG` |
| `TGFRNG` | `CODUSULIB` | `TSIUSU` | `CODUSU` |
| `TGFTAB` | `NUTAB` | `TGFEXC` | `NUTAB` |
| `TGFTAB` | `CODTABORIG` | `TGFNTA` | `CODTAB` |
| `TGFTAB` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFTAG` | `NUAGENDAMENTO` | `TCBERR` | `NUAGENDCTZ` |
| `TGFTAG` | `TIPOAGE` | `TCBERR` | `TIPO` |
| `TGFTAG` | `TIPOAGE` | `TCBHCT` | `TIPO` |
| `TGFTAG` | `NUAGENDAMENTO` | `TCBHCT` | `NUAGENDCTZ` |
| `TGFTAG` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFTIT` | `CODCTACTB2` | `TCBPLA` | `CODCTACTB` |
| `TGFTIT` | `CODCTACTB3` | `TCBPLA` | `CODCTACTB` |
| `TGFTIT` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TGFTIT` | `CODPARCTEF` | `TGFPAR` | `CODPARC` |
| `TGFTOL` | `CODTIPOPER` | `TGFLIC` | `CODTIPOPER` |
| `TGFTOL` | `EVENTO` | `TGFLIC` | `EVENTO` |
| `TGFTOP` | `CODCTACTBEFD` | `TCBPLA` | `CODCTACTB` |
| `TGFTOP` | `NUNOTAMODELO` | `TGFCAB` | `NUNOTA` |
| `TGFTOP` | `CODCFPS` | `TGFCFO` | `CODCFO` |
| `TGFTOP` | `CODCFO_ENTRADA` | `TGFCFO` | `CODCFO` |
| `TGFTOP` | `CODCFO_ENTRADA_FORA` | `TGFCFO` | `CODCFO` |
| `TGFTOP` | `CODCFO_SAIDA` | `TGFCFO` | `CODCFO` |
| `TGFTOP` | `CODCFO_SAIDA_FORA` | `TGFCFO` | `CODCFO` |
| `TGFTOP` | `CODCFO_TERC` | `TGFCFO` | `CODCFO` |
| `TGFTOP` | `CODCFO_COMBUST_LUBRIF` | `TGFCFO` | `CODCFO` |
| `TGFTOP` | `CODTIPOPER` | `TGFIMA` | `CODIGO` |
| `TGFTOP` | `NULAYOUT` | `TGFLAY` | `NULAYOUT` |
| `TGFTOP` | `CODLOCALIMPXML` | `TGFLOC` | `CODLOCAL` |
| `TGFTOP` | `CODMODRPS` | `TGFMON` | `CODMODNF` |
| `TGFTOP` | `CODMODNF` | `TGFMON` | `CODMODNF` |
| `TGFTOP` | `CODMODNFSE` | `TGFMON` | `CODMODNF` |
| `TGFTOP` | `CODMODRO` | `TGFMON` | `CODMODNF` |
| `TGFTOP` | `CODMODCFECANC` | `TGFMON` | `CODMODNF` |
| `TGFTOP` | `CODMODDAD` | `TGFMON` | `CODMODNF` |
| `TGFTOP` | `CODINTERM` | `TGFPAR` | `CODPARC` |
| `TGFTOP` | `CODTIPOPER` | `TGFTOL` | `CODTIPOPER` |
| `TGFTOP` | `TOPBACKORDER` | `TGFTOP` | `CODTIPOPER` |
| `TGFTOP` | `CODTIPOPERDENEG` | `TGFTOP` | `CODTIPOPER` |
| `TGFTOP` | `CODTOPDENEGCTE` | `TGFTOP` | `CODTIPOPER` |
| `TGFTOP` | `CODTIPOPERREM` | `TGFTOP` | `CODTIPOPER` |
| `TGFTOP` | `CODTIPOPERSEPARACAO` | `TGFTOP` | `CODTIPOPER` |
| `TGFTOP` | `TOPATENDIMENTO` | `TGFTOP` | `CODTIPOPER` |
| `TGFTOP` | `CODTIPOPERPENRET` | `TGFTOP` | `CODTIPOPER` |
| `TGFTOP` | `CODTIPOPERDESTINO` | `TGFTOP` | `CODTIPOPER` |
| `TGFTOP` | `CODTIPOPER` | `TGFTRN` | `CODTIPOPER` |
| `TGFTOP` | `CODTIPOPER` | `TSILIB` | `CODTIPOPER` |
| `TGFTOP` | `CODREMEDI` | `TSIREM` | `CODIGO` |
| `TGFTPP` | `CODTIPPARC` | `TGFPPA` | `CODTIPPARC` |
| `TGFTPP` | `CODTAB` | `TGFTAB` | `CODTAB` |
| `TGFTPV` | `CODCTACTB_2` | `TCBPLA` | `CODCTACTB` |
| `TGFTPV` | `CODCTACTB_1` | `TCBPLA` | `CODCTACTB` |
| `TGFTPV` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFTPV` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TGFTPV` | `CODOBSPADRAO` | `TGFOBS` | `CODOBSPADRAO` |
| `TGFTPV` | `CODTIPVENDA` | `TGFPPG` | `CODTIPVENDA` |
| `TGFTRN` | `NURNG` | `TGFRNG` | `NURNG` |
| `TGFTRN` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TGFUFP` | `CODUF` | `TSIUFS` | `CODUF` |
| `TGFUNM` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFVALP` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TGFVALP` | `CODPARCPAG` | `TGFPAR` | `CODPARC` |
| `TGFVALP` | `CODPARCFORN` | `TGFPAR` | `CODPARC` |
| `TGFVAR` | `SEQUENCIA` | `TGFITE` | `SEQUENCIA` |
| `TGFVAR` | `NUNOTA` | `TGFITE` | `NUNOTA` |
| `TGFVAR` | `NUNOTAORIG` | `TGFITE` | `NUNOTA` |
| `TGFVAR` | `SEQUENCIAORIG` | `TGFITE` | `SEQUENCIA` |
| `TGFVEI` | `CODPARCPROPANTT` | `TGFPAR` | `CODPARC` |
| `TGFVEI` | `CODMOTORISTA` | `TGFPAR` | `CODPARC` |
| `TGFVEI` | `CODPROD` | `TGFPRO` | `CODPROD` |
| `TGFVEI` | `CODCID` | `TSICID` | `CODCID` |
| `TGFVEI` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TGFVEI` | `CODEMPFOLHA` | `TSIEMP` | `CODEMP` |
| `TGFVEN` | `CODVEND` | `TGFCER` | `CHAVE` |
| `TGFVEN` | `TIPOCERTIF` | `TGFCER` | `TIPO` |
| `TGFVEN` | `CODFORM` | `TGFFOC` | `CODFORM` |
| `TGFVEN` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TGFVEN` | `CODVEND` | `TGFRGV` | `CODVEND` |
| `TGFVEN` | `CODGER` | `TGFVEN` | `CODVEND` |
| `TGFVEN` | `CODCENCUSPAD` | `TSICUS` | `CODCENCUS` |
| `TGFVEN` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFVEN` | `CODREG` | `TSIREG` | `CODREG` |
| `TGFVEN` | `CODPARC` | `TSIUSU` | `CODPARC` |
| `TGFVIAG` | `NUVIAG` | `TGFMDFE` | `NUVIAG` |
| `TGFVIAG` | `NUVIAG` | `TGFMME` | `NUVIAG` |
| `TGFVIAG` | `CODVEIREB3` | `TGFVEI` | `CODVEICULO` |
| `TGFVIAG` | `CODVEIREB2` | `TGFVEI` | `CODVEICULO` |
| `TGFVIAG` | `CODVEIPRIN` | `TGFVEI` | `CODVEICULO` |
| `TGFVIAG` | `CODVEIREB1` | `TGFVEI` | `CODVEICULO` |
| `TGFVIAG` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TGFVIAG` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TGFVOA` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TPRAMP` | `CODLOCALBAIXA` | `TGFLOC` | `CODLOCAL` |
| `TPRAMP` | `CODPRODMP` | `TGFPRO` | `CODPROD` |
| `TPRAMP` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TPRAPA` | `CODPRODPA` | `TGFPRO` | `CODPROD` |
| `TPRAPO` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TPRATV` | `CODUSULOGON` | `TSIUSU` | `CODUSU` |
| `TPRAUD` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TPRCAP` | `UNIDADE` | `TGFVOL` | `CODVOL` |
| `TPREIATV` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TPREIATV` | `CODEXEC` | `TSIUSU` | `CODUSU` |
| `TPRESR` | `CODPRODPA` | `TGFPRO` | `CODPROD` |
| `TPRIATV` | `CODPARCTERC` | `TGFPAR` | `CODPARC` |
| `TPRIATV` | `CODUSUFIN` | `TSIUSU` | `CODUSU` |
| `TPRIATV` | `CODEXEC` | `TSIUSU` | `CODUSU` |
| `TPRIATV` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TPRIATV` | `CODULTEXEC` | `TSIUSU` | `CODUSU` |
| `TPRIPA` | `CODPRODPA` | `TGFPRO` | `CODPROD` |
| `TPRIPROC` | `CODPARCTERC` | `TGFPAR` | `CODPARC` |
| `TPRIPROC` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TPRIPROC` | `CODUSUFINAL` | `TSIUSU` | `CODUSU` |
| `TPRIPROC` | `CODUSUINC` | `TSIUSU` | `CODUSU` |
| `TPRLMP` | `CODLOCALORIG` | `TGFLOC` | `CODLOCAL` |
| `TPRLMP` | `CODLOCALBAIXA` | `TGFLOC` | `CODLOCAL` |
| `TPRLMP` | `CODPRODPA` | `TGFPRO` | `CODPROD` |
| `TPRLMP` | `CODPRODMP` | `TGFPRO` | `CODPROD` |
| `TPRLMP` | `CODVOL` | `TGFVOL` | `CODVOL` |
| `TPRLMP` | `CODUSUALT` | `TSIUSU` | `CODUSU` |
| `TPRLMP` | `CODUSUCAD` | `TSIUSU` | `CODUSU` |
| `TPRLOP` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TPRLPA` | `CODLOCDEST` | `TGFLOC` | `CODLOCAL` |
| `TPRLPA` | `CODPRODPA` | `TGFPRO` | `CODPROD` |
| `TPRLPA` | `CODUSUALT` | `TSIUSU` | `CODUSU` |
| `TPRLPA` | `CODUSUCAD` | `TSIUSU` | `CODUSU` |
| `TPROEST` | `NUNOTAMODELO` | `TGFCAB` | `NUNOTA` |
| `TPROEST` | `NUNOTAMODELOKANBAN` | `TGFCAB` | `NUNOTA` |
| `TPROEST` | `NUMODELOENCAD` | `TGFCAB` | `NUNOTA` |
| `TPROEST` | `CODLOCALORIG` | `TGFLOC` | `CODLOCAL` |
| `TPROEST` | `CODLOCALBAIXAMP` | `TGFLOC` | `CODLOCAL` |
| `TPROEST` | `CODLOCALDEST` | `TGFLOC` | `CODLOCAL` |
| `TPROEST` | `CODLOCALDESTPERDA` | `TGFLOC` | `CODLOCAL` |
| `TPROEST` | `CODLOCALDESTENCAD` | `TGFLOC` | `CODLOCAL` |
| `TPROEST` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TPROEST` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TPROEST` | `CODPARCENCAD` | `TGFPAR` | `CODPARC` |
| `TPROEST` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TPROEST` | `CODTIPOPERKANBAN` | `TGFTOP` | `CODTIPOPER` |
| `TPROEST` | `CODTIPOPERENCAD` | `TGFTOP` | `CODTIPOPER` |
| `TPROEST` | `CODTIPOPERPERDA` | `TGFTOP` | `CODTIPOPER` |
| `TPROEST` | `CODTIPVENDA` | `TGFTPV` | `CODTIPVENDA` |
| `TPROEST` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TPROEST` | `CODEMPDESTENCAD` | `TSIEMP` | `CODEMP` |
| `TPROEST` | `CODEMPORIG` | `TSIEMP` | `CODEMP` |
| `TPROEST` | `CODEMPDEST` | `TSIEMP` | `CODEMP` |
| `TPRPLP` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TPRPLP` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TPRPRC` | `CODLOCALALMOXARIFE` | `TGFLOC` | `CODLOCAL` |
| `TPRPRC` | `CODLOCALMANUFATURA` | `TGFLOC` | `CODLOCAL` |
| `TPRPRC` | `CODUSUCAD` | `TSIUSU` | `CODUSU` |
| `TPRPRC` | `CODUSUALT` | `TSIUSU` | `CODUSU` |
| `TPRROPE` | `NUNOTA` | `TGFCAB` | `NUNOTA` |
| `TPRROPE` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIACI` | `CODGRUPO` | `TSIGRU` | `CODGRUPO` |
| `TSIACI` | `CODREL` | `TSIIMP` | `CODREL` |
| `TSIACI` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIAGE` | `CODBAI` | `TSIBAI` | `CODBAI` |
| `TSIAGE` | `CODBCO` | `TSIBCO` | `CODBCO` |
| `TSIAGE` | `CODCID` | `TSICID` | `CODCID` |
| `TSIAGE` | `CODEND` | `TSIEND` | `CODEND` |
| `TSIANX` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIANX` | `CODUSUALT` | `TSIUSU` | `CODUSU` |
| `TSIARF` | `NURFE` | `TSIDRF` | `NURFE` |
| `TSIARF` | `SEQUENCIA` | `TSIDRF` | `SEQUENCIA` |
| `TSIARF` | `NURFE` | `TSIRFE` | `NURFE` |
| `TSIATA` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIAVI` | `CODGRUPO` | `TSIGRU` | `CODGRUPO` |
| `TSIAVI` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIBAI` | `CODREG` | `TSIREG` | `CODREG` |
| `TSICEP` | `CODBAI` | `TSIBAI` | `CODBAI` |
| `TSICEP` | `CODCID` | `TSICID` | `CODCID` |
| `TSICEP` | `CODEND` | `TSIEND` | `CODEND` |
| `TSICID` | `CODCID` | `TGFISS` | `CODCID` |
| `TSICID` | `CODPARCNFSE` | `TGFPAR` | `CODPARC` |
| `TSICID` | `CODCID` | `TSICAN` | `CODCID` |
| `TSICID` | `CODREG` | `TSIREG` | `CODREG` |
| `TSICID` | `UF` | `TSIUFS` | `CODUF` |
| `TSICTA` | `CODCTACTB` | `TCBPLA` | `CODCTACTB` |
| `TSICTA` | `CODLANCBAIXABOLRAP` | `TGFHBC` | `CODLANC` |
| `TSICTA` | `MODBOLETA` | `TGFMON` | `CODMODNF` |
| `TSICTA` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TSICTA` | `CODTIPOPERBAIXABOLRAP` | `TGFTOP` | `CODTIPOPER` |
| `TSICTA` | `CODBCO` | `TSIAGE` | `CODBCO` |
| `TSICTA` | `CODAGE` | `TSIAGE` | `CODAGE` |
| `TSICTA` | `CODBCO` | `TSIBCO` | `CODBCO` |
| `TSICTA` | `CODCORRBCO` | `TSIBCO` | `CODBCO` |
| `TSICTA` | `CTAMINBOLETA` | `TSICTA` | `CODCTABCOINT` |
| `TSICTA` | `CODCTABCOINTREM` | `TSICTA` | `CODCTABCOINT` |
| `TSICTA` | `CODCTABAIXA` | `TSICTA` | `CODCTABCOINT` |
| `TSICTA` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TSICTA` | `NURFEMODBOLETO` | `TSIRFE` | `NURFE` |
| `TSICTA` | `NURFEMODCHEQG` | `TSIRFE` | `NURFE` |
| `TSICTA` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSICTA` | `CODOPEREXCL` | `TSIUSU` | `CODUSU` |
| `TSICUS` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TSICUS` | `CODPARCRESP` | `TGFPAR` | `CODPARC` |
| `TSICUS` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TSICUS` | `CODUSURESP` | `TSIUSU` | `CODUSU` |
| `TSIDSB` | `NUDSB` | `TSIDSG` | `NUDSB` |
| `TSIEMP` | `CODEMP` | `TGFCER` | `CHAVE` |
| `TSIEMP` | `TIPOREGRA` | `TGFCER` | `TIPO` |
| `TSIEMP` | `CODEMP` | `TGFEMP` | `CODEMP` |
| `TSIEMP` | `CODEMP` | `TGFIMA` | `CODIGO` |
| `TSIEMP` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TSIEMP` | `CODBAI` | `TSIBAI` | `CODBAI` |
| `TSIEMP` | `CODCID` | `TSICID` | `CODCID` |
| `TSIEMP` | `EMPAGRUPARGOL` | `TSIEMP` | `CODEMP` |
| `TSIEMP` | `CODEMPMATRIZ` | `TSIEMP` | `CODEMP` |
| `TSIEMP` | `CODEND` | `TSIEND` | `CODEND` |
| `TSIEND` | `TIPO` | `TSITEND` | `TIPO` |
| `TSIERF` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIESTATSERVICO` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIFER` | `CODCID` | `TSICID` | `CODCID` |
| `TSIFER` | `CODPAIS` | `TSIPAI` | `CODPAIS` |
| `TSIFER` | `CODUF` | `TSIUFS` | `CODUF` |
| `TSIFTD` | `MODULO` | `TSIFTM` | `MODULO` |
| `TSIFTD` | `CODIGO` | `TSIFTM` | `CODIGO` |
| `TSIFTM` | `CODIGO` | `TSIFTD` | `CODIGO` |
| `TSIFTM` | `MODULO` | `TSIFTD` | `MODULO` |
| `TSIGDG` | `NUGDG` | `TSIDSG` | `NUGDG` |
| `TSIGRE` | `CODGRUPORELPAI` | `TSIGRE` | `CODGRUPOREL` |
| `TSIHCF` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIIMP` | `CODGRUPOREL` | `TSIGRE` | `CODGRUPOREL` |
| `TSIIRT` | `SEQUENCIA` | `TSIOBC` | `SEQUENCIA` |
| `TSIIRT` | `CODIGO` | `TSIOBC` | `CODIGO` |
| `TSIJPR` | `JOBSTATUS` | `TSIJPS` | `JOBSTATUS` |
| `TSIJPR` | `MIMETYPE` | `TSITPA` | `DOCTASTE` |
| `TSIJPR` | `TIPODOC` | `TSITPD` | `DOCTYPE` |
| `TSIJPR` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSILBA` | `CODUSUSOLIC` | `TSIUSU` | `CODUSU` |
| `TSILBA` | `CODUSULIBER` | `TSIUSU` | `CODUSU` |
| `TSILIB` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TSILIB` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TSILIB` | `CODUSULIB` | `TSIUSU` | `CODUSU` |
| `TSILIB` | `CODUSUSOLICIT` | `TSIUSU` | `CODUSU` |
| `TSILIM` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIMAP` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIOBC` | `CODNAT` | `TGFNAT` | `CODNAT` |
| `TSIOBC` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TSIOBC` | `CODTIPTIT` | `TGFTIT` | `CODTIPTIT` |
| `TSIOBC` | `CODTIPOPER` | `TGFTOP` | `CODTIPOPER` |
| `TSIOBC` | `CODBCO` | `TSIBCO` | `CODBCO` |
| `TSIOBC` | `CODCTABCOINT` | `TSICTA` | `CODCTABCOINT` |
| `TSIOBC` | `CODCENCUS` | `TSICUS` | `CODCENCUS` |
| `TSIOBC` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TSIOBC` | `NURFE` | `TSIRFE` | `NURFE` |
| `TSIOBCLOG` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIPAR` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIPER` | `CODGRUPO` | `TSIGRU` | `CODGRUPO` |
| `TSIPER` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIREG` | `CODTABMIN` | `TGFNTA` | `CODTAB` |
| `TSIREG` | `CODTAB` | `TGFNTA` | `CODTAB` |
| `TSIREG` | `CODREG` | `TGFPAR` | `CODREG` |
| `TSIREG` | `CODTAB` | `TGFTAB` | `CODTAB` |
| `TSIREG` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TSIREG` | `CODREG` | `TSIBAI` | `CODREG` |
| `TSIREG` | `CODREG` | `TSICID` | `CODREG` |
| `TSIREM` | `MODULO` | `TSIIRE` | `MODULO` |
| `TSIREM` | `CODIGO` | `TSIIRE` | `CODIGO` |
| `TSIRET` | `CODIGO` | `TSIIRT` | `CODIGO` |
| `TSIRFE` | `NURFE` | `TSIRFA` | `NURFE` |
| `TSIRFE` | `NURFEDEPENDENTE` | `TSIRFE` | `NURFE` |
| `TSIRFE` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIRLG` | `SEQACESSO` | `TSIACM` | `SEQACESSO` |
| `TSIRLG` | `CODUSU` | `TSIACM` | `CODUSU` |
| `TSIRLG` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIRTD` | `TIPREG` | `TSIRTM` | `TIPREG` |
| `TSIRTD` | `CODIGO` | `TSIRTM` | `CODIGO` |
| `TSIRTM` | `CODIGO` | `TSIRTD` | `CODIGO` |
| `TSIRTM` | `TIPREG` | `TSIRTD` | `TIPREG` |
| `TSISBP` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSISESSAOITERACAO` | `CODUSU` | `TSIUSU` | `CODUSU` |
| `TSIUFS` | `CODPARCSECRECEST` | `TGFPAR` | `CODPARC` |
| `TSIUFS` | `TIPTITGNREFCPST` | `TGFTIT` | `CODTIPTIT` |
| `TSIUFS` | `CODPAIS` | `TSIPAI` | `CODPAIS` |
| `TSIUFS` | `AD_SUPERVISOR` | `TSIUSU` | `CODUSU` |
| `TSIUSU` | `CODUSU` | `TGFCER` | `CHAVE` |
| `TSIUSU` | `CODPARCPERFIL` | `TGFCTT` | `CODPARC` |
| `TSIUSU` | `CODCONTATOPERFIL` | `TGFCTT` | `CODCONTATO` |
| `TSIUSU` | `CODPARC` | `TGFPAR` | `CODPARC` |
| `TSIUSU` | `CODPARCPERFIL` | `TGFPAR` | `CODPARC` |
| `TSIUSU` | `TOPBAIXADESPESA` | `TGFTOP` | `CODTIPOPER` |
| `TSIUSU` | `TOPBAIXARECEITA` | `TGFTOP` | `CODTIPOPER` |
| `TSIUSU` | `CODVEND` | `TGFVEN` | `CODVEND` |
| `TSIUSU` | `CODCENCUSPAD` | `TSICUS` | `CODCENCUS` |
| `TSIUSU` | `CODEMP` | `TSIEMP` | `CODEMP` |
| `TSIUSU` | `CODGRUPO` | `TSIGRU` | `CODGRUPO` |

