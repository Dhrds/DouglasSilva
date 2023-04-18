create table clientes (
id int auto_increment not null,
nome varchar(255) not  null,
nascimento date ,
cep varchar(9),
bairro varchar(50),
cidade varchar(50),
uf varchar(50),
rua varchar(100),
numero varchar(10),
complemento varchar(50),
profissao varchar(100),
estado_civil varchar(50),
email varchar(50),
numero varchar(16),
primary key (id)
);