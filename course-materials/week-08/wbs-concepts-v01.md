<!-- Text extracted with pdftotext -layout from wbs-concepts-v01.pdf; original language kept. -->

PREPD 2026/2027

Planeamento da Dissertação
     Construção da WBS

               Alberto Borges Pereira
                    abp@isep.ipp.pt
Ciclo de vida do projeto e principais outputs
Elementos a adotar:
Âmbito:

 – Âmbito do Produto: O que se espera que o produto seja
 – Âmbito do Projeto: O que se espera que o projecto faça
 – Requisitos:

     • Técnicos, Funcionais, Qualidade, etc.
 – Deliverable / Entregável: Entrega do projecto
 – Work Package: Um pacote de trabalho pode ser descrito, estimado,

     agendado, monitorizado e controlado
 – Restrições, Pressupostos, Exclusões
 – Elaboração progressiva, Rolling Wave
 – Scope Creep, Gold Plating

Internal Use Only
EAP / WBS:

 –Técnica de gestão do âmbito com as seguintes características:

      • Decomposição gráfica em árvore, top-down, completa, detalhe variável com detalhe crescente
      • Orientada aos entregáveis / deliverables
      • Sistema de templates para permitir reutilização
      • Trabalho / entregas não identificadas na WBS estão fora do âmbito
      • Tarefas terminais: 8 a 80 horas, objetivas, estimáveis, com deliverable
      • Base da estimativa (bottom-up) do tempo, custo, recursos e da identificação de riscos
      • Dicionário com informação complementar

Internal Use Only
Entregáveis:

 – Incluem
    • Elementos que compõem o produto ou serviço
    • Resultados auxiliares (documentação, gestão de projeto,…)

 – Podem ser identificados em função de:
    • Natureza do produto (Exº Documentação, Software, Formação,…)
    • Arquitectura técnica do produto (Exº de Válvulas, Casco, Motor,…)
    • Funcionalidade a entregar (Exº Funcionalidades de facturação,
        venda,.. )

Internal Use Only
Exemplo:

                                                                               Título do Organigrama

                                                                                          (1) Projecto
                                                                                        Sistema de GC

                                                                                           57,18 PM

                                            (1.1) Incremento 1                                                                                              (1.2) Incremento 2
                                                  16,3 PM                                                                                                        40,88 PM

(1.1.1) Gestão                                                                 (1.1.2) Desenvolvimento                                                      (1.2.1) Gestão  (1.2.2) Desenvolvimento
   2,445 PM                                                                            13,855 PM                                                               6,132 PM             34,748 PM

      Gestão                    Desenho                                        Codificação                                      Teste       Integração        Gestão              Desenho
    Qualidade                   (1.1.2.1)                                        (1.1.2.2)                                    (1.1.2.3)      (1.1.2.4)      Qualidade             (1.2.2.1)
     (1.1.1.1)                 2,4939 PM                                        8,313 PM                                     1,1084 PM                       (1.1.1.1)            5,62 PM
    1,467 PM                                                                                                                                1,9397 PM       3,6792 PM
                                                                                                                                                                                Codificação
      Gestão      SGDB            GUI         Processamento       SGDB             GUI        Processamento     SGDB            GUI         Processamento     Gestão              (1.2.2.2)
     (1.1.1.2)  (1.1.2.1.1)    (1.1.2.1.2)       (1.1.2.1.3)    (1.1.2.2.1)    (1.1.2.2.2)       (1.1.2.2.3)  (1.1.2.3.1)    (1.1.2.3.2)       (1.1.2.3.3)   (1.1.1.2)           18,72 PM
    0,978 PM                                                                                                                                                2,4528 PM
                                                                                                                                                                                    Teste
                  G Stock        G Stock        G Stock           G Stock        G Stock        G Stock         G Stock        G Stock        G Stock                             (1.2.2.3)
                (1.1.2.1.1.1)  (1.1.2.1.2.1)  (1.1.2.1.3.1)     (1.1.2.2.1.1)  (1.1.2.2.2.1)  (1.1.2.2.3.1)   (1.1.2.3.1.1)  (1.1.2.3.2.1)  (1.1.2.3.3.1)                         2,50 PM

                Facturação     Facturação     Facturação        Facturação     Facturação     Facturação      Facturação     Facturação     Facturação                           Protótipo
                (1.1.2.1.1.2)  (1.1.2.1.2.2)  (1.1.2.1.3.2)     (1.1.2.2.1.2)  (1.1.2.2.2.2)  (1.1.2.2.3.2)   (1.1.2.3.1.2)  (1.1.2.3.2.2)  (1.1.2.3.3.2)                         (1.2.2.4)
                                                                                                                                                                                  3,54 PM
                    Caixa          Caixa          Caixa             Caixa          Caixa          Caixa           Caixa          Caixa          Caixa
                (1.1.2.1.1.3)  (1.1.2.1.2.3)  (1.1.2.1.3.3)     (1.1.2.2.1.3)  (1.1.2.2.2.3)  (1.1.2.2.3.3)   (1.1.2.3.1.3)  (1.1.2.3.2.3)  (1.1.2.3.3.3)                        Integração
                                                                                                                                                                                  (1.2.2.5)
                                                                                                                                                                                  4,37 PM

