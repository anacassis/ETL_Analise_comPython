create table materias(
	id int primary key auto_increment not null, 
    nome_materia varchar(100));
   
select * from materias;
create table estudantes_materias(
	estudante_id int not null, 
    materia_id int not null, 
    foreign key (estudante_id) references estudantes(id),
    foreign key (materia_id) references materias(id)
    );
    
insert into materias(nome_materia) values("Matemática");
insert into materias(nome_materia) values("Física");
insert into materias(nome_materia) values("Geografia");
insert into materias(nome_materia) values("Inglês");

select * from estudantes;
insert into estudantes_materias (estudante_id, materia_id) Values (1,4);
insert into estudantes_materias (estudante_id, materia_id) Values (1,1);
insert into estudantes_materias (estudante_id, materia_id) Values (2,3);
insert into estudantes_materias (estudante_id, materia_id) Values (3,4);
insert into estudantes_materias (estudante_id, materia_id) Values (3,1);
insert into estudantes_materias (estudante_id, materia_id) Values (4,2);
insert into estudantes_materias (estudante_id, materia_id) Values (4,1);

select * from estudantes_materias;

select * from estudantes
join estudantes_materias on estudante_id = estudantes.id;

select * from estudantes_materias
join materias on id = estudantes_materias.materia_id
join estudantes on estudante_id = estudantes.id;


