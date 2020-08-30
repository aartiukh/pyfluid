import sympy as sp
import numpy as np

def vector_one():
    t = sp.symbols('t')
    vector = np.array([-539.6375615020955 + 539.6337433969725 * sp.exp(t), -375.60648142580203 +
                       375.60767260044304 * sp.exp(t), -261.30219193201566 +
                       261.322070631259 * sp.exp(t), -159.09279210933326 +
                       159.1525129143559 * sp.exp(t), -96.86349261617227 +
                       96.97543964778379 * sp.exp(t), -82.21687863234763 +
                       82.37221466514808 * sp.exp(t), -87.39593458193708 +
                       87.58971744358452 * sp.exp(t), -107.12233748316402 +
                       107.35757014531958 * sp.exp(t), -151.4345279502723 +
                       151.71967766733286 * sp.exp(t), -260.66073430297604 +
                       261.00770573243636 * sp.exp(t), -614.1398046038818 +
                       614.537338154802 * sp.exp(t), -1431.355486819206 +
                       1431.650924958073 * sp.exp(t), -1944.532577217367 +
                       1944.5340403282187 * sp.exp(t), -1468.4324689786245 +
                       1468.1007894563604 * sp.exp(t), 1169.1621738251251 -
                       1169.8906848535685 * sp.exp(t), -365.20416366439383 +
                       365.2058574584351 * sp.exp(t), -253.2728341084351 +
                       253.26351273870966 * sp.exp(t), -177.9655484789129 +
                       177.95823839407186 * sp.exp(t), -116.10671965260617 +
                       116.12097345207923 * sp.exp(t), -80.82334456797736 +
                       80.87946893411268 * sp.exp(t), -73.1883793149565 +
                       73.28661272124073 * sp.exp(t), -78.53377919976907 +
                       78.66708468522033 * sp.exp(t), -94.30688363957805 +
                       94.4717637112416 * sp.exp(t), -126.66842355521204 +
                       126.86262590456369 * sp.exp(t), -195.57097545272654 +
                       195.78525450099863 * sp.exp(t), -349.70959927598824 +
                       349.89044925564986 * sp.exp(t), -500.9226829235922 +
                       500.90238029834006 * sp.exp(t), -228.92334725373814 +
                       228.56417881521776 * sp.exp(t), 751.9502858401434 -
                       752.6574456978153 * sp.exp(t), 3581.0560776540624 -
                       3582.1529846385642 * sp.exp(t), -241.3594654469986 +
                       241.37997327583275 * sp.exp(t), -169.12073906770462 +
                       169.11506637613047 * sp.exp(t), -118.37059526328046 +
                       118.34844159326394 * sp.exp(t), -77.63204773826008 +
                       77.60842609234192 * sp.exp(t), -55.850061220574155 +
                       55.84723267535942 * sp.exp(t), -52.34601169525068 +
                       52.37234772583064 * sp.exp(t), -56.86102129621336 +
                       56.91125164820863 * sp.exp(t), -67.2184749138998 +
                       67.2857444610311 * sp.exp(t), -86.09606811674652 +
                       86.17141195725415 * sp.exp(t), -119.76741642285552 +
                       119.82959601819005 * sp.exp(t), -165.02054053788848 +
                       164.99852522440028 * sp.exp(t), -100.92236132877723 +
                       100.65476896514288 * sp.exp(t), 297.0960248626064 -
                       297.7196762283711 * sp.exp(t), 1169.3031947047575 -
                       1170.2804298862045 * sp.exp(t), 3347.6240514774245 -
                       3348.9726522489627 * sp.exp(t), -128.88547560730893 +
                       128.94338251127485 * sp.exp(t), -97.76218724171991 +
                       97.78020883892628 * sp.exp(t), -69.19568714325098 +
                       69.1769663004145 * sp.exp(t), -43.53839881952298 +
                       43.49215430117948 * sp.exp(t), -29.145869445658775 +
                       29.094137126124387 * sp.exp(t), -27.073681501692715 +
                       27.0320667101966 * sp.exp(t), -29.864762114872782 +
                       29.83218522003959 * sp.exp(t), -34.71213822381791 +
                       34.6813995310594 * sp.exp(t), -41.494650385834795 +
                       41.453955207175625 * sp.exp(t), -48.102668518738646 +
                       48.024789668625715 * sp.exp(t), -32.255525057317705 +
                       32.06120155739713 * sp.exp(t), 94.7937147198213 -
                       95.25725151519492 * sp.exp(t), 417.81065201149806 -
                       418.6350532589737 * sp.exp(t), 963.8560045962562 -
                       965.0229801439052 * sp.exp(t), 2086.393146979716 -
                       2087.8688719039187 * sp.exp(t), -58.850804301245674 +
                       58.95097192238414 * sp.exp(t), -53.78467813107814 +
                       53.843205985626106 * sp.exp(t), -40.229049124876745 +
                       40.237294939526386 * sp.exp(t), -23.43868755086591 +
                       23.39821189667792 * sp.exp(t), -11.568098496650832 +
                       11.498798934699748 * sp.exp(t), -8.458496010885387 +
                       8.381473052889328 * sp.exp(t), -9.176469373716378 +
                       9.09599452589805 * sp.exp(t), -10.293536316961896 +
                       10.204663999413368 * sp.exp(t), -10.180171986153692 +
                       10.071672166021106 * sp.exp(t), -3.8854533477467186 +
                       3.7281882521490814 * sp.exp(t), 29.979407192977163 -
                       30.26817027521189 * sp.exp(t), 136.8063383112676 -
                       137.36853264715145 * sp.exp(t), 322.812499523296 -
                       323.71539880242585 * sp.exp(t), 553.0520863374076 -
                       554.2454447187746 * sp.exp(t), 852.9292223412303 -
                       854.3012808000354 * sp.exp(t), -37.08087535283161 +
                       37.20499104534851 * sp.exp(t), -38.052823175917304 +
                       38.143710455595304 * sp.exp(t), -30.339293902714807 +
                       30.37818705986802 * sp.exp(t), -17.546440078059327 +
                       17.527616488134374 * sp.exp(t), -6.303534397438088 +
                       6.243255020676225 * sp.exp(t), -1.7390853247458464 +
                       1.6609322059540892 * sp.exp(t), -0.978227641663457 +
                       0.8904850367639092 * sp.exp(t), -0.6032049536391724 +
                       0.5032582923324824 * sp.exp(t), 1.4780531075428414 -
                       1.6005552418385776 * sp.exp(t), 10.282117837134697 -
                       10.458008675460748 * sp.exp(t), 42.0150307617586 -
                       42.32968932020187 * sp.exp(t), 119.16585660582902 -
                       119.75111401320515 * sp.exp(t), 228.04121305200886 -
                       228.94117540136537 * sp.exp(t), 333.2558570655906 -
                       334.39421267650346 * sp.exp(t), 415.10051433055247 -
                       416.32591225107444 * sp.exp(t), -30.47400779870729 +
                       30.608297264416123 * sp.exp(t), -32.614167844764665 +
                       32.72159757510695 * sp.exp(t), -27.102352891013066 +
                       27.15960197216728 * sp.exp(t), -16.349228354036157 +
                       16.346662862023827 * sp.exp(t), -5.7708203482063745 +
                       5.7221651568730625 * sp.exp(t), -0.6556792881665361 +
                       0.5852621238391622 * sp.exp(t), 0.7234972442180307 -
                       0.8054175058818043 * sp.exp(t), 1.5223616823934467 -
                       1.6173977167210865 * sp.exp(t), 3.950342402397215 -
                       4.069089646174975 * sp.exp(t), 12.83333150555288 -
                       13.008832664873498 * sp.exp(t), 41.59228763410343 -
                       41.91211392823235 * sp.exp(t), 104.67914986770211 -
                       105.26851219617507 * sp.exp(t), 185.92306904294628 -
                       186.8120963791571 * sp.exp(t), 256.082357359714 -
                       257.1824601856736 * sp.exp(t), 297.22546481736424 -
                       298.3742308223231 * sp.exp(t), -28.77810484823398 +
                       28.915252209515877 * sp.exp(t), -31.145610219205775 +
                       31.257965042322386 * sp.exp(t), -26.224582529665298 +
                       26.287593259251814 * sp.exp(t), -16.106991886783995 +
                       16.109872488665886 * sp.exp(t), -5.819363974434301 +
                       5.7750167065549745 * sp.exp(t), -0.6126246731421614 +
                       0.5455472974193847 * sp.exp(t), 0.9111962849587649 -
                       0.990167992542045 * sp.exp(t), 1.798568727709041 -
                       1.8908269207398982 * sp.exp(t), 4.287283701357137 -
                       4.403698896684348 * sp.exp(t), 13.1390689114511 -
                       13.313633409676221 * sp.exp(t), 40.95856599808437 -
                       41.279579783995246 * sp.exp(t), 100.17199421636028 -
                       100.76228439609731 * sp.exp(t), 174.40529059513443 -
                       175.2904164343744 * sp.exp(t), 236.39744620171774 -
                       237.48533411122446 * sp.exp(t), 269.37589095332805 -
                       270.50184698567534 * sp.exp(t), -30.47400779870719 +
                       30.608297264415967 * sp.exp(t), -32.614167844764644 +
                       32.72159757510694 * sp.exp(t), -27.102352891013055 +
                       27.15960197216728 * sp.exp(t), -16.349228354036168 +
                       16.346662862023834 * sp.exp(t), -5.77082034820637 +
                       5.722165156873057 * sp.exp(t), -0.6556792881665299 +
                       0.5852621238391542 * sp.exp(t), 0.7234972442180414 -
                       0.8054175058818123 * sp.exp(t), 1.5223616823934556 -
                       1.6173977167210989 * sp.exp(t), 3.9503424023972276 -
                       4.069089646174991 * sp.exp(t), 12.833331505552891 -
                       13.008832664873518 * sp.exp(t), 41.59228763410345 -
                       41.91211392823238 * sp.exp(t), 104.67914986770217 -
                       105.26851219617515 * sp.exp(t), 185.9230690429463 -
                       186.81209637915714 * sp.exp(t), 256.08235735971385 -
                       257.1824601856737 * sp.exp(t), 297.2254648173643 -
                       298.37423082232283 * sp.exp(t), -37.080875352831455 +
                       37.204991045348365 * sp.exp(t), -38.052823175917275 +
                       38.14371045559527 * sp.exp(t), -30.339293902714807 +
                       30.378187059868026 * sp.exp(t), -17.546440078059337 +
                       17.527616488134385 * sp.exp(t), -6.303534397438113 +
                       6.243255020676248 * sp.exp(t), -1.7390853247458735 +
                       1.660932205954114 * sp.exp(t), -0.978227641663489 +
                       0.8904850367639412 * sp.exp(t), -0.6032049536392097 +
                       0.5032582923325224 * sp.exp(t), 1.4780531075427916 -
                       1.6005552418385278 * sp.exp(t), 10.282117837134619 -
                       10.45800867546067 * sp.exp(t), 42.01503076175845 -
                       42.32968932020172 * sp.exp(t), 119.16585660582867 -
                       119.75111401320483 * sp.exp(t), 228.04121305200795 -
                       228.94117540136446 * sp.exp(t), 333.25585706558843 -
                       334.3942126765013 * sp.exp(t), 415.1005143305449 -
                       416.32591225106614 * sp.exp(t), -58.85080430124559 +
                       58.95097192238403 * sp.exp(t), -53.784678131078195 +
                       53.84320598562615 * sp.exp(t), -40.22904912487675 +
                       40.237294939526414 * sp.exp(t), -23.438687550865918 +
                       23.398211896677928 * sp.exp(t), -11.568098496650837 +
                       11.49879893469975 * sp.exp(t), -8.458496010885389 +
                       8.38147305288933 * sp.exp(t), -9.176469373716381 +
                       9.095994525898059 * sp.exp(t), -10.293536316961903 +
                       10.204663999413372 * sp.exp(t), -10.180171986153699 +
                       10.071672166021116 * sp.exp(t), -3.8854533477467257 +
                       3.7281882521490886 * sp.exp(t), 29.979407192977185 -
                       30.268170275211908 * sp.exp(t), 136.8063383112678 -
                       137.36853264715165 * sp.exp(t), 322.81249952329654 -
                       323.7153988024264 * sp.exp(t), 553.0520863374089 -
                       554.2454447187762 * sp.exp(t), 852.9292223412341 -
                       854.3012808000401 * sp.exp(t), -128.88547560730856 +
                       128.9433825112745 * sp.exp(t), -97.76218724171983 +
                       97.7802088389262 * sp.exp(t), -69.19568714325095 +
                       69.17696630041448 * sp.exp(t), -43.53839881952298 +
                       43.49215430117949 * sp.exp(t), -29.145869445658754 +
                       29.094137126124373 * sp.exp(t), -27.073681501692683 +
                       27.03206671019657 * sp.exp(t), -29.864762114872747 +
                       29.83218522003955 * sp.exp(t), -34.71213822381787 +
                       34.681399531059355 * sp.exp(t), -41.49465038583475 +
                       41.45395520717559 * sp.exp(t), -48.102668518738554 +
                       48.024789668625615 * sp.exp(t), -32.255525057317506 +
                       32.0612015573969 * sp.exp(t), 94.79371471982226 -
                       95.25725151519588 * sp.exp(t), 417.8106520115018 -
                       418.6350532589776 * sp.exp(t), 963.8560045962682 -
                       965.0229801439174 * sp.exp(t), 2086.393146979758 -
                       2087.8688719039606 * sp.exp(t), -241.35946544699698 +
                       241.37997327583105 * sp.exp(t), -169.1207390677038 +
                       169.11506637612962 * sp.exp(t), -118.37059526327991 +
                       118.3484415932634 * sp.exp(t), -77.63204773825974 +
                       77.60842609234157 * sp.exp(t), -55.85006122057385 +
                       55.84723267535913 * sp.exp(t), -52.34601169525035 +
                       52.37234772583032 * sp.exp(t), -56.86102129621302 +
                       56.91125164820828 * sp.exp(t), -67.21847491389937 +
                       67.28574446103066 * sp.exp(t), -86.09606811674595 +
                       86.17141195725355 * sp.exp(t), -119.7674164228547 +
                       119.82959601818919 * sp.exp(t), -165.02054053788692 +
                       164.99852522439872 * sp.exp(t), -100.9223613287707 +
                       100.65476896513643 * sp.exp(t), 297.0960248626305 -
                       297.71967622839605 * sp.exp(t), 1169.3031947048253 -
                       1170.2804298862718 * sp.exp(t), 3347.6240514776314 -
                       3348.9726522491646 * sp.exp(t), -365.20416366438747 +
                       365.20585745842874 * sp.exp(t), -253.27283410843057 +
                       253.26351273870515 * sp.exp(t), -177.96554847890906 +
                       177.958238394068 * sp.exp(t), -116.10671965260282 +
                       116.12097345207586 * sp.exp(t), -80.82334456797433 +
                       80.87946893410962 * sp.exp(t), -73.18837931495348 +
                       73.2866127212377 * sp.exp(t), -78.53377919976572 +
                       78.66708468521699 * sp.exp(t), -94.3068836395741 +
                       94.47176371123768 * sp.exp(t), -126.66842355520683 +
                       126.86262590455848 * sp.exp(t), -195.570975452719 +
                       195.78525450099121 * sp.exp(t), -349.70959927597505 +
                       349.8904492556366 * sp.exp(t), -500.92268292355686 +
                       500.90238029830465 * sp.exp(t), -228.92334725363997 +
                       228.5641788151193 * sp.exp(t), 751.9502858403702 -
                       752.6574456980409 * sp.exp(t), 3581.0560776546254 -
                       3582.152984639134 * sp.exp(t), -539.6375615019748 +
                       539.6337433968517 * sp.exp(t), -375.60648142570085 +
                       375.6076726003419 * sp.exp(t), -261.3021919319517 +
                       261.3220706311951 * sp.exp(t), -159.09279210933667 +
                       159.15251291435936 * sp.exp(t), -96.863492616258 +
                       96.97543964786958 * sp.exp(t), -82.21687863249889 +
                       82.3722146652994 * sp.exp(t), -87.39593458214193 +
                       87.58971744378908 * sp.exp(t), -107.12233748341832 +
                       107.35757014557379 * sp.exp(t), -151.43452795057402 +
                       151.71967766763456 * sp.exp(t), -260.6607343033184 +
                       261.00770573277873 * sp.exp(t), -614.1398046042349 +
                       614.5373381551549 * sp.exp(t), -1431.3554868193862 +
                       1431.6509249582534 * sp.exp(t), -1944.5325772169663 +
                       1944.5340403278146 * sp.exp(t), -1468.4324689772247 +
                       1468.100789454961 * sp.exp(t), 1169.1621738287288 -
                       1169.890684857163 * sp.exp(t)])
    return vector