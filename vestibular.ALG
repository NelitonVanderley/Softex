Algoritmo "AlunosAprovados"
Var
nome, turma, melhorAluno, melhorAlunoA, melhorAlunoB, melhorAlunoC, melhorAlunoD,     turmaMelhorAluno: caracter
nota, maiornota, maiornotaA, maiornotaB, maiornotaC, maiornotaD: real
cont, numAprovados, turmaA, turmaB, turmaC, turmaD: inteiro
Inicio
cont<- 0
numAprovados <- 0
maiornota <- 0
turmaA <- 0
turmaB <- 0
turmaC <- 0
turmaD <- 0
maiornotaA <- 0
maiornotaB <- 0
maiornotaC <- 0
maiornotaD <- 0
Enquanto (cont<= 100) e  (cont > 0) faca
   Escreva ("Informe seu nome: ")
   Leia (nome)
   Escreva ("Informe sua nota; ")
   Leia (nota)
   Escreva ("Informe sua turma: ")
   Leia (turma)
   EscrevaL ("Aluno ", cont, " cadastrado!")
   Escolha turma
           caso "A"
                maiornotaA <- nota
                melhorAlunoA <- nome
           caso "B"
                maiornotaB <- nota
                melhorAlunoB <- nome
           caso "C"
                maiornotaC <- nota
                melhorAlunoC <- nome
           caso "D"
                maiornotaD <- nota
                melhorAlunoD <- nome
   fimescolha
   
   Se nota >=7 entao
      EscrevaL ("Aluno ", nome, " Aprovado!")
      numAprovados <- numAprovados + 1
     Escolha turma
             caso "A"
                  turmaA <- turmaA + 1
             caso "B"
                  turmaB <- turmaB + 1
             caso "C"
                  turmaC <- turmaC + 1
             caso "D"
                  turmaD <- turmaD + 1
     fimescolha
   fimse
   
   Se (nota> maiornota)   entao
     maiornota <- nota
     melhorAluno <- nome
     turmaMelhorAluno <- turma
   fimse
   cont <- cont + 1
fimenquanto
Escreval ("-----------------------------------------------------------------")
EscrevaL("Quantidade de alunos Aprovados por turma: ")
EscrevaL( "turma A : ", turmaA, " !  - Melhor Aluno foi ", melhoralunoA, " com a nota ", maiornotaA, " !")
EscrevaL( "turma B : ", turmaB, " !  - Melhor Aluno foi ", melhoralunoB, " com a nota ", maiornotaB, " !")
EscrevaL( "turma C : ", turmaC, " !  - Melhor Aluno foi ", melhoralunoC, " com a nota ", maiornotaC, " !")
EscrevaL( "turma D : ", turmaD, " !  - Melhor Aluno foi ", melhoralunoD, " com a nota ", maiornotaD, " !")
EscrevaL("Quantidade total de alunos Aprovados: ", numAprovados, " !")
EscrevaL("O Melhor aluno(a) é ", melhorAluno, ", da turma ",turmaMelhorAluno ,", com a nota ", maiornota, " !")
Fimalgoritmo
