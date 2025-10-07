**Column A - ID** 
*  Integer 
* AICC Identification number, duplicate values not allowed. Used to join Fire Perimeters (polygons) to Fire Locations (points). Perimeters FIREID = Fire points ID.
* Likely not useful, but could be an input variable if the above is useful
**Column B - NAME**
* String 
* Name assigned to incident
* Often provide an approximate location, could be input variable
**Column C - FIRESEASON**
* Integer
* Year that fire started
* input variable?  - might be useful for selecting which rows to use
**Column D - FIRESEASONS**
* Integer range
* format: *startyear - endyear*
* group of ten years the fire took place in
* input variable? - might be useful for selecting which rows to use
* Question - are there changes made to the fire recording system at the start of these 10 year sections - seems like some columns start being recorded at 10 year intervals
**Column E - LASTUPDATTIME**
* Date and time
* Date and time the record was updated. Date is expressed MM/DD/YYYY, time is in 12 hour format
* input variable?
**Column F - MGMTORGID**
* String
* Agency that has primary protection responsibility at the point of origin at the time of the incident.
* DOF, AFS, USFS, etc.?
* input variable?
**Column G - MGMTOFFICEID**
* String
* Unit ID code for the administrative unit at the point or origin at the time of the incident.
* input variable?
**Column H - MGMTOPTIONID**
* String
* Fire Management Options at the time of ignition.
* Values generally include: Critical, Full, Modified, Limited, Unplanned, Prescribed.
* Question: What does this mean?
* input variable?
**Column I - PRESCRIBEDFIRE**
* Yes or No - represent as bool
* This field describes whether the fire type was a prescribed fire (i.e., planned ignition).
* input variable?
**Column J - LATITUDE**
* Float
* Latitude coordinate of where the incident started. Format is decimal degrees. This value can change as more information about the fire event becomes available.
* Output variable?
**Column K - LONGITUDE**
* Float
* Longitude coordinate of where the incident started. Format is decimal degrees. This value can change as more information about the fire event becomes available.
* Output variable?
**Column L - MAPNAME**
* String
* Name of the UGSG topographic map.
* Input variable? 
**Column M - MAPNUMBER**
* empty column - might have gotten combined with mapname
* n/a
**Column N - NEARESTWEATHERSTA**
* string
* Name of the nearest weather station. Include station identification number, if known.
* Input variable 
**Column O - ORIGINOWNERID**
* string
* Land owner at site of fire origin at the time of the incident, if known.
* input variable
**Column P - ORIGINADMINUNITID
* string
* Administrative unit at the site of fire origin, if known.
* input variable?
**Column Q - DISCOVERYDATETIME**
* date and time
* Date and time the fire was discovered. Date is expressed as MM/DD/YYYY, time is in 12 hour format.
* output variable
**Column R - DISCOVERYSIZE**
* float
* Estimated size of fire at time of discovery, expressed in acres.
* output variable
Column S - IADATETIME
* date and time 
* Date and time of initial attack, if any. Date is expressed as MM/DD/YYYY, time is in 12 hour format.
* mostly empty column
* input variable?
**Column T - IASIZE**
* float
* Estimated size of fire at the time of initial attack, expressed in acres.
* output variable
**Column U - INITIALBEHAVIOR**
* string 
* initial behavior of the fire, if known
* Values generally include: Creeping, Crowning, Out, Rank 1, Rank 2, Rank 3, Rank 4, Rank 5, Rank 6, Running, Smoldering, Unknown.
* output variable
**Column V - CONTROLDATETIME**
* date and time
* Date and time the fire was classified as controlled. Date is in MM/DD/YYYY format, time is in 12 hour format.
* output variable?
**Column W - OUTDATE**
* date and time
* Date the fire was classified as out. Date is expressed as MM/DD/YYYY, time is in 12 hour format.
* output variable?
**Column X - ESTIMATEDTOTALACRES**
* float
* Estimated total acres of fire. This field SHOULD be used to calculate total acres.
* output variable
**Column Y - ACTUALTOTALACRES**
* float
* Actual total acres, if known. This field SHOULD NOT be used to calculate total acreages.
* output variable
**Column Z - ESTIMATEDTOTALCOST**
* float/money
* Estimated total cost., expressed in US Dollars.
* output variable
**Column AA - GENERALCAUSE**
* string
* General cause of the fire, if known.
* Values generally include: False Alarm (F/A), Human, Lightning, Lightning-WFU, Natural Out, Prescribed, Unknown.
* input variable
**Column AB - SPECIFICCAUSE**
* string
* Specific cause of the fire, if known.
* input variable
**Column AC - ORIGINSLOPE**
* int range
* Approximate slope at site of fire origin. Expressed in a range of degrees.
* unknown, 0-25, 26-40, 41-55, 56-75, 76+
* input variable
**Column AD - ORIGINASPECT**
* direction a slope faces
* Approximate aspect at site of fire origin, if known. Expressed in compass directions, may be descriptive, or Unknown.
* Expressed in compass directions (East, North, Northeast, Northwest, South, Southwest, Southeast, West) or may be descriptive (Flat, Ridge Top), or Unknown.
* input variable
**Column AE - ORIGINELEVATION** 
* integer range
* Estimated elevation of the fire origin in 500 foot (0-500) increments or 1000 foot increments for values over 500. Units are feet above mean sea level (MSL).
* 0-500, 501-1500, 1500 -2500, 2501- 3500, etc. , 8501+
* input variable
**Column AF - ORIGINTOWNSHIP**
* Int + cardinal direction char i.e 002W
* Public Land Survey Township where the fire started.
* input variable
**Column AG - ORIGINRANGE**
* int + cardinal direction char i.e 003N
* Public Land Survey Range number of the Township where the fire started.
* input variable
**Column AH - ORIGINSECTION**
* int
* Public Land Survey Section number of where the fire started. Sections are generally numbered from 1-36.
* input variable 
**Column AI - ORIGINQUARTER**
* mostly empty
* Public Land Survey Section Subdivision of where the fire started.
* input varaible
**Column AJ - ORIGINMERIDIAN**
* string
* Public Land Survey Meridian of where the fire started.
* Copper River, Fairbanks, Seward, Kateel, or Umiat
* input variable
**Column AK - STRUCTURESTHREATENED**
* int 
* number of structures threatened if known
* output variable?
**Column AL - STRUCTURESBRNED**
* int
* number of structures burned, if known
* output variable
**Column AM - PRIMARYFUELTYPE**
* string
* Primary fuel type, if known.
* Aspen/Birch, Black Spruce, Brush, Dead White Spruce, Grass, Hardwoods, Live White Spruce, Mixed(Hardwoods/Softwoods), Mixed Trees, Other, Slash, Tundra, Unknown, White Spruce, Tussock
* input variable
**Columns AN -AR **
* all empty 
* HARDCOPYREPORTAVAILABLE, TYPE1ASSIGNEDDATE, TYPE1RELEASEDDATE, TYPE2ASSIGNEDDATE, TYPE2RELEASEDDATE
**Column AS - AFSNUMBER**
* string
* Fire event number assigned by BLM Alaska Fire Service dispatch.
* input variable - probably not actually useful
**Column AT - DOFNUMBER**
* string
* Fire event number assigned by DNR Division of Forestry dispatch.
* input variable - probably not actually useful
**COLUMN AU - USFSNUMBER**
* string
* Fire event number assigned by USDA Forest Service dispatch.
* input variable - probably not actually useful
**COLUMN AV - ADDITIONALNUMBER**
* string
* mostly empty
* Any additional number assigned to the fire event.
* input variable - probably not actually useful
**COLUMN AW - FALSEALARM**
* bool Y/N
* Describes is the fire event was classified as a false alarm. Yes (Y) or No (N)
* input variable - maybe remove false alarms from data
* Question - should we remove false alarms from the dataset?
**COLUMN AX - FORCESITRPT**
* Data and time
* Forces a fire to appear on the sit report on the day in the field. Used for fires that are reported after they start or are already out.
* input variable - probably not actually useful
* question - what does this actually mean?
**COLUMN AY - FORCESITRPT**
* Null
* Whether the the fire has appeared on a situation report, Field not typically used.
* input variable - definitely not useful 
**COLUMN AZ - RECORDNUMBER**
* int
* Fire sequence number, unique within a give year
* input variable - probably not useful - could maybe find number of fires in a given year by finding maximum
**COLUMN BA - COMPLEX**
* string
* mostly empty
* Name of complex. Applicable only if fire was incorporated into a complex at any point before declared contained. A complex is two or more incidents located in the same general area which are assigned to a single incident commander or unified command.
* input variable - probably not useful
* Question: Is this an important thing to look at?
**COLUMN BB - IMPORT_NOTES**
* string 
* For the scenario where the record has been imported from another system, notes about the fire event record.
* neither - ignore column
**COLUMN BC - WFUFIRE**
* bool
* Wildland Fire Use. A natural cause fire that is managed for resource objectives.
* mostly empty
* input variable - might be useful for finding outliers
**COLUMN BD - REPORTRECEIVEDDATE**
* date and time
* Date and time of final report. Date is expressed as MM/DD/YYYY, time is in 12 hour format.
* input variable - almost certainly not useful
**COLUMN BE - ISCOMPLEX**
* bool y/n
* Specifies if the fire was part of a complex. Yes (Y) or null.
* input variable - likely not useful but not sure
**COLUMN BF - CARRYOVER**
* string
* The name of the previous seasons fire that is carried into this season. Coal seam fires are an example. Value is the a string of the fire name.
* input variable - probably not useful, mostly empty
**COLUMN BG - STATEADSID**
* string
* The unique ID in the state dispatch system
* input variable - probably useless
**COLUMN BH - ORIGINAL_LATITUDE**
* float 
* Originally reported latitude coordinate of where the incident started. Format is decimal degrees.
* output variable
**COLUMN BI - ORIGINAL_LONGITUDE**
* float 
* Originally reported longitude coordinate of where the incident started. Format is decimal degrees.
* Typically negative numbers, but could be positive if the fire is in the Aleutians.
* output variable
**COLUMN BJ -IRWINID**
* hash string?
* ID assigned by IRWIN system
* input variable - probably useless
**COLUMN BK - SUPPRESSIONSTRATEGY**
* String
* suppression strategy being used for fire
* Confine, Full Suppression, Monitor, N/A, Poit Zone Protection, Point Zone Suppression, NULL
* Input variable?
**COLUMN BL - FIREMGMTCOMPLEXITY**
* String
* Complexity of the fire management. Value are Type 1 through Type 5. Type 1 is the most complex. Usually implies a fire urban interface and/or multiple agencies involved.
* Input Variable?
**COLUMN BM - ADSPERMISSIONSTATE**
* String
* Whether the Fire is managed via the ICS 209 system. Denotes who can update certain attributes in the fire record.
* Null, false, default, or ICS209
* Input Variable - probably useless
**COLUMN BN - OWNERKIND**
* String
* Type of owner
* Federal, Private, Other, Null
* Other includes State of Alaska
* Input Variable 
**COLUMN BO - FIRECODEREQUESTED**
* Bool 
* Whether the fire code system should supply a fire code.
* input variable - probably not useful
* Question - What does this mean?
**COLUMN BP - ISREIMBURSABLE**
* Bool 
* Specifies whether agencies can recover costs associated with an incident.
* Input variable - not useful
**COLUMN BQ - ISFSASSISTED**
* Bool
* Whether the fire code was issued to allow the USFS to supply resources.
* input variable - not useful
**COLUMN BR - ISTRESPASS**
* Bool
* Specifies if the fire was caused human-caused fire and where negligence or intent has been established.
* input variable - probably not useful
**COLUMN BS - FIRECODENOTES**
* String
* Notes on why the firecode was issued.
* input variable - probably not useful
**COLUMN BT - CONTAINMENTDATETIME**
* Date and time
* Date and time the fire was contained, if known. Date is expressed as MM/DD/YYYY, time is in 12 hour format.
* output variable 
**COLUMN BU - CONFLICTIRWINID**
* String
* IRWIN ID of conflicting Irwin record. Another is fire is very close and is not out.
* input variable - I don't think this is useful
**COLUMN BV - COMPLEXPARENTIRWINID**
* If the fire is part of a complex this field will be an IRWID ID. If the fire is not part of a complex, this field will be NULL.
* input variable - I don't think this is useful
**COLUMN BW - ISVALID**
* for internal use
* not useful for us
**COLUMN BX - MERGEDINTO**
* string
* mostly empty
* Record number of the consuming fire.
* input variable - probably not useful
**COLUMN BY - MERGEDDATE**
* Date
* Date fire merged with another fire.
* input variable - probably not useful
**COLUMN BZ - MERGED_REL_IRWINIRID**
* String
* For the scenario where multiple fires have burned together, identified the IRWIN ID
* This probably isn't useful
**COLUMN CA - COMPLEX_REL_IRWINIRID**
* String 
* Mostly empty
* For the scenario where multiple fires are managed as a complex, identifies the complex by capturing a complex ID.
* This probably isn't useful
**COLUMN CB - FIRECAUSE**
* String
* Cause of fire
* Natural, Human, Undetermined, false alarm, null
* ouptput variable?
**COLUMN CC - ISQUARANTINED**
* bool
* Identified quarantined records.
* variable ?type?
**COLUMN CD - CERTIFIED_IN_INFORM**
* bool
* Identifies records that have been certified in the  InFORM reporting platform.
* proably not useful
**COLUMN CE - WCE_INCIDENTID**
* string
* WildCAD incident ID
* might be useful
* question? - what is wildCAD
**COLUMN CF - MGMTOPTION_PROTDATE**
* Fire Management Options and Conversion Date (when appropriate) at the time of ignition.
* Values generally include: Critical, Full, Modified (Jul 10), Modified (Aug 10), Modified (Aug 20) , Limited, Unplanned, Prescribed.
* input variable - not sure if useful

