library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_unsigned.all;

entity datapath is
port(
	-- Entradas de dados
	clk: in std_logic;
	SW: in std_logic_vector(17 downto 0);
	
	-- Entradas de controle
	R1, R2, E1, E2, E3, E4, E5: in std_logic;
	
	-- Saídas de dados
	hex0, hex1, hex2, hex3, hex4, hex5, hex6, hex7: out std_logic_vector(6 downto 0);
	ledr: out std_logic_vector(15 downto 0);
	
	-- Saídas de status
	end_game, end_time, end_round, end_FPGA: out std_logic
);
end entity;

architecture arc of datapath is
---------------------------SIGNALS-----------------------------------------------------------
--contadores
signal tempo, X: std_logic_vector(3 downto 0);
--FSM_clock
signal CLK_1Hz, CLK_050Hz, CLK_033Hz, CLK_025Hz, CLK_020Hz: std_logic;
--Logica combinacional
signal RESULT: std_logic_vector(7 downto 0);
--Registradores
signal SEL: std_logic_vector(3 downto 0);
signal USER: std_logic_vector(14 downto 0);
signal Bonus, Bonus_reg: std_logic_vector(3 downto 0);
--ROMs
signal CODE_aux: std_logic_vector(14 downto 0);
signal CODE: std_logic_vector(31 downto 0);
--COMP
signal erro: std_logic;
--NOR enables displays
signal E23, E25, E12: std_logic;

--signals implícitos--

--dec termometrico
signal stermoround, stermobonus, andtermo: std_logic_vector(15 downto 0);
--decoders HEX 7-0
signal sdecod7, sdec7, sdecod6, sdec6, sdecod5, sdecod4, sdec4, sdecod3, sdecod2, sdec2, sdecod1, sdecod0, sdec0: std_logic_vector(6 downto 0);
signal smuxhex7, smuxhex6, smuxhex5, smuxhex4, smuxhex3, smuxhex2, smuxhex1, smuxhex0: std_logic_vector(6 downto 0);
signal edec2, edec0: std_logic_vector(3 downto 0);
--saida ROMs
signal srom0, srom1, srom2, srom3: std_logic_vector(31 downto 0);
signal srom0a, srom1a, srom2a, srom3a: std_logic_vector(14 downto 0);
--FSM_clock
signal E2orE3: std_logic;

---------------------------COMPONENTS-----------------------------------------------------------
component counter_time is 
port(
	R, E, clock: in std_logic;
	Q: out std_logic_vector(3 downto 0);
	tc: out std_logic
);
end component;

component counter_round is
port(
	R, E, clock: in std_logic;
	Q: out std_logic_vector(3 downto 0);
	tc: out std_logic
);
end component;

component decoder_termometrico is
 port(
	X: in  std_logic_vector(3 downto 0);
	S: out std_logic_vector(15 downto 0)
);
end component;

component FSM_clock_de2 is
port(
	reset, E: in std_logic;
	clock: in std_logic;
	CLK_1Hz, CLK_050Hz, CLK_033Hz, CLK_025Hz, CLK_020Hz: out std_logic
);
end component;

component FSM_clock_emu is
port(
	reset, E: in std_logic;
	clock: in std_logic;
	CLK_1Hz, CLK_050Hz, CLK_033Hz, CLK_025Hz, CLK_020Hz: out std_logic
);
end component;

component decoder7seg is
port(
	C: in std_logic_vector(3 downto 0);
	F: out std_logic_vector(6 downto 0)
 );
end component;

component d_code is
port(
	C: in std_logic_vector(3 downto 0);
	F: out std_logic_vector(6 downto 0)
 );
end component;

component mux21_7bits is
port(
	F1: in std_logic_vector(6 downto 0);
	F2: in std_logic_vector(6 downto 0);
	Selector: in std_logic;
	saida: out std_logic_vector(6 downto 0)
);
end component;

component mux21_16bits is
port(
	F1: in std_logic_vector(15 downto 0);
	F2: in std_logic_vector(15 downto 0);
	Selector: in std_logic;
	saida: out std_logic_vector(15 downto 0)
);
end component;

component mux41_1bit is
port(
	F1: in std_logic;
	F2: in std_logic;
	F3: in std_logic;
	F4: in std_logic;
	Selector: in std_logic_vector(1 downto 0);
	saida: out std_logic
);
end component;

