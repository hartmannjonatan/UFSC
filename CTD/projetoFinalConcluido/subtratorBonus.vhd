library IEEE;
use IEEE.Std_Logic_1164.all;
use IEEE.std_logic_unsigned.all; -- necessário para o -
entity subtratorBonus is
port (bonus: in std_logic_vector(3 downto 0);
    	erro: in std_logic;
    	F: out std_logic_vector(3 downto 0)
);
end subtratorBonus;
architecture circuito of subtratorBonus is
begin
    F <= bonus - erro;
end circuito;