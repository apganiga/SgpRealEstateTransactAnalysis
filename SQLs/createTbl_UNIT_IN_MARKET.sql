USE [REAL_ESTATE]
GO

/****** Object:  Table [dbo].[UNIT_IN_MARKET]    Script Date: 3/5/2020 11:27:19 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[UNIT_IN_MARKET]') AND type in (N'U'))
DROP TABLE [dbo].[UNIT_IN_MARKET]
GO

/****** Object:  Table [dbo].[UNIT_IN_MARKET]    Script Date: 3/5/2020 11:27:19 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[UNIT_IN_MARKET](
	[AD_ID] [int] NOT NULL,
	[CONDO_NAME] [varchar](50) NOT NULL,
	[PRICE] [real] NULL,
	[TYPE] [varchar](10) NULL,
	[TENURE] [varchar](10) NULL,
	[TOP_] [varchar](10) NULL,
	[AREA] [smallint] NULL,
	[PSF] [varchar](10) NULL,
	[AGENT_NUMBER] [varchar](11) NULL,
	[PAGE_NO] [smallint] NULL,
	[SOURCE] [varchar](10) NULL,
	[AGENT_COMMENT] [varchar](500) NULL,
	[DATE_CAPTURED] [timestamp] NULL
) ON [PRIMARY]
GO


