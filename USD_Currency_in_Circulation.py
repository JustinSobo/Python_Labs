# This fun lab calculates the total number of notes printed and then returns the total number of dollars that have been physically printed (USD).
# ref: "https://www.federalreserve.gov/paymentsystems/coin_currcircvolume.htm"
billion = 1000000000

one = (1*13.1*billion)
two = (2*1.4*billion)
five = (5*3.2*billion)
ten = (10*2.3*billion)
twenty = (20*11.7*billion)
fifty = (50*2.3*billion)
hundred = (100*16.4*billion)
other = (750*0.0004*billion)

print(one+two+five+ten+twenty+fifty+hundred+other)
# Approx. 2,044,199,999,999.9998 dollars have been physically printed.
