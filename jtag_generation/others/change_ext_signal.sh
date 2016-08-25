find  -type f -name 'pos0*.txt' -exec sed -i 's/^0 \; \:RO\_MODE0\[0\]\[1\]/1 \; \:RO\_MODE0\[0\]\[1\]/' {} \;
find  -type f -name 'pos1*.txt' -exec sed -i 's/^0 \; \:RO\_MODE0\[1\]\[1\]/1 \; \:RO\_MODE0\[1\]\[1\]/' {} \;
find  -type f -name 'pos2*.txt' -exec sed -i 's/^0 \; \:RO\_MODE0\[2\]\[1\]/1 \; \:RO\_MODE0\[2\]\[1\]/' {} \;
find  -type f -name 'pos3*.txt' -exec sed -i 's/^0 \; \:RO\_MODE0\[3\]\[1\]/1 \; \:RO\_MODE0\[3\]\[1\]/' {} \;
find  -type f -name 'pos4*.txt' -exec sed -i 's/^0 \; \:RO\_MODE0\[4\]\[1\]/1 \; \:RO\_MODE0\[4\]\[1\]/' {} \;
find  -type f -name 'pos5*.txt' -exec sed -i 's/^0 \; \:RO\_MODE0\[5\]\[1\]/1 \; \:RO\_MODE0\[5\]\[1\]/' {} \;
