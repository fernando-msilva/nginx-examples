create table exemplos (
	id int not null primary key auto_increment,
    livro varchar(30) not null,
    cap varchar(30) not null,
    server_name varchar(20) not null
);

insert into exemplos (livro, cap, server_name) values ('nginx cookbook','1','mysql 2');
insert into exemplos (livro, cap, server_name) values ('nginx cookbook','2','mysql 2');