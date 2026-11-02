<!-- Text extracted with pdftotext -layout from slr-mini-tutorial.pdf; original language kept. -->

                                                                                                                                                                                          06/10/2026

                                                                          MESTRADO EM ENGENHARIA INFORMÁTICA – Preparação para a Dissertação (PREPD)
                                                                                                                             2026/2027

     Systematic Literature Review & State of the Art Module

          MINI-SLR · TUTORIAL DE AUTOAPRENDIZAGEM

                       “You have to start your Master’s dissertation tomorrow.
                            How would you find out what is already known?”

                                                                                              Ana Maria Madureira

1

MINI-SLR · ATIVIDADE PRÁTICA

Objetivos da Atividade: da Questão de Investigação à Evidência

Mini-SLR com PRISMA · aplicação orientada ao contexto de uma dissertação de Mestrado em Engenharia Informática

      1 · Compreender o processo                                               2 · Tomar decisões metodológicas                             3 · Garantir transparência

Reconhecer as etapas de uma SLR e perceber a função                         Transformar Research Questions em conceitos,            Interpretar e construir um fluxo PRISMA que torne
de cada uma: protocolo, pesquisa, seleção, avaliação,                       queries, critérios de inclusão/exclusão e campos de     explícito como se passou dos resultados da pesquisa
extração, síntese e reporting.                                              Data Extraction coerentes.                              ao corpus final.

        4 · Sintetizar criticamente                                             5 · Identificar um Research Gap                         6 · Transferir para a dissertação

Passar de uma lista de papers para padrões                                  Distinguir observação, limitação e gap e construir uma  Aplicar o processo ao próprio tema de investigação e
comparáveis: técnicas, dados, avaliação, resultados,                        cadeia defensável Evidence → Limita on → Gap →          produzir um mini-protocolo que possa evoluir para
limitações e qualidade da evidência.                                        Research Opportunity.                                   uma revisão real.

No final, o estudante deverá conseguir justificar não apenas quais estudos encontrou, mas
como os selecionou, o que aprendeu com eles e por que razão existe espaço para uma nova

                                                contribuição.

               Atividade para alunos de Mestrado em Engenharia Informática

2
                                                                                                                                                                                              06/10/2026

MINI-SLR · TUTORIAL DE AUTOAPRENDIZAGEM

Como utilizar este tutorial

Pode percorrê-lo autonomamente, mesmo sem ter assistido à aula presencial

           1 · Siga a sequência                                                   2 · Pare nos desafios                                       3 · Replique no seu tema

Não salte diretamente para o PRISMA. A lógica                          Sempre que encontrar uma pergunta ou “DESAFIO”,                Em cada etapa, substitua o exemplo XAI/CDSS pelo
começa nas Research Questions e termina na síntese                     tente responder antes de avançar. Compare depois               tema da sua dissertação: conceitos, query, critérios e
e no research gap.                                                     com o exemplo seguinte.                                        extração.

                           Como ler os slides                                                                         Regra de autoavaliação

AZUL/VERDE = decisão ou procedimento metodológico                                             Pergunte: “Consigo explicar por que fiz esta escolha e consigo reproduzi-la mais tarde?”
LARANJA = ponto de atenção/limitação                                                          Se não, registe a decisão antes de avançar.
Caixas finais = interpretação ou resultado esperado

                   Tempo sugerido: 45–60 min para compreender o exemplo + 20–30 min para começar a adaptar o protocolo ao seu tema.

               Tutorial autónomo · Mestrado em Engenharia Informática

3

MINI-SLR · TUTORIAL DE AUTOAPRENDIZAGEM

Visão global: o que acontece numa SLR?

Use este mapa para se orientar durante o tutorial

  1 · PROTOCOL         2 · SEARCH                                           3 · SELECT            4 · ASSESS         5 · EXTRACT       6 · SYNTHESISE        7 · REPORT

