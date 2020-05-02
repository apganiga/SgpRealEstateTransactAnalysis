USE [REAL_ESTATE]
GO

/****** Object:  Table [dbo].[TRANSACTIONS]    Script Date: 2/5/2020 11:26:38 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[TRANSACTIONS](
	[TRANS_ID] [numeric](18, 0) NOT NULL,
	[CONDO_NAME] [nvarchar](100) NOT NULL,
	[Area] [int] NULL,
	[typeOfArea] [nchar](10) NULL,
	[typeOfSale] [smallint] NULL,
	[floorRange_low] [smallint] NULL,
	[floorRange_high] [smallint] NULL,
	[noOfUnits] [smallint] NULL,
	[propertyType] [varchar](20) NULL,
	[contractDate] [date] NOT NULL,
	[contractDate_month] [smallint] NOT NULL,
	[contractDate_year] [smallint] NOT NULL,
	[district] [smallint] NULL,
	[DateCaptured] [datetime] NULL
) ON [PRIMARY]
GO


