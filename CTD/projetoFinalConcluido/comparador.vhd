library ieee;
use ieee.std_logic_1164.all;
entity comparador is port (
		Bonus_Reg: in std_logic_vector(3 downto 0);
		end_game: out std_logic
	);
end comparador;
architecture behv of comparador is
begin
	end_game <= '1' when Bonus_Reg = "0000" else '0';
end behv;