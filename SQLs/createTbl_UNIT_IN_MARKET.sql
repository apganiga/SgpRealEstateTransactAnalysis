USE [REAL_ESTATE]
GO

/****** Object:  Table [dbo].[UNIT_IN_MARKET]    Script Date: 2/5/2020 11:26:42 AM ******/
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
	[PSF] [nchar](10) NULL,
	[AGENT_NUMBER] [varchar](8) NULL,
	[PAGE_NO] [smallint] NULL,
	[SOURCE] [varchar](10) NULL,
	[AGENT_COMMENT] [varchar](200) NULL,
	[DATE_CAPTURED] [timestamp] NULL
) ON [PRIMARY]
GO


