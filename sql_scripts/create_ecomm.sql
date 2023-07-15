create table sale (
	salesid int,
    listid int,
    sellerid int,
    buyerid int,
    eventid int,
    dateid int,
    qtysold int,
    pricepaid double,
    commission double,
    saletime DATETIME,
    PRIMARY KEY (salesid)
);
create table listing (
	listid int,
    sellerid int,
    eventid int,
    dateid int,
    numtickets int,
    priceperticket double,
    totalprice double,
    listtime DATETIME,
    PRIMARY KEY (listid)
);
create table date (
	dateid int,
    caldate DATE,
    day VARCHAR(2),
    week int,
    month VARCHAR(3),
    qtr int,
    year int,
    holiday int,
    PRIMARY KEY(dateid)
);