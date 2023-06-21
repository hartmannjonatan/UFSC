library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ROM1a is
port(
	  address: in std_logic_vector(3 downto 0);
	  output : out std_logic_vector(14 downto 0)
);
end ROM1a;

architecture arc_ROM1a of ROM1a is
begin

--         switches 0 a 14
--        EDCBA9876543210                 round
output <="010011000100000" when address = "0000" else
         "100001000100001" when address = "0001" else
		 "001001001100000" when address = "0010" else
		 "000100010100000" when address = "0011" else
		 "011001001000000" when address = "0100" else
		 "010111000000000" when address = "0101" else
		 "110100100000000" when address = "0110" else
		 "000000000111100" when address = "0111" else
		 "100010011000000" when address = "1000" else
		 "011110000000000" when address = "1001" else
		 "100000010110000" when address = "1010" else
		 "001010000100001" when address = "1011" else
		 "000101011000000" when address = "1100" else
		 "010000100000110" when address = "1101" else
		 "001100000001001" when address = "1110" else
		 "000010001001001";
			 
end arc_ROM1a;