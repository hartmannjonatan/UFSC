library ieee;
use ieee.std_logic_1164.all;

entity controle is
port(
-- Entradas de controle
	enter, reset, CLOCK: in std_logic;
-- Entradas de status
	end_game, end_time, end_round, end_FPGA: in std_logic;
-- Saídas de comandos
	R1, R2, E1, E2, E3, E4, E5: out std_logic
);
end controle;

architecture bhv of controle is
    type STATES is (Init, Setup, Play_FPGA, Play_user, Count_Round, Waiting, Result);
    signal EA, PE: STATES;
begin
    P1: process(clock, reset)
    begin
        if reset = '0' then
            EA<=Init;
        end if;
        if (clock'event AND clock = '1') then
                EA <= PE;
            end if;
    end process;
    
    P2: process(EA, enter, end_game, end_time, end_round, end_FPGA)
    begin
        case EA is
            when Init => 
                R1 <= '1';
                R2 <= '1';
                E1 <= '0';
                E2 <= '0';
                E3 <= '0';
                E4 <= '0';
                E5 <= '0';
                PE <= Setup;
            when Setup => 
                R1 <= '0';
                R2 <= '0';
                E1 <= '1';
                E2 <= '0';
                E3 <= '0';
                E4 <= '0';
                E5 <= '0';
                if enter = '0' then
                    PE<=Play_FPGA;
                elsif enter = '1' then
                    PE <= Setup;
                end if;
            when Play_FPGA => 
                R1 <= '0';
                R2 <= '0';
                E1 <= '0';
                E2 <= '1';
                E3 <= '0';
                E4 <= '0';
                E5 <= '0';
                if end_FPGA = '1' then
                    PE<=Play_user;
                elsif end_FPGA = '0' then
                    PE <= Play_FPGA;
                end if;
            when Play_user => 
                R1 <= '0';
                R2 <= '0';
                E1 <= '0';
                E2 <= '0';
                E3 <= '1';
                E4 <= '0';
                E5 <= '0';
                if end_time = '0' then
                    if enter = '0' then
                        PE <= Count_round;
                    elsif enter = '1' then
                        PE <= Play_user;
                    end if;
                elsif end_time = '1' then
                    PE <= Result;
                end if;
            when Count_round => 
                R1 <= '1';
                R2 <= '0';
                E1 <= '0';
                E2 <= '0';
                E3 <= '0';
                E4 <= '1';
                E5 <= '0';
                if end_round = '1' or end_game = '1' then
                    PE<= Result;
                end if;
                if end_round = '0' and end_game = '0' then
                    PE<= Waiting;
                end if;
            when Waiting => 
                R1 <= '0';
                R2 <= '0';
                E1 <= '0';
                E2 <= '0';
                E3 <= '0';
                E4 <= '0';
                E5 <= '0';
                if enter = '0' then
                    PE<= Play_FPGA;
                elsif enter = '1' then
                    PE <= Waiting;
                end if;
            when Result => 
                R1 <= '0';
                R2 <= '0';
                E1 <= '0';
                E2 <= '0';
                E3 <= '0';
                E4 <= '0';
                E5 <= '1';
                if enter = '0' then
                    PE<= Init;
                elsif enter = '1' then
                    PE <= Result;
                end if;
        end case;
    end process;
end bhv;
    
