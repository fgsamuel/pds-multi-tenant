# Grupo IndexOutOfBoundsException

## Descrição

A ideia é criar uma aplicação multi-tenant utilizando a estratégia de um banco de dados para cada tenant.

## O que falta fazer

- [ ] testes, testes e mais testes
- [ ] Documentação
- [ ] Criar duas instâncias separadas de Admin. Um para o tenant e outro para backoffice geral
- [ ] Mover a lógica de criação do banco para um arquivo separado
- [ ] Criar um middleware para acionar a criação do banco ao salvar o tenant
- [ ] Salvar a conexão com o banco como url (dj_database_url)
- [ ] Mover a classe `Database` do `settings` para um arquivo separado
- [ ] Verificar a utilização do `dramatiq` para gestão de filas
- [ ] Mudar a estratégia de alteração de tenant por subdomínio (?)
- [ ] Lançar erro 404 quando o tenant não for encontrado
