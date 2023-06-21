library ieee;
use ieee.std_logic_1164.all;
use IEEE.std_logic_unsigned.all; -- necessário para o -
entity counter_time is port(
	R, E, clock: in std_logic;
	Q: out std_logic_vector(3 downto 0);
	tc: out std_logic
);
end counter_time;
architecture bhv of counter_time is
signal count: std_logic_vector(3 downto 0);
begin
	P1: process(clock, R)
	begin
	    if R = '1' then
			count <= "1010";
			tc <= '0';
		elsif clock'event and clock= '1' then
		    if E = '1' then
    		    if count-'1' = "0000" then
    		        count <= "1010";
    		        tc <= '1';
    		    else
    			    count <= count - '1';
    			    tc <= '0';
    			end if;
    		end if;
		end if;
	end process;
	Q <= count;
end bhv;