create table cms.category (
	catid int,
	catgroup VARCHAR(50),
	catname VARCHAR(50),
	catdesc VARCHAR(100),
	PRIMARY KEY (catid)
);
create table cms.event (
	eventid int,
	venueid int,
	catid int,
	dateid int,
	eventname VARCHAR(100),
	starttime timestamp,
	PRIMARY KEY (eventid)
);
create table cms.venue (
	venueid int,
	venuename VARCHAR(50),
	venuecity VARCHAR(50),
	venuestate VARCHAR(3),
	venueseats int,
	PRIMARY KEY (venueid)
);