library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ROM3a is
port(
	  address: in std_logic_vector(3 downto 0);
	  output : out std_logic_vector(14 downto 0)
);
end ROM3a;

architecture arc_ROM3a of ROM3a is
begin

--         switches 0 a 14
--         EDCBA9876543210                 round
output <= "110000011001100" when address = "0000" else --ED7632
		  "010010010101001" when address = "0001" else --DA7530
		  "001110000100110" when address = "0010" else --CBA512
		  "100011100011000" when address = "0011" else --EA9843
	      "011110010000001" when address = "0100" else --DCBA70
		  "001100001100101" when address = "0101" else --CB6520
		  "000100110010011" when address = "0110" else --B87410
		  "001001100101100" when address = "0111" else --C98532
		  "111111000000000" when address = "1000" else --EDCBA9
		  "000000000111111" when address = "1001" else --543210
	      "101001010001010" when address = "1010" else --EC9731
		  "011110001010000" when address = "1011" else --DCBA64
		  "101010000010101" when address = "1100" else --ECA420
		  "010001001110010" when address = "1101" else --D96541
		  "110011100001000" when address = "1110" else --EDA983
		  "001100010100101";                           --CB7520
		 
end arc_ROM3a;