library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ROM2 is
port(
	  address: in std_logic_vector(3 downto 0);
	  output : out std_logic_vector(31 downto 0)
);
end ROM2;

architecture arc_ROM2 of ROM2 is
begin

--         HEX7      HEX6     HEX5     HEX4     HEX3     HEX2     HEX1     HEX0               round

output <= "1011"	& "1111" & "1010" & "1111"	& "0101" & "0011" & "1111" & "1101" when address = "0000" else
--         b       des      a       des     5       3       des     d

          "1110"	& "1111" & "1010" & "1111"	& "0101" & "0000" & "1111" & "1101" when address = "0001" else
--          e       des      a       des     5       0       des     d

		 "0111"	& "1111" & "0100" & "1111"	& "1000" & "1010" & "1111" & "0011" when address = "0010" else
--         7       des      4       des     8       a       des     3

			 "1101"	& "1111" & "1100" & "1111"	& "1010" & "1110" & "1111" & "1011" when address = "0011" else
--         d       des      c       des     a       e       des     b

			 "1011"	& "1111" & "0001" & "1111"	& "1010" & "1001" & "1111" & "1110" when address = "0100" else
--          d       des      1       des     a       9       des     e

			 "0000"	& "1111" & "0100" & "1111"	& "1000" & "0110" & "1111" & "0101" when address = "0101" else
--          0       des      4       des     8       6       des     5

			 "0000"	& "1111" & "0111" & "1111"	& "1011" & "0101" & "1111" & "1010" when address = "0110" else
--          0       des      7       des     b       5       des     a			 
			 
			 "1000"	& "1111" & "0001" & "1111"	& "0111" & "1100" & "1111" & "0000" when address = "0111" else
--          8       des      1       des     7       c       des     0

			 "0101"	& "1111" & "1101" & "1111"	& "0001" & "1100" & "1111" & "0110" when address = "1000" else
--          5       des      d       des     1       c       des     6

			 "1010"	& "1111" & "0010" & "1111"	& "0111" & "1100" & "1111" & "0000" when address = "1001" else
--         a       des      2       des     7       c       des     0

			 "1101"	& "1111" & "0000" & "1111"	& "0110" & "0101" & "1111" & "1000" when address = "1010" else
--           d       des      0       des     6       5       des     8

			 "0101"	& "1111" & "0011" & "1111"	& "1011" & "0010" & "1111" & "0000" when address = "1011" else
--         5       des      3       des     b       2       des     0

			 "0000"	& "1111" & "0010" & "1111"	& "1100" & "0011" & "1111" & "0001" when address = "1100" else
--          0       des      2       des     c       3       des     1

			 "1101"	& "1111" & "1001" & "1111"	& "1010" & "1011" & "1111" & "1100" when address = "1101" else
--          d       des      9       des     a       b       des     c

			 "0101"	& "1111" & "0111" & "1111"	& "1011" & "1101" & "1111" & "0100" when address = "1110" else
--          5       des      7       des     b       d       des     4

			 "0011"	& "1111" & "0101" & "1111"	& "1000" & "1011" & "1111" & "0110";
--         3       des      5       des     8       b       des     6
			 
end arc_ROM2;