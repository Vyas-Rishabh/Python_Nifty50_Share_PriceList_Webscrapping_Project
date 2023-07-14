#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
from bs4 import BeautifulSoup


# In[17]:


#HTML Code
html_code = '''
<div style="overflow-x:auto;width: 100%;">
        <table width="100%" cellspacing="0" cellpadding="0" border="0" class="mystocksbig mystocks newtab cls">
        <thead>

            <tr>
                
                <th class="alignleft large" rowspan="2"><a href="nse-replica.asp?order=symbol.dispname">COMPANY</a></th>
                
                <th class="alignleft large" rowspan="2"><a href="nse-replica.asp?order=researchText.sector">INDUSTRY</a></th>
                
                <th class="alignright large" rowspan="2"><a href="nse-replica.asp?order=nse.[close] desc">MARKET PRICE<small>(Rs)</small></a></th>
                
                <th class="alignright arrow" rowspan="2"><a href="nse-replica.asp?order=nse.change">CHANGE<small>(%)</small></a><span><img src="https://www.eqimg.com/researchmaster/images/down-trans.gif" alt="desc" title="desc" width="10" height="9" valign="absmiddle"></span></th>
                
                <th class="alignright large" rowspan="2"><a href="nse-replica.asp?order=researchText.no_shares_act desc">NO OF<br>SHARES<small>(m)</small></a></th>
                
                <th class="alignright large" rowspan="2"><a href="nse-replica.asp?order=mktcap desc">MARKET CAP.**<small>(Rs m)</small></a></th>
                
                <th class="alignright large"><a href="nse-replica.asp?order=Free_Float_Shares desc">FREE FLOAT <br>ADJ. FACTOR#</a></th>
                
                <th class="alignright large"><a href="nse-replica.asp?order=researchText.earnings desc">EARNINGS *<small>(Rs m)</small></a></th>
                
                <th class="alignright large"><a href="nse-replica.asp?order=eps desc">EPS<small>(Rs)</small></a></th>
                
                <th class="alignright large"><a href="nse-replica.asp?order=per desc">PER<small>(X)</small></a></th> 
            </tr>
            
        </thead>
        <tbody>
        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=TCS&amp;name=TCS-Stock-Quote-Chart">TCS</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/software">SOFTWARE</a></td>
	        
	        <td class="alignright">3,482.1</td>
	        <td class="alignright msgain"><small>4.2</small></td>
	        <td class="alignright">3,659.1<input type="hidden" id="TCSwtg" name="TCSwtg" value="15.1"></td>
	        <td class="alignright">12,741,000</td>
	        
	        <td class="alignright">0.3</td>
	        
	        <td class="alignright">439,040
	        </td>
	        <td class="alignright">120.0</td>
	        <td class="alignright">29.0</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=TEMH&amp;name=TECH-MAHINDRA-Stock-Quote-Chart">TECH MAHINDRA</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/software">SOFTWARE</a></td>
	        
	        <td class="alignright">1,223.0</td>
	        <td class="alignright msgain"><small>4.1</small></td>
	        <td class="alignright">974.7<input type="hidden" id="TEMHwtg" name="TEMHwtg" value="1.4"></td>
	        <td class="alignright">1,192,115</td>
	        
	        <td class="alignright">0.6</td>
	        
	        <td class="alignright">48,860
	        </td>
	        <td class="alignright">50.1</td>
	        <td class="alignright">24.4</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=INFY&amp;name=INFOSYS-Stock-Quote-Chart">INFOSYS</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/software">SOFTWARE</a></td>
	        
	        <td class="alignright">1,418.0</td>
	        <td class="alignright msgain"><small>3.9</small></td>
	        <td class="alignright">4,150.2<input type="hidden" id="INFYwtg" name="INFYwtg" value="7.0"></td>
	        <td class="alignright">5,884,973</td>
	        
	        <td class="alignright">0.8</td>
	        
	        <td class="alignright">241,080
	        </td>
	        <td class="alignright">58.1</td>
	        <td class="alignright">24.4</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=HTECH&amp;name=HCL-TECHNOLOGIES-Stock-Quote-Chart">HCL TECHNOLOGIES</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/software">SOFTWARE</a></td>
	        
	        <td class="alignright">1,149.0</td>
	        <td class="alignright msgain"><small>3.6</small></td>
	        <td class="alignright">2,713.7<input type="hidden" id="HTECHwtg" name="HTECHwtg" value="3.7"></td>
	        <td class="alignright">3,118,001</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">150,950
	        </td>
	        <td class="alignright">55.6</td>
	        <td class="alignright">20.7</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=LTI&amp;name=LTIMINDTREE-Stock-Quote-Chart">LTIMINDTREE</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/software">SOFTWARE</a></td>
	        
	        <td class="alignright">5,056.0</td>
	        <td class="alignright msgain"><small>3.3</small></td>
	        <td class="alignright">295.9<input type="hidden" id="LTIwtg" name="LTIwtg" value="1.8"></td>
	        <td class="alignright">1,496,009</td>
	        
	        <td class="alignright">0.3</td>
	        
	        <td class="alignright">34,290
	        </td>
	        <td class="alignright">115.9</td>
	        <td class="alignright">43.6</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=ECHM&amp;name=EICHER-MOTORS-Stock-Quote-Chart">EICHER MOTORS</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/auto">AUTOMOBILES</a></td>
	        
	        <td class="alignright">3,352.5</td>
	        <td class="alignright msgain"><small>2.9</small></td>
	        <td class="alignright">273.7<input type="hidden" id="ECHMwtg" name="ECHMwtg" value="1.1"></td>
	        <td class="alignright">917,440</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">25,988
	        </td>
	        <td class="alignright">95.0</td>
	        <td class="alignright">35.3</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=WPRO&amp;name=WIPRO-Stock-Quote-Chart">WIPRO</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/software">SOFTWARE</a></td>
	        
	        <td class="alignright">403.2</td>
	        <td class="alignright msgain"><small>2.3</small></td>
	        <td class="alignright">5,219.2<input type="hidden" id="WPROwtg" name="WPROwtg" value="2.5"></td>
	        <td class="alignright">2,104,373</td>
	        
	        <td class="alignright">0.3</td>
	        
	        <td class="alignright">116,975
	        </td>
	        <td class="alignright">22.4</td>
	        <td class="alignright">18.0</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=HALC&amp;name=HINDALCO-Stock-Quote-Chart">HINDALCO</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/aluminium">ALUMINIUM</a></td>
	        
	        <td class="alignright">443.4</td>
	        <td class="alignright msgain"><small>1.9</small></td>
	        <td class="alignright">2,247.2<input type="hidden" id="HALCwtg" name="HALCwtg" value="1.2"></td>
	        <td class="alignright">996,406</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">100,880
	        </td>
	        <td class="alignright">44.9</td>
	        <td class="alignright">9.9</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=TTEA&amp;name=TATA-CONSUMER-Stock-Quote-Chart">TATA CONSUMER</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/consprds">FMCG</a></td>
	        
	        <td class="alignright">848.7</td>
	        <td class="alignright msgain"><small>1.3</small></td>
	        <td class="alignright">929.0<input type="hidden" id="TTEAwtg" name="TTEAwtg" value="0.9"></td>
	        <td class="alignright">788,406</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">13,465
	        </td>
	        <td class="alignright">14.5</td>
	        <td class="alignright">58.6</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=HROH&amp;name=HERO-MOTOCORP-Stock-Quote-Chart">HERO MOTOCORP</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/auto">AUTOMOBILES</a></td>
	        
	        <td class="alignright">3,113.8</td>
	        <td class="alignright msgain"><small>1.3</small></td>
	        <td class="alignright">199.8<input type="hidden" id="HROHwtg" name="HROHwtg" value="0.7"></td>
	        <td class="alignright">622,267</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">27,968
	        </td>
	        <td class="alignright">140.0</td>
	        <td class="alignright">22.2</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=DIVI&amp;name=DIVIS-LABORATORIES-Stock-Quote-Chart">DIVIS LABORATORIES</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/pharma">PHARMACEUTICALS</a></td>
	        
	        <td class="alignright">3,660.6</td>
	        <td class="alignright msgain"><small>1.1</small></td>
	        <td class="alignright">265.5<input type="hidden" id="DIVIwtg" name="DIVIwtg" value="1.2"></td>
	        <td class="alignright">971,774</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">18,234
	        </td>
	        <td class="alignright">68.7</td>
	        <td class="alignright">53.3</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=TISCO&amp;name=TATA-STEEL-Stock-Quote-Chart">TATA STEEL</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/steel">STEEL</a></td>
	        
	        <td class="alignright">116.1</td>
	        <td class="alignright msgain"><small>1.1</small></td>
	        <td class="alignright">12,221.5<input type="hidden" id="TISCOwtg" name="TISCOwtg" value="1.7"></td>
	        <td class="alignright">1,418,912</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">76,572
	        </td>
	        <td class="alignright">6.3</td>
	        <td class="alignright">18.5</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=HLL&amp;name=HUL-Stock-Quote-Chart">HUL</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/consprds">FMCG</a></td>
	        
	        <td class="alignright">2,679.0</td>
	        <td class="alignright msgain"><small>0.9</small></td>
	        <td class="alignright">2,349.6<input type="hidden" id="HLLwtg" name="HLLwtg" value="7.5"></td>
	        <td class="alignright">6,294,555</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">101,450
	        </td>
	        <td class="alignright">43.2</td>
	        <td class="alignright">62.0</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=NEST&amp;name=NESTLE-Stock-Quote-Chart">NESTLE</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/food">FOOD &amp; TOBACCO</a></td>
	        
	        <td class="alignright">23,010.0</td>
	        <td class="alignright msgain"><small>0.8</small></td>
	        <td class="alignright">96.4<input type="hidden" id="NESTwtg" name="NESTwtg" value="2.6"></td>
	        <td class="alignright">2,218,525</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">25,484
	        </td>
	        <td class="alignright">264.3</td>
	        <td class="alignright">87.1</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=UNPS&amp;name=UPL-Stock-Quote-Chart">UPL </a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/chemicals">CHEMICALS</a></td>
	        
	        <td class="alignright">636.1</td>
	        <td class="alignright msgain"><small>0.8</small></td>
	        <td class="alignright">750.6<input type="hidden" id="UNPSwtg" name="UNPSwtg" value="0.6"></td>
	        <td class="alignright">477,461</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">42,570
	        </td>
	        <td class="alignright">56.7</td>
	        <td class="alignright">11.2</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=LART&amp;name=LT-Stock-Quote-Chart">L&amp;T</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/engg">ENGINEERING</a></td>
	        
	        <td class="alignright">2,469.7</td>
	        <td class="alignright msgain"><small>0.8</small></td>
	        <td class="alignright">1,405.6<input type="hidden" id="LARTwtg" name="LARTwtg" value="4.1"></td>
	        <td class="alignright">3,471,343</td>
	        
	        <td class="alignright">1.0</td>
	        
	        <td class="alignright">126,249
	        </td>
	        <td class="alignright">89.8</td>
	        <td class="alignright">27.5</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=CIPL&amp;name=CIPLA-Stock-Quote-Chart">CIPLA</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/pharma">PHARMACEUTICALS</a></td>
	        
	        <td class="alignright">1,028.5</td>
	        <td class="alignright msgain"><small>0.8</small></td>
	        <td class="alignright">807.2<input type="hidden" id="CIPLwtg" name="CIPLwtg" value="1.0"></td>
	        <td class="alignright">830,205</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">28,355
	        </td>
	        <td class="alignright">35.1</td>
	        <td class="alignright">29.3</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=ONGC&amp;name=ONGC-Stock-Quote-Chart">ONGC</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/energy">ENERGY</a></td>
	        
	        <td class="alignright">169.1</td>
	        <td class="alignright msgain"><small>0.7</small></td>
	        <td class="alignright">12,580.3<input type="hidden" id="ONGCwtg" name="ONGCwtg" value="2.5"></td>
	        <td class="alignright">2,126,696</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">327,436
	        </td>
	        <td class="alignright">26.0</td>
	        <td class="alignright">6.5</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=MNDRA&amp;name=ADANI-PORTS--SEZ-Stock-Quote-Chart">ADANI PORTS &amp; SEZ</a></td>
	        
	        <td class="alignleft">MISCELLANEOUS</td>
	        
	        <td class="alignright">721.8</td>
	        <td class="alignright msgain"><small>0.6</small></td>
	        <td class="alignright">2,160.1<input type="hidden" id="MNDRAwtg" name="MNDRAwtg" value="1.8"></td>
	        <td class="alignright">1,559,188</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">51,711
	        </td>
	        <td class="alignright">23.9</td>
	        <td class="alignright">30.2</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=ASPN&amp;name=ASIAN-PAINTS-Stock-Quote-Chart">ASIAN PAINTS</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/paint">PAINTS</a></td>
	        
	        <td class="alignright">3,412.7</td>
	        <td class="alignright msgain"><small>0.4</small></td>
	        <td class="alignright">959.2<input type="hidden" id="ASPNwtg" name="ASPNwtg" value="3.9"></td>
	        <td class="alignright">3,273,454</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">41,015
	        </td>
	        <td class="alignright">42.8</td>
	        <td class="alignright">79.8</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=SLIC&amp;name=SBI-LIFE-INSURANCE-Stock-Quote-Chart">SBI LIFE INSURANCE </a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/insurance">INSURANCE</a></td>
	        
	        <td class="alignright">1,318.8</td>
	        <td class="alignright msgain"><small>0.4</small></td>
	        <td class="alignright">1,001.0<input type="hidden" id="SLICwtg" name="SLICwtg" value="1.6"></td>
	        <td class="alignright">1,320,073</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">17,206
	        </td>
	        <td class="alignright">17.2</td>
	        <td class="alignright">76.7</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=ITC&amp;name=ITC-Stock-Quote-Chart">ITC</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/food">FOOD &amp; TOBACCO</a></td>
	        
	        <td class="alignright">473.7</td>
	        <td class="alignright msgain"><small>0.4</small></td>
	        <td class="alignright">12,451.2<input type="hidden" id="ITCwtg" name="ITCwtg" value="7.0"></td>
	        <td class="alignright">5,898,155</td>
	        
	        <td class="alignright">1.0</td>
	        
	        <td class="alignright">194,277
	        </td>
	        <td class="alignright">15.6</td>
	        <td class="alignright">30.4</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=TELCO&amp;name=TATA-MOTORS-Stock-Quote-Chart">TATA MOTORS</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/auto">AUTOMOBILES</a></td>
	        
	        <td class="alignright">622.7</td>
	        <td class="alignright msgain"><small>0.3</small></td>
	        <td class="alignright">3,321.9<input type="hidden" id="TELCOwtg" name="TELCOwtg" value="2.5"></td>
	        <td class="alignright">2,068,523</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">23,535
	        </td>
	        <td class="alignright">7.1</td>
	        <td class="alignright">87.9</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=IOC&amp;name=IOC-Stock-Quote-Chart">IOC</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/energy">ENERGY</a></td>
	        
	        <td class="alignright">96.5</td>
	        <td class="alignright msgain"><small>0.3</small></td>
	        <td class="alignright">14,121.2<input type="hidden" id="IOCwtg" name="IOCwtg" value="1.6"></td>
	        <td class="alignright">1,361,993</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">108,421
	        </td>
	        <td class="alignright">7.7</td>
	        <td class="alignright">12.6</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=ADEX&amp;name=ADANI-ENTERPRISES-Stock-Quote-Chart">ADANI ENTERPRISES</a></td>
	        
	        <td class="alignleft">MISCELLANEOUS</td>
	        
	        <td class="alignright">2,367.8</td>
	        <td class="alignright msgain"><small>0.2</small></td>
	        <td class="alignright">1,140.0<input type="hidden" id="ADEXwtg" name="ADEXwtg" value="3.2"></td>
	        <td class="alignright">2,699,238</td>
	        
	        <td class="alignright">0.3</td>
	        
	        <td class="alignright">22,089
	        </td>
	        <td class="alignright">19.4</td>
	        <td class="alignright">122.2</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=INDIN&amp;name=INDUSIND-BANK-Stock-Quote-Chart">INDUSIND BANK</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/bank">BANKING</a></td>
	        
	        <td class="alignright">1,379.0</td>
	        <td class="alignright msgain"><small>0.2</small></td>
	        <td class="alignright">776.0<input type="hidden" id="INDINwtg" name="INDINwtg" value="1.3"></td>
	        <td class="alignright">1,070,136</td>
	        
	        <td class="alignright">0.8</td>
	        
	        <td class="alignright">74,431
	        </td>
	        <td class="alignright">95.9</td>
	        <td class="alignright">14.4</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=COIND&amp;name=COAL-INDIA-Stock-Quote-Chart">COAL INDIA</a></td>
	        
	        <td class="alignleft">MINING</td>
	        
	        <td class="alignright">230.4</td>
	        <td class="alignright msgain"><small>0.2</small></td>
	        <td class="alignright">6,162.7<input type="hidden" id="COINDwtg" name="COINDwtg" value="1.7"></td>
	        <td class="alignright">1,419,584</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">281,331
	        </td>
	        <td class="alignright">45.7</td>
	        <td class="alignright">5.0</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=BPCL&amp;name=BPCL-Stock-Quote-Chart">BPCL</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/energy">ENERGY</a></td>
	        
	        <td class="alignright">379.7</td>
	        <td class="alignright msgain"><small>0.0</small></td>
	        <td class="alignright">2,169.3<input type="hidden" id="BPCLwtg" name="BPCLwtg" value="1.0"></td>
	        <td class="alignright">823,557</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">-609
	        </td>
	        <td class="alignright">-0.3</td>
	        <td class="alignright">-</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=ICBK&amp;name=ICICI-BANK-Stock-Quote-Chart">ICICI BANK</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/bank">BANKING</a></td>
	        
	        <td class="alignright">955.5</td>
	        <td class="alignright msloss"><small>-0.0</small></td>
	        <td class="alignright">6,997.2<input type="hidden" id="ICBKwtg" name="ICBKwtg" value="7.9"></td>
	        <td class="alignright">6,685,814</td>
	        
	        <td class="alignright">1.0</td>
	        
	        <td class="alignright">344,630
	        </td>
	        <td class="alignright">49.3</td>
	        <td class="alignright">19.4</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=RELI&amp;name=RELIANCE-IND-Stock-Quote-Chart">RELIANCE IND.</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/energy">ENERGY</a></td>
	        
	        <td class="alignright">2,739.7</td>
	        <td class="alignright msloss"><small>-0.1</small></td>
	        <td class="alignright">6,766.1<input type="hidden" id="RELIwtg" name="RELIwtg" value="22.0"></td>
	        <td class="alignright">18,536,771</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">741,310
	        </td>
	        <td class="alignright">109.6</td>
	        <td class="alignright">25.0</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=BAJAU&amp;name=BAJAJ-AUTO-Stock-Quote-Chart">BAJAJ AUTO</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/auto">AUTOMOBILES</a></td>
	        
	        <td class="alignright">4,860.0</td>
	        <td class="alignright msloss"><small>-0.1</small></td>
	        <td class="alignright">283.0<input type="hidden" id="BAJAUwtg" name="BAJAUwtg" value="1.6"></td>
	        <td class="alignright">1,375,173</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">55,309
	        </td>
	        <td class="alignright">195.5</td>
	        <td class="alignright">24.9</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=HDBK&amp;name=HDFC-BANK-Stock-Quote-Chart">HDFC BANK</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/bank">BANKING</a></td>
	        
	        <td class="alignright">1,638.8</td>
	        <td class="alignright msloss"><small>-0.1</small></td>
	        <td class="alignright">5,591.8<input type="hidden" id="HDBKwtg" name="HDBKwtg" value="10.9"></td>
	        <td class="alignright">9,163,840</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">461,487
	        </td>
	        <td class="alignright">82.5</td>
	        <td class="alignright">19.9</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=BTVL&amp;name=BHARTI-AIRTEL-Stock-Quote-Chart">BHARTI AIRTEL</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/telecom">TELECOM</a></td>
	        
	        <td class="alignright">883.5</td>
	        <td class="alignright msloss"><small>-0.2</small></td>
	        <td class="alignright">5,984.9<input type="hidden" id="BTVLwtg" name="BTVLwtg" value="6.3"></td>
	        <td class="alignright">5,287,642</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">115,353
	        </td>
	        <td class="alignright">19.3</td>
	        <td class="alignright">45.8</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=BAFIN&amp;name=BAJAJ-FINSERV-Stock-Quote-Chart">BAJAJ FINSERV</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/finance">FINANCE</a></td>
	        
	        <td class="alignright">1,611.3</td>
	        <td class="alignright msloss"><small>-0.2</small></td>
	        <td class="alignright">1,592.8<input type="hidden" id="BAFINwtg" name="BAFINwtg" value="3.0"></td>
	        <td class="alignright">2,566,424</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">122,084
	        </td>
	        <td class="alignright">76.6</td>
	        <td class="alignright">21.0</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=SUNP&amp;name=SUN-PHARMA-Stock-Quote-Chart">SUN PHARMA</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/pharma">PHARMACEUTICALS</a></td>
	        
	        <td class="alignright">1,072.6</td>
	        <td class="alignright msloss"><small>-0.3</small></td>
	        <td class="alignright">2,399.3<input type="hidden" id="SUNPwtg" name="SUNPwtg" value="3.1"></td>
	        <td class="alignright">2,573,527</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">85,608
	        </td>
	        <td class="alignright">35.7</td>
	        <td class="alignright">30.1</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=MARUTI&amp;name=MARUTI-SUZUKI-Stock-Quote-Chart">MARUTI SUZUKI</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/auto">AUTOMOBILES</a></td>
	        
	        <td class="alignright">9,618.0</td>
	        <td class="alignright msloss"><small>-0.3</small></td>
	        <td class="alignright">302.1<input type="hidden" id="MARUTIwtg" name="MARUTIwtg" value="3.4"></td>
	        <td class="alignright">2,905,406</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">80,336
	        </td>
	        <td class="alignright">265.9</td>
	        <td class="alignright">36.2</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=KOTAK&amp;name=KOTAK-MAHINDRA-BANK-Stock-Quote-Chart">KOTAK MAHINDRA BANK</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/bank">BANKING</a></td>
	        
	        <td class="alignright">1,861.7</td>
	        <td class="alignright msloss"><small>-0.4</small></td>
	        <td class="alignright">1,987.2<input type="hidden" id="KOTAKwtg" name="KOTAKwtg" value="4.4"></td>
	        <td class="alignright">3,699,593</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">147,804
	        </td>
	        <td class="alignright">74.4</td>
	        <td class="alignright">25.0</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=BJFN&amp;name=BAJAJ-FINANCE-Stock-Quote-Chart">BAJAJ FINANCE</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/finance">FINANCE</a></td>
	        
	        <td class="alignright">7,438.9</td>
	        <td class="alignright msloss"><small>-0.5</small></td>
	        <td class="alignright">605.9<input type="hidden" id="BJFNwtg" name="BJFNwtg" value="5.3"></td>
	        <td class="alignright">4,507,367</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">115,060
	        </td>
	        <td class="alignright">189.9</td>
	        <td class="alignright">39.2</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=JLVY&amp;name=JSW-STEEL-Stock-Quote-Chart">JSW STEEL</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/steel">STEEL</a></td>
	        
	        <td class="alignright">797.4</td>
	        <td class="alignright msloss"><small>-0.6</small></td>
	        <td class="alignright">2,417.2<input type="hidden" id="JLVYwtg" name="JLVYwtg" value="2.3"></td>
	        <td class="alignright">1,927,492</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">42,760
	        </td>
	        <td class="alignright">17.7</td>
	        <td class="alignright">45.1</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=APLH&amp;name=APOLLO-HOSPITALS-Stock-Quote-Chart">APOLLO HOSPITALS</a></td>
	        
	        <td class="alignleft">MISCELLANEOUS</td>
	        
	        <td class="alignright">5,148.0</td>
	        <td class="alignright msloss"><small>-0.7</small></td>
	        <td class="alignright">143.8<input type="hidden" id="APLHwtg" name="APLHwtg" value="0.9"></td>
	        <td class="alignright">740,204</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">8,877
	        </td>
	        <td class="alignright">61.7</td>
	        <td class="alignright">83.4</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=SBI&amp;name=SBI-Stock-Quote-Chart">SBI</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/bank">BANKING</a></td>
	        
	        <td class="alignright">581.8</td>
	        <td class="alignright msloss"><small>-0.7</small></td>
	        <td class="alignright">8,924.6<input type="hidden" id="SBIwtg" name="SBIwtg" value="6.2"></td>
	        <td class="alignright">5,191,893</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">565,584
	        </td>
	        <td class="alignright">63.4</td>
	        <td class="alignright">9.2</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=GRSM&amp;name=GRASIM-Stock-Quote-Chart">GRASIM</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/textiles">TEXTILES</a></td>
	        
	        <td class="alignright">1,747.5</td>
	        <td class="alignright msloss"><small>-0.7</small></td>
	        <td class="alignright">658.4<input type="hidden" id="GRSMwtg" name="GRSMwtg" value="1.4"></td>
	        <td class="alignright">1,150,577</td>
	        
	        <td class="alignright">0.6</td>
	        
	        <td class="alignright">108,692
	        </td>
	        <td class="alignright">165.1</td>
	        <td class="alignright">10.6</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=NTPC&amp;name=NTPC-Stock-Quote-Chart">NTPC</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/power">POWER</a></td>
	        
	        <td class="alignright">186.5</td>
	        <td class="alignright msloss"><small>-0.7</small></td>
	        <td class="alignright">9,696.7<input type="hidden" id="NTPCwtg" name="NTPCwtg" value="2.1"></td>
	        <td class="alignright">1,808,428</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">167,547
	        </td>
	        <td class="alignright">17.3</td>
	        <td class="alignright">10.8</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=REDY&amp;name=DR-REDDYS-LAB-Stock-Quote-Chart">DR. REDDYS LAB</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/pharma">PHARMACEUTICALS</a></td>
	        
	        <td class="alignright">5,099.4</td>
	        <td class="alignright msloss"><small>-0.8</small></td>
	        <td class="alignright">166.6<input type="hidden" id="REDYwtg" name="REDYwtg" value="1.0"></td>
	        <td class="alignright">849,333</td>
	        
	        <td class="alignright">0.7</td>
	        
	        <td class="alignright">44,702
	        </td>
	        <td class="alignright">268.4</td>
	        <td class="alignright">19.0</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=CEMCO&amp;name=ULTRATECH-CEMENT-Stock-Quote-Chart">ULTRATECH CEMENT</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/cement">CEMENT</a></td>
	        
	        <td class="alignright">8,155.0</td>
	        <td class="alignright msloss"><small>-1.0</small></td>
	        <td class="alignright">288.7<input type="hidden" id="CEMCOwtg" name="CEMCOwtg" value="2.8"></td>
	        <td class="alignright">2,354,237</td>
	        
	        <td class="alignright">0.4</td>
	        
	        <td class="alignright">50,694
	        </td>
	        <td class="alignright">175.6</td>
	        <td class="alignright">46.4</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=MAHM&amp;name=MM-Stock-Quote-Chart">M&amp;M</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/auto">AUTOMOBILES</a></td>
	        
	        <td class="alignright">1,551.5</td>
	        <td class="alignright msloss"><small>-1.0</small></td>
	        <td class="alignright">1,243.5<input type="hidden" id="MAHMwtg" name="MAHMwtg" value="2.3"></td>
	        <td class="alignright">1,929,335</td>
	        
	        <td class="alignright">0.8</td>
	        
	        <td class="alignright">98,690
	        </td>
	        <td class="alignright">79.4</td>
	        <td class="alignright">19.5</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=TITN&amp;name=TITAN-Stock-Quote-Chart">TITAN</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/retail">RETAILING</a></td>
	        
	        <td class="alignright">3,051.7</td>
	        <td class="alignright msloss"><small>-1.1</small></td>
	        <td class="alignright">887.8<input type="hidden" id="TITNwtg" name="TITNwtg" value="3.2"></td>
	        <td class="alignright">2,709,257</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">32,730
	        </td>
	        <td class="alignright">36.9</td>
	        <td class="alignright">82.8</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=PGRID&amp;name=POWER-GRID-Stock-Quote-Chart">POWER GRID</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/power">POWER</a></td>
	        
	        <td class="alignright">240.4</td>
	        <td class="alignright msloss"><small>-1.1</small></td>
	        <td class="alignright">6,975.5<input type="hidden" id="PGRIDwtg" name="PGRIDwtg" value="2.0"></td>
	        <td class="alignright">1,676,550</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">152,507
	        </td>
	        <td class="alignright">21.9</td>
	        <td class="alignright">11.0</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=UTIB&amp;name=AXIS-BANK-Stock-Quote-Chart">AXIS BANK</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/bank">BANKING</a></td>
	        
	        <td class="alignright">948.6</td>
	        <td class="alignright msloss"><small>-1.2</small></td>
	        <td class="alignright">3,079.9<input type="hidden" id="UTIBwtg" name="UTIBwtg" value="3.5"></td>
	        <td class="alignright">2,921,423</td>
	        
	        <td class="alignright">0.9</td>
	        
	        <td class="alignright">108,527
	        </td>
	        <td class="alignright">35.2</td>
	        <td class="alignright">26.9</td>
	        </tr>
		        
	        <tr bgcolor="white" height="22">
	        <td class="alignleft"><a href="/result.asp?symbol=HDFCL&amp;name=HDFC-LIFE-INSURANCE-Stock-Quote-Chart">HDFC LIFE INSURANCE</a></td>
	        
	        <td class="alignleft"><a style="color:black" href="/research-it/sector-info/insurance">INSURANCE</a></td>
	        
	        <td class="alignright">665.4</td>
	        <td class="alignright msloss"><small>-2.2</small></td>
	        <td class="alignright">2,149.7<input type="hidden" id="HDFCLwtg" name="HDFCLwtg" value="1.7"></td>
	        <td class="alignright">1,430,397</td>
	        
	        <td class="alignright">0.5</td>
	        
	        <td class="alignright">13,357
	        </td>
	        <td class="alignright">6.2</td>
	        <td class="alignright">107.1</td>
	        </tr>
		        
        </tbody>
        <tfoot>
        <tr>
        <td colspan="4">TOTAL</td>
        <td class="alignright">164,544</td>
        <td class="alignright">151,155,047</td>
        <td class="alignright"></td>
        <td class="alignright">6,422,901</td>
        <td class="alignright">Avg. PER</td>
        <td class="alignright">23.5</td>
        </tr>
        </tfoot>
    </table>
        </div>
'''


# In[18]:


#Create a BeautifulSoup object
soup = BeautifulSoup(html_code,'html.parser')


# In[19]:


#find the table from data
table = soup.find('table')


# In[20]:


#Initialize an empty lists for columns and rows
columns = []
rows = []


# In[21]:


# Extract column names
thead = table.find('thead')
for th in thead.find_all('th'):
    columns.append(th.text.strip())

# Extract data rows
tbody = table.find('tbody')
for tr in tbody.find_all('tr'):
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    rows.append(row)


# In[22]:


#Truncate or pad rows to match the number of columns
max_columns = max(len(columns), max(len(row) for row in rows))
rows1 = [row[:max_columns] + [''] * (max_columns - len(row)) for row in rows]

# Create DataFrame
df = pd.DataFrame(rows1, columns=columns)

# Print DataFrame
print(df)

# Save DataFrame to Excel
df.to_csv('data.csv', index='COMPANY')


# In[ ]:





# In[ ]:




