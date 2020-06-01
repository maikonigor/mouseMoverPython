#!/bin/sh
#
# Implementacao simples dum "Manipulador de eventos de teclado" em shell script.
# Autor: Sandro Marcell (smarcell)
# <smarcell@myopera.com> | <http://www.myopera.com/smarcell/blog>
# Boa Vista, Roraima - 10/05/2011.
#
PATH="/bin:/usr/bin:/usr/local/bin"

# Define a tecla que controlara a parada do evento
tecla_controle="m"
# Boas praticas de programacao =)
# - Sempre defina as variaveis antes de utiliza-las
tecla_pressionada=""
x=0
y=0
# Poe o terminal em modo especial de interpretacao de caracteres
stty -echo -icanon min 0

# O evento ocorrera dentro deste loop
while true
do
   [ "$tecla_pressionada" = "$tecla_controle" ] && break
   # Seus codigos aqui!
   #echo "Pressione a tecla '$tecla_controle' para sair do loop." ;
   sleep 0.1s
   read tecla_pressionada
   case "$tecla_pressionada" in
     "w") y=$(expr $y - 50);;
     "s") y=$(expr $y + 50);;
     "a") x=$(expr $x - 50);;
     "d") x=$(expr $x + 50);;
   esac
   #echo $x@$y

   echo $x@$y > /dev/ttyS11
   cat /dev/ttyS11
done

# Restaura o modo padrao do terminal
stty sane

echo ">> Voce pressionou a tecla '$tecla_controle' e finalizou o loop!"

exit 0
