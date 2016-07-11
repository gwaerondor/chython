INPUT=${1}
OUTPUT=${INPUT}.translated.py

python ~/chython/chython/chython.py ${INPUT} ${OUTPUT}
python ${OUTPUT}