component mux41_15bits is
port(
	F1: in std_logic_vector(14 downto 0);
	F2: in std_logic_vector(14 downto 0);
	F3: in std_logic_vector(14 downto 0);
	F4: in std_logic_vector(14 downto 0);
	Selector: in std_logic_vector(1 downto 0);
	saida: out std_logic_vector(14 downto 0)
);
end component;

component mux41_32bits is
port(
	F1: in std_logic_vector(31 downto 0);
	F2: in std_logic_vector(31 downto 0);
	F3: in std_logic_vector(31 downto 0);
	F4: in std_logic_vector(31 downto 0);
	Selector: in std_logic_vector(1 downto 0);
	saida: out std_logic_vector(31 downto 0)
);
end component;

component registrador4bits is 
port(
	CLK, RST, EN: in std_logic;
	D: in std_logic_vector(3 downto 0);
	Q: out std_logic_vector(3 downto 0)
);
end component;

component registrador15bits is 
port(
	CLK, RST, EN: in std_logic;
	D: in std_logic_vector(14 downto 0);
	Q: out std_logic_vector(14 downto 0)
);
end component;

component registrador1000 is 
port(
	CLK, RST, EN: in std_logic;
	D: in std_logic_vector(3 downto 0);
	Q: out std_logic_vector(3 downto 0)
);
end component;

component comparador15bits is
port(
	CODE_aux: in std_logic_vector(14 downto 0);
	USER: in std_logic_vector(14 downto 0);
	erro: out std_logic
);
end component;

component comparador is
port(
	Bonus_Reg: in std_logic_vector(3 downto 0);
	end_game: out std_logic
);
end component;

component subtratorBonus is
port(
	bonus: in std_logic_vector(3 downto 0);
	erro: in std_logic;
	F: out std_logic_vector(3 downto 0)
);
end component;

component resultLogica is 
port (X: in std_logic_vector(3 downto 0);
	Bonus_reg: in std_logic_vector(3 downto 0);
	Sel: in std_logic_vector(1 downto 0);
	points: out std_logic_vector(7 downto 0)
);
end component;

component ROM0 is
port(
	address: in std_logic_vector(3 downto 0);
	output : out std_logic_vector(31 downto 0)
);
end component;

component ROM1 is
port(
	address: in std_logic_vector(3 downto 0);
	output : out std_logic_vector(31 downto 0)
);
end component;

component ROM2 is
port(
	address: in std_logic_vector(3 downto 0);
	output : out std_logic_vector(31 downto 0)
);
end component;

component ROM3 is
port(
	address: in std_logic_vector(3 downto 0);
	output : out std_logic_vector(31 downto 0)
);
end component;

component ROM0a is
port(
	address: in std_logic_vector(3 downto 0);
	output : out std_logic_vector(14 downto 0)
);
end component;

component ROM1a is
port(
	address: in std_logic_vector(3 downto 0);
	output : out std_logic_vector(14 downto 0)
);
end component;

component ROM2a is
port(
	address: in std_logic_vector(3 downto 0);
	output : out std_logic_vector(14 downto 0)
);
end component;

component ROM3a is
port(
	address: in std_logic_vector(3 downto 0);
	output : out std_logic_vector(14 downto 0)
);
end component;

-- COMECO DO CODIGO ---------------------------------------------------------------------------------------

begin	

--Conexoes e atribuicoes a partir daqui. Dica: usar os mesmos nomes e I/O ja declarados nos components. Todos os signals necessarios ja estao declarados.

-- fsmClock
E2orE3 <= E2 or E3;
fsmClockEmu: FSM_clock_emu port map(R1, E2orE3, clk, CLK_1Hz, CLK_050Hz, CLK_033Hz, CLK_025Hz, CLK_020Hz);

-- Contadores
counterTime: counter_time port map(R1, E3, CLK_1Hz, tempo, end_time);
counterRound: counter_round port map(R2, E4, clk, X, end_round);

-- Registradores
regSEL: registrador4bits port map(clk, R2, E1, SW(3 downto 0), SEL);
regUSE: registrador15bits port map(clk, R2, E3, SW(14 downto 0), USER);
regBONUS: registrador1000 port map(clk, R2, E4, Bonus, Bonus_reg);

-- ROMs
rom_0: ROM0 port map(X, srom0);
rom_0a: ROM0a port map(X, srom0a);
rom_1: ROM1 port map(X, srom1);
rom_1a: ROM1a port map(X, srom1a);
rom_2: ROM2 port map(X, srom2);
rom_2a: ROM2a port map(X, srom2a);
rom_3: ROM3 port map(X, srom3);
rom_3a: ROM3a port map(X, srom3a);

