library ieee;
use ieee.std_logic_1164.all;
entity registrador4bits is port (
		CLK, RST, EN: in std_logic;
		D: in std_logic_vector(3 downto 0);
		Q: out std_logic_vector(3 downto 0)
	);
end registrador4bits;
architecture behv of registrador4bits is
signal internalQ : std_logic_vector(3 downto 0);
begin
	process(CLK, RST)
	begin
		if RST = '1' then
			internalQ <= "0000";
		elsif (CLK'event and CLK = '1') then
			if (EN = '1') then
				internalQ <= D;
			end if;
		end if;
	end process;
	Q <= internalQ;
end behv;