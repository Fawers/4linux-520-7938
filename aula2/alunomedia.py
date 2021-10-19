# 1. Um aluno é aprovado se a média das 3 avaliações for superior a 6;
# 2. Caso o aluno retido possuir média igual ou superior a 4, ele está de recuperação;
# 3. Caso o aluno retido possuir média inferior a 4, ele está automaticamente retido;

# 1. Precisamos das notas para calcular a média do aluno
# 2. Precisamos calcular a média a partir das notas
# 3. Validar de o aluno está aprovado, em recuperação ou retido a partir do valor da média

# 1. Precisamos capturar cada nota do aluno e armazená-la em variáveis
# 2. A partir das notas, precisamos calcular a média e guardá-la em outra variável
# 3. Primeiro testamos see a média é maior do que 6: 3.1 Se for verdade, apresentar a
# mensagem “Aprovado”
# 4. Caso contrário, testar se a média é maior ou igual a 4. 4.1 Se for verdade, apresentar a
# mensagem “Em recuperação”
# 5. Caso contrário, apresentar a mensagem "Retido’

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media > 6:
    print("Aprovado")

elif media >= 4:
    print("Recuperação")

else:
    print("Reprovado")