Objetivo + RQs     Conceitos + query                                   Deduplicar             Quality assessment  Matriz estruturada  Comparar padrões   PRISMA + respostas
Scope + critérios  Bases + search log                                  Screening + full text  Risco de bias       Dados por RQ        Limitações + gaps  Conclusões + threats

                           O processo é iterativo                                                                       Onde entra o PRISMA?

Uma pilot search pode revelar novos sinónimos; alterações são possíveis, mas devem ser        PRISMA documenta sobretudo a identificação e seleção. Não substitui a qualidade da
justificadas e documentadas.                                                                  query, avaliação, extração ou síntese.

                   O exemplo XAI/CDSS irá percorrer estas sete etapas, sempre com números e decisões explícitas.

               Tutorial autónomo · Mestrado em Engenharia Informática

4
01 · PURPOSE                                                                                                                                                                                                   06/10/2026

From Literature to Knowledge                                                                                                                                                                                02

                   Mestrado em Engenharia Informática · Revisão Sistemática da Literatura

5

MINI-SLR · ATIVIDADE PRÁTICA

Atividade: Construir e Interpretar uma Mini-SLR com PRISMA

Mestrado em Engenharia Informática · do problema de investigação ao research gap

         Objetivo da atividade                                                                 Competências a desenvolver                               Caso de Engenharia Informática

Compreender, através de um caso completo, como                                             Formular RQs; construir queries; definir critérios;        Explainable AI em Clinical Decision Support Systems:
uma revisão sistemática transforma uma questão de                                          interpretar PRISMA; estruturar data extraction;            técnicas XAI, modelos de ML/DL, dados, avaliação e
investigação num corpus selecionado, evidência                                             distinguir descrição de síntese crítica; derivar research  interação com utilizadores clínicos.
sintetizada e um gap defensável.                                                           gaps.

                    O que os alunos irão fazer                                                                                                   Output esperado

Acompanhar uma mini-SLR passo a passo, discutir decisões metodológicas e, em                                           No ﬁnal, cada grupo deverá conseguir explicar a cadeia: RQ → Search Strategy →
pontos-chave, decidir como avançariam: termos de pesquisa, seleção, extração e                                         Selec on → PRISMA → Extrac on → Results → Cri cal Synthesis → Research Gap.
interpretação.

Pergunta orientadora: Como demonstramos, de forma transparente e reproduzível, que existe espaço para uma nova contribuição científica?

               Caso pedagógico: resultados simulados para aprendizagem do processo; não constituem uma SLR publicada.

6
                                                                                                                                                                                                                                                             06/10/2026

MINI-SLR · ATIVIDADE PRÁTICA

1 · Definir o problema e as Research Questions

Antes de pesquisar, precisamos de saber exatamente o que queremos descobrir

                 Objetivo                                        Âmbito                                                               Unidade de análise

Analisar abordagens recentes de Explainable AI  2020–2026 · estudos empíricos · AI/ML aplicado a                            Artigos científicos que implementam e avaliam
(XAI) em sistemas de apoio à decisão clínica    CDSS · componente de explicabilidade.                                       mecanismos XAI em contexto de decisão clínica.
baseados em IA.

Which XAI techniques are most frequently used in AI-based CDSS?                                                        RQ1
How is the explainability of these systems evaluated?                                                                  RQ2
What limitations and research gaps are reported?                                                                       RQ3

                                     DESAFIO AOS GRUPOS · Que campos terão de extrair de cada paper para responder às três RQs?

               Caso pedagógico: resultados simulados para aprendizagem do processo; não constituem uma SLR publicada.

7

MINI-SLR · TUTORIAL DE AUTOAPRENDIZAGEM

Antes da query: onde devo pesquisar?

Google, Google Scholar e bases bibliográficas não desempenham o mesmo papel numa revisão sistemática.

                        Scopus                                     Web of Science                                                                                                                                                         IEEE Xplore

