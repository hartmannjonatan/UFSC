library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ROM1 is
port(
	  address: in std_logic_vector(3 downto 0);
	  output : out std_logic_vector(31 downto 0)
);
end ROM1;

architecture arc_ROM1 of ROM1 is
begin

--         HEX7      HEX6     HEX5     HEX4     HEX3     HEX2     HEX1     HEX0               round

output <= "1101"	& "1111" & "0101" & "1111"	& "1001" & "1111" & "1010" & "1111" when address = "0000" else
--         d        des       5      des       9       des       a       des

          "1111"	& "1110" & "1111" & "0101"	& "1111" & "1001" & "1111" & "0000" when address = "0001" else
--          des        e       des       5      des       9       des       0

		 "0101"	& "1111" & "0110" & "1111"	& "1001" & "1111" & "1011" & "1100" when address = "0010" else
--         5        des       6      des       9       des       c       des

			 "1111"	& "1011" & "1111" & "0101"	& "1111" & "0111" & "1111" & "1101" when address = "0011" else
--         des        b       des       5      des       7       des       d

			 "0110"	& "1111" & "1101" & "1111"	& "1100" & "1111" & "1001" & "1111" when address = "0100" else
--          6        des       d      des       c       des       9       des

			 "1111"	& "1010" & "1111" & "1101"	& "1111" & "1011" & "1111" & "1001" when address = "0101" else
--          des        a       des       d      des       b       des       9

			 "1110"	& "1111" & "1101" & "1111"	& "1011" & "1111" & "1000" & "1111" when address = "0110" else
--          e        des       d      des       b       des       8       des			 
			 
			 "1111"	& "0011" & "1111" & "0100"	& "1111" & "0101" & "1111" & "0010" when address = "0111" else
--          des        3       des       4      des       5       des       2

			 "0111"	& "1111" & "1110" & "1111"	& "1010" & "1111" & "0110" & "1111" when address = "1000" else
--          7        des       e      des       a       des       6       des

			 "1111"	& "1101" & "1111" & "1100"	& "1111" & "1010" & "1111" & "1011" when address = "1001" else
--         des        d       des       c      des       a       des       b

			 "0101"	& "1111" & "0100" & "1111"	& "0111" & "1111" & "1110" & "1111" when address = "1010" else
--           5        des       4      des       7       des       e       des

			 "1111"	& "1010" & "1111" & "0101"	& "1111" & "0000" & "1111" & "1100" when address = "1011" else
--         des        a       des       5      des       0       des       c

			 "0111"	& "1111" & "1001" & "1111"	& "0110" & "1111" & "1011" & "1111" when address = "1100" else
--          7        des       9      des       6       des       b       des

			 "1111"	& "1000" & "1111" & "0001"	& "1111" & "0010" & "1111" & "1101" when address = "1101" else
--          des        8       des       1      des       2       des       d

			 "1011"	& "1111" & "0000" & "1111"	& "0011" & "1111" & "1100" & "1111" when address = "1110" else
--          b        des       0      des       3       des       c       des

			 "1111"	& "1010" & "1111" & "0110"	& "1111" & "0011" & "1111" & "0000";
--         des        a       des       6      des       3       des       0
			 
end arc_ROM1;