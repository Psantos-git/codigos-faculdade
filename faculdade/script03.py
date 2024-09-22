Alunos_menor_23 = 0
Alunos_gostando = 0
Total_Aluno = 0

parada = 0

while(parada!=1):
    idade = int(input("Informe sua idade"))
    if(idade < 23):
        Alunos_menor_23 += 1

    gostando = input("Esta Gostando Do Curso ? Responda com S para sim e N para não")
    if (gostando.upper() == "S"):
        Alunos_gostando += 1

    Total_Aluno += 1
    parada = int(input("Deseja continuar 1- para Sair e 0 para Continuar"))

print(f'Alunos que são menores de 23:{Alunos_menor_23}')
print(f'Alunos que estão gostando do curso:{Alunos_gostando}')
print(f'Quantiade de alunos que responderam a pesquisa:{Total_Aluno}')