Base bibliográfica multidisciplinar             Base bibliográfica multidisciplinar                                                                                                                                 Engenharia, Informática, IA, eletrónica
 PESQUISA PRINCIPAL                              PESQUISA PRINCIPAL                                                                                                                                                  PESQUISA PRINCIPAL

                 ACM Digital Library                               Google Scholar                                                                                                                                                           Google

Computing / Computer Science                    Motor de pesquisa académico                                                                                                                                         Pesquisa Web / grey literature
 PESQUISA PRINCIPAL                              COMPLEMENTAR                                                                                                                                                        SÓ SE JUSTIFICADO

                            Para Engenharia Informática                                                                                                      E ChatGPT / GenAI?

Uma combinação frequente é Scopus + Web of Science + IEEE Xplore + ACM DL. A escolha                                        Pode apoiar conceitos, sinónimos e refinamento da query. Não substitui a pesquisa
final deve ser justificada pela RQ e pela cobertura necessária.                                                             documentada nas bases bibliográficas nem constitui, por si só, uma systematic search.

                                                                                                          Regra: escolha as fontes antes de executar a pesquisa e justifique por que são adequadas ao seu domínio.

8
                                                                                                                                                                                                                   06/10/2026

    MINI-SLR · TUTORIAL DE AUTOAPRENDIZAGEM

    Searching ≠ Screening ≠ Reading ≠ Synthesis

    Encontrar referências é apenas o início: cada etapa responde a uma pergunta diferente e produz um output diferente.

            1 · SEARCHING                                 2 · SCREENING                                                                                                        4 · SYNTHESIS

    Onde está a literatura potencialmente             Quais destes records cumprem os          3 · READING + EXTRACTION                                                  O que significa a evidência quando
    relevante?                                        critérios?
                                                                                               O que diz cada estudo incluído?                                           comparada?
    INPUT RQs + conceitos + search string  →
    AÇÃO executar a query nas bases                   INPUT records recuperados                →                                                    → INPUT dados extraídos
    OUTPUT conjunto inicial de records                AÇÃO deduplicar + title/abstract + full             INPUT corpus final
                                                      text                                                AÇÃO leitura crítica + extraction matrix             AÇÃO comparar padrões, diferenças e
    Ex.: 163 records identificados                    OUTPUT estudos elegíveis                            OUTPUT evidência estruturada por RQ
                                                                                                                                                               limitações
                                                      Ex.: 18 studies included
                                                                                                                                                               OUTPUT respostas às RQs + research

                                                                                               Ex.: técnica XAI, avaliação, limitações                                   gaps

                                                                                                                                                                         Ex.: technical XAI ≠ clinical usefulness

                                                                                                                Erro frequente
                   “Encontrei 50 ar gos no Google/Scopus, portanto já tenho a revisão da literatura.” → Não. A pesquisa gera candidatos; a revisão exige seleção, leitura crítica, extração e síntese.

                                                                     Pergunta de autoavaliação: Em que etapa estou agora — e qual é o output que devo produzir antes de avançar?

                                                                                                            SEARCH encontra · SCREENING seleciona · READING extrai evidência · SYNTHESIS constrói conhecimento

9

    MINI-SLR · TUTORIAL DE AUTOAPRENDIZAGEM

    Como pesquisar numa base de dados: exemplo Scopus

    A interface pode mudar; o procedimento metodológico mantém-se.

    Documents Authors Affiliations Advanced Search                                             SEARCH                        1 · Escolha Documents

                                      Search documents                                                  Procura literatura por tópico. Author/Affiliation servem outros objetivos.

     Cole aqui a search string — não a pergunta em linguagem natural.                                                   2 · Pesquise nos campos certos

                   Search field                             Limits / Filters                            Em Scopus, TITLE-ABS-KEY é uma opção habitual para título, abstract e
                                                                                                        keywords.
    Article title, Abstract, Keywords      Year · document type · language/access, apenas se previstos
                                                                                                                           3 · Use Boolean operators
                                          A er Search → Results
                                                                                                        OR liga sinónimos; AND combina conceitos; parênteses preservam a lógica.
    1) registe o número de resultados
    2) verifique se aparecem artigos claramente relevantes                                                                     4 · Exporte e registe
    3) refine apenas se a pilot search o justificar
    4) Export → RIS / CSV / BibTeX                                                                      Guarde query exata, data, filtros, n de resultados e ficheiro exportado.

                                           Exemplo de sintaxe avançada Scopus: TITLE-ABS-KEY( ("explainable AI" OR XAI) AND ("clinical decision support" OR CDSS) )
                                                                          Esquema didático da interface. Consulte a interface atual da Scopus para executar a pesquisa.

