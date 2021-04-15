module test #(
	parameter DATAWIDTH    = 32,
	parameter ADDRESSWIDTH = 32
) (
	input                           clk            , // Clock
	input                           rst_n          , // Asynchronous reset active low
	//
	input  logic [ADDRESSWIDTH-1:0] avms_address   ,
	input  logic                    avms_read      ,
	input  logic                    avms_write     ,
	input  logic [   DATAWIDTH-1:0] avms_writedata ,
	input  logic [ DATAWIDTH/8-1:0] avms_byteenable,
	output logic [   DATAWIDTH-1:0] avms_readdata
);

logic [31:0][31:0] memory;

always_ff @(posedge clk or negedge rst_n) begin : proc_memory
	if(~rst_n) begin
		memory <= '0;
	end else if (avms_write) begin
		memory[avms_address] <= avms_writedata;
	end
end

always_ff @(posedge clk or negedge rst_n) begin : proc_avms_readdata
	if(~rst_n) begin
		avms_readdata <= '0;
	end else if (avms_read) begin
		avms_readdata <= memory[avms_address];
	end
end

endmodule