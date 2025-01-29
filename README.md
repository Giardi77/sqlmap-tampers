# sqlmap-tampers

### in order to use the tampers you should move them in the sqlmap/tamper directory

if installed with pip just do this to reveal sqlmap location

<code>
  pip list -v 2> /dev/null | grep sqlmap | export pipbinslocation=$(awk '{print $3}') && echo "${pipbinslocation}/sqlmap/tamper/"
</code>

if installed with apt it should be under

<code>
  /usr/share/sqlmap/tamper
</code>
