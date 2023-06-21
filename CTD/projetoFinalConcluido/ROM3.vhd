library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ROM3 is
port(
	  address: in std_logic_vector(3 downto 0);
	  output : out std_logic_vector(31 downto 0)
);
end ROM3;

architecture arc_ROM3 of ROM3 is
begin

--         HEX7      HEX6     HEX5     HEX4     HEX3     HEX2     HEX1     HEX0               round

output <= "1111"	& "1110" & "1101" & "0111"	& "0110" & "0011" & "0010" & "1111" when address = "0000" else
--        des E D 7 6 3 2 des 

          "1111"	& "1101" & "1010" & "0111"	& "0101" & "0011" & "1111" & "1111" when address = "0001" else
--        des D A 7 5 3 0 des

		  "1111"	& "1100" & "1011" & "1010"	& "0101" & "0010" & "0001" & "1111" when address = "0010" else
--        des      C        B        A         5        2        1        des

		  "1111"	& "1110" & "1010" & "1001"	& "1000" & "0100" & "0011" & "1111" when address = "0011" else
--        des E A 9 8 4 3 des 

		  "1111"	& "1101" & "1100" & "1011"	& "1010" & "0111" & "0000" & "1111" when address = "0100" else
--        des D C B A 7 0 des   

		  "1111"	& "1100" & "1011" & "0110"	& "0101" & "0010" & "0000" & "1111" when address = "0101" else
--        des C B 6 5 2 0 des

		  "1111"	& "1011" & "1000" & "0111"	& "0010" & "0001" & "0000" & "1111" when address = "0110" else
--        des C B 8 7 4 1 0 des
			 
		  "1111"	& "1100" & "1001" & "1000"	& "0101" & "0011" & "0010" & "1111" when address = "0111" else
--        des C 9 8 5 3 2 des

		  "1111"	& "1110" & "1101" & "1100"	& "1011" & "1010" & "1001" & "1111" when address = "1000" else
--        des E D C B A 9 des

	      "1111"	& "0101" & "0100" & "0011"	& "0010" & "0001" & "0000" & "1111" when address = "1001" else
--        des 5 4 3 2 1 0 des

		  "1111"	& "1110" & "1100" & "1001"	& "0111" & "0011" & "0001" & "1111" when address = "1010" else
--        des E C 9 7 3 1 des

		  "1111"	& "1101" & "1100" & "1011"	& "1010" & "0110" & "0100" & "1111" when address = "1011" else
--        des D C B A 6 4 des

		  "1111"	& "1110" & "1100" & "1010"	& "0100" & "0010" & "0000" & "1111" when address = "1100" else
--        des E C A 4 2 0 des

		  "1111"	& "1101" & "1001" & "0110"	& "0101" & "0100" & "0001" & "1111" when address = "1101" else
--        des D 9 6 5 4 1 des

		  "1111"	& "1110" & "1101" & "1010"	& "1001" & "1000" & "0011" & "1111" when address = "1110" else
--        des E D A 9 8 3 des

		  "1111"	& "1100" & "1011" & "0111"	& "0101" & "0010" & "0000" & "1111";
--        des C B 7 5 2 0 des

end arc_ROM3;