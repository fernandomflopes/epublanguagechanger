# Conversor de idomas para arquivos epub 

Este script resolve o problema da leitura em voz alta do leitor de epubs Google Books Reader. A leitura em voz alta do google reader nao possui opcao para selecionar o idioma que sera lido, entao o usuario deve realizar a alteracao do idioma manualmente em um arquivo de metadados interno do epub. Apesar de simples, esta alteracao nescessita de alguns passos e acaba se tornando uma tarefa tediosa. Este script automatiza estes passos sendo necessario apenas especificar o caminho do epub e o idioma a ser alterado.

# Como usar
```
$ python3 main.py file.epub br
```