library ieee;
use ieee.std_logic_1164.all;
entity registrador15bits is port (
		CLK, RST, EN: in std_logic;
		D: in std_logic_vector(14 downto 0);
		Q: out std_logic_vector(14 downto 0)
	);
end registrador15bits;
architecture behv of registrador15bits is
signal internalQ : std_logic_vector(14 downto 0);
begin
	process(CLK, RST)
	begin
		if RST = '1' then
			internalQ <= "000000000000000";
		elsif (CLK'event and CLK = '1') then
			if (EN = '1') then
				internalQ <= D;
			end if;
		end if;
	end process;
	Q <= internalQ;
end behv;