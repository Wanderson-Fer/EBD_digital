create table if not exists pessoa(
    id_pessoa integer primary key autoincrement,
    nome varchar(60) not null,
    funcao varchar(15),
    endereco varchar(255),
    data_nascimento date,
    genero varchar(10),
    contato varchar(17)  -- ddd(xx)xxxxx-xxxx
);

create table if not exists classe(
    id_classe integer primary key autoincrement,
    nome varchar(50) not null
);

create table if not exists licao(
    id_licao integer primary key autoincrement,
    id_pessoa integer,  -- Id do professor
    id_classe integer,
    nome varchar(50) not null,
    data date,
    visitante integer,
    observacao text,
    constraint fk_licao_pessoa
        foreign key (id_pessoa) references pessoa(id_pessoa),
    constraint fk_licao_classe
        foreign key (id_classe) references classe(id_classe)
);

create table if not exists licao_pessoa(
    id_licao integer,
    id_pessoa integer,
    presenca boolean,
    revista boolean,
    biblia boolean,
    oferta float,
    primary key (id_licao, id_pessoa),
    constraint fk_licao_pessoa_licao
        foreign key (id_licao) references licao(id_licao),
    constraint fk_licao_pessoa_pessoa
        foreign key (id_pessoa) references pessoa(id_pessoa)
);

--select * from pessoa;
--select * from classe;
--select * from licao;
--select * from licao_pessoa;
