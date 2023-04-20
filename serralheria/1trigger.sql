delimiter $$
create trigger atualizado before insert 
on parametros_mensagem
 FOR EACH ROW 
 begin
 update verificacao set foi_verificado = 'N';
 end$$
 delimiter ;
 
 
 drop trigger atualizado;