10
                                                                                                                                                                                                                            06/10/2026

    MINI-SLR · TUTORIAL DE AUTOAPRENDIZAGEM

    A mesma estratégia em plataformas diferentes

    A lógica conceptual mantém-se, mas a sintaxe e os campos de pesquisa podem variar.

                              IEEE Xplore — Advanced Search                                                                                         Scopus — Advanced Search

    • introduza keywords, phrases ou Boolean expression                                                                • pode usar field codes
    • AND / OR / NOT em maiúsculas                                                                                     • TITLE-ABS-KEY(...) procura em title + abstract + keywords
    • selecione Data Fields quando necessário                                                                          • combine blocos com AND e sinónimos com OR
    • execute Search e refine apenas segundo o protocolo                                                               • registe a query exatamente como foi executada

              RQ             → CONCEPTS                               →  QUERY                                         → DATABASE                        →  EXPORT                         →  LOG

    What do I need to know?         terms + synonyms                     Boolean string                                       Scopus / WoS / IEEE / ACM     RIS / CSV / BibTeX                date + query + filters + n

                       Google Scholar                                                            Google                                                                       Replication rule

    Útil para descoberta complementar, “Cited by”, localizar artigos     Útil sobretudo para grey literature, normas, relatórios ou                         Outro investigador deve conseguir repetir a mesma query, nos
    e snowballing. Não deve ser a única fonte de uma SLR.                documentação quando o protocolo prevê essas fontes.                                mesmos campos e filtros, e explicar diferenças nos resultados.

                             Não copie cegamente a mesma sintaxe entre bases: adapte a query e documente a versão executada em cada plataforma.

11

    MINI-SLR · ATIVIDADE PRÁTICA

    2 · Transformar as RQs numa Search Strategy

    Conceitos → sinónimos → Boolean query → fontes → critérios

                     Explainability                                                     Decision Support                                                                       Healthcare

    “explainable AI” · XAI · explainability · interpretability           “clinical decision support” · CDSS · decision support                              healthcare · medical · clinical
                                                                         system

                                                                                      Boolean query

    ("explainable artificial intelligence" OR "explainable AI" OR XAI OR explainability OR interpretability)
    AND ("clinical decision support" OR CDSS OR "clinical decision support system")
    AND (healthcare OR medical OR clinical)

                                      Fontes                                                                                                     Critérios essenciais

    Scopus · IEEE Xplore · Web of Science                                                                              Include: empirical AI/ML + CDSS + XAI
    Janela: 2020–2026                                                                                                  Exclude: review/editorial · non-clinical · no empirical evaluation

                             DISCUSSÃO · O que acontece à precision e recall se retirarmos o bloco Healthcare?

               Caso pedagógico: resultados simulados para aprendizagem do processo; não constituem uma SLR publicada.

12
                                                                                                                                                                                                                                     06/10/2026

MINI-SLR · ATIVIDADE PRÁTICA

3 · Executar a pesquisa e documentar o screening

Search results ≠ unique studies ≠ included evidence

Scopus                                                                                                                 74                                               Identification
IEEE Xplore
                                                                                                                                                         163 records

                                                                                                                       48

