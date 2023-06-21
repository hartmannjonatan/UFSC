library IEEE;
use IEEE.Std_Logic_1164.all;
use IEEE.std_logic_unsigned.all; -- necessário para o +
entity mux21_7bits is
port (F1: in std_logic_vector(6 downto 0);
		F2: in std_logic_vector(6 downto 0);
		Selector: in std_logic;
		saida: out std_logic_vector(6 downto 0)
);
end mux21_7bits;
architecture circuito of mux21_7bits is
begin
saida <= F1 when Selector = '0' else F2;
end circuito;