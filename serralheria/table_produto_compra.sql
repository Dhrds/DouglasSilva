create table material (
id int auto_increment not null,
descricao varchar(255) not  null,
data_compra date ,
quantidade float,
peso float,
valor_quilo float,
valor_unidade float,
fornecedor varchar(255),
id_fornecedor int ,
primary key (id)
);