-- MUX 4:1
mux4x1_1bit: mux41_1bit port map(CLK_020Hz, CLK_025Hz, CLK_033Hz, CLK_050Hz, SEL(1 downto 0), end_FPGA);
mux4X1_32bits: mux41_32bits port map(srom0, srom1, srom2, srom3, SEL(3 downto 2), CODE);
mux4X1_15bits: mux41_15bits port map(srom0a, srom1a, srom2a, srom3a, SEL(3 downto 2), CODE_aux);

-- LÓGICA COMB.
result_logica: resultLogica port map(X, Bonus_reg, SEL(1 downto 0), RESULT);

-- Comparadores
comp_igualdade: comparador15bits port map(CODE_aux, USER, erro);
comp_0: comparador port map(Bonus_reg, end_game);

-- Subtrator
subtrator: subtratorBonus port map(Bonus_reg, erro, Bonus);

-- Nor Displays
E23 <= E2 nor E3;
E25 <= E2 nor E5;
E12 <= E1 nor E2;

-- Decoder Termometrico
decTermometricoBonus: decoder_termometrico port map(Bonus_reg, stermobonus);
decTermometricoRound: decoder_termometrico port map(X, stermoround);
andtermo <= stermoround and not(E1&E1&E1&E1&E1&E1&E1&E1&E1&E1&E1&E1&E1&E1&E1&E1);

-- d-code
dcode_hex7: d_code port map(CODE(31 downto 28), sdecod7);
dcode_hex6: d_code port map(CODE(27 downto 24), sdecod6);
dcode_hex5: d_code port map(CODE(23 downto 20), sdecod5);
dcode_hex4: d_code port map(CODE(19 downto 16), sdecod4);
dcode_hex3: d_code port map(CODE(15 downto 12), sdecod3);
dcode_hex2: d_code port map(CODE(11 downto 8), sdecod2);
dcode_hex1: d_code port map(CODE(7 downto 4), sdecod1);
dcode_hex0: d_code port map(CODE(3 downto 0), sdecod0);

-- dec7seg
dec7seg_hex7: decoder7seg port map(RESULT(7 downto 4), sdec7);
dec7seg_hex6: decoder7seg port map(RESULT(3 downto 0), sdec6);
dec7seg_hex4: decoder7seg port map(tempo, sdec4);
edec2 <= "00"&SEL(3 downto 2);
dec7seg_hex2: decoder7seg port map(edec2, sdec2);
edec0 <= "00"&SEL(1 downto 0);
dec7seg_hex0: decoder7seg port map(edec0, sdec0);

-- Mux 2:1
mux2X1_16bits: mux21_16bits port map(andtermo, stermobonus, SW(17), LEDR(15 downto 0));
mux2X1_hex7: mux21_7bits port map(sdecod7, sdec7, E5, smuxhex7);
mux2X1_hex6: mux21_7bits port map(sdecod6, sdec6, E5, smuxhex6);
mux2X1_hex5: mux21_7bits port map(sdecod5, "0000111", E3, smuxhex5);
mux2X1_hex4: mux21_7bits port map(sdecod4, sdec4, E3, smuxhex4);
mux2X1_hex3: mux21_7bits port map(sdecod3, "1000110", E1, smuxhex3);
mux2X1_hex2: mux21_7bits port map(sdecod2, sdec2, E1, smuxhex2);
mux2X1_hex1: mux21_7bits port map(sdecod1, "1000111", E1, smuxhex1);
mux2X1_hex0: mux21_7bits port map(sdecod0, sdec0, E1, smuxhex0);

-- HEX
HEX7 <= E25&E25&E25&E25&E25&E25&E25 or smuxhex7;
HEX6 <= E25&E25&E25&E25&E25&E25&E25 or smuxhex6;
HEX5 <= E23&E23&E23&E23&E23&E23&E23 or smuxhex5;
HEX4 <= E23&E23&E23&E23&E23&E23&E23 or smuxhex4;
HEX3 <= E12&E12&E12&E12&E12&E12&E12 or smuxhex3;
HEX2 <= E12&E12&E12&E12&E12&E12&E12 or smuxhex2;
HEX1 <= E12&E12&E12&E12&E12&E12&E12 or smuxhex1;
HEX0 <= E12&E12&E12&E12&E12&E12&E12 or smuxhex0;

end arc;