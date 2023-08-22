import wavedrom
svg = wavedrom.render("""
{
"signal" : 
 [
    { "name": "CLK_REF  (62.5 MHz)", "wave": "P..............|.....", "period": 2 },
    { "name": "CLK_MASTER (125 MHz)", "wave": "P.............................|...........", "period": 1 },
    { "name": "SYNC", "wave": "l...h...l.....................|...h...l...", "node": "....a", "period": 1 },
  {},
    { "name": "FRAME", "wave": "=.....=.......................|.....=.....", "data": ["", "N", "N+1"], "period": 1, "phase": 0 },
  { "name": "ADDRESS", "wave": "=.....=...................=...|.....=.....", "data": ["", "0", "", "0"], "node": "......b", "period": 1, "phase": 0 }
 ],
 "edge":
 [
 "a~>b"
 ],
"config" : { "hscale" : 0.5, "skin": "narrow" }
} 
""")
svg.saveas("ncr_clk_sync_lineperiod_OK.svg")