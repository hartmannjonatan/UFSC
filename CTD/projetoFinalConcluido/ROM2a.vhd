library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ROM2a is
port(
	  address: in std_logic_vector(3 downto 0);
	  output : out std_logic_vector(14 downto 0)
);
end ROM2a;

architecture arc_ROM2a of ROM2a is
begin

--         switches 0 a 14
--        EDCBA9876543210                 round
output <="010110000101000" when address = "0000" else
         "110010000100001" when address = "0001" else
		 "000010110011000" when address = "0010" else
		 "111110000000000" when address = "0011" else
		 "110011000000010" when address = "0100" else
		 "000000101110001" when address = "0101" else
		 "000110010100001" when address = "0110" else
		 "001000110000011" when address = "0111" else
		 "011000001100010" when address = "1000" else
		 "001010100000101" when address = "1001" else
		 "010000101100001" when address = "1010" else
		 "000100000101101" when address = "1011" else
		 "001000000001111" when address = "1100" else
		 "011111000000000" when address = "1101" else
		 "010100010110000" when address = "1110" else
		 "000100101101000";
			 
end arc_ROM2a;