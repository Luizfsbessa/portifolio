Projeto OTIF
Objetivo - Criar data viz parar indicador logístico com base nas entregas realizadas.

Ferramenta - POWER BI / FIGMA
Dataset - Fictício, gerado artificialmente
Meta OTIF - 75%

Questões: 
- Calcular o % de entregas concluidas.
- Calcular o % de entregas realizadas dentro do prazo.
- Analisar o volume de entregas por região.
- Analisar periodo histórico e identificar padrões.
- Sugerir melhorias.

Analise exploratória:
-Em primeiro foi explorado a quantidade total de entregas.
	Qtd NF = COUNTROWS('Notas Fiscais')
-Com o valor total de entregas segui com a calculo de entregas efetivas sem ocorrência de sinistro.
	Qtd In Full = CALCULATE([Qtd NF],'Notas Fiscais'[In Full Delivery]="In Full")
-Para entender o nivel de serviço, realizo o calculo de entregas efetuadas dentro do prazo.
	Qtd On time = CALCULATE([Qtd NF],'Notas Fiscais'[On Time Delivery]="On Time")
-Utilizei a abordagem do mapa geografico e para apresentação da volume de entregas por região atraves de bolhas.
-Gerando uma gráfico de linha para analisar os dados históricos, pude perceber o GAP no ultimo trimestre.
  
Conclusões
Em análise ao retrospecto observa-se um GAP crônico na operação logística evidenciado pela não conformidade com a meta de OTIF.
Esse GAP se intensifica no ultimo trimestre, o que me leva a crer que estou lidando com dados de um
e-commerce que experimenta um pico de vendas em novembro, possivelmente devido à Blackfriday.
Com base nas informações apresentadas, proponho a melhoria na cadeia logística de entregas. Dada a baixa taxa de entregas
pontuais, deve-se questionar o dimencionamento da frota e a qualidade dos prestadores de serviço. Acredito que, com um 
alinhamento operacional adequado, será possível elevar os índice de OTIF. 
Dito isto, a sazonalidade do final do ano pode ser amenizada com a melhoria supracita, recomendo
fortemente um reforço temporário para lidar com o aumento de volume das demandas durante esse período.