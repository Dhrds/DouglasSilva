create table estoque
  (
id int auto_increment not null,
id_produto int not  null,
data_ date ,
quantidade float ,
peso float,
primary key (id),
foreign key (id_produto ) references material(id)
);