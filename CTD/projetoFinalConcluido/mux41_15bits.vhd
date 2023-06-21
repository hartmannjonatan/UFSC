library IEEE;
use IEEE.Std_Logic_1164.all;
use IEEE.std_logic_unsigned.all; -- necessário para o +
entity mux41_15bits is
port (F1: in std_logic_vector(14 downto 0);
		F2: in std_logic_vector(14 downto 0);
		F3: in std_logic_vector(14 downto 0);
		F4: in std_logic_vector(14 downto 0);
		Selector: in std_logic_vector(1 downto 0);
		saida: out std_logic_vector(14 downto 0)
);
end mux41_15bits;
architecture circuito of mux41_15bits is
begin
saida <= F1 when Selector = "00" else
		F2 when Selector = "01" else
		F3 when Selector = "10" else
		F4;
end circuito;