Internal Use Only
EAP / WBS:

  – Decomposição completa:
      • Não deve existir nada que seja esperado pelo cliente que não seja atribuível a uma
           componente da WBS

  – Decomposição hierárquica:
      • O âmbito de uma componente é exactamente igual à soma do âmbito das suas
           subcomponentes
      • Ou seja, não fica retida nenhuma funcionalidade na “componente mãe” (nota: poderá
           não ser aplicável com os critérios de qualidade)

  – Consistência dos critérios de decomposição:
      • Quando uma componente é decomposta para o nível seguinte, deve ser utilizado
           apenas um critério para todas as suas subcomponentes

Internal Use Only
Entregável:

  – Critérios de Progresso

           • mensuráveis
           • Regra 0/100; 50/100; 0/50/100, etc.

  – Critérios de aceitação

           • Objetivos
           • Não ambíguos

   Diz-se que os requisitos de uma componente estão definidos de forma verificável quando:

   • A sua consecução pode ser verificada de acordo com um critério objetivo do tipo “Sim/Não”, ausente de
      ambiguidade

   • Em face da especificação dos critérios do produto desenvolvido, duas partes independentes tirariam a mesma
      conclusão (i.e. Sim/Não) sem necessidade de realizarem pressupostos

   A forma mais eficaz (nem sempre possível) de assegurar a verificabilidade consegue-se através da quantificação
   dos critérios

Internal Use Only
Dicionário da WBS:

  • Inclui informação adicional sobre os elementos da WBS

  • Alguns elementos:
       – código
       –Descrição adicional
       –Critérios de progresso
       –Critérios de aceitação (entregáveis)
       –Restrições técnicas, orçamentais ou outras
       –Tipos de recursos necessários
       –Formas de estimar o custo
       –Milestones
       –Responsável ou Owner
       –Critérios de qualidade
       –Etc.

Internal Use Only
            Exemplo de WBS

Internal Use Only
Elementos retirados do Project Charter:

Nome do Projeto:       Construção de uma moradia Data: 24/10/2024
Descrição
                       Este projeto consiste na construção de uma moradia após a escolha do
                       terreno e o projeto de construção.

Principais Stakeholders Família, Câmara municipal, vizinhos, Empreiteiro

Requisitos principais  • 4 quartos, 3 Wc, sala, cozinha, escritório
Principais entregas    • Piso térreo
                       • Classe A+
                       • Entre 250 e 350 m2
                       • Garagem para 4 carros

                       • Maqueta 3D
                       • Estrutura
                       • Revestimentos
                       • Jardins
                       • Passeios

Internal Use Only
         Estrutura da EAP / WBS por ciclo de vida

                                              1. Projeto

         1.1 Planeamento                           1.2                                                   1.3
                                              Construção                                            Acabament

  1.1.1  1.1.2 planos de    1.2.1               1.2.2                             1.2.3     1.3.1         os   piscina
Maqueta  especialidades   Estrutura           Revestim                          Instalaçõ  Jardins
                                                                                                        1.3.2
   3D                                           entos                               es               passeios

                          1.2.1.1   1.2.1.2    1.2.2.1       1.2.2.2  1.2.3.1     1.2.3.2
                          Pilares  Alvenaria  Caixilhari  pavimentos    Inst    Canalizaçõ

                                        s         as                  elétrica       es

Internal Use Only
Dicionário da EAP / WBS

Dicionário da      Tipo        Descrição adicional / critérios de aceitação           Critérios de progresso
EAP                Fase
                               Será contratado um arquiteto e um engenheiro de        Maqueta entregue – 25%
1.1                            eficiência energética.                                 Maquete aprovada - 50%
Planeamento                    Esta fase só será concluída após aprovação formal      Planos de especialidades entregues –
                               dos seus entregáveis.                                  75%
1.1 Maqueta        Entregável                                                         Planos de especialidades aprovados –
3D                             Deverá ser realizada com um software próprio e         100%
                               compatível para visualização noutros Pcs. Deverá
1.2 Planos de      Entregável  ter um versão que inclua a decoração. Deverão ser      Maqueta exterior – 25%
especialidade                  enviadas duas versões.                                 Maqueta interior – 50%
                               O cliente tem 15 dias para aprovar.                    Maquete inicial entregue – 75%
1.2.2.1            Pacote de                                                          Maquete final entregue e aprovada –
Caixilharias       trabalho    Deverão ser realizados os planos de especialidade      100%
                               por engenheiros qualificados e supervisionados
                               pelo arquiteto. Deverá existir um plano de eficiência  Planos de especialidade entregues –
                               energética.                                            25%
                               O cliente tem 15 dias para aprovar.                    Plano de eficiência energética entregue –
                                                                                      50%
                               Deverão ter eficiência energética A+. A sua            Planos aprovados – 75%
                               instalação será supervisionada pelo Eng de             Planos licenciados – 100%
                               eficiência energética
                                                                                      7 janelas – 10% cada
                                                                                      2 portas – 10% cada
                                                                                      Aprovação - 10%

Internal Use Only
PREPD 2026/2027

Planeamento da Dissertação
     Construção da WBS

               Alberto Borges Pereira
                    abp@isep.ipp.pt
