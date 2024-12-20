toc.dat                                                                                             0000600 0004000 0002000 00000123436 14705727145 0014464 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP       (    5    
        	    |            ub_natts    13.16    13.16 �    ~           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                    0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         �           1262    16677    ub_natts    DATABASE     h   CREATE DATABASE ub_natts WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE ub_natts;
                postgres    false                     2615    17507    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                postgres    false         �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   postgres    false    3         �            1259    17508    cadastro_motivos    TABLE     �   CREATE TABLE public.cadastro_motivos (
    id bigint NOT NULL,
    tipo character varying,
    motivo character varying,
    disponibilidade boolean
);
 $   DROP TABLE public.cadastro_motivos;
       public         heap    postgres    false    3         �            1259    17514    cadastro_motivos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cadastro_motivos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.cadastro_motivos_id_seq;
       public          postgres    false    200    3         �           0    0    cadastro_motivos_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.cadastro_motivos_id_seq OWNED BY public.cadastro_motivos.id;
          public          postgres    false    201         �            1259    17516    ciclo    TABLE     �   CREATE TABLE public.ciclo (
    id bigint NOT NULL,
    id_maquina bigint,
    id_producao bigint,
    op_producao bigint,
    id_usuario bigint,
    data timestamp without time zone
);
    DROP TABLE public.ciclo;
       public         heap    postgres    false    3         �            1259    17519    ciclo_id_seq    SEQUENCE     u   CREATE SEQUENCE public.ciclo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.ciclo_id_seq;
       public          postgres    false    3    202         �           0    0    ciclo_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.ciclo_id_seq OWNED BY public.ciclo.id;
          public          postgres    false    203         �            1259    17521    componentes    TABLE     x   CREATE TABLE public.componentes (
    id bigint NOT NULL,
    cod character varying,
    descricao character varying
);
    DROP TABLE public.componentes;
       public         heap    postgres    false    3         �            1259    17527    componentes_id_seq    SEQUENCE     {   CREATE SEQUENCE public.componentes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.componentes_id_seq;
       public          postgres    false    204    3         �           0    0    componentes_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.componentes_id_seq OWNED BY public.componentes.id;
          public          postgres    false    205         �            1259    17529    maquina    TABLE     �   CREATE TABLE public.maquina (
    id bigint NOT NULL,
    nome character varying,
    fabricante character varying,
    ano character varying
);
    DROP TABLE public.maquina;
       public         heap    postgres    false    3         �            1259    17535    maquina_id_seq    SEQUENCE     w   CREATE SEQUENCE public.maquina_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.maquina_id_seq;
       public          postgres    false    206    3         �           0    0    maquina_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.maquina_id_seq OWNED BY public.maquina.id;
          public          postgres    false    207         �            1259    17537    oee    TABLE     �   CREATE TABLE public.oee (
    id bigint NOT NULL,
    op bigint,
    disponibilidade real,
    perfomance real,
    qualidade real,
    oee real,
    maquina bigint,
    dtoee timestamp(0) with time zone,
    id_producao bigint
);
    DROP TABLE public.oee;
       public         heap    postgres    false    3         �            1259    17540 
   oee_id_seq    SEQUENCE     s   CREATE SEQUENCE public.oee_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 !   DROP SEQUENCE public.oee_id_seq;
       public          postgres    false    3    208         �           0    0 
   oee_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE public.oee_id_seq OWNED BY public.oee.id;
          public          postgres    false    209         �            1259    17542 	   operators    TABLE     �   CREATE TABLE public.operators (
    operator_id integer NOT NULL,
    name character varying(100) NOT NULL,
    employee_number character varying(50) NOT NULL,
    workstation_id integer NOT NULL
);
    DROP TABLE public.operators;
       public         heap    postgres    false    3         �            1259    17545    operators_operator_id_seq    SEQUENCE     �   CREATE SEQUENCE public.operators_operator_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.operators_operator_id_seq;
       public          postgres    false    210    3         �           0    0    operators_operator_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.operators_operator_id_seq OWNED BY public.operators.operator_id;
          public          postgres    false    211         �            1259    17547    ordem    TABLE     w   CREATE TABLE public.ordem (
    id bigint NOT NULL,
    ord_f character varying,
    cavi bigint,
    ativa boolean
);
    DROP TABLE public.ordem;
       public         heap    postgres    false    3         �            1259    17553    ordem_id_seq    SEQUENCE     u   CREATE SEQUENCE public.ordem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.ordem_id_seq;
       public          postgres    false    212    3         �           0    0    ordem_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.ordem_id_seq OWNED BY public.ordem.id;
          public          postgres    false    213         �            1259    17555    parada    TABLE     N  CREATE TABLE public.parada (
    id bigint NOT NULL,
    inicio_parada timestamp without time zone,
    id_motivo bigint,
    id_usuario bigint,
    id_maquina bigint,
    id_producao bigint,
    fim_parada timestamp without time zone,
    justificativa character varying,
    estado boolean,
    tempo interval,
    dispo boolean
);
    DROP TABLE public.parada;
       public         heap    postgres    false    3         �            1259    17561    parada_id_seq    SEQUENCE     v   CREATE SEQUENCE public.parada_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.parada_id_seq;
       public          postgres    false    3    214         �           0    0    parada_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.parada_id_seq OWNED BY public.parada.id;
          public          postgres    false    215         �            1259    17563    parada_programada    TABLE     F  CREATE TABLE public.parada_programada (
    id bigint NOT NULL,
    inicio_parada timestamp without time zone,
    id_motivo bigint,
    id_usuario bigint,
    id_maquina bigint,
    id_producao bigint,
    fim_parada timestamp without time zone,
    justificativa character varying,
    estado boolean,
    tempo interval
);
 %   DROP TABLE public.parada_programada;
       public         heap    postgres    false    3         �            1259    17569    parada_programada_id_seq    SEQUENCE     �   CREATE SEQUENCE public.parada_programada_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.parada_programada_id_seq;
       public          postgres    false    3    216         �           0    0    parada_programada_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.parada_programada_id_seq OWNED BY public.parada_programada.id;
          public          postgres    false    217         �            1259    17571    pecas    TABLE     �   CREATE TABLE public.pecas (
    data_inicio timestamp without time zone,
    data_fim timestamp without time zone,
    usuario character varying,
    id bigint NOT NULL,
    id_maquina bigint
);
    DROP TABLE public.pecas;
       public         heap    postgres    false    3         �            1259    17577    pecas_id_seq    SEQUENCE     u   CREATE SEQUENCE public.pecas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.pecas_id_seq;
       public          postgres    false    218    3         �           0    0    pecas_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.pecas_id_seq OWNED BY public.pecas.id;
          public          postgres    false    219         �            1259    17579    producao    TABLE     r  CREATE TABLE public.producao (
    id bigint NOT NULL,
    id_maquina bigint,
    qtde_coletada bigint,
    dt_inicio timestamp without time zone,
    dt_fim timestamp without time zone,
    estado boolean,
    id_usuario bigint,
    liberacao boolean,
    t_padrao bigint,
    id_produto bigint,
    lote character varying,
    p_ciclo bigint,
    qtde_total bigint
);
    DROP TABLE public.producao;
       public         heap    postgres    false    3         �            1259    17585    producao_id_seq    SEQUENCE     x   CREATE SEQUENCE public.producao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.producao_id_seq;
       public          postgres    false    220    3         �           0    0    producao_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.producao_id_seq OWNED BY public.producao.id;
          public          postgres    false    221         �            1259    17587    produtos    TABLE     �   CREATE TABLE public.produtos (
    id bigint NOT NULL,
    nome character varying,
    pecas_ciclo bigint,
    t_padrao bigint
);
    DROP TABLE public.produtos;
       public         heap    postgres    false    3         �            1259    17593    produtos_id_seq    SEQUENCE     x   CREATE SEQUENCE public.produtos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.produtos_id_seq;
       public          postgres    false    3    222         �           0    0    produtos_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.produtos_id_seq OWNED BY public.produtos.id;
          public          postgres    false    223         �            1259    17595    refugo    TABLE       CREATE TABLE public.refugo (
    id bigint NOT NULL,
    data timestamp without time zone,
    quantidade bigint,
    id_motivo bigint,
    id_usuario bigint,
    id_maquina bigint,
    id_producao bigint,
    justificativa character varying,
    id_componente bigint
);
    DROP TABLE public.refugo;
       public         heap    postgres    false    3         �            1259    17601    refugo_id_seq    SEQUENCE     v   CREATE SEQUENCE public.refugo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.refugo_id_seq;
       public          postgres    false    3    224         �           0    0    refugo_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.refugo_id_seq OWNED BY public.refugo.id;
          public          postgres    false    225         �            1259    17603    teste    TABLE     y   CREATE TABLE public.teste (
    texto character varying,
    dt_inicio timestamp without time zone,
    botao boolean
);
    DROP TABLE public.teste;
       public         heap    postgres    false    3         �            1259    17609    usuarios    TABLE     �   CREATE TABLE public.usuarios (
    id bigint NOT NULL,
    nome character varying,
    setor character varying,
    senha character varying,
    usuario character varying,
    privilegio bigint
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false    3         �            1259    17615    usuarios_id_seq    SEQUENCE     x   CREATE SEQUENCE public.usuarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.usuarios_id_seq;
       public          postgres    false    3    227         �           0    0    usuarios_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;
          public          postgres    false    228         �            1259    17617    worksessions    TABLE     A  CREATE TABLE public.worksessions (
    session_id integer NOT NULL,
    operator_id integer,
    workstation_id integer,
    start_time timestamp without time zone NOT NULL,
    end_time timestamp without time zone,
    is_done boolean DEFAULT false,
    CONSTRAINT no_overlap_sessions CHECK ((end_time > start_time))
);
     DROP TABLE public.worksessions;
       public         heap    postgres    false    3         �            1259    17622    worksessions_session_id_seq    SEQUENCE     �   CREATE SEQUENCE public.worksessions_session_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.worksessions_session_id_seq;
       public          postgres    false    3    229         �           0    0    worksessions_session_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.worksessions_session_id_seq OWNED BY public.worksessions.session_id;
          public          postgres    false    230         �            1259    17624    workstations    TABLE     �   CREATE TABLE public.workstations (
    workstation_id integer NOT NULL,
    name character varying(100) NOT NULL,
    location character varying(100)
);
     DROP TABLE public.workstations;
       public         heap    postgres    false    3         �            1259    17627    workstations_workstation_id_seq    SEQUENCE     �   CREATE SEQUENCE public.workstations_workstation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.workstations_workstation_id_seq;
       public          postgres    false    3    231         �           0    0    workstations_workstation_id_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.workstations_workstation_id_seq OWNED BY public.workstations.workstation_id;
          public          postgres    false    232         �           2604    17629    cadastro_motivos id    DEFAULT     z   ALTER TABLE ONLY public.cadastro_motivos ALTER COLUMN id SET DEFAULT nextval('public.cadastro_motivos_id_seq'::regclass);
 B   ALTER TABLE public.cadastro_motivos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    201    200         �           2604    17630    ciclo id    DEFAULT     d   ALTER TABLE ONLY public.ciclo ALTER COLUMN id SET DEFAULT nextval('public.ciclo_id_seq'::regclass);
 7   ALTER TABLE public.ciclo ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202         �           2604    17631    componentes id    DEFAULT     p   ALTER TABLE ONLY public.componentes ALTER COLUMN id SET DEFAULT nextval('public.componentes_id_seq'::regclass);
 =   ALTER TABLE public.componentes ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    205    204         �           2604    17632 
   maquina id    DEFAULT     h   ALTER TABLE ONLY public.maquina ALTER COLUMN id SET DEFAULT nextval('public.maquina_id_seq'::regclass);
 9   ALTER TABLE public.maquina ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    207    206         �           2604    17633    oee id    DEFAULT     `   ALTER TABLE ONLY public.oee ALTER COLUMN id SET DEFAULT nextval('public.oee_id_seq'::regclass);
 5   ALTER TABLE public.oee ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208         �           2604    17634    operators operator_id    DEFAULT     ~   ALTER TABLE ONLY public.operators ALTER COLUMN operator_id SET DEFAULT nextval('public.operators_operator_id_seq'::regclass);
 D   ALTER TABLE public.operators ALTER COLUMN operator_id DROP DEFAULT;
       public          postgres    false    211    210         �           2604    17635    ordem id    DEFAULT     d   ALTER TABLE ONLY public.ordem ALTER COLUMN id SET DEFAULT nextval('public.ordem_id_seq'::regclass);
 7   ALTER TABLE public.ordem ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    213    212         �           2604    17636 	   parada id    DEFAULT     f   ALTER TABLE ONLY public.parada ALTER COLUMN id SET DEFAULT nextval('public.parada_id_seq'::regclass);
 8   ALTER TABLE public.parada ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214         �           2604    17637    parada_programada id    DEFAULT     |   ALTER TABLE ONLY public.parada_programada ALTER COLUMN id SET DEFAULT nextval('public.parada_programada_id_seq'::regclass);
 C   ALTER TABLE public.parada_programada ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    216         �           2604    17638    pecas id    DEFAULT     d   ALTER TABLE ONLY public.pecas ALTER COLUMN id SET DEFAULT nextval('public.pecas_id_seq'::regclass);
 7   ALTER TABLE public.pecas ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218         �           2604    17639    producao id    DEFAULT     j   ALTER TABLE ONLY public.producao ALTER COLUMN id SET DEFAULT nextval('public.producao_id_seq'::regclass);
 :   ALTER TABLE public.producao ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    220         �           2604    17640    produtos id    DEFAULT     j   ALTER TABLE ONLY public.produtos ALTER COLUMN id SET DEFAULT nextval('public.produtos_id_seq'::regclass);
 :   ALTER TABLE public.produtos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    222         �           2604    17641 	   refugo id    DEFAULT     f   ALTER TABLE ONLY public.refugo ALTER COLUMN id SET DEFAULT nextval('public.refugo_id_seq'::regclass);
 8   ALTER TABLE public.refugo ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    225    224         �           2604    17642    usuarios id    DEFAULT     j   ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);
 :   ALTER TABLE public.usuarios ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    227         �           2604    17643    worksessions session_id    DEFAULT     �   ALTER TABLE ONLY public.worksessions ALTER COLUMN session_id SET DEFAULT nextval('public.worksessions_session_id_seq'::regclass);
 F   ALTER TABLE public.worksessions ALTER COLUMN session_id DROP DEFAULT;
       public          postgres    false    230    229         �           2604    17644    workstations workstation_id    DEFAULT     �   ALTER TABLE ONLY public.workstations ALTER COLUMN workstation_id SET DEFAULT nextval('public.workstations_workstation_id_seq'::regclass);
 J   ALTER TABLE public.workstations ALTER COLUMN workstation_id DROP DEFAULT;
       public          postgres    false    232    231         [          0    17508    cadastro_motivos 
   TABLE DATA           M   COPY public.cadastro_motivos (id, tipo, motivo, disponibilidade) FROM stdin;
    public          postgres    false    200       3163.dat ]          0    17516    ciclo 
   TABLE DATA           [   COPY public.ciclo (id, id_maquina, id_producao, op_producao, id_usuario, data) FROM stdin;
    public          postgres    false    202       3165.dat _          0    17521    componentes 
   TABLE DATA           9   COPY public.componentes (id, cod, descricao) FROM stdin;
    public          postgres    false    204       3167.dat a          0    17529    maquina 
   TABLE DATA           <   COPY public.maquina (id, nome, fabricante, ano) FROM stdin;
    public          postgres    false    206       3169.dat c          0    17537    oee 
   TABLE DATA           o   COPY public.oee (id, op, disponibilidade, perfomance, qualidade, oee, maquina, dtoee, id_producao) FROM stdin;
    public          postgres    false    208       3171.dat e          0    17542 	   operators 
   TABLE DATA           W   COPY public.operators (operator_id, name, employee_number, workstation_id) FROM stdin;
    public          postgres    false    210       3173.dat g          0    17547    ordem 
   TABLE DATA           7   COPY public.ordem (id, ord_f, cavi, ativa) FROM stdin;
    public          postgres    false    212       3175.dat i          0    17555    parada 
   TABLE DATA           �   COPY public.parada (id, inicio_parada, id_motivo, id_usuario, id_maquina, id_producao, fim_parada, justificativa, estado, tempo, dispo) FROM stdin;
    public          postgres    false    214       3177.dat k          0    17563    parada_programada 
   TABLE DATA           �   COPY public.parada_programada (id, inicio_parada, id_motivo, id_usuario, id_maquina, id_producao, fim_parada, justificativa, estado, tempo) FROM stdin;
    public          postgres    false    216       3179.dat m          0    17571    pecas 
   TABLE DATA           O   COPY public.pecas (data_inicio, data_fim, usuario, id, id_maquina) FROM stdin;
    public          postgres    false    218       3181.dat o          0    17579    producao 
   TABLE DATA           �   COPY public.producao (id, id_maquina, qtde_coletada, dt_inicio, dt_fim, estado, id_usuario, liberacao, t_padrao, id_produto, lote, p_ciclo, qtde_total) FROM stdin;
    public          postgres    false    220       3183.dat q          0    17587    produtos 
   TABLE DATA           C   COPY public.produtos (id, nome, pecas_ciclo, t_padrao) FROM stdin;
    public          postgres    false    222       3185.dat s          0    17595    refugo 
   TABLE DATA           �   COPY public.refugo (id, data, quantidade, id_motivo, id_usuario, id_maquina, id_producao, justificativa, id_componente) FROM stdin;
    public          postgres    false    224       3187.dat u          0    17603    teste 
   TABLE DATA           8   COPY public.teste (texto, dt_inicio, botao) FROM stdin;
    public          postgres    false    226       3189.dat v          0    17609    usuarios 
   TABLE DATA           O   COPY public.usuarios (id, nome, setor, senha, usuario, privilegio) FROM stdin;
    public          postgres    false    227       3190.dat x          0    17617    worksessions 
   TABLE DATA           n   COPY public.worksessions (session_id, operator_id, workstation_id, start_time, end_time, is_done) FROM stdin;
    public          postgres    false    229       3192.dat z          0    17624    workstations 
   TABLE DATA           F   COPY public.workstations (workstation_id, name, location) FROM stdin;
    public          postgres    false    231       3194.dat �           0    0    cadastro_motivos_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.cadastro_motivos_id_seq', 13, true);
          public          postgres    false    201         �           0    0    ciclo_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.ciclo_id_seq', 97, true);
          public          postgres    false    203         �           0    0    componentes_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.componentes_id_seq', 4, true);
          public          postgres    false    205         �           0    0    maquina_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.maquina_id_seq', 1, false);
          public          postgres    false    207         �           0    0 
   oee_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.oee_id_seq', 1176, true);
          public          postgres    false    209         �           0    0    operators_operator_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.operators_operator_id_seq', 8, true);
          public          postgres    false    211         �           0    0    ordem_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.ordem_id_seq', 11, true);
          public          postgres    false    213         �           0    0    parada_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.parada_id_seq', 168, true);
          public          postgres    false    215         �           0    0    parada_programada_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.parada_programada_id_seq', 3, true);
          public          postgres    false    217         �           0    0    pecas_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.pecas_id_seq', 1862, true);
          public          postgres    false    219         �           0    0    producao_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.producao_id_seq', 241, true);
          public          postgres    false    221         �           0    0    produtos_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.produtos_id_seq', 2, true);
          public          postgres    false    223         �           0    0    refugo_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.refugo_id_seq', 59, true);
          public          postgres    false    225         �           0    0    usuarios_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.usuarios_id_seq', 8, true);
          public          postgres    false    228         �           0    0    worksessions_session_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.worksessions_session_id_seq', 11, true);
          public          postgres    false    230         �           0    0    workstations_workstation_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.workstations_workstation_id_seq', 5, true);
          public          postgres    false    232         �           2606    17646 $   cadastro_motivos cadastro_motivos_pk 
   CONSTRAINT     b   ALTER TABLE ONLY public.cadastro_motivos
    ADD CONSTRAINT cadastro_motivos_pk PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.cadastro_motivos DROP CONSTRAINT cadastro_motivos_pk;
       public            postgres    false    200         �           2606    17648    ciclo ciclo_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.ciclo
    ADD CONSTRAINT ciclo_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.ciclo DROP CONSTRAINT ciclo_pk;
       public            postgres    false    202         �           2606    17650    componentes componentes_pk 
   CONSTRAINT     X   ALTER TABLE ONLY public.componentes
    ADD CONSTRAINT componentes_pk PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.componentes DROP CONSTRAINT componentes_pk;
       public            postgres    false    204         �           2606    17652    maquina maquina_pk 
   CONSTRAINT     P   ALTER TABLE ONLY public.maquina
    ADD CONSTRAINT maquina_pk PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.maquina DROP CONSTRAINT maquina_pk;
       public            postgres    false    206         �           2606    17654 
   oee oee_pk 
   CONSTRAINT     H   ALTER TABLE ONLY public.oee
    ADD CONSTRAINT oee_pk PRIMARY KEY (id);
 4   ALTER TABLE ONLY public.oee DROP CONSTRAINT oee_pk;
       public            postgres    false    208         �           2606    17656 
   oee oee_un 
   CONSTRAINT     F   ALTER TABLE ONLY public.oee
    ADD CONSTRAINT oee_un UNIQUE (dtoee);
 4   ALTER TABLE ONLY public.oee DROP CONSTRAINT oee_un;
       public            postgres    false    208         �           2606    17658 '   operators operators_employee_number_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.operators
    ADD CONSTRAINT operators_employee_number_key UNIQUE (employee_number);
 Q   ALTER TABLE ONLY public.operators DROP CONSTRAINT operators_employee_number_key;
       public            postgres    false    210         �           2606    17660    operators operators_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.operators
    ADD CONSTRAINT operators_pkey PRIMARY KEY (operator_id);
 B   ALTER TABLE ONLY public.operators DROP CONSTRAINT operators_pkey;
       public            postgres    false    210         �           2606    17662    ordem ordem_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.ordem
    ADD CONSTRAINT ordem_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.ordem DROP CONSTRAINT ordem_pk;
       public            postgres    false    212         �           2606    17664    parada parada_pk 
   CONSTRAINT     N   ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_pk PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.parada DROP CONSTRAINT parada_pk;
       public            postgres    false    214         �           2606    17666 &   parada_programada parada_programada_pk 
   CONSTRAINT     d   ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_pk PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.parada_programada DROP CONSTRAINT parada_programada_pk;
       public            postgres    false    216         �           2606    17668    producao producao_pk 
   CONSTRAINT     R   ALTER TABLE ONLY public.producao
    ADD CONSTRAINT producao_pk PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.producao DROP CONSTRAINT producao_pk;
       public            postgres    false    220         �           2606    17670    produtos produtos_pk 
   CONSTRAINT     R   ALTER TABLE ONLY public.produtos
    ADD CONSTRAINT produtos_pk PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.produtos DROP CONSTRAINT produtos_pk;
       public            postgres    false    222         �           2606    17672    refugo refugo_pk 
   CONSTRAINT     N   ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_pk PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.refugo DROP CONSTRAINT refugo_pk;
       public            postgres    false    224         �           2606    17674    usuarios usuarios_pk 
   CONSTRAINT     R   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pk PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_pk;
       public            postgres    false    227         �           2606    17676    worksessions worksessions_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.worksessions
    ADD CONSTRAINT worksessions_pkey PRIMARY KEY (session_id);
 H   ALTER TABLE ONLY public.worksessions DROP CONSTRAINT worksessions_pkey;
       public            postgres    false    229         �           2606    17678    workstations workstations_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.workstations
    ADD CONSTRAINT workstations_pkey PRIMARY KEY (workstation_id);
 H   ALTER TABLE ONLY public.workstations DROP CONSTRAINT workstations_pkey;
       public            postgres    false    231         �           1259    17679    idx_operator_id    INDEX     O   CREATE INDEX idx_operator_id ON public.worksessions USING btree (operator_id);
 #   DROP INDEX public.idx_operator_id;
       public            postgres    false    229         �           1259    17680    idx_start_time    INDEX     M   CREATE INDEX idx_start_time ON public.worksessions USING btree (start_time);
 "   DROP INDEX public.idx_start_time;
       public            postgres    false    229         �           1259    17681    idx_workstation_id    INDEX     U   CREATE INDEX idx_workstation_id ON public.worksessions USING btree (workstation_id);
 &   DROP INDEX public.idx_workstation_id;
       public            postgres    false    229         �           2606    17682    ciclo ciclo_fk    FK CONSTRAINT     r   ALTER TABLE ONLY public.ciclo
    ADD CONSTRAINT ciclo_fk FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);
 8   ALTER TABLE ONLY public.ciclo DROP CONSTRAINT ciclo_fk;
       public          postgres    false    206    202    2981         �           2606    17687    ciclo ciclo_fk_1    FK CONSTRAINT     v   ALTER TABLE ONLY public.ciclo
    ADD CONSTRAINT ciclo_fk_1 FOREIGN KEY (id_producao) REFERENCES public.producao(id);
 :   ALTER TABLE ONLY public.ciclo DROP CONSTRAINT ciclo_fk_1;
       public          postgres    false    2997    202    220         �           2606    17692    ciclo ciclo_fk_2    FK CONSTRAINT     u   ALTER TABLE ONLY public.ciclo
    ADD CONSTRAINT ciclo_fk_2 FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);
 :   ALTER TABLE ONLY public.ciclo DROP CONSTRAINT ciclo_fk_2;
       public          postgres    false    227    3003    202         �           2606    17697 !   operators fk_operator_workstation    FK CONSTRAINT     �   ALTER TABLE ONLY public.operators
    ADD CONSTRAINT fk_operator_workstation FOREIGN KEY (workstation_id) REFERENCES public.workstations(workstation_id) ON DELETE SET NULL;
 K   ALTER TABLE ONLY public.operators DROP CONSTRAINT fk_operator_workstation;
       public          postgres    false    210    3010    231         �           2606    17702    parada parada_fk    FK CONSTRAINT     u   ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_fk FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);
 :   ALTER TABLE ONLY public.parada DROP CONSTRAINT parada_fk;
       public          postgres    false    3003    214    227         �           2606    17707    parada parada_fk_1    FK CONSTRAINT     ~   ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_fk_1 FOREIGN KEY (id_motivo) REFERENCES public.cadastro_motivos(id);
 <   ALTER TABLE ONLY public.parada DROP CONSTRAINT parada_fk_1;
       public          postgres    false    2975    200    214         �           2606    17712    parada parada_fk_2    FK CONSTRAINT     v   ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_fk_2 FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);
 <   ALTER TABLE ONLY public.parada DROP CONSTRAINT parada_fk_2;
       public          postgres    false    2981    214    206         �           2606    17717    parada parada_fk_3    FK CONSTRAINT     x   ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_fk_3 FOREIGN KEY (id_producao) REFERENCES public.producao(id);
 <   ALTER TABLE ONLY public.parada DROP CONSTRAINT parada_fk_3;
       public          postgres    false    214    220    2997         �           2606    17722 &   parada_programada parada_programada_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_fk FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);
 P   ALTER TABLE ONLY public.parada_programada DROP CONSTRAINT parada_programada_fk;
       public          postgres    false    216    227    3003         �           2606    17727 (   parada_programada parada_programada_fk_1    FK CONSTRAINT     �   ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_fk_1 FOREIGN KEY (id_motivo) REFERENCES public.cadastro_motivos(id);
 R   ALTER TABLE ONLY public.parada_programada DROP CONSTRAINT parada_programada_fk_1;
       public          postgres    false    200    2975    216         �           2606    17732 (   parada_programada parada_programada_fk_2    FK CONSTRAINT     �   ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_fk_2 FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);
 R   ALTER TABLE ONLY public.parada_programada DROP CONSTRAINT parada_programada_fk_2;
       public          postgres    false    2981    216    206         �           2606    17737 (   parada_programada parada_programada_fk_3    FK CONSTRAINT     �   ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_fk_3 FOREIGN KEY (id_producao) REFERENCES public.producao(id);
 R   ALTER TABLE ONLY public.parada_programada DROP CONSTRAINT parada_programada_fk_3;
       public          postgres    false    220    216    2997         �           2606    17742    producao producao_fk    FK CONSTRAINT     x   ALTER TABLE ONLY public.producao
    ADD CONSTRAINT producao_fk FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);
 >   ALTER TABLE ONLY public.producao DROP CONSTRAINT producao_fk;
       public          postgres    false    220    2981    206         �           2606    17747    producao producao_fk_1    FK CONSTRAINT     {   ALTER TABLE ONLY public.producao
    ADD CONSTRAINT producao_fk_1 FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);
 @   ALTER TABLE ONLY public.producao DROP CONSTRAINT producao_fk_1;
       public          postgres    false    227    3003    220         �           2606    17752    producao producao_fk_2    FK CONSTRAINT     {   ALTER TABLE ONLY public.producao
    ADD CONSTRAINT producao_fk_2 FOREIGN KEY (id_produto) REFERENCES public.produtos(id);
 @   ALTER TABLE ONLY public.producao DROP CONSTRAINT producao_fk_2;
       public          postgres    false    222    220    2999         �           2606    17757    refugo refugo_fk    FK CONSTRAINT     |   ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk FOREIGN KEY (id_motivo) REFERENCES public.cadastro_motivos(id);
 :   ALTER TABLE ONLY public.refugo DROP CONSTRAINT refugo_fk;
       public          postgres    false    200    224    2975         �           2606    17762    refugo refugo_fk_1    FK CONSTRAINT     w   ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk_1 FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);
 <   ALTER TABLE ONLY public.refugo DROP CONSTRAINT refugo_fk_1;
       public          postgres    false    227    3003    224         �           2606    17767    refugo refugo_fk_2    FK CONSTRAINT     v   ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk_2 FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);
 <   ALTER TABLE ONLY public.refugo DROP CONSTRAINT refugo_fk_2;
       public          postgres    false    206    2981    224         �           2606    17772    refugo refugo_fk_3    FK CONSTRAINT     x   ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk_3 FOREIGN KEY (id_producao) REFERENCES public.producao(id);
 <   ALTER TABLE ONLY public.refugo DROP CONSTRAINT refugo_fk_3;
       public          postgres    false    2997    224    220         �           2606    17777    refugo refugo_fk_4    FK CONSTRAINT     }   ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk_4 FOREIGN KEY (id_componente) REFERENCES public.componentes(id);
 <   ALTER TABLE ONLY public.refugo DROP CONSTRAINT refugo_fk_4;
       public          postgres    false    204    2979    224         �           2606    17782 *   worksessions worksessions_operator_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.worksessions
    ADD CONSTRAINT worksessions_operator_id_fkey FOREIGN KEY (operator_id) REFERENCES public.operators(operator_id);
 T   ALTER TABLE ONLY public.worksessions DROP CONSTRAINT worksessions_operator_id_fkey;
       public          postgres    false    2989    210    229         �           2606    17787 -   worksessions worksessions_workstation_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.worksessions
    ADD CONSTRAINT worksessions_workstation_id_fkey FOREIGN KEY (workstation_id) REFERENCES public.workstations(workstation_id);
 W   ALTER TABLE ONLY public.worksessions DROP CONSTRAINT worksessions_workstation_id_fkey;
       public          postgres    false    231    3010    229                                                                                                                                                                                                                                          3163.dat                                                                                            0000600 0004000 0002000 00000000735 14705727145 0014267 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        3	Refugo	Queimada	\N
4	Refugo	Deformada	\N
5	Refugo	Corte Irregular	\N
6	Refugo	Mal moldada	\N
7	Refugo	Risco	\N
8	Refugo	Quebrada	\N
12	Refugo	Suja	\N
13	Refugo	Contaminada	\N
15	Refugo	Migração	\N
16	Refugo	Delaminação	\N
17	Refugo	Dobra	\N
18	Refugo	Manta Descolando	\N
19	Refugo	Agulhamento	\N
2	Refugo	Ruga	\N
10	Parada	Manutenção	\N
20	Parada	Outros	\N
14	Parada	Ajuste	\N
21	Parada	Café Automatico	t
22	Parada	Refeição Automatico	t
1	Parada	Automático	\N
\.


                                   3165.dat                                                                                            0000600 0004000 0002000 00000000005 14705727145 0014257 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           3167.dat                                                                                            0000600 0004000 0002000 00000000057 14705727145 0014270 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        2	101	parafuso m8
4	teste	1223
1	000	Peca
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 3169.dat                                                                                            0000600 0004000 0002000 00000000333 14705727145 0014267 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        5	Torno 5	Fundimazza	2000
6	Torno 6	SENAI	2000
7	Torno 7	SENAI	2000
8	Torno 8	SENAI	2000
4	Usinagem 4	Fundimazza	2000
3	Célula de Solda 3	SENAI	2000
2	Célula de Solda 2	SENAI	2000
1	Célula de Solda 1	SENAI	2021
\.


                                                                                                                                                                                                                                                                                                     3171.dat                                                                                            0000600 0004000 0002000 00000004452 14705727145 0014266 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        2	2	100	50	30	50	1	2023-01-16 18:00:00-03	\N
3	2	20	50	30	50	1	2023-01-17 03:41:00-03	\N
757	\N	100	36.585365	100	36.585365	1	2023-01-17 07:23:23-03	197
760	\N	100	0	0	0	1	2023-01-17 07:59:17-03	198
762	\N	100	0	0	0	1	2023-01-17 08:01:34-03	199
766	\N	84.96393	3.4632034	50	1.4712368	1	2023-01-18 05:21:02-03	200
772	\N	63.944695	0.3545261	-300	-0.68010193	1	2023-01-18 07:43:40-03	201
781	\N	99.99529	0.32833713	99	0.32503846	1	2023-01-19 07:00:07-03	202
788	\N	100	67.41573	66.666664	44.94382	1	2023-02-09 10:38:36-03	203
796	\N	100	0	0	0	1	2023-02-09 13:37:47-03	204
805	\N	100	238.4106	66.666664	158.9404	1	2023-02-10 09:28:58-03	206
806	\N	75.22072	0	0	0	2	2023-02-13 07:18:57-03	208
816	\N	77.09963	0	0	0	1	2023-02-13 07:15:37-03	207
827	\N	99.991356	0.3456719	100	0.34564203	1	2023-02-13 07:48:00-03	209
839	\N	86.04651	0	0	0	1	2023-02-14 12:49:20-03	211
841	\N	99.76955	1.3758628	50	0.686346	2	2023-02-13 07:48:16-03	210
854	\N	56.49562	28.969234	98.83721	16.176043	1	2023-02-15 05:23:28-03	212
868	\N	100	0	0	0	1	2023-02-15 10:20:37-03	214
871	\N	99.7321	6.34117	79.06977	5.0005155	2	2023-02-15 08:15:44-03	213
886	\N	97.07138	4.310527	100	4.184288	1	2023-02-16 06:54:50-03	216
902	\N	0.041613076	15.737308	99.51923	0.006517293	1	2023-02-16 13:43:54-03	217
919	\N	99.93002	1.1010144	93.333336	1.0268943	1	2023-02-17 11:48:40-03	219
935	\N	99.73289	9.89899	100	9.872548	1	2023-02-22 05:20:44-03	220
979	\N	89.577675	19.348597	100	17.332024	1	2023-02-23 06:40:35-03	221
999	\N	98.997826	3.6339815	100	3.5975626	1	2023-02-23 11:43:17-03	222
1005	\N	99.327736	0.045121092	100	0.04481776	1	2023-02-24 10:25:29-03	223
1026	\N	100	0	0	0	1	2023-02-27 15:30:00-03	224
1039	\N	100	0.16788147	100	0.16788147	1	2023-02-27 12:50:04-03	225
1065	\N	99.893906	0.16521643	100	0.16504115	1	2023-02-28 08:51:30-03	226
1070	\N	94.3701	0.07441184	100	0.07022253	2	2023-02-28 12:17:09-03	227
1071	\N	94.419136	0.07466711	100	0.07050004	3	2023-02-28 12:34:07-03	228
1073	\N	100	0	0	0	2	2023-03-03 11:30:12-03	231
1081	\N	97.92418	3.7422478	100	3.6645656	1	2023-03-03 07:33:12-03	229
1097	\N	34.72014	50.957382	100	17.692472	1	2023-03-06 07:52:13-03	232
1133	\N	99.1551	2.6706564	100	2.648092	1	2023-03-08 05:52:06-03	234
1154	\N	100	14.457831	100	14.457831	1	2023-03-13 13:05:06-03	236
1176	\N	100	0.018753165	100	0.018753165	1	2023-03-13 13:31:44-03	237
\.


                                                                                                                                                                                                                      3173.dat                                                                                            0000600 0004000 0002000 00000000217 14705727145 0014263 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        3	Bob Johnson	0695451955	3
4	Alice Williams	0689611603	4
5	Chris Evans	0688731827	4
1	João Silva	0700267891	1
2	Maria Souza	0671880258	2
\.


                                                                                                                                                                                                                                                                                                                                                                                 3175.dat                                                                                            0000600 0004000 0002000 00000000074 14705727145 0014266 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	1A	1	t
2	2B	2	t
3	3C	3	t
4	4D	4	t
11	6F	6	t
5	5E	5	t
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                    3177.dat                                                                                            0000600 0004000 0002000 00000000120 14705727145 0014260 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        168	2023-05-03 09:52:55	10	2	1	240	2023-05-03 09:55:19	teste	f	00:02:24	\N
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                3179.dat                                                                                            0000600 0004000 0002000 00000000005 14705727145 0014264 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           3181.dat                                                                                            0000600 0004000 0002000 00000002127 14705727145 0014264 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        2023-03-13 16:06:46.433	2023-03-13 16:06:51.433		1848	1
2023-03-13 16:06:31.692	2023-03-13 16:06:36.692		1847	1
2023-03-13 16:04:58.439	2023-03-13 16:05:48.439		1846	1
2023-03-13 16:04:54.32	2023-03-13 16:05:44.32		1845	1
2023-03-17 09:23:47.04821	2023-03-17 09:23:52.04821	\N	1849	1
2023-03-17 09:24:23.8448	2023-03-17 09:24:28.8448	\N	1850	1
2023-03-17 09:24:25.744519	2023-03-17 09:24:30.744519	\N	1851	1
2023-03-17 09:24:26.780725	2023-03-17 09:24:31.780725	\N	1852	1
2023-03-17 09:24:38.756019	2023-03-17 09:24:43.756019	\N	1853	1
2023-03-17 09:25:06.849849	2023-03-17 09:25:11.849849	\N	1854	1
2023-05-03 10:45:40.692	2023-05-03 11:30:40.692	\N	1855	1
2023-05-03 11:33:11.221604	2023-05-03 12:42:49.221604	\N	1856	1
2023-05-03 12:42:49.311694	2023-05-03 12:48:05.311694	\N	1857	1
2023-05-03 12:48:06.069986	2023-05-03 12:54:31.069986	\N	1858	1
2023-05-03 12:54:41.777724	2023-05-03 13:00:28.777724	\N	1859	1
2023-05-03 13:00:19.567911	2023-05-03 13:05:36.567911	\N	1860	1
2023-05-03 13:05:36.714049	2023-05-03 13:10:55.714049	\N	1861	1
2023-05-03 13:10:56.100715	2023-05-03 13:20:34.100715	\N	1862	1
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                         3183.dat                                                                                            0000600 0004000 0002000 00000004003 14705727145 0014261 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        206	1	3	2023-02-10 12:28:58	2023-02-10 12:54:08	f	2	t	3	2	a	3	\N
208	2	0	2023-02-13 10:18:57	2023-02-13 10:47:16	f	2	t	3	2	a	1	\N
207	1	0	2023-02-13 10:15:37	2023-02-13 10:47:34	f	2	t	120	1	111	1	\N
209	1	3	2023-02-13 10:48:00	2023-02-14 15:43:45	f	2	t	30	1	111	1	\N
211	1	0	2023-02-14 15:49:20	2023-02-14 16:22:18	f	2	t	60	1	111	1	\N
210	2	2	2023-02-13 10:48:16	2023-02-15 11:15:32	f	2	t	3	2	q	1	\N
212	1	86	2023-02-15 08:23:28	2023-02-15 13:20:20	f	2	t	60	1	111	1	\N
214	1	0	2023-02-15 13:20:37	2023-02-16 09:51:48	f	2	t	120	2	111	1	\N
213	2	86	2023-02-15 11:15:44	2023-02-16 09:51:57	f	2	t	60	1	100	1	\N
216	1	17	2023-02-16 09:54:50	2023-02-16 16:29:13	f	2	t	60	1	Teste	1	\N
217	1	208	2023-02-16 16:43:54	2023-02-17 14:45:36	f	2	t	60	1	Teste	1	\N
219	1	75	2023-02-17 14:48:40	2023-02-22 08:20:34	f	2	t	60	1	111	1	\N
220	1	147	2023-02-22 08:20:44	2023-02-23 09:05:44	f	2	t	60	1	111	1	\N
221	1	50	2023-02-23 09:40:35	2023-02-23 14:29:04	f	2	t	60	1	111	1	\N
222	1	49	2023-02-23 14:43:17	2023-02-24 13:25:19	f	2	t	60	1	111	1	\N
202	1	100	2023-01-19 10:00:07	2023-02-09 13:36:37	f	2	t	60	1	\N	\N	\N
223	1	2	2023-02-24 13:25:29	2023-02-27 15:48:00	f	1	t	60	1	Teste	1	\N
224	1	0	2023-02-27 18:30:00	2023-02-27 15:48:00	f	1	t	114	1	123	1	\N
225	1	2	2023-02-27 15:50:04	2023-02-28 11:51:23	f	2	t	60	1	111	1	\N
226	1	7	2023-02-28 11:51:30	2023-03-03 10:32:52	f	2	t	60	1	111	1	\N
227	2	3	2023-02-28 15:17:09	2023-03-03 14:29:17	f	2	t	60	1	teste3	1	\N
228	3	3	2023-02-28 15:34:07	2023-03-03 14:29:26	f	2	t	60	1	Teste4	1	\N
231	2	0	2023-03-03 14:30:12	2023-03-03 17:18:24	f	2	t	60	1	Teste	1	\N
229	1	159	2023-03-03 10:33:12	2023-03-06 10:52:03	f	2	t	60	1	Teste	1	\N
232	1	55	2023-03-06 10:52:13	2023-03-06 16:03:05	f	2	t	60	1	teste	1	\N
234	1	202	2023-03-08 08:52:06	2023-03-13 16:00:14	f	2	t	60	1	Teste	1	203
236	1	1	2023-03-13 16:05:06	2023-03-13 16:12:01	f	2	t	60	1	teste	1	2
237	1	1	2023-03-13 16:31:44	2023-03-17 09:24:10	f	2	t	60	1	teste	1	\N
240	1	\N	2023-05-03 09:52:23	\N	t	2	t	60	1	111	1	\N
241	3	\N	2023-05-03 09:58:15	\N	t	2	t	120	2	Teste	1	\N
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             3185.dat                                                                                            0000600 0004000 0002000 00000000040 14705727145 0014260 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	a	1	60
2	cristiano	1	120
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                3187.dat                                                                                            0000600 0004000 0002000 00000000123 14705727145 0014264 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        58	2023-02-17 16:40:00	2	4	2	1	219	1	1
59	2023-02-17 16:41:00	3	8	2	1	219	1	1
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                             3189.dat                                                                                            0000600 0004000 0002000 00000000307 14705727145 0014272 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        BACKFRAME_BAR	\N	\N
BACKFRAME_BAR	\N	\N
2023-01-18 14:42:01	\N	\N
2023-01-18 14:42:01	2023-01-17 14:46:11	\N
2023-01-18 14:42:01	2023-01-17 14:46:11	\N
2023-01-18 14:42:01	2023-01-17 14:46:11	t
\.


                                                                                                                                                                                                                                                                                                                         3190.dat                                                                                            0000600 0004000 0002000 00000000403 14705727145 0014257 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	renan	adm	$2b$12$LVLGlWfEMebpDKPz87GTneuqVDA3kTZgX.XApV8g8xfk/uR9dkAOK	renan	2
2	adm	adm	$2b$12$46jR.CzoGZoge7IQERB.o.tdDdXwJfrXg7dJcGQryWgbjHI6hnB.u	adm	2
8	Guilherme	Operação	$2b$12$5Dx15XGKf1Kss5CxE1NWPe7BeLSQl5TlqpWmIqrT4ArXx.WDLPqxK	guilherme	1
\.


                                                                                                                                                                                                                                                             3192.dat                                                                                            0000600 0004000 0002000 00000000433 14705727145 0014264 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        7	1	2	2024-09-11 09:54:18.001745	2024-09-21 15:20:00.953405	t
8	1	1	2024-09-21 13:40:46.144547	2024-09-21 15:20:00.953	t
10	1	2	2024-09-21 13:56:34.964841	2024-09-21 15:20:00.953	t
9	1	1	2024-10-17 14:04:00	2024-10-17 14:04:14	t
11	1	1	2024-10-17 14:08:06	2024-10-17 14:11:33	t
\.


                                                                                                                                                                                                                                     3194.dat                                                                                            0000600 0004000 0002000 00000000163 14705727145 0014266 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        3	Estação C	Linha 1
4	Estação D	Linha 2
1	Estação de Reparos 1	Linha 1
2	Estação de Reparos 2	Linha 1
\.


                                                                                                                                                                                                                                                                                                                                                                                                             restore.sql                                                                                         0000600 0004000 0002000 00000100637 14705727145 0015407 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 13.16
-- Dumped by pg_dump version 13.16

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE ub_natts;
--
-- Name: ub_natts; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE ub_natts WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Portuguese_Brazil.1252';


ALTER DATABASE ub_natts OWNER TO postgres;

\connect ub_natts

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cadastro_motivos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cadastro_motivos (
    id bigint NOT NULL,
    tipo character varying,
    motivo character varying,
    disponibilidade boolean
);


ALTER TABLE public.cadastro_motivos OWNER TO postgres;

--
-- Name: cadastro_motivos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cadastro_motivos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cadastro_motivos_id_seq OWNER TO postgres;

--
-- Name: cadastro_motivos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cadastro_motivos_id_seq OWNED BY public.cadastro_motivos.id;


--
-- Name: ciclo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ciclo (
    id bigint NOT NULL,
    id_maquina bigint,
    id_producao bigint,
    op_producao bigint,
    id_usuario bigint,
    data timestamp without time zone
);


ALTER TABLE public.ciclo OWNER TO postgres;

--
-- Name: ciclo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ciclo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ciclo_id_seq OWNER TO postgres;

--
-- Name: ciclo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ciclo_id_seq OWNED BY public.ciclo.id;


--
-- Name: componentes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.componentes (
    id bigint NOT NULL,
    cod character varying,
    descricao character varying
);


ALTER TABLE public.componentes OWNER TO postgres;

--
-- Name: componentes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.componentes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.componentes_id_seq OWNER TO postgres;

--
-- Name: componentes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.componentes_id_seq OWNED BY public.componentes.id;


--
-- Name: maquina; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.maquina (
    id bigint NOT NULL,
    nome character varying,
    fabricante character varying,
    ano character varying
);


ALTER TABLE public.maquina OWNER TO postgres;

--
-- Name: maquina_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.maquina_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.maquina_id_seq OWNER TO postgres;

--
-- Name: maquina_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.maquina_id_seq OWNED BY public.maquina.id;


--
-- Name: oee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oee (
    id bigint NOT NULL,
    op bigint,
    disponibilidade real,
    perfomance real,
    qualidade real,
    oee real,
    maquina bigint,
    dtoee timestamp(0) with time zone,
    id_producao bigint
);


ALTER TABLE public.oee OWNER TO postgres;

--
-- Name: oee_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oee_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oee_id_seq OWNER TO postgres;

--
-- Name: oee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oee_id_seq OWNED BY public.oee.id;


--
-- Name: operators; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.operators (
    operator_id integer NOT NULL,
    name character varying(100) NOT NULL,
    employee_number character varying(50) NOT NULL,
    workstation_id integer NOT NULL
);


ALTER TABLE public.operators OWNER TO postgres;

--
-- Name: operators_operator_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.operators_operator_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.operators_operator_id_seq OWNER TO postgres;

--
-- Name: operators_operator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.operators_operator_id_seq OWNED BY public.operators.operator_id;


--
-- Name: ordem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ordem (
    id bigint NOT NULL,
    ord_f character varying,
    cavi bigint,
    ativa boolean
);


ALTER TABLE public.ordem OWNER TO postgres;

--
-- Name: ordem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ordem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ordem_id_seq OWNER TO postgres;

--
-- Name: ordem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ordem_id_seq OWNED BY public.ordem.id;


--
-- Name: parada; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parada (
    id bigint NOT NULL,
    inicio_parada timestamp without time zone,
    id_motivo bigint,
    id_usuario bigint,
    id_maquina bigint,
    id_producao bigint,
    fim_parada timestamp without time zone,
    justificativa character varying,
    estado boolean,
    tempo interval,
    dispo boolean
);


ALTER TABLE public.parada OWNER TO postgres;

--
-- Name: parada_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parada_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parada_id_seq OWNER TO postgres;

--
-- Name: parada_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parada_id_seq OWNED BY public.parada.id;


--
-- Name: parada_programada; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parada_programada (
    id bigint NOT NULL,
    inicio_parada timestamp without time zone,
    id_motivo bigint,
    id_usuario bigint,
    id_maquina bigint,
    id_producao bigint,
    fim_parada timestamp without time zone,
    justificativa character varying,
    estado boolean,
    tempo interval
);


ALTER TABLE public.parada_programada OWNER TO postgres;

--
-- Name: parada_programada_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parada_programada_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parada_programada_id_seq OWNER TO postgres;

--
-- Name: parada_programada_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parada_programada_id_seq OWNED BY public.parada_programada.id;


--
-- Name: pecas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pecas (
    data_inicio timestamp without time zone,
    data_fim timestamp without time zone,
    usuario character varying,
    id bigint NOT NULL,
    id_maquina bigint
);


ALTER TABLE public.pecas OWNER TO postgres;

--
-- Name: pecas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pecas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pecas_id_seq OWNER TO postgres;

--
-- Name: pecas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pecas_id_seq OWNED BY public.pecas.id;


--
-- Name: producao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producao (
    id bigint NOT NULL,
    id_maquina bigint,
    qtde_coletada bigint,
    dt_inicio timestamp without time zone,
    dt_fim timestamp without time zone,
    estado boolean,
    id_usuario bigint,
    liberacao boolean,
    t_padrao bigint,
    id_produto bigint,
    lote character varying,
    p_ciclo bigint,
    qtde_total bigint
);


ALTER TABLE public.producao OWNER TO postgres;

--
-- Name: producao_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.producao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producao_id_seq OWNER TO postgres;

--
-- Name: producao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.producao_id_seq OWNED BY public.producao.id;


--
-- Name: produtos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produtos (
    id bigint NOT NULL,
    nome character varying,
    pecas_ciclo bigint,
    t_padrao bigint
);


ALTER TABLE public.produtos OWNER TO postgres;

--
-- Name: produtos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.produtos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.produtos_id_seq OWNER TO postgres;

--
-- Name: produtos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.produtos_id_seq OWNED BY public.produtos.id;


--
-- Name: refugo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.refugo (
    id bigint NOT NULL,
    data timestamp without time zone,
    quantidade bigint,
    id_motivo bigint,
    id_usuario bigint,
    id_maquina bigint,
    id_producao bigint,
    justificativa character varying,
    id_componente bigint
);


ALTER TABLE public.refugo OWNER TO postgres;

--
-- Name: refugo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.refugo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.refugo_id_seq OWNER TO postgres;

--
-- Name: refugo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.refugo_id_seq OWNED BY public.refugo.id;


--
-- Name: teste; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teste (
    texto character varying,
    dt_inicio timestamp without time zone,
    botao boolean
);


ALTER TABLE public.teste OWNER TO postgres;

--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    id bigint NOT NULL,
    nome character varying,
    setor character varying,
    senha character varying,
    usuario character varying,
    privilegio bigint
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuarios_id_seq OWNER TO postgres;

--
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- Name: worksessions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.worksessions (
    session_id integer NOT NULL,
    operator_id integer,
    workstation_id integer,
    start_time timestamp without time zone NOT NULL,
    end_time timestamp without time zone,
    is_done boolean DEFAULT false,
    CONSTRAINT no_overlap_sessions CHECK ((end_time > start_time))
);


ALTER TABLE public.worksessions OWNER TO postgres;

--
-- Name: worksessions_session_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.worksessions_session_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.worksessions_session_id_seq OWNER TO postgres;

--
-- Name: worksessions_session_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.worksessions_session_id_seq OWNED BY public.worksessions.session_id;


--
-- Name: workstations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.workstations (
    workstation_id integer NOT NULL,
    name character varying(100) NOT NULL,
    location character varying(100)
);


ALTER TABLE public.workstations OWNER TO postgres;

--
-- Name: workstations_workstation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.workstations_workstation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workstations_workstation_id_seq OWNER TO postgres;

--
-- Name: workstations_workstation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.workstations_workstation_id_seq OWNED BY public.workstations.workstation_id;


--
-- Name: cadastro_motivos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cadastro_motivos ALTER COLUMN id SET DEFAULT nextval('public.cadastro_motivos_id_seq'::regclass);


--
-- Name: ciclo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ciclo ALTER COLUMN id SET DEFAULT nextval('public.ciclo_id_seq'::regclass);


--
-- Name: componentes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componentes ALTER COLUMN id SET DEFAULT nextval('public.componentes_id_seq'::regclass);


--
-- Name: maquina id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maquina ALTER COLUMN id SET DEFAULT nextval('public.maquina_id_seq'::regclass);


--
-- Name: oee id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oee ALTER COLUMN id SET DEFAULT nextval('public.oee_id_seq'::regclass);


--
-- Name: operators operator_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operators ALTER COLUMN operator_id SET DEFAULT nextval('public.operators_operator_id_seq'::regclass);


--
-- Name: ordem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ordem ALTER COLUMN id SET DEFAULT nextval('public.ordem_id_seq'::regclass);


--
-- Name: parada id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada ALTER COLUMN id SET DEFAULT nextval('public.parada_id_seq'::regclass);


--
-- Name: parada_programada id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada_programada ALTER COLUMN id SET DEFAULT nextval('public.parada_programada_id_seq'::regclass);


--
-- Name: pecas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pecas ALTER COLUMN id SET DEFAULT nextval('public.pecas_id_seq'::regclass);


--
-- Name: producao id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producao ALTER COLUMN id SET DEFAULT nextval('public.producao_id_seq'::regclass);


--
-- Name: produtos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtos ALTER COLUMN id SET DEFAULT nextval('public.produtos_id_seq'::regclass);


--
-- Name: refugo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.refugo ALTER COLUMN id SET DEFAULT nextval('public.refugo_id_seq'::regclass);


--
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- Name: worksessions session_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worksessions ALTER COLUMN session_id SET DEFAULT nextval('public.worksessions_session_id_seq'::regclass);


--
-- Name: workstations workstation_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workstations ALTER COLUMN workstation_id SET DEFAULT nextval('public.workstations_workstation_id_seq'::regclass);


--
-- Data for Name: cadastro_motivos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cadastro_motivos (id, tipo, motivo, disponibilidade) FROM stdin;
\.
COPY public.cadastro_motivos (id, tipo, motivo, disponibilidade) FROM '$$PATH$$/3163.dat';

--
-- Data for Name: ciclo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ciclo (id, id_maquina, id_producao, op_producao, id_usuario, data) FROM stdin;
\.
COPY public.ciclo (id, id_maquina, id_producao, op_producao, id_usuario, data) FROM '$$PATH$$/3165.dat';

--
-- Data for Name: componentes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.componentes (id, cod, descricao) FROM stdin;
\.
COPY public.componentes (id, cod, descricao) FROM '$$PATH$$/3167.dat';

--
-- Data for Name: maquina; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.maquina (id, nome, fabricante, ano) FROM stdin;
\.
COPY public.maquina (id, nome, fabricante, ano) FROM '$$PATH$$/3169.dat';

--
-- Data for Name: oee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oee (id, op, disponibilidade, perfomance, qualidade, oee, maquina, dtoee, id_producao) FROM stdin;
\.
COPY public.oee (id, op, disponibilidade, perfomance, qualidade, oee, maquina, dtoee, id_producao) FROM '$$PATH$$/3171.dat';

--
-- Data for Name: operators; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.operators (operator_id, name, employee_number, workstation_id) FROM stdin;
\.
COPY public.operators (operator_id, name, employee_number, workstation_id) FROM '$$PATH$$/3173.dat';

--
-- Data for Name: ordem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ordem (id, ord_f, cavi, ativa) FROM stdin;
\.
COPY public.ordem (id, ord_f, cavi, ativa) FROM '$$PATH$$/3175.dat';

--
-- Data for Name: parada; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.parada (id, inicio_parada, id_motivo, id_usuario, id_maquina, id_producao, fim_parada, justificativa, estado, tempo, dispo) FROM stdin;
\.
COPY public.parada (id, inicio_parada, id_motivo, id_usuario, id_maquina, id_producao, fim_parada, justificativa, estado, tempo, dispo) FROM '$$PATH$$/3177.dat';

--
-- Data for Name: parada_programada; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.parada_programada (id, inicio_parada, id_motivo, id_usuario, id_maquina, id_producao, fim_parada, justificativa, estado, tempo) FROM stdin;
\.
COPY public.parada_programada (id, inicio_parada, id_motivo, id_usuario, id_maquina, id_producao, fim_parada, justificativa, estado, tempo) FROM '$$PATH$$/3179.dat';

--
-- Data for Name: pecas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pecas (data_inicio, data_fim, usuario, id, id_maquina) FROM stdin;
\.
COPY public.pecas (data_inicio, data_fim, usuario, id, id_maquina) FROM '$$PATH$$/3181.dat';

--
-- Data for Name: producao; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producao (id, id_maquina, qtde_coletada, dt_inicio, dt_fim, estado, id_usuario, liberacao, t_padrao, id_produto, lote, p_ciclo, qtde_total) FROM stdin;
\.
COPY public.producao (id, id_maquina, qtde_coletada, dt_inicio, dt_fim, estado, id_usuario, liberacao, t_padrao, id_produto, lote, p_ciclo, qtde_total) FROM '$$PATH$$/3183.dat';

--
-- Data for Name: produtos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.produtos (id, nome, pecas_ciclo, t_padrao) FROM stdin;
\.
COPY public.produtos (id, nome, pecas_ciclo, t_padrao) FROM '$$PATH$$/3185.dat';

--
-- Data for Name: refugo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.refugo (id, data, quantidade, id_motivo, id_usuario, id_maquina, id_producao, justificativa, id_componente) FROM stdin;
\.
COPY public.refugo (id, data, quantidade, id_motivo, id_usuario, id_maquina, id_producao, justificativa, id_componente) FROM '$$PATH$$/3187.dat';

--
-- Data for Name: teste; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teste (texto, dt_inicio, botao) FROM stdin;
\.
COPY public.teste (texto, dt_inicio, botao) FROM '$$PATH$$/3189.dat';

--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarios (id, nome, setor, senha, usuario, privilegio) FROM stdin;
\.
COPY public.usuarios (id, nome, setor, senha, usuario, privilegio) FROM '$$PATH$$/3190.dat';

--
-- Data for Name: worksessions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.worksessions (session_id, operator_id, workstation_id, start_time, end_time, is_done) FROM stdin;
\.
COPY public.worksessions (session_id, operator_id, workstation_id, start_time, end_time, is_done) FROM '$$PATH$$/3192.dat';

--
-- Data for Name: workstations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.workstations (workstation_id, name, location) FROM stdin;
\.
COPY public.workstations (workstation_id, name, location) FROM '$$PATH$$/3194.dat';

--
-- Name: cadastro_motivos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cadastro_motivos_id_seq', 13, true);


--
-- Name: ciclo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ciclo_id_seq', 97, true);


--
-- Name: componentes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.componentes_id_seq', 4, true);


--
-- Name: maquina_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.maquina_id_seq', 1, false);


--
-- Name: oee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oee_id_seq', 1176, true);


--
-- Name: operators_operator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.operators_operator_id_seq', 8, true);


--
-- Name: ordem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ordem_id_seq', 11, true);


--
-- Name: parada_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.parada_id_seq', 168, true);


--
-- Name: parada_programada_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.parada_programada_id_seq', 3, true);


--
-- Name: pecas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pecas_id_seq', 1862, true);


--
-- Name: producao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.producao_id_seq', 241, true);


--
-- Name: produtos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.produtos_id_seq', 2, true);


--
-- Name: refugo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.refugo_id_seq', 59, true);


--
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 8, true);


--
-- Name: worksessions_session_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.worksessions_session_id_seq', 11, true);


--
-- Name: workstations_workstation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.workstations_workstation_id_seq', 5, true);


--
-- Name: cadastro_motivos cadastro_motivos_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cadastro_motivos
    ADD CONSTRAINT cadastro_motivos_pk PRIMARY KEY (id);


--
-- Name: ciclo ciclo_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ciclo
    ADD CONSTRAINT ciclo_pk PRIMARY KEY (id);


--
-- Name: componentes componentes_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componentes
    ADD CONSTRAINT componentes_pk PRIMARY KEY (id);


--
-- Name: maquina maquina_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maquina
    ADD CONSTRAINT maquina_pk PRIMARY KEY (id);


--
-- Name: oee oee_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oee
    ADD CONSTRAINT oee_pk PRIMARY KEY (id);


--
-- Name: oee oee_un; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oee
    ADD CONSTRAINT oee_un UNIQUE (dtoee);


--
-- Name: operators operators_employee_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operators
    ADD CONSTRAINT operators_employee_number_key UNIQUE (employee_number);


--
-- Name: operators operators_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operators
    ADD CONSTRAINT operators_pkey PRIMARY KEY (operator_id);


--
-- Name: ordem ordem_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ordem
    ADD CONSTRAINT ordem_pk PRIMARY KEY (id);


--
-- Name: parada parada_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_pk PRIMARY KEY (id);


--
-- Name: parada_programada parada_programada_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_pk PRIMARY KEY (id);


--
-- Name: producao producao_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producao
    ADD CONSTRAINT producao_pk PRIMARY KEY (id);


--
-- Name: produtos produtos_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtos
    ADD CONSTRAINT produtos_pk PRIMARY KEY (id);


--
-- Name: refugo refugo_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_pk PRIMARY KEY (id);


--
-- Name: usuarios usuarios_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pk PRIMARY KEY (id);


--
-- Name: worksessions worksessions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worksessions
    ADD CONSTRAINT worksessions_pkey PRIMARY KEY (session_id);


--
-- Name: workstations workstations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workstations
    ADD CONSTRAINT workstations_pkey PRIMARY KEY (workstation_id);


--
-- Name: idx_operator_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_operator_id ON public.worksessions USING btree (operator_id);


--
-- Name: idx_start_time; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_start_time ON public.worksessions USING btree (start_time);


--
-- Name: idx_workstation_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_workstation_id ON public.worksessions USING btree (workstation_id);


--
-- Name: ciclo ciclo_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ciclo
    ADD CONSTRAINT ciclo_fk FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);


--
-- Name: ciclo ciclo_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ciclo
    ADD CONSTRAINT ciclo_fk_1 FOREIGN KEY (id_producao) REFERENCES public.producao(id);


--
-- Name: ciclo ciclo_fk_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ciclo
    ADD CONSTRAINT ciclo_fk_2 FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);


--
-- Name: operators fk_operator_workstation; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operators
    ADD CONSTRAINT fk_operator_workstation FOREIGN KEY (workstation_id) REFERENCES public.workstations(workstation_id) ON DELETE SET NULL;


--
-- Name: parada parada_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_fk FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);


--
-- Name: parada parada_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_fk_1 FOREIGN KEY (id_motivo) REFERENCES public.cadastro_motivos(id);


--
-- Name: parada parada_fk_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_fk_2 FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);


--
-- Name: parada parada_fk_3; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada
    ADD CONSTRAINT parada_fk_3 FOREIGN KEY (id_producao) REFERENCES public.producao(id);


--
-- Name: parada_programada parada_programada_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_fk FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);


--
-- Name: parada_programada parada_programada_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_fk_1 FOREIGN KEY (id_motivo) REFERENCES public.cadastro_motivos(id);


--
-- Name: parada_programada parada_programada_fk_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_fk_2 FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);


--
-- Name: parada_programada parada_programada_fk_3; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parada_programada
    ADD CONSTRAINT parada_programada_fk_3 FOREIGN KEY (id_producao) REFERENCES public.producao(id);


--
-- Name: producao producao_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producao
    ADD CONSTRAINT producao_fk FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);


--
-- Name: producao producao_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producao
    ADD CONSTRAINT producao_fk_1 FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);


--
-- Name: producao producao_fk_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producao
    ADD CONSTRAINT producao_fk_2 FOREIGN KEY (id_produto) REFERENCES public.produtos(id);


--
-- Name: refugo refugo_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk FOREIGN KEY (id_motivo) REFERENCES public.cadastro_motivos(id);


--
-- Name: refugo refugo_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk_1 FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);


--
-- Name: refugo refugo_fk_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk_2 FOREIGN KEY (id_maquina) REFERENCES public.maquina(id);


--
-- Name: refugo refugo_fk_3; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk_3 FOREIGN KEY (id_producao) REFERENCES public.producao(id);


--
-- Name: refugo refugo_fk_4; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.refugo
    ADD CONSTRAINT refugo_fk_4 FOREIGN KEY (id_componente) REFERENCES public.componentes(id);


--
-- Name: worksessions worksessions_operator_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worksessions
    ADD CONSTRAINT worksessions_operator_id_fkey FOREIGN KEY (operator_id) REFERENCES public.operators(operator_id);


--
-- Name: worksessions worksessions_workstation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worksessions
    ADD CONSTRAINT worksessions_workstation_id_fkey FOREIGN KEY (workstation_id) REFERENCES public.workstations(workstation_id);


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 