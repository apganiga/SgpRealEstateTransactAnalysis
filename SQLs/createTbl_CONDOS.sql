USE [REAL_ESTATE]
GO

/****** Object:  Table [dbo].[CONDOS]    Script Date: 2/5/2020 11:26:27 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[CONDOS](
	[CONDO_ID] [numeric](18, 0) NOT NULL,
	[CONDO_NAME] [nvarchar](100) NOT NULL,
	[ADDRESS] [nvarchar](200) NULL,
	[ZIP] [nchar](10) NULL,
	[DISTRICT_ID] [nchar](10) NULL
) ON [PRIMARY]
GO


