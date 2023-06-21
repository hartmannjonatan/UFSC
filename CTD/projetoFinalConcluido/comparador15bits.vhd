library ieee;
use ieee.std_logic_1164.all;
entity comparador15bits is port (
		CODE_aux: in std_logic_vector(14 downto 0);
		USER: in std_logic_vector(14 downto 0);
		erro: out std_logic
	);
end comparador15bits;
architecture behv of comparador15bits is
signal aux: std_logic_vector(14 downto 0);
begin
-- 	process
-- 	begin
-- 		if CODE_aux = USER then
-- 			erro<='0';
-- 		else
-- 		    erro<='1';
-- 		end if;
-- 	end process;
    -- aux <= not(CODE_aux xnor USER);
	erro <= '0' when CODE_aux = USER else '1';
end behv;