Web of Science                                                                                                                                            Deduplication
                                                                                                                       41

                                                                                                                                            31 duplicates → 132 unique records

                                                                                                                                                                       Title / abstract screening

                                                                                                                                                         86 excluded → 46 retained

                   QUESTÃO                                                                                                                                              Retrieval
                   Porque é metodologicamente insuficiente escrever apenas “foram selecionados 18 artigos relevantes”?

                                                                                                                                                         3 unavailable → 43 full texts assessed

               Caso pedagógico: resultados simulados para aprendizagem do processo; não constituem uma SLR publicada.

13

MINI-SLR · TUTORIAL DE AUTOAPRENDIZAGEM

4 · Figura PRISMA: como ler o processo de seleção

O diagrama documenta, passo a passo, como passámos de 163 registos identificados para 18 estudos incluídos.

IDENTIF            Records identified from databases                                                                   Records removed before screening                                 1 · IDENTIFICATION
ICATIO             Scopus 74 · IEEE Xplore 48 · WoS 41                                                                          Duplicates removed                      Quantos registos foram encontrados e onde?
                                                                                                                                        n = 31
   N                            TOTAL n = 163

                   Unique records screened                                                                             Records excluded                                                          2 · SCREENING
                         Title + abstract                                                                                     n = 86                                    Que registos permanecem após duplicados e análise de
                              n = 132
                                                                                                                                                                                                título/abstract?
          SCREEN
            ING    Reports sought for retrieval                                                                              Reports not retrieved                                                 3 · ELIGIBILITY
                                n = 46                                                                                                 n=3                              Após leitura integral, que estudos cumprem realmente os
         ELIGIBIL
             ITY    Full-text reports assessed                                                                                    Full texts excluded · n = 25                                       critérios?
                            for eligibility                                                                                       No real XAI: 8 · Not CDSS: 6
          INCLUD                n = 43                                                                                 No empirical eval.: 5 · Insufficient methods: 4
             ED                                                                                                                  Duplicate/extended study: 2

14                 Studies included in synthesis                                                                                                                                                      4 · INCLUDED
                                 n = 18                                                                                                                                     O corpus final é a base para Data Extraction e síntese.

                                                                                                                                                                        ↓ con nuidade → remoção / exclusão

                   Como interpretar: cada seta representa uma decisão documentada. Os números devem ser coerentes entre etapas e os motivos de exclusão devem ser registados.
                                                                           Exemplo pedagógico com contagens simuladas · estrutura inspirada no PRISMA 2020 (Page et al., 2021).
                                                                                                                                                                                                                  06/10/2026

MINI-SLR · ATIVIDADE PRÁTICA

5 · Construir a Data Extraction Matrix

Não começar a escrever: primeiro estruturar a evidência

Study   Domain                 AI        XAI       Data          Evaluation                                                           Users       Limitations
 S01   Cardiology           XGBoost      SHAP      EHR          Fidelity+expert                                                      Clinicians   Single centre
                                                                                                                                                 No external val.
S02    Radiology            CNN          Grad-CAM  Images                                                              Visual          None       Small sample
                                                                                                                                       None
S03    ICU                  Transformer  SHAP      EHR                                                                 Quantitative  Clinicians     Few users

S04    Oncology             RF           LIME      Tabular                                                             Usability                                               RQ3

                          RQ1                                                    RQ2                                                                           Limitations + validation + generalisation

     XAI technique + AI model + context                     Evaluation + users + metrics

                            DESAFIO · Identifiquem um campo que falta e um campo que poderia ser dispensável para estas RQs.

               Caso pedagógico: resultados simulados para aprendizagem do processo; não constituem uma SLR publicada.

15

MINI-SLR · ATIVIDADE PRÁTICA

6 · Sintetizar resultados: responder às RQs

