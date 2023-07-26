# BibliotecaKa

Essa é uma aplicação que faz a gestão de uma biblioteca.

Empréstimo de Livros
Cada livro só poderá ser emprestado por um período fixo de tempo. Se desejarem desenvolver algo mais complexo, deem uma olhada na seção Modo Hard.
Devolução de Livros
Todos os livros emprestados deverão ter uma data de retorno.
Deverá ser criada uma lógica onde, se a devolução cair em um fim de semana (sábado ou domingo), a data de retorno deverá ser modificada para ser no próximo dia útil.
Caso o estudante não devolva o livro até o prazo estipulado, deverá ser impedido (bloqueado) de solicitar outros empréstimos.
Bloqueio de Novos Empréstimos
Se um estudante não efetuar a devolução dos livros no prazo estipulado, ele não poderá emprestar mais livros até completar a devolução dos anteriores. Após completar as devoluções pendentes, o bloqueio deve permanecer por alguns dias.
Usuários
O sistema deve permitir o cadastro de usuários. Deve haver, no mínimo, 2 tipos de usuários:

Estudante.
Colaborador da biblioteca.
Deve ser possível também usuários não autenticados acessarem a plataforma para visualizar informações sobre os livros, como disponibilidade, título, etc.

Funcionalidades permitidas aos estudantes:
De maneira geral, ao acessar a plataforma, um estudante pode:

Ver seu próprio histórico de livros emprestados.
Obter informações sobre livros.
"Seguir" um livro a fim de receber notificações no email conforme a disponibilidade/status do livro.
Funcionalidades permitidas aos colaboradores:
De maneira geral, ao acessar a plataforma, um colaborador pode:

Cadastrar novos livros.
Emprestar livros.
Verificar o histórico de empréstimo de cada estudante.
Verificar status do estudante (se está bloqueado não pode emprestar uma nova cópia durante determinado tempo).
