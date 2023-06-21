library IEEE;
use IEEE.Std_Logic_1164.all;
use IEEE.std_logic_unsigned.all; -- necessário para o +
entity resultLogica is
port (X: in std_logic_vector(3 downto 0);
	Bonus_reg: in std_logic_vector(3 downto 0);
	Sel: in std_logic_vector(1 downto 0);
	points: out std_logic_vector(7 downto 0)
);
end resultLogica;
architecture circuito of resultLogica is
signal Bonus: std_logic_vector(4 downto 0);
signal aux1: std_logic_vector(9 downto 0);
signal aux2: std_logic_vector(9 downto 0);
signal aux3: std_logic_vector(9 downto 0);
signal total: std_logic_vector(9 downto 0);
signal Value: std_logic_vector(5 downto 0);
begin
    -- X: 0000 | Bonus_Reg: 1000 | Sel: 00
    Bonus<="0"&Bonus_reg; -- 0 1000 = 01000
    aux1<= "0000"&Bonus(4 downto 1)&"00"; -- 0000 0100 00 = 0000010000
    Value<="00"&X; -- 00 0000 = 000000
    aux2<="000"&Sel&"00000"; -- 000 00 00000 = 0000000000
    aux3<="000000"&Value(5 downto 2); -- 000000 0000 = 0000000000
    total <= aux2+aux1+aux3; -- 0000010000
    points <= total(7 downto 0); -- 00010000
end circuito;