Contar é apenas o início; a interpretação é o objetivo
                     Técnicas XAI identificadas nos 18 estudos

       SHAP                                                                                                            9                                     RQ1 · Descrição

                                                                                                                                     SHAP surge em 9/18 estudos; LIME e Grad-CAM em 5 cada.

       LIME                                                                                                            5

                Grad-CAM                                                                                               5
     Feature importance
                                                                                                                                                 Interpretação correta
                 Attention
                                                                                                                       4             Frequência de utilização não demonstra superioridade, robustez ou utilidade

                                                                                                                                     clínica.

                                                                                                                       3

       Counterfactuals                                                                                                 2

                                                   Número de estudos (categorias não exclusivas)                                                            Próxima pergunta

                                         Como interpretar                                                                            Como foi avaliada a explicabilidade — tecnicamente ou com utilizadores
                                                                                                                                     reais?
SHAP é a técnica mais frequente neste exemplo. Isso descreve utilização — não prova que seja a técnica
mais eficaz ou clinicamente mais útil.

               Caso pedagógico: resultados simulados para aprendizagem do processo; não constituem uma SLR publicada.

16
                                                                                                                                                                                                 06/10/2026

MINI-SLR · ATIVIDADE PRÁTICA

7 · Da descrição à Critical Synthesis

A discrepância entre avaliação técnica e valor para o utilizador revela um padrão

Technical / quantitative                                                                                               13

Visual / qualitative                                                                                                   9                         RQ3 · Padrões de limitação
With clinicians
Formal usability                                                                                                           • Limited clinical validation

                                                                                                                           • Small/single-centre datasets

                                                                                                                       5   • Technical rather than cognitive evaluation
                                                                                                                           • Limited external validation

                                                                                                                           • Little evidence of decision impact

                                                                                                                       3

Decision impact                                                                                                        2

                                                                        Critical synthesis

Most studies can generate explanations; far fewer demonstrate that those explanations are understandable, useful or decision-relevant for clinicians.

               Caso pedagógico: resultados simulados para aprendizagem do processo; não constituem uma SLR publicada.

17

MINI-SLR · ATIVIDADE PRÁTICA

8 · Derivar o Research Gap e a Research Opportunity

O gap deve ser rastreável à evidência — não apenas plausível

         EVIDENCE               OBSERVATION                                                                                    LIMITATION                    GAP                           OPPORTUNITY

Post-hoc XAI is common.   Few studies evaluate with                                                                    Technical XAI ≠ clinical  Insufficient evidence of        Human-centred XAI designed and
                          clinicians.                                                                                  usefulness.               improved understanding,         evaluated with clinicians.
                                                                                                                                                 calibrated trust and decision-
                                                                                                                                                 making.

                                                                                  Conclusão da mini-SLR

                   O corpus ilustrativo sugere um gap entre technical explainability e clinically meaningful explainability: os mecanismos XAI são frequentes, mas a evidência de valor clínico
                   human-centred permanece limitada.

                                          REFLEXÃO FINAL · Que evidência adicional seria necessária para tornar este gap mais convincente?

               Caso pedagógico: resultados simulados para aprendizagem do processo; não constituem uma SLR publicada.

18
                                                                                                                                                                                                                                         06/10/2026

MINI-SLR · ATIVIDADE PRÁTICA

9 · Aplicação pelos grupos: construir um Mini-SLR Protocol

Transferir o processo para um problema de Engenharia Informática

          Escolher um problema                                                           Desenhar o protocolo                                  Planear a evidência

Ex.: LLMs for software testing · AI for cybersecurity ·                       2 RQs · concept blocks · Boolean query · 3 fontes ·  Data extraction fields · expected synthesis · como
federated learning · misinformation detection · code                          inclusion/exclusion criteria.                        reconheceriam um research gap.
generation.

                                                                              Output do grupo — 1 página / 1 slide

1. Research problem + 2 RQs
2. Search string + databases
3. 4 inclusion + 4 exclusion criteria
4. 6–8 data extraction fields
5. Um exemplo de Evidence → Limita on → Possible Gap

                            Tempo sugerido                                                                                                                    Peer review

15–20 min de trabalho em grupo                                                                                                  5 min: outro grupo testa coerência e rastreabilidade do protocolo

               Atividade para alunos de Mestrado em Engenharia Informática · foco em desenho metodológico e pensamento crítico

19

MINI-SLR · ATIVIDADE PRÁTICA

Passos Seguintes: da Mini-SLR Pedagógica a uma Revisão Sistemática Real

Exemplo passo a passo aplicado ao tema XAI em Clinical Decision Support Systems

                                1 · Freeze the protocol                                                                                                          5 · Full-text + quality

Finalizar RQs, scope, bases, query, critérios e plano de quality assessment.                                                    Avaliar elegibilidade integral e qualidade metodológica com critérios previamente definidos.
Ex.: RQ1–RQ3 + Scopus/IEEE/WoS + 2020–2026.                                                                                     Ex.: clareza do método, dataset, baselines, validação, threats to validity.

                                  2 · Pilot the search                                                                                                          6 · Extract consistently

Executar a query numa base; inspecionar 20–30 resultados; identificar termos em falta e falsos                                  Pilotar a extraction form e preencher a matriz para todos os estudos incluídos.
positivos.                                                                                                                      Ex.: AI model, XAI, dataset, metrics, clinicians, findings, limitations.
Ex.: acrescentar “decision support system*” se necessário.
                                                                                                                                                                 7 · Synthesize by RQ
                                   3 · Run & export
                                                                                                                                Agrupar e comparar estudos; procurar convergências, divergências, heterogeneidade e força da
Executar a pesquisa final em todas as bases e exportar metadados completos.                                                     evidência.
Ex.: CSV/RIS/BibTeX com DOI, abstract, keywords e source.                                                                       Ex.: technical XAI evaluation vs clinician evaluation.

                              4 · Deduplicate & screen                                                                                                     8 · Report & position research

Remover duplicados; aplicar IC/EC a title/abstract; registar decisões e motivos.                                                Atualizar PRISMA, responder às RQs, discutir limitações da própria review e derivar o gap/contribuição.
Ex.: 163 → 132 → 46.                                                                                                            Ex.: human-centred clinical XAI evaluation.

                                         Deliverables finais: protocolo + search log + screening log + quality assessment + extraction matrix + PRISMA + síntese por RQ + limitations + research gap.

               Do exercício ao trabalho de dissertação: tornar cada decisão rastreável, justificável e reproduzível.

20
                                                                                                                                                                                      06/10/2026

    MINI-SLR · TUTORIAL DE AUTOAPRENDIZAGEM                                                                                                    ✓ Search Strategy

    Checklist de autoaprendizagem                                                                            Decompor o tema em conceitos/sinónimos e construir uma Boolean query.

    Confirme que já consegue transferir o método para o seu tema de dissertação

                                       ✓ Research Questions

        Formular RQs específicas e indicar os dados necessários para lhes responder.

                                          ✓ Selection                                                                                               ✓ PRISMA

    Definir inclusion/exclusion criteria antes da seleção dos estudos.                                       Explicar cada número do fluxo e a razão das exclusões.

                                   ✓ Quality & Extraction                                                                                     ✓ Critical Synthesis

    Distinguir eligibility de quality assessment e criar uma extraction matrix.                              Comparar estudos por padrões, em vez de os resumir autor a autor.

                                        ✓ Research Gap                                                                                             ✓ Next step

    Demonstrar Evidence → Limita on → Gap → Research Opportunity.                                            Identificar a próxima ação concreta para iniciar a SLR do próprio tema.

                                                                                 Se alguma resposta ainda não for clara

    Volte à etapa correspondente e replique o exemplo com o seu próprio tema.

    Objetivo final: autonomia para iniciar e documentar uma revisão sistemática no contexto da dissertação.

21
