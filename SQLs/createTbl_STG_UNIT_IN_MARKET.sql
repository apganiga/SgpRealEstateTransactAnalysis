USE [REAL_ESTATE]
GO

/****** Object:  Table [stg].[STG_UNIT_IN_MARKET]    Script Date: 3/5/2020 8:41:44 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[stg].[STG_UNIT_IN_MARKET]') AND type in (N'U'))
DROP TABLE [stg].[STG_UNIT_IN_MARKET]
GO

/****** Object:  Table [stg].[STG_UNIT_IN_MARKET]    Script Date: 3/5/2020 8:41:44 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [stg].[STG_UNIT_IN_MARKET](
	[CONDO_NAME] [varchar](100) NOT NULL,
	[PRICE] [varchar](100) NULL,
	[TYPE] [varchar](100) NULL,
	[TENURE] [varchar](100) NULL,
	[TOP_] [varchar](100) NULL,
	[AREA] [varchar](100) NULL,
	[PSF] [varchar](100) NULL,
	[AGENT_NUMBER] [varchar](100) NULL,
	[PAGE_NO] [varchar](100) NULL,
	[SOURCE] [varchar](100) NULL,
	[AGENT_COMMENT] [varchar](5000) NULL
) ON [PRIMARY]
GO


