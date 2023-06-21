library ieee;
use ieee.std_logic_1164.all;
use IEEE.std_logic_unsigned.all; -- necessário para o +
entity counter_round is port(
	R, E, clock: in std_logic;
	Q: out std_logic_vector(3 downto 0);
	tc: out std_logic
);
end counter_round;
architecture bhv of counter_round is
signal count: std_logic_vector(3 downto 0);
signal aux: std_logic_vector(4 downto 0);
begin
	P1: process(clock, R)
	begin
	    aux <= '0'&count+'1';
	    if R = '1' then
			count <= "0000";
			tc <= '0';
		elsif clock'event and clock= '1' then
		    if E = '1' then
    		    if aux >= "01111" then
    		        count <= "0000";
    		        tc <= '1';
    		    else
    			    count <= count + '1';
    			    tc <= '0';
    			end if;
    		end if;
		end if;
	end process;
	Q <= count